#!/usr/bin/env python3
"""Build the v13 resolved as-of subset with time-bounded search metadata."""

from __future__ import annotations

import ast
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from datasets import load_dataset


ROOT = Path(__file__).resolve().parent
ARTIFACTS_DIR = ROOT / "artifacts"
QUESTIONS_PATH = ROOT / "resolved_asof_questions.json"
GROUND_TRUTH_PATH = ROOT / "resolved_asof_ground_truth.json"
CASES_PATH = ROOT / "resolved_asof_cases.md"
SPEC_PATH = ROOT / "resolved_asof_spec.md"
DATASET_NAME = "futurex-ai/Futurex-Past"

MONTHS = (
    "January|February|March|April|May|June|July|August|September|October|November|December"
)
DATE_PATTERNS = [
    re.compile(rf"\b\d{{1,2}}\s+(?:{MONTHS})\s+\d{{4}}\b"),
    re.compile(rf"\b(?:{MONTHS})\s+\d{{1,2}},\s+\d{{4}}\b"),
]

CASE_SPECS = [
    {"source_id": "694fd4d0ae81c200695c89cf", "category": "central_bank_decision", "pattern": "winner market"},
    {"source_id": "6956690920a2e600672a7864", "category": "central_bank_decision", "pattern": "winner market"},
    {"source_id": "695a609d7b2e6a00694886f6", "category": "central_bank_decision", "pattern": "winner market"},
    {"source_id": "6962468be87498005daa01c4", "category": "central_bank_decision", "pattern": "winner market"},
    {"source_id": "695bb4008b62560069adce53", "category": "commodity_thresholds", "pattern": "statement-truth set"},
    {"source_id": "695bb4008b62560069adce54", "category": "commodity_bucket", "pattern": "interval bin"},
    {"source_id": "695bb4008b62560069adce56", "category": "commodity_hit_levels", "pattern": "threshold ladder"},
    {"source_id": "695bb4008b62560069adce59", "category": "commodity_bucket", "pattern": "interval bin"},
    {"source_id": "6957ba8a03568a006853e82e", "category": "first_hit", "pattern": "winner market"},
    {"source_id": "6957ba8a03568a006853e82f", "category": "first_hit", "pattern": "winner market"},
    {"source_id": "69590c18deacd00066876763", "category": "crypto_binary", "pattern": "binary"},
    {"source_id": "69590c18deacd00066876764", "category": "crypto_binary", "pattern": "binary"},
    {"source_id": "698b2507175d47006853871d", "category": "agriculture_bucket", "pattern": "interval bin"},
    {"source_id": "6981ea9930057a005cdb9e46", "category": "supply_shock_binary", "pattern": "binary"},
    {"source_id": "69a977a47e9d43005df0d703", "category": "single_stock_direction", "pattern": "binary"},
]


