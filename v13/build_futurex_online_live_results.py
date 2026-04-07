#!/usr/bin/env python3
"""Build a repo-facing scored report for the official FutureX-Online live run."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
BENCH = ROOT.parent.parent / ".bench" / "futurex-online-live-results-20260324-144021"
SUMMARY_PATH = BENCH / "summary.json"
QUESTIONS_PATH = ROOT / "questions.json"
GROUND_TRUTH_PATH = ROOT / "ground_truth.json"
OUT_JSON = ROOT / "futurex_online_live_results.json"
OUT_MD = ROOT / "futurex_online_live_results.md"
BOXED_RE = re.compile(r"^\\boxed\{(.+)\}$")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def extract_prediction_tokens(prediction: str | None) -> list[str]:
    if not prediction:
        return []
    match = BOXED_RE.fullmatch(prediction.strip())
    if not match:
        return []
    return sorted(part.strip() for part in match.group(1).split(",") if part.strip())


def build_payload() -> dict[str, Any]:
    summary = load_json(SUMMARY_PATH)
    questions = load_json(QUESTIONS_PATH)
    ground_truth = load_json(GROUND_TRUTH_PATH)

    official_questions = {
        case["id"]: case for case in questions["cases"] if case.get("source_type") == "futurex_online"
    }
    gt_cases = {
        case["id"]: case for case in ground_truth["cases"] if case["id"] in official_questions
    }
    source_id_to_v13 = {
        case["resolution_spec"]["source_id"]: case["id"]
        for case in gt_cases.values()
        if case["resolution_spec"]["source"] == "futurex_past_backfill"
    }

    base_prediction_map = {item["id"]: item["prediction"] for item in summary["runs"]["base"]["predictions"]}
    skill_prediction_map = {item["id"]: item["prediction"] for item in summary["runs"]["skill"]["predictions"]}

    cases = []
    resolved_count = 0
    pending_count = 0
    base_correct_count = 0
    skill_correct_count = 0

    for task in summary["tasks"]:
        v13_id = source_id_to_v13[task["id"]]
        gt_entry = gt_cases[v13_id]
        question = official_questions[v13_id]
        resolved = gt_entry.get("status") == "resolved"
        answer_tokens = sorted(gt_entry.get("answer_tokens", []))
        base_prediction = base_prediction_map.get(task["id"])
        skill_prediction = skill_prediction_map.get(task["id"])
        base_correct = extract_prediction_tokens(base_prediction) == answer_tokens if resolved else None
        skill_correct = extract_prediction_tokens(skill_prediction) == answer_tokens if resolved else None
        if resolved:
            resolved_count += 1
            base_correct_count += int(bool(base_correct))
            skill_correct_count += int(bool(skill_correct))
        else:
            pending_count += 1
        cases.append(
            {
                "id": v13_id,
                "source_id": task["id"],
                "title": task["title"],
                "prompt": question["prompt"],
                "end_time": question.get("end_time"),
                "level": task.get("level"),
                "ground_truth_status": gt_entry.get("status", "pending"),
                "ground_truth_box": gt_entry.get("answer_box"),
                "ground_truth_tokens": answer_tokens,
                "base_prediction": base_prediction,
                "skill_prediction": skill_prediction,
                "base_correct": base_correct,
                "skill_correct": skill_correct,
            }
        )

    return {
        "benchmark": "v13-futurex-online-live",
        "timestamp": summary["timestamp"],
        "today_context": summary["today_context"],
        "case_count": len(cases),
        "resolved_case_count": resolved_count,
        "pending_case_count": pending_count,
        "source_summary_path": SUMMARY_PATH.name,
        "runs": {
            "base": {
                "correct": base_correct_count,
                "resolved_total": resolved_count,
                "accuracy": round(base_correct_count / resolved_count, 4) if resolved_count else None,
                "duration_seconds": summary["runs"]["base"]["duration_seconds"],
            },
            "skill": {
                "correct": skill_correct_count,
                "resolved_total": resolved_count,
                "accuracy": round(skill_correct_count / resolved_count, 4) if resolved_count else None,
                "duration_seconds": summary["runs"]["skill"]["duration_seconds"],
            },
        },
        "cases": cases,
    }


def build_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# v13 FutureX-Online Official Live A/B",
        "",
        f"Run timestamp: `{payload['timestamp']}`",
        f"Today context: `{payload['today_context']}`",
        f"Case count: `{payload['case_count']}`",
        f"Resolved cases: `{payload['resolved_case_count']}`",
        f"Pending cases: `{payload['pending_case_count']}`",
        "",
        "Only resolved cases count toward accuracy. Pending cases remain unanswered by design until the external source settles them.",
        "",
        "| Run | Correct on resolved subset | Accuracy on resolved subset | Duration (s) |",
        "|-----|----------------------------|-----------------------------|--------------|",
        f"| `base` | `{payload['runs']['base']['correct']}/{payload['runs']['base']['resolved_total']}` | `{payload['runs']['base']['accuracy']}` | `{payload['runs']['base']['duration_seconds']:.2f}` |",
        f"| `skill` | `{payload['runs']['skill']['correct']}/{payload['runs']['skill']['resolved_total']}` | `{payload['runs']['skill']['accuracy']}` | `{payload['runs']['skill']['duration_seconds']:.2f}` |",
        "",
        "## Per-Case Status",
        "",
        "| Case ID | Source ID | Ground Truth | Base | Skill | Status |",
        "|---------|-----------|--------------|------|-------|--------|",
    ]

    for case in payload["cases"]:
        if case["ground_truth_status"] != "resolved":
            status = "pending"
        elif case["base_correct"] and case["skill_correct"]:
            status = "both correct"
        elif case["base_correct"] and not case["skill_correct"]:
            status = "base only"
        elif not case["base_correct"] and case["skill_correct"]:
            status = "skill only"
        else:
            status = "both incorrect"
        lines.append(
            f"| `{case['id']}` | `{case['source_id']}` | `{case['ground_truth_box'] or 'pending'}` | `{case['base_prediction']}` | `{case['skill_prediction']}` | {status} |"
        )

    lines.extend(["", "## Full Cases", ""])
    for case in payload["cases"]:
        base_status = "pending" if case["base_correct"] is None else ("correct" if case["base_correct"] else "incorrect")
        skill_status = "pending" if case["skill_correct"] is None else ("correct" if case["skill_correct"] else "incorrect")
        lines.extend(
            [
                f"### {case['id']} — {case['title']}",
                "",
                f"- FutureX source id: `{case['source_id']}`",
                f"- End time: `{case['end_time']}`",
                f"- Difficulty level: `{case['level']}`",
                f"- Ground truth: `{case['ground_truth_box'] or 'pending'}`",
                f"- Base: `{case['base_prediction']}` ({base_status})",
                f"- Skill: `{case['skill_prediction']}` ({skill_status})",
                "",
                "Prompt:",
                "",
                "```text",
                case["prompt"],
                "```",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    payload = build_payload()
    write_json(OUT_JSON, payload)
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
