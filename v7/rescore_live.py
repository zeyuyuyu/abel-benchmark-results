#!/usr/bin/env python3
"""Backfill scores for the v7 FutureX-Online live-only benchmark."""

from __future__ import annotations

import argparse
import ast
import json
import re
from datetime import date
from pathlib import Path
from typing import Any

from datasets import load_dataset


ROOT = Path(__file__).resolve().parent
DEFAULT_RESULTS_PATH = ROOT / "results.json"
DEFAULT_SUMMARY_PATH = ROOT / "artifacts" / "summary.full.json"
DEFAULT_CASES_PATH = ROOT / "cases.md"
FUTUREX_PAST_DATASET = "futurex-ai/Futurex-Past"
BOXED_PREDICTION_RE = re.compile(r"^\\boxed\{(?:Yes|No|[A-Z](?:, [A-Z])*)\}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--results-path",
        type=Path,
        default=DEFAULT_RESULTS_PATH,
        help="Path to the compact v7 results JSON.",
    )
    parser.add_argument(
        "--summary-path",
        type=Path,
        default=DEFAULT_SUMMARY_PATH,
        help="Path to the full raw summary JSON artifact.",
    )
    parser.add_argument(
        "--cases-path",
        type=Path,
        default=DEFAULT_CASES_PATH,
        help="Path to the rendered markdown report.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the rescored JSON to stdout without writing files.",
    )
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def extract_boxed_content(prediction: str) -> str:
    match = re.search(r"\\boxed\{([^}]*)\}", prediction)
    if match:
        return match.group(1).strip()
    return prediction.strip()


def normalize_prediction_tokens(prediction: str) -> list[str]:
    content = extract_boxed_content(prediction)
    if not content:
        return []
    return sorted(
        part.strip().lower()
        for part in content.split(",")
        if part.strip()
    )


def normalize_ground_truth(value: Any) -> list[str]:
    if isinstance(value, list):
        return sorted(str(item).strip().lower() for item in value if str(item).strip())
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return []
        try:
            parsed = ast.literal_eval(stripped)
        except Exception:  # noqa: BLE001
            parsed = stripped
        return normalize_ground_truth(parsed)
    return [str(value).strip().lower()]


def build_prediction_map(run_payload: dict[str, Any]) -> dict[str, str]:
    return {
        str(item["id"]): str(item["prediction"])
        for item in run_payload.get("predictions", [])
        if isinstance(item, dict) and "id" in item and "prediction" in item
    }


def load_resolved_ground_truth(task_ids: set[str]) -> dict[str, dict[str, Any]]:
    dataset = load_dataset(FUTUREX_PAST_DATASET, split="train")
    resolved: dict[str, dict[str, Any]] = {}
    for row in dataset:
        task_id = row.get("id")
        if task_id in task_ids:
            resolved[task_id] = {
                "ground_truth": row.get("ground_truth"),
                "title": row.get("en_title") or row.get("title"),
                "source": "futurex-past",
            }
    return resolved


