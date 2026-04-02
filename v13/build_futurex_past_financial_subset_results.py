#!/usr/bin/env python3
"""Build repo-facing results for the historical FutureX-Past 10-case subset."""

from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
BENCH = ROOT.parent.parent / ".bench" / "futurex-results-20260324-115311"
SUMMARY_PATH = BENCH / "summary.json"
TASKS_PATH = BENCH / "futurex_past_financial_subset.json"
OUT_JSON = ROOT / "futurex_past_financial_subset_results.json"
OUT_MD = ROOT / "futurex_past_financial_subset_results.md"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


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
        return [part.strip() for part in stripped.split(",") if part.strip()]
    return [str(value).strip()]


def boxed_from_tokens(tokens: list[str]) -> str:
    return "\\boxed{" + ", ".join(tokens) + "}"


def build_payload() -> dict[str, Any]:
    summary = load_json(SUMMARY_PATH)
    tasks = load_json(TASKS_PATH)

    base_score = summary["runs"]["past"]["base"]["score"]
    skill_score = summary["runs"]["past"]["skill"]["score"]
    base_task_map = {task["id"]: task for task in base_score["tasks"]}
    skill_task_map = {task["id"]: task for task in skill_score["tasks"]}

    cases = []
    for task in tasks:
        ground_truth_tokens = normalize_tokens(task["ground_truth"])
        base = base_task_map[task["id"]]
        skill = skill_task_map[task["id"]]
        cases.append(
            {
                "id": task["id"],
                "title": task["title"],
                "prompt": task["prompt"],
                "end_time": task.get("end_time"),
                "level": task.get("level"),
                "ground_truth_tokens": ground_truth_tokens,
                "ground_truth_box": boxed_from_tokens(ground_truth_tokens),
                "base_prediction": base["prediction"],
                "skill_prediction": skill["prediction"],
                "base_correct": base["correct"],
                "skill_correct": skill["correct"],
            }
        )

    return {
        "benchmark": "v13-futurex-past-financial-subset",
        "timestamp": summary["timestamp"],
        "today_context": summary["today_context"],
        "case_count": len(cases),
        "source_summary_path": str(SUMMARY_PATH),
        "runs": {
            "base": {
                "correct": base_score["correct"],
                "total": base_score["total"],
                "accuracy": base_score["accuracy"],
                "duration_seconds": summary["runs"]["past"]["base"]["result"]["duration_seconds"],
            },
            "skill": {
                "correct": skill_score["correct"],
                "total": skill_score["total"],
                "accuracy": skill_score["accuracy"],
                "duration_seconds": summary["runs"]["past"]["skill"]["result"]["duration_seconds"],
            },
        },
        "cases": cases,
    }


def build_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# v13 FutureX-Past Financial Subset A/B",
        "",
        f"Run timestamp: `{payload['timestamp']}`",
        f"Today context: `{payload['today_context']}`",
        f"Case count: `{payload['case_count']}`",
        "",
        "| Run | Correct | Accuracy | Duration (s) |",
        "|-----|---------|----------|--------------|",
        f"| `base` | `{payload['runs']['base']['correct']}/{payload['runs']['base']['total']}` | `{payload['runs']['base']['accuracy']}` | `{payload['runs']['base']['duration_seconds']:.2f}` |",
        f"| `skill` | `{payload['runs']['skill']['correct']}/{payload['runs']['skill']['total']}` | `{payload['runs']['skill']['accuracy']}` | `{payload['runs']['skill']['duration_seconds']:.2f}` |",
        "",
        "## Per-Case Status",
        "",
        "| Case ID | Ground Truth | Base | Skill | Status |",
        "|---------|--------------|------|-------|--------|",
    ]

    for case in payload["cases"]:
        if case["base_correct"] and case["skill_correct"]:
            status = "both correct"
        elif case["base_correct"] and not case["skill_correct"]:
            status = "base only"
        elif not case["base_correct"] and case["skill_correct"]:
            status = "skill only"
        else:
            status = "both incorrect"
        lines.append(
            f"| `{case['id']}` | `{case['ground_truth_box']}` | `{case['base_prediction']}` | `{case['skill_prediction']}` | {status} |"
        )

    lines.extend(["", "## Full Cases", ""])
    for case in payload["cases"]:
        lines.extend(
            [
                f"### {case['id']} — {case['title']}",
                "",
                f"- End time: `{case['end_time']}`",
                f"- Difficulty level: `{case['level']}`",
                f"- Ground truth: `{case['ground_truth_box']}`",
                f"- Base: `{case['base_prediction']}` ({'correct' if case['base_correct'] else 'incorrect'})",
                f"- Skill: `{case['skill_prediction']}` ({'correct' if case['skill_correct'] else 'incorrect'})",
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
