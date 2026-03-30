#!/usr/bin/env python3
"""Build the v14 Track G full FutureX-Past as-of pack."""

from __future__ import annotations

import ast
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

from datasets import load_dataset


ROOT = Path(__file__).resolve().parent
QUESTIONS_PATH = ROOT / "track_g_past_asof_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_g_past_asof_ground_truth.json"
CASES_PATH = ROOT / "track_g_past_asof_cases.md"
SPEC_PATH = ROOT / "track_g_past_asof_spec.md"
DATASET_NAME = "futurex-ai/Futurex-Past"

MONTHS = (
    "January|February|March|April|May|June|July|August|September|October|November|December"
)
DATE_PATTERNS = [
    re.compile(rf"\b\d{{1,2}}\s+(?:{MONTHS})\s+\d{{4}}\b"),
    re.compile(rf"\b(?:{MONTHS})\s+\d{{1,2}},\s+\d{{4}}\b"),
]

# Keep legacy finance tags where we already curated category/pattern labels.
LEGACY_FINANCE_TAGS: dict[str, tuple[str, str]] = {
    "694fd4d0ae81c200695c89cf": ("central_bank_decision", "winner market"),
    "6956690920a2e600672a7864": ("central_bank_decision", "winner market"),
    "695a609d7b2e6a00694886f6": ("central_bank_decision", "winner market"),
    "6962468be87498005daa01c4": ("central_bank_decision", "winner market"),
    "695bb4008b62560069adce53": ("commodity_thresholds", "statement-truth set"),
    "695bb4008b62560069adce54": ("commodity_bucket", "interval bin"),
    "695bb4008b62560069adce56": ("commodity_hit_levels", "threshold ladder"),
    "695bb4008b62560069adce59": ("commodity_bucket", "interval bin"),
    "6957ba8a03568a006853e82e": ("first_hit", "winner market"),
    "6957ba8a03568a006853e82f": ("first_hit", "winner market"),
    "69590c18deacd00066876763": ("crypto_binary", "binary"),
    "69590c18deacd00066876764": ("crypto_binary", "binary"),
    "698b2507175d47006853871d": ("agriculture_bucket", "interval bin"),
    "6981ea9930057a005cdb9e46": ("supply_shock_binary", "binary"),
    "69a977a47e9d43005df0d703": ("single_stock_direction", "binary"),
}

LEGACY_CASE_ID_BY_SOURCE: dict[str, str] = {
    "694fd4d0ae81c200695c89cf": "v13ra_001",
    "6956690920a2e600672a7864": "v13ra_002",
    "695a609d7b2e6a00694886f6": "v13ra_003",
    "6962468be87498005daa01c4": "v13ra_004",
    "695bb4008b62560069adce53": "v13ra_005",
    "695bb4008b62560069adce54": "v13ra_006",
    "695bb4008b62560069adce56": "v13ra_007",
    "695bb4008b62560069adce59": "v13ra_008",
    "6957ba8a03568a006853e82e": "v13ra_009",
    "6957ba8a03568a006853e82f": "v13ra_010",
    "69590c18deacd00066876763": "v13ra_011",
    "69590c18deacd00066876764": "v13ra_012",
    "698b2507175d47006853871d": "v13ra_013",
    "6981ea9930057a005cdb9e46": "v13ra_014",
    "69a977a47e9d43005df0d703": "v13ra_015",
}


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
    return [str(value).strip()] if value is not None else []


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


def infer_answer_format(prompt: str, answer_tokens: list[str]) -> str:
    if "\\boxed{Yes}" in prompt or "\\boxed{No}" in prompt:
        return "boxed_yes_no"
    if answer_tokens and all(token in {"Yes", "No"} for token in answer_tokens):
        return "boxed_yes_no"
    return "boxed_letters"


def legacy_tags(source_id: str) -> tuple[str, str]:
    category, pattern = LEGACY_FINANCE_TAGS.get(source_id, ("unlabeled", "unknown"))
    return category, pattern