def render_cases_markdown(results: dict[str, Any]) -> str:
    scoring = results["scoring"]
    lines = [
        "# v7 FutureX-Online Live-Only A/B",
        "",
        f"Date run: March 24, 2026",
        "",
        f"Last rescored: {scoring['rescored_at']}",
        "",
        f"Model: `{results['model']}`",
        "",
        f"Reasoning effort: `{results['reasoning_effort']}`",
        "",
        "Setup: identical Codex CLI runs over unresolved current-week `FutureX-Online` finance tasks, with the only intentional variable being whether the installed `causal-abel` skill was present in `CODEX_HOME`.",
        "",
        "This version intentionally excludes `FutureX-Past`, so there is no historical-answer leakage from already-resolved questions.",
        "",
        "## Live Run Summary",
        "",
        "| Run | Questions | Valid box answers | Total Time | Notes |",
        "|-----|-----------|-------------------|------------|-------|",
        f"| Base | {results['task_count']} | {results['base_valid_prediction_count']}/{results['task_count']} | {results['base_duration_seconds']}s | Returned an invalid BTC answer: `\\boxed{{}}` |",
        f"| Skill | {results['task_count']} | {results['skill_valid_prediction_count']}/{results['task_count']} | {results['skill_duration_seconds']}s | Confirmed `causal-abel` usage from session log |",
        "",
        "Key observations:",
        "",
        f"- The two runs produced different predictions on `{len(results['prediction_differences'])}/{results['task_count']}` live questions.",
        f"- The skill-enabled run was slower by `{results['duration_delta_seconds']}s`.",
        "- The skill-enabled run avoided the base run's malformed BTC output.",
        "- The skill-enabled run switched Banxico from `hold` to `cut`.",
        "",
        "## Scoring Status",
        "",
        "| Metric | Base | Skill |",
        "|--------|------|-------|",
        f"| Resolved questions | {scoring['resolved_task_count']}/{results['task_count']} | {scoring['resolved_task_count']}/{results['task_count']} |",
        f"| Correct | {scoring['base_correct_count']}/{scoring['resolved_task_count']} | {scoring['skill_correct_count']}/{scoring['resolved_task_count']} |" if scoring["resolved_task_count"] else "| Correct | pending | pending |",
        f"| Accuracy on resolved subset | {scoring['base_accuracy']} | {scoring['skill_accuracy']} |" if scoring["resolved_task_count"] else "| Accuracy on resolved subset | pending | pending |",
        "",
    ]

    if scoring["pending_task_count"]:
        lines.extend(
            [
                "Pending tasks:",
                "",
            ]
        )
        for task in scoring["pending_tasks"]:
            lines.append(f"- `{task['title']}` (`{task['id']}`), end time `{task['end_time']}`")
        lines.append("")

    lines.extend(
        [
            "## Evidence That The Skill Was Actually Used",
            "",
            "The skill-side session log shows direct Abel CAP probing, including:",
            "",
            "- `python3 scripts/cap_probe.py capabilities`",
            "- `python3 scripts/cap_probe.py normalize-node BTC`",
            "- `python3 scripts/cap_probe.py observe BTC`",
            "- `python3 scripts/cap_probe.py observe SPY`",
            "- `python3 scripts/cap_probe.py paths SPY BTC --max-paths 3`",
            "- `python3 scripts/cap_probe.py traverse-parents COIN --top-k 8`",
            "- `python3 scripts/cap_probe.py traverse-parents MSTR --top-k 8`",
            "- `python3 scripts/cap_probe.py traverse-parents EWY --top-k 8`",
            "",
            "See [`artifacts/skill_session_excerpt.txt`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/artifacts/skill_session_excerpt.txt).",
            "",
            "## Per-Task Predictions",
            "",
            "| Task | Base | Skill | Ground Truth | Status |",
            "|------|------|-------|--------------|--------|",
        ]
    )

    for task in results["tasks"]:
        ground_truth = task.get("ground_truth_display", "pending")
        if task.get("resolved"):
            if task["base_correct"] and task["skill_correct"]:
                status = "both correct"
            elif task["base_correct"] and not task["skill_correct"]:
                status = "base only"
            elif not task["base_correct"] and task["skill_correct"]:
                status = "skill only"
            else:
                status = "both incorrect"
        else:
            status = "pending"
        lines.append(
            f"| `{task['title']}` | `{task['base_prediction']}` | `{task['skill_prediction']}` | `{ground_truth}` | {status} |"
        )

    lines.extend(
        [
            "",
            "## Reproducibility",
            "",
            "- Harness: [`test_script.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/test_script.py)",
            "- Rescorer: [`rescore_live.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/rescore_live.py)",
            "- Refresh command: `python3 /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/rescore_live.py`",
            "- Compact summary: [`results.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/results.json)",
            "- Full raw summary: [`artifacts/summary.full.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/artifacts/summary.full.json)",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()
    compact = load_json(args.results_path)
    summary = load_json(args.summary_path)

    task_map = {task["id"]: task for task in summary["tasks"]}
    task_ids = set(task_map)
    resolved_ground_truth = load_resolved_ground_truth(task_ids)
    base_prediction_map = build_prediction_map(summary["runs"]["base"])
    skill_prediction_map = build_prediction_map(summary["runs"]["skill"])

    rescored_tasks = []
    base_correct_count = 0
    skill_correct_count = 0
    pending_tasks = []
    for task_id, task in task_map.items():
        gt_payload = resolved_ground_truth.get(task_id)
        ground_truth_raw = gt_payload["ground_truth"] if gt_payload else None
        expected_tokens = normalize_ground_truth(ground_truth_raw) if gt_payload else []
        base_prediction = base_prediction_map.get(task_id, "")
        skill_prediction = skill_prediction_map.get(task_id, "")
        base_valid = bool(BOXED_PREDICTION_RE.fullmatch(base_prediction))
        skill_valid = bool(BOXED_PREDICTION_RE.fullmatch(skill_prediction))
        base_correct = None
        skill_correct = None
        if gt_payload:
            base_correct = base_valid and normalize_prediction_tokens(base_prediction) == expected_tokens
            skill_correct = skill_valid and normalize_prediction_tokens(skill_prediction) == expected_tokens
            base_correct_count += int(base_correct)
            skill_correct_count += int(skill_correct)
        if not gt_payload:
            pending_tasks.append(
                {
                    "id": task_id,
                    "title": task["title"],
                    "end_time": task["end_time"],
                }
            )
        rescored_tasks.append(
            {
                "id": task_id,
                "title": task["title"],
                "base_prediction": base_prediction,
                "skill_prediction": skill_prediction,
                "base_valid": base_valid,
                "skill_valid": skill_valid,
                "resolved": bool(gt_payload),
                "ground_truth_raw": ground_truth_raw,
                "ground_truth_display": str(ground_truth_raw) if gt_payload else "pending",
                "expected_tokens": expected_tokens,
                "base_tokens": normalize_prediction_tokens(base_prediction),
                "skill_tokens": normalize_prediction_tokens(skill_prediction),
                "base_correct": base_correct,
                "skill_correct": skill_correct,
                "resolution_source": gt_payload["source"] if gt_payload else None,
                "end_time": task["end_time"],
                "differed": base_prediction != skill_prediction,
            }
        )

    resolved_task_count = len(rescored_tasks) - len(pending_tasks)
    base_accuracy = round(base_correct_count / resolved_task_count, 4) if resolved_task_count else None
    skill_accuracy = round(skill_correct_count / resolved_task_count, 4) if resolved_task_count else None

    compact["tasks"] = rescored_tasks
    compact["base_valid_prediction_count"] = sum(int(task["base_valid"]) for task in rescored_tasks)
    compact["skill_valid_prediction_count"] = sum(int(task["skill_valid"]) for task in rescored_tasks)
    compact["base_invalid_predictions"] = [
        {
            "id": task["id"],
            "title": task["title"],
            "prediction": task["base_prediction"],
        }
        for task in rescored_tasks
        if not task["base_valid"]
    ]
    compact["skill_invalid_predictions"] = [
        {
            "id": task["id"],
            "title": task["title"],
            "prediction": task["skill_prediction"],
        }
        for task in rescored_tasks
        if not task["skill_valid"]
    ]
    compact["prediction_differences"] = [
        {
            "id": task["id"],
            "title": task["title"],
            "base_prediction": task["base_prediction"],
            "skill_prediction": task["skill_prediction"],
        }
        for task in rescored_tasks
        if task["differed"]
    ]
    compact["scoring"] = {
        "rescored_at": date.today().isoformat(),
        "ground_truth_dataset": FUTUREX_PAST_DATASET,
        "resolved_task_count": resolved_task_count,
        "pending_task_count": len(pending_tasks),
        "pending_tasks": pending_tasks,
        "base_correct_count": base_correct_count,
        "skill_correct_count": skill_correct_count,
        "base_accuracy": base_accuracy,
        "skill_accuracy": skill_accuracy,
        "all_tasks_resolved": not pending_tasks,
    }

    rendered_cases = render_cases_markdown(compact)
    if args.dry_run:
        print(json.dumps(compact, indent=2, ensure_ascii=False))
        return

    args.results_path.write_text(
        json.dumps(compact, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    args.cases_path.write_text(rendered_cases, encoding="utf-8")
    print(
        json.dumps(
            {
                "results_path": str(args.results_path),
                "cases_path": str(args.cases_path),
                "resolved_task_count": resolved_task_count,
                "pending_task_count": len(pending_tasks),
                "base_correct_count": base_correct_count,
                "skill_correct_count": skill_correct_count,
                "base_accuracy": base_accuracy,
                "skill_accuracy": skill_accuracy,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
