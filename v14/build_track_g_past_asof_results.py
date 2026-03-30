#!/usr/bin/env python3
"""Build repo-facing results for the v14 Track G past-asof benchmark."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
QUESTIONS_PATH = ROOT / "track_g_past_asof_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_g_past_asof_ground_truth.json"
OUT_JSON = ROOT / "track_g_past_asof_results.json"
OUT_MD = ROOT / "track_g_past_asof_results.md"
BOXED_RE = re.compile(r"^\\boxed\{(?:Yes|No|[A-Z](?:, ?[A-Z])*)\}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("summary_path", type=Path)
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_valid_boxed(prediction: str | None) -> bool:
    return bool(prediction and BOXED_RE.fullmatch(prediction.strip()))


def mark(prediction: str | None, correct: bool) -> str:
    if prediction is None:
        return "`None`"
    suffix = " ✅" if correct else " ❌"
    return f"`{prediction}`{suffix}"


def build_outputs(summary: dict[str, Any]) -> tuple[dict[str, Any], str]:
    questions = {item["id"]: item for item in load_json(QUESTIONS_PATH)["cases"]}
    truth = {item["id"]: item for item in load_json(GROUND_TRUTH_PATH)["cases"]}

    enriched_cases: list[dict[str, Any]] = []
    for case in summary["cases"]:
        q = questions[case["id"]]
        t = truth[case["id"]]
        base_prediction = case.get("base_prediction")
        skill_prediction = case.get("skill_prediction")
        answer_box = t["answer_box"]
        base_correct = base_prediction == answer_box
        skill_correct = skill_prediction == answer_box
        enriched_cases.append(
            {
                "id": case["id"],
                "title": q["title"],
                "category": q["category"],
                "search_cutoff": q["search_cutoff"],
                "answer_box": answer_box,
                "base_prediction": base_prediction,
                "skill_prediction": skill_prediction,
                "base_correct": base_correct,
                "skill_correct": skill_correct,
                "base_valid": is_valid_boxed(base_prediction),
                "skill_valid": is_valid_boxed(skill_prediction),
            }
        )

    result_json = {
        "timestamp": summary["timestamp"],
        "benchmark": "v14_track_g_past_asof",
        "case_count": len(enriched_cases),
        "base": {
            "correct_case_count": summary["runs"]["base"]["correct_case_count"],
            "valid_case_count": summary["runs"]["base"]["valid_case_count"],
            "accuracy": summary["runs"]["base"]["accuracy"],
            "duration_seconds": summary["runs"]["base"]["duration_seconds"],
            "category_scores": summary["runs"]["base"]["category_scores"],
        },
        "skill": {
            "correct_case_count": summary["runs"]["skill"]["correct_case_count"],
            "valid_case_count": summary["runs"]["skill"]["valid_case_count"],
            "accuracy": summary["runs"]["skill"]["accuracy"],
            "duration_seconds": summary["runs"]["skill"]["duration_seconds"],
            "category_scores": summary["runs"]["skill"]["category_scores"],
        },
        "cases": enriched_cases,
        "source_summary_path": str(summary.get("source_summary_path", "")),
    }

    total = len(enriched_cases)
    lines = [
        "# v14 Track G Past-As-Of Results",
        "",
        f"Full `historical_asof_search_cutoff` run over the {total}-case Track G pack.",
        "",
        f"- Base: `{summary['runs']['base']['correct_case_count']}/{total} = {summary['runs']['base']['accuracy']:.2%}`",
        f"- Skill: `{summary['runs']['skill']['correct_case_count']}/{total} = {summary['runs']['skill']['accuracy']:.2%}`",
        f"- Base valid outputs: `{summary['runs']['base']['valid_case_count']}/{total}`",
        f"- Skill valid outputs: `{summary['runs']['skill']['valid_case_count']}/{total}`",
        f"- Base duration: `{summary['runs']['base']['duration_seconds']:.2f}s`",
        f"- Skill duration: `{summary['runs']['skill']['duration_seconds']:.2f}s`",
        "",
        "| Case ID | Category | Cutoff | Ground truth | Base | Skill | Notes |",
        "|---|---|---|---|---|---|---|",
    ]
    for case in enriched_cases:
        notes: list[str] = []
        if not case["base_valid"]:
            notes.append("base_invalid_or_missing")
        if not case["skill_valid"]:
            notes.append("skill_invalid_or_missing")
        if not notes:
            notes.append("completed")
        lines.append(
            f"| `{case['id']}` | `{case['category']}` | `{case['search_cutoff']}` | "
            f"`{case['answer_box']}` | {mark(case['base_prediction'], case['base_correct'])} | "
            f"{mark(case['skill_prediction'], case['skill_correct'])} | {', '.join(notes)} |"
        )

    lines.extend(["", "## Per-Category", ""])
    for category in sorted(summary["runs"]["base"]["category_scores"]):
        base_stats = summary["runs"]["base"]["category_scores"][category]
        skill_stats = summary["runs"]["skill"]["category_scores"][category]
        lines.append(
            f"- `{category}`: base `{base_stats['correct']}/{base_stats['case_count']}`, "
            f"skill `{skill_stats['correct']}/{skill_stats['case_count']}`"
        )

    for case in enriched_cases:
        lines.extend(
            [
                "",
                f"## {case['id']} — {case['title']}",
                "",
                f"- Category: `{case['category']}`",
                f"- Search cutoff: `{case['search_cutoff']}`",
                f"- Ground truth: `{case['answer_box']}`",
                f"- `codex only`: {mark(case['base_prediction'], case['base_correct'])}",
                f"- `codex + skill`: {mark(case['skill_prediction'], case['skill_correct'])}",
            ]
        )

    return result_json, "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    summary = load_json(args.summary_path)
    summary["source_summary_path"] = str(args.summary_path)
    result_json, markdown = build_outputs(summary)
    OUT_JSON.write_text(json.dumps(result_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_MD.write_text(markdown, encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