def normalize_tokens(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return []
        try:
            parsed = ast.literal_eval(stripped)
        except Exception:  # noqa: BLE001
            parsed = stripped
        if isinstance(parsed, list):
            return [str(item).strip() for item in parsed if str(item).strip()]
        return [str(parsed).strip()]
    return [str(value).strip()]


def parse_date_string(raw: str) -> datetime | None:
    for fmt in ("%d %B %Y", "%B %d, %Y", "%Y-%m-%d", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(raw, fmt)
        except ValueError:
            continue
    return None


def infer_search_cutoff(title: str, prompt: str, resolved_around: str) -> tuple[str, str]:
    resolved_dt = parse_date_string(resolved_around)
    candidates: list[datetime] = []
    text = f"{title}\n{prompt}"
    for pattern in DATE_PATTERNS:
        for match in pattern.findall(text):
            parsed = parse_date_string(match)
            if parsed is not None:
                candidates.append(parsed)
    if candidates:
        explicit_max = max(candidates)
        if resolved_dt is not None:
            explicit_max = min(explicit_max, resolved_dt)
        return explicit_max.strftime("%Y-%m-%d"), "latest_explicit_date_in_prompt"
    if resolved_dt is not None:
        return resolved_dt.strftime("%Y-%m-%d"), "resolved_around_fallback"
    return resolved_around, "resolved_around_fallback"


def build_markdown(
    questions: list[dict[str, Any]], ground_truth_map: dict[str, dict[str, Any]]
) -> str:
    lines = [
        "# v13 Resolved As-Of Subset",
        "",
        "This subset uses `FutureX-Past` cases, but each case is evaluated under an explicit as-of search cutoff.",
        "",
        "- Search is allowed.",
        "- But any searched evidence must be dated on or before the case-level cutoff.",
        "- This is meant to simulate what the model could have known at that time, not what we know now.",
        "",
    ]
    for case in questions:
        truth = ground_truth_map[case["id"]]
        lines.extend(
            [
                f"## {case['id']} — {case['title']}",
                "",
                f"- Category: `{case['category']}`",
                f"- Pattern: `{case['futurex_pattern']}`",
                f"- Search cutoff: `{case['search_cutoff']}`",
                f"- Cutoff source: `{case['search_cutoff_source']}`",
                f"- Resolved around: `{case['resolved_around']}`",
                f"- Answer format: `{case['answer_format']}`",
                "",
                "Question / prompt:",
                "```text",
                case["prompt"],
                "```",
                "",
                f"Ground truth: `{truth['answer_box']}`",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def build_spec(question_count: int) -> str:
    return "\n".join(
        [
            "# v13 Resolved As-Of Spec",
            "",
            "## Purpose",
            "",
            "This subset keeps the convenience of resolved `FutureX-Past` questions while imposing an explicit as-of search rule.",
            "",
            "- The cases are historical and immediately scoreable.",
            "- Search is allowed.",
            "- But evidence must be constrained to each case's `search_cutoff`.",
            "- This subset is better than unrestricted historical search when the goal is to simulate decision-time reasoning.",
            "",
            "## Composition",
            "",
            f"- Total cases: `{question_count}`",
            "- Same 15 categorized `FutureX-Past` finance cases used in the resolved companion.",
            "- Each case adds `search_cutoff` and `search_cutoff_source` metadata.",
            "",
            "## Files",
            "",
            "- `resolved_asof_questions.json`",
            "- `resolved_asof_ground_truth.json`",
            "- `resolved_asof_cases.md`",
            "- `resolved_asof_test_script.py`",
            "",
            "## Evaluation Rule",
            "",
            "- If the benchmark runner uses search, it should reject sources dated after the case cutoff.",
            "- If a source date is unavailable or ambiguous, it should not be relied on.",
        ]
    ) + "\n"


def main() -> None:
    dataset = load_dataset(DATASET_NAME, split="train")
    row_map = {row["id"]: row for row in dataset}

    questions: list[dict[str, Any]] = []
    ground_truth: list[dict[str, Any]] = []
    for index, spec in enumerate(CASE_SPECS, start=1):
        row = row_map[spec["source_id"]]
        case_id = f"v13ra_{index:03d}"
        title = row.get("en_title") or row.get("title")
        prompt = row["prompt"]
        resolved_around = row["end_time"]
        search_cutoff, search_cutoff_source = infer_search_cutoff(title, prompt, resolved_around)
        answer_tokens = normalize_tokens(row["ground_truth"])

        questions.append(
            {
                "id": case_id,
                "source_id": row["id"],
                "title": title,
                "category": spec["category"],
                "futurex_pattern": spec["pattern"],
                "resolved_around": resolved_around,
                "search_cutoff": search_cutoff,
                "search_cutoff_source": search_cutoff_source,
                "prompt": prompt,
                "answer_format": "boxed_yes_no" if "\\boxed{Yes}" in prompt else "boxed_letters",
                "usage_policy": {
                    "search_allowed": True,
                    "as_of_cutoff_enforced": True,
                    "rule": "Do not use or rely on sources published after search_cutoff.",
                },
            }
        )
        ground_truth.append(
            {
                "id": case_id,
                "source_id": row["id"],
                "title": title,
                "category": spec["category"],
                "answer_tokens": answer_tokens,
                "answer_box": "\\boxed{" + ", ".join(answer_tokens) + "}",
                "source_dataset": DATASET_NAME,
                "resolved_around": resolved_around,
                "search_cutoff": search_cutoff,
                "search_cutoff_source": search_cutoff_source,
            }
        )

    question_doc = {
        "version": "v13-resolved-asof-subset",
        "question_count": len(questions),
        "cases": questions,
    }
    truth_doc = {
        "version": "v13-resolved-asof-subset",
        "case_count": len(ground_truth),
        "cases": ground_truth,
    }

    QUESTIONS_PATH.write_text(
        json.dumps(question_doc, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    GROUND_TRUTH_PATH.write_text(
        json.dumps(truth_doc, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    GROUND_TRUTH_MAP = {item["id"]: item for item in ground_truth}
    CASES_PATH.write_text(build_markdown(questions, GROUND_TRUTH_MAP), encoding="utf-8")
    SPEC_PATH.write_text(build_spec(len(questions)), encoding="utf-8")
    print(f"Built v13 resolved as-of subset with {len(questions)} cases.")


if __name__ == "__main__":
    main()