def build_markdown(
    questions: list[dict[str, Any]],
    truth_map: dict[str, dict[str, Any]],
    *,
    source_count: int,
    legacy_labeled_count: int,
) -> str:
    lines = [
        "# v14 Track G Historical As-Of Cases",
        "",
        "This markdown materializes the full FutureX-Past pack under the Track G",
        "`historical_asof_search_cutoff` regime.",
        "",
        f"- Source dataset: `{DATASET_NAME}`",
        f"- Case count: `{source_count}`",
        f"- Legacy finance-tagged cases: `{legacy_labeled_count}`",
        "- Search is allowed, but evidence must not use sources after each case's `search_cutoff`.",
        "",
    ]
    for case in questions:
        truth = truth_map[case["id"]]
        lines.extend(
            [
                f"## {case['id']} — {case['title']}",
                "",
                f"- Track: `agentic_live_analysis`",
                f"- Task family: `futurex_style_live_prediction`",
                f"- Evaluation regime: `historical_asof_search_cutoff`",
                f"- Source id: `{case['source_id']}`",
                f"- Category: `{case['category']}`",
                f"- Pattern: `{case['futurex_pattern']}`",
                f"- Search cutoff: `{case['search_cutoff']}`",
                f"- Search cutoff source: `{case['search_cutoff_source']}`",
                f"- Resolved around: `{case['resolved_around']}`",
                "",
                "Prompt:",
                "```text",
                case["prompt"],
                "```",
                "",
                "Ground truth:",
                "```json",
                json.dumps(
                    {
                        "answer_box": truth["answer_box"],
                        "answer_tokens": truth["answer_tokens"],
                    },
                    indent=2,
                    ensure_ascii=False,
                ),
                "```",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def build_spec(
    *,
    case_count: int,
    legacy_labeled_count: int,
    category_counts: Counter[str],
    level_counts: Counter[str],
) -> str:
    lines = [
        "# v14 Track G Historical As-Of Spec",
        "",
        "## Purpose",
        "",
        "This is the canonical full FutureX-Past materialization for Track G under",
        "`historical_asof_search_cutoff`.",
        "",
        "## Composition",
        "",
        f"- Total cases: `{case_count}`",
        f"- Legacy finance-tagged cases: `{legacy_labeled_count}`",
        "- Remaining cases are labeled `category = unlabeled` unless we have prior",
        "  curated category tags.",
        "",
        "## Evaluation Rule",
        "",
        "- Search is allowed.",
        "- But evidence must be dated on or before each case's `search_cutoff`.",
        "- If source dates are unavailable or ambiguous, they should not be relied on.",
        "",
        "## Category Breakdown",
        "",
    ]
    for category, count in sorted(category_counts.items()):
        lines.append(f"- `{category}`: `{count}`")
    lines.extend(["", "## Level Breakdown", ""])
    for level, count in sorted(level_counts.items()):
        lines.append(f"- `level={level}`: `{count}`")
    lines.extend(
        [
            "",
            "## Files",
            "",
            "- `track_g_past_asof_questions.json`",
            "- `track_g_past_asof_ground_truth.json`",
            "- `track_g_past_asof_cases.md`",
            "- `build_track_g_past_asof_pack.py`",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    dataset = load_dataset(DATASET_NAME, split="train")
    questions: list[dict[str, Any]] = []
    truths: list[dict[str, Any]] = []
    category_counts: Counter[str] = Counter()
    level_counts: Counter[str] = Counter()
    legacy_labeled_count = 0

    for index, row in enumerate(dataset, start=1):
        source_id = str(row["id"])
        title = str(row.get("title") or source_id)
        prompt = str(row.get("prompt") or "")
        resolved_around = str(row.get("end_time") or "")
        search_cutoff, search_cutoff_source = infer_search_cutoff(title, prompt, resolved_around)
        answer_tokens = normalize_tokens(row.get("ground_truth"))
        answer_box = "\\boxed{" + ", ".join(answer_tokens) + "}"
        category, pattern = legacy_tags(source_id)
        if category != "unlabeled":
            legacy_labeled_count += 1
        category_counts[category] += 1
        level_counts[str(row.get("level"))] += 1

        case_id = LEGACY_CASE_ID_BY_SOURCE.get(source_id, f"v14ga_{index:04d}")
        questions.append(
            {
                "id": case_id,
                "track": "agentic_live_analysis",
                "task_family": "futurex_style_live_prediction",
                "evaluation_regime": "historical_asof_search_cutoff",
                "source_family": ["FutureX-Past"],
                "source_casebook": DATASET_NAME,
                "source_case_id": source_id,
                "source_id": source_id,
                "title": title,
                "category": category,
                "futurex_pattern": pattern,
                "level": row.get("level"),
                "prompt": prompt,
                "resolved_around": resolved_around,
                "search_cutoff": search_cutoff,
                "search_cutoff_source": search_cutoff_source,
                "answer_format": infer_answer_format(prompt, answer_tokens),
                "usage_policy": {
                    "search_allowed": True,
                    "as_of_cutoff_enforced": True,
                    "rule": "Do not use or rely on sources published after search_cutoff.",
                },
            }
        )
        truths.append(
            {
                "id": case_id,
                "source_id": source_id,
                "title": title,
                "category": category,
                "futurex_pattern": pattern,
                "level": row.get("level"),
                "answer_tokens": answer_tokens,
                "answer_box": answer_box,
                "source_dataset": DATASET_NAME,
                "resolved_around": resolved_around,
                "search_cutoff": search_cutoff,
                "search_cutoff_source": search_cutoff_source,
            }
        )

    casebook = {
        "version": "v14-track-g-past-asof-questions-full",
        "split": "track_g_past_asof",
        "case_count": len(questions),
        "notes": [
            "Full FutureX-Past materialization under Track G historical as-of regime.",
            "Search is allowed, but evidence must respect case-level search_cutoff.",
            "Category tags are curated only for the legacy finance subset; other rows are unlabeled.",
        ],
        "cases": questions,
    }
    truth_doc = {
        "version": "v14-track-g-past-asof-ground-truth-full",
        "split": "track_g_past_asof",
        "case_count": len(truths),
        "notes": [
            "Ground truth is fully available because these are historical cases.",
            "This pack is for time-bounded open-book evaluation, not hidden live resolution.",
        ],
        "cases": truths,
    }

    truth_map = {item["id"]: item for item in truths}
    QUESTIONS_PATH.write_text(json.dumps(casebook, indent=2, ensure_ascii=False) + "\n")
    GROUND_TRUTH_PATH.write_text(json.dumps(truth_doc, indent=2, ensure_ascii=False) + "\n")
    CASES_PATH.write_text(
        build_markdown(
            questions,
            truth_map,
            source_count=len(questions),
            legacy_labeled_count=legacy_labeled_count,
        )
    )
    SPEC_PATH.write_text(
        build_spec(
            case_count=len(questions),
            legacy_labeled_count=legacy_labeled_count,
            category_counts=category_counts,
            level_counts=level_counts,
        )
    )
    print(f"wrote {QUESTIONS_PATH}")
    print(f"wrote {GROUND_TRUTH_PATH}")
    print(f"wrote {CASES_PATH}")
    print(f"wrote {SPEC_PATH}")
    print(f"built full track_g_past_asof with {len(questions)} cases")


if __name__ == "__main__":
    main()
