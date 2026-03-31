#!/usr/bin/env python3
"""Build repo-facing results for v14 Track H causal-ops benchmark."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
QUESTIONS_PATH = ROOT / "track_h_causal_ops_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_h_causal_ops_ground_truth.json"
OUT_JSON = ROOT / "track_h_causal_ops_results.json"
OUT_MD = ROOT / "track_h_causal_ops_results.md"
BOXED_RE = re.compile(r"^\\boxed\{[A-D]\}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("summary_path", type=Path)
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def is_valid(pred: str | None) -> bool:
    return bool(pred and BOXED_RE.fullmatch(pred.strip()))


def mark(pred: str | None, ok: bool) -> str:
    if pred is None:
        return "`None`"
    return f"`{pred}`{' ✅' if ok else ' ❌'}"


def build_outputs(summary: dict[str, Any]) -> tuple[dict[str, Any], str]:
    questions = {case["id"]: case for case in load_json(QUESTIONS_PATH)["cases"]}
    truths = {case["id"]: case for case in load_json(GROUND_TRUTH_PATH)["cases"]}

    enriched: list[dict[str, Any]] = []
    for row in summary["cases"]:
        q = questions[row["id"]]
        t = truths[row["id"]]
        base = row.get("base_prediction")
        skill = row.get("skill_prediction")
        answer_box = t["answer_box"]
        enriched.append(
            {
                "id": row["id"],
                "title": q["title"],
                "task_family": q["task_family"],
                "answer_box": answer_box,
                "base_prediction": base,
                "skill_prediction": skill,
                "base_valid": is_valid(base),
                "skill_valid": is_valid(skill),
                "base_correct": base == answer_box,
                "skill_correct": skill == answer_box,
            }
        )

    valid_both = [row for row in enriched if row["base_valid"] and row["skill_valid"]]
    base_valid_both_correct = sum(1 for row in valid_both if row["base_correct"])
    skill_valid_both_correct = sum(1 for row in valid_both if row["skill_correct"])

    result_json = {
        "timestamp": summary["timestamp"],
        "benchmark": "v14_track_h_causal_ops",
        "case_count": len(enriched),
        "base": {
            "correct_case_count": summary["runs"]["base"]["correct_case_count"],
            "valid_case_count": summary["runs"]["base"]["valid_case_count"],
            "accuracy": summary["runs"]["base"]["accuracy"],
            "duration_seconds": summary["runs"]["base"]["duration_seconds"],
            "family_scores": summary["runs"]["base"]["family_scores"],
        },
        "skill": {
            "correct_case_count": summary["runs"]["skill"]["correct_case_count"],
            "valid_case_count": summary["runs"]["skill"]["valid_case_count"],
            "accuracy": summary["runs"]["skill"]["accuracy"],
            "duration_seconds": summary["runs"]["skill"]["duration_seconds"],
            "family_scores": summary["runs"]["skill"]["family_scores"],
        },
        "valid_only": {
            "case_count": len(valid_both),
            "base_correct_case_count": base_valid_both_correct,
            "skill_correct_case_count": skill_valid_both_correct,
            "base_accuracy": round(base_valid_both_correct / len(valid_both), 4) if valid_both else None,
            "skill_accuracy": round(skill_valid_both_correct / len(valid_both), 4) if valid_both else None,
        },
        "cases": enriched,
        "source_summary_path": str(summary.get("source_summary_path", "")),
    }

    total = len(enriched)
    lines = [
        "# v14 Track H Causal Ops Results",
        "",
        f"Full Track H run over `{total}` cases.",
        "",
        f"- Base raw: `{summary['runs']['base']['correct_case_count']}/{total} = {summary['runs']['base']['accuracy']:.2%}`",
        f"- Skill raw: `{summary['runs']['skill']['correct_case_count']}/{total} = {summary['runs']['skill']['accuracy']:.2%}`",
        f"- Base valid outputs: `{summary['runs']['base']['valid_case_count']}/{total}`",
        f"- Skill valid outputs: `{summary['runs']['skill']['valid_case_count']}/{total}`",
        f"- Base duration: `{summary['runs']['base']['duration_seconds']:.2f}s`",
        f"- Skill duration: `{summary['runs']['skill']['duration_seconds']:.2f}s`",
        "",
        "## Valid-Only (Both Sides Valid)",
        "",
        f"- Cases used: `{len(valid_both)}`",
        f"- Base: `{base_valid_both_correct}/{len(valid_both)}`"
        + (f" = {base_valid_both_correct / len(valid_both):.2%}" if valid_both else ""),
        f"- Skill: `{skill_valid_both_correct}/{len(valid_both)}`"
        + (f" = {skill_valid_both_correct / len(valid_both):.2%}" if valid_both else ""),
        "",
        "| Case ID | Family | Ground truth | Base | Skill |",
        "|---|---|---|---|---|",
    ]
    for row in enriched:
        lines.append(
            f"| `{row['id']}` | `{row['task_family']}` | `{row['answer_box']}` | "
            f"{mark(row['base_prediction'], row['base_correct'])} | "
            f"{mark(row['skill_prediction'], row['skill_correct'])} |"
        )

    lines.extend(["", "## Per-Family", ""])
    for family in sorted(summary["runs"]["base"]["family_scores"]):
        base = summary["runs"]["base"]["family_scores"][family]
        skill = summary["runs"]["skill"]["family_scores"][family]
        lines.append(
            f"- `{family}`: base `{base['correct']}/{base['case_count']}`, "
            f"skill `{skill['correct']}/{skill['case_count']}`"
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
