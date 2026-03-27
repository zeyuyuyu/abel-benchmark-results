#!/usr/bin/env python3
"""Build the v13 resolved companion subset."""

from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Any

from datasets import load_dataset


ROOT = Path(__file__).resolve().parent
ARTIFACTS_DIR = ROOT / "artifacts"
QUESTIONS_PATH = ROOT / "resolved_questions.json"
GROUND_TRUTH_PATH = ROOT / "resolved_ground_truth.json"
CASES_PATH = ROOT / "resolved_cases.md"
SPEC_PATH = ROOT / "resolved_casebook_spec.md"
SOURCE_ROWS_PATH = ARTIFACTS_DIR / "futurex_past_resolved_rows.json"
DATASET_NAME = "futurex-ai/Futurex-Past"

CASE_SPECS = [
    {
        "source_id": "694fd4d0ae81c200695c89cf",
        "category": "central_bank_decision",
        "pattern": "winner market",
    },
    {
        "source_id": "6956690920a2e600672a7864",
        "category": "central_bank_decision",
        "pattern": "winner market",
    },
    {
        "source_id": "695a609d7b2e6a00694886f6",
        "category": "central_bank_decision",
        "pattern": "winner market",
    },
    {
        "source_id": "6962468be87498005daa01c4",
        "category": "central_bank_decision",
        "pattern": "winner market",
    },
    {
        "source_id": "695bb4008b62560069adce53",
        "category": "commodity_thresholds",
        "pattern": "statement-truth set",
    },
    {
        "source_id": "695bb4008b62560069adce54",
        "category": "commodity_bucket",
        "pattern": "interval bin",
    },
    {
        "source_id": "695bb4008b62560069adce56",
        "category": "commodity_hit_levels",
        "pattern": "threshold ladder",
    },
    {
        "source_id": "695bb4008b62560069adce59",
        "category": "commodity_bucket",
        "pattern": "interval bin",
    },
    {
        "source_id": "6957ba8a03568a006853e82e",
        "category": "first_hit",
        "pattern": "winner market",
    },
    {
        "source_id": "6957ba8a03568a006853e82f",
        "category": "first_hit",
        "pattern": "winner market",
    },
    {
        "source_id": "69590c18deacd00066876763",
        "category": "crypto_binary",
        "pattern": "binary",
    },
    {
        "source_id": "69590c18deacd00066876764",
        "category": "crypto_binary",
        "pattern": "binary",
    },
    {
        "source_id": "698b2507175d47006853871d",
        "category": "agriculture_bucket",
        "pattern": "interval bin",
    },
    {
        "source_id": "6981ea9930057a005cdb9e46",
        "category": "supply_shock_binary",
        "pattern": "binary",
    },
    {
        "source_id": "69a977a47e9d43005df0d703",
        "category": "single_stock_direction",
        "pattern": "binary",
    },
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


def build_markdown(
    questions: list[dict[str, Any]], ground_truth_map: dict[str, dict[str, Any]]
) -> str:
    lines = [
        "# v13 Resolved Companion Cases",
        "",
        "This companion subset is intentionally separate from the live-only main benchmark.",
        "",
        "- Use it for fast regression and category-level scoring.",
        "- Do not treat it as the main benchmark, because the answers are already publicly resolvable.",
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
                f"- Resolved around: `{case['resolved_around']}`",
                f"- Answer format: `{case['answer_format']}`",
                "",
                "Prompt:",
                "```text",
                case["prompt"],
                "```",
                "",
                f"Ground truth: `{truth['answer_box']}`",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def build_spec(question_count: int) -> str:
    return "\n".join(
        [
            "# v13 Resolved Companion Spec",
            "",
            "## Purpose",
            "",
            "This is a quick-scoring companion subset for v13.",
            "",
            "- It is categorized.",
            "- It uses official `Futurex-Past` ground truth.",
            "- It is useful for immediate regression checks.",
            "- It is not the main benchmark, because historical search leakage remains possible.",
            "",
            "## Composition",
            "",
            f"- Total cases: `{question_count}`",
            "- Central-bank decisions",
            "- Commodity threshold / bucket questions",
            "- First-hit stock questions",
            "- Crypto binary questions",
            "- Agriculture bucket question",
            "- Supply-shock binary question",
            "- Single-stock direction question",
            "",
            "## Files",
            "",
            "- `resolved_questions.json`",
            "- `resolved_ground_truth.json`",
            "- `resolved_cases.md`",
            "- `artifacts/futurex_past_resolved_rows.json`",
            "- `resolved_test_script.py`",
            "",
            "## Markdown Policy",
            "",
            "- `resolved_cases.md` expands every case and includes ground truth because this subset is already resolved.",
        ]
    ) + "\n"


def main() -> None:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    dataset = load_dataset(DATASET_NAME, split="train")
    row_map = {row["id"]: row for row in dataset}

    questions: list[dict[str, Any]] = []
    ground_truth: list[dict[str, Any]] = []
    source_rows: list[dict[str, Any]] = []
    for index, spec in enumerate(CASE_SPECS, start=1):
        row = row_map[spec["source_id"]]
        case_id = f"v13r_{index:03d}"
        title = row.get("en_title") or row.get("title")
        answer_tokens = normalize_tokens(row["ground_truth"])
        questions.append(
            {
                "id": case_id,
                "source_id": row["id"],
                "title": title,
                "category": spec["category"],
                "futurex_pattern": spec["pattern"],
                "resolved_around": row["end_time"],
                "prompt": row["prompt"],
                "answer_format": "boxed_yes_no" if "\\boxed{Yes}" in row["prompt"] else "boxed_letters",
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
                "resolved_around": row["end_time"],
            }
        )
        source_rows.append(row)

    QUESTIONS_PATH.write_text(
        json.dumps(
            {
                "version": "v13-resolved-companion",
                "question_count": len(questions),
                "cases": questions,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    GROUND_TRUTH_PATH.write_text(
        json.dumps(
            {
                "version": "v13-resolved-companion",
                "case_count": len(ground_truth),
                "cases": ground_truth,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    SOURCE_ROWS_PATH.write_text(
        json.dumps(source_rows, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    ground_truth_map = {item["id"]: item for item in ground_truth}
    CASES_PATH.write_text(build_markdown(questions, ground_truth_map), encoding="utf-8")
    SPEC_PATH.write_text(build_spec(len(questions)), encoding="utf-8")
    print(f"Built v13 resolved companion with {len(questions)} cases.")


if __name__ == "__main__":
    main()
