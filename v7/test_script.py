#!/usr/bin/env python3
"""Run a live-only FutureX-Online financial A/B for Codex base vs skill."""

from __future__ import annotations

import json
import os
import re
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from collections import Counter
from typing import Any

from datasets import load_dataset


WORKDIR = Path("/Users/zeyu/Documents/bach_private_cache")
BENCH_DIR = WORKDIR / ".bench"
BASE_HOME = BENCH_DIR / "codex_home_base"
SKILL_HOME = BENCH_DIR / "codex_home_skill"
MODEL = "gpt-5.4"
REASONING_EFFORT = "low"
TIMEOUT_SECONDS = 1800
TODAY_CONTEXT = "March 24, 2026 (UTC+8, Asia/Shanghai)"
DATASET_NAME = "futurex-ai/Futurex-Online"
BOXED_PREDICTION_RE = re.compile(r"^\\boxed\{(?:Yes|No|[A-Z](?:, [A-Z])*)\}$")


ONLINE_TASK_IDS = [
    "69a2e39e5692ef005cdbf2d9",  # S&P 500 Single-Day Gains and Losses (%) in Q1
    "69a2e39e5692ef005cdbf2e9",  # What will KOSPI (^KS11) hit in Q1 2026?
    "69a2e39e5692ef005cdbf2d8",  # Q1 S&P 500 Performance
    "69a2e39e5692ef005cdbf2e8",  # Will KOSPI (KS11) close above __ end of Q1?
    "69a4319df2cb3b006875e9d0",  # What price will Bitcoin hit by March 2026? (add your prediction)
    "699c4887d1d3cf005c1e48ad",  # Banxico interest rate decision in March
    "69a2e39e5692ef005cdbf27c",  # Robinhood launches prediction market through MIAXdx by March 31?
]


@dataclass(frozen=True)
class RunConfig:
    name: str
    codex_home: Path


RUNS = [
    RunConfig(name="base", codex_home=BASE_HOME),
    RunConfig(name="skill", codex_home=SKILL_HOME),
]


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def load_selected_tasks() -> list[dict[str, Any]]:
    dataset = load_dataset(DATASET_NAME, split="train")
    rows = {row["id"]: row for row in dataset}
    tasks = []
    for task_id in ONLINE_TASK_IDS:
        row = rows[task_id]
        tasks.append(
            {
                "id": row["id"],
                "title": row["en_title"],
                "prompt": row["prompt"],
                "end_time": row["end_time"],
                "level": row["level"],
            }
        )
    return tasks


def boxed_answer_hint(task_prompt: str) -> str:
    if "\\boxed{Yes} or \\boxed{No}" in task_prompt:
        return r"\boxed{Yes}" + " or " + r"\boxed{No}"
    return r"\boxed{A}" + " or " + r"\boxed{B, C}"


def build_prompt(tasks: list[dict[str, Any]]) -> str:
    intro = (
        "These are unresolved current-week FutureX-Online financial tasks. "
        f"Assume today's date is {TODAY_CONTEXT}. "
        "Make the best live predictions you can as of that date. "
        "Use tools, shell, and web-accessible resources if helpful. "
        "If the specialized installed skill `causal-abel` is available and useful for market or macro questions, use it. "
        "Return only valid JSON. No markdown fences, no prose before or after the JSON.\n\n"
        "Output schema:\n"
        "{\n"
        '  "predictions": [\n'
        '    {"id": "task-id", "prediction": "\\\\boxed{...}"}\n'
        "  ]\n"
        "}\n"
    )
    sections = []
    for task in tasks:
        sections.append(
            "\n".join(
                [
                    f"Task ID: {task['id']}",
                    f"Title: {task['title']}",
                    f"End Time: {task['end_time']}",
                    f"Level: {task['level']}",
                    f"Expected answer format example: {boxed_answer_hint(task['prompt'])}",
                    "Official FutureX prompt:",
                    task["prompt"],
                ]
            )
        )
    return intro + "\n\n".join(sections)


def parse_json_payload(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", stripped, re.DOTALL)
        if match:
            return json.loads(match.group(0))
        raise


def validate_predictions(
    tasks: list[dict[str, Any]], predictions: list[dict[str, str]]
) -> dict[str, Any]:
    task_ids = [task["id"] for task in tasks]
    task_id_set = set(task_ids)
    counts = Counter(item["id"] for item in predictions)
    duplicates = sorted(task_id for task_id, count in counts.items() if count > 1)
    prediction_map = {item["id"]: item["prediction"] for item in predictions}
    missing_task_ids = [task_id for task_id in task_ids if task_id not in prediction_map]
    extra_task_ids = sorted(task_id for task_id in prediction_map if task_id not in task_id_set)
    invalid_predictions = [
        item for item in predictions if not BOXED_PREDICTION_RE.fullmatch(item["prediction"])
    ]
    return {
        "task_count_expected": len(tasks),
        "prediction_count_returned": len(predictions),
        "valid_prediction_count": len(predictions) - len(invalid_predictions),
        "all_tasks_returned": not missing_task_ids and not extra_task_ids,
        "all_predictions_valid": not invalid_predictions,
        "duplicate_task_ids": duplicates,
        "missing_task_ids": missing_task_ids,
        "extra_task_ids": extra_task_ids,
        "invalid_predictions": invalid_predictions,
    }


def run_codex_batch(run: RunConfig, output_path: Path, prompt: str, api_key: str) -> dict[str, Any]:
    cmd = [
        "codex",
        "exec",
        "--skip-git-repo-check",
        "-C",
        str(WORKDIR),
        "-s",
        "danger-full-access",
        "-m",
        MODEL,
        "-c",
        f'reasoning_effort="{REASONING_EFFORT}"',
        "--color",
        "never",
        "-o",
        str(output_path),
        prompt,
    ]
    env = os.environ.copy()
    env["CODEX_HOME"] = str(run.codex_home)
    env["ABEL_API_KEY"] = api_key
    started = time.time()
    completed = subprocess.run(
        cmd,
        cwd=WORKDIR,
        capture_output=True,
        text=True,
        env=env,
        timeout=TIMEOUT_SECONDS,
        check=False,
    )
    duration = round(time.time() - started, 2)
    raw_output = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
    parsed = None
    parse_error = None
    try:
        parsed = parse_json_payload(raw_output)
    except Exception as exc:  # noqa: BLE001
        parse_error = str(exc)
    predictions = []
    if isinstance(parsed, dict):
        for item in parsed.get("predictions", []):
            if isinstance(item, dict) and "id" in item and "prediction" in item:
                predictions.append(
                    {
                        "id": str(item["id"]),
                        "prediction": str(item["prediction"]),
                    }
                )
    return {
        "returncode": completed.returncode,
        "duration_seconds": duration,
        "stdout": completed.stdout[-4000:],
        "stderr": completed.stderr[-4000:],
        "raw_output": raw_output,
        "parsed_output": parsed,
        "parse_error": parse_error,
        "predictions": predictions,
    }


def main() -> None:
    api_key = require_env("ABEL_API_KEY")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    out_dir = BENCH_DIR / f"futurex-online-live-results-{timestamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    tasks = load_selected_tasks()
    prompt = build_prompt(tasks)
    (out_dir / "futurex_online_live_financial_subset.json").write_text(
        json.dumps(tasks, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    results: dict[str, Any] = {
        "timestamp": timestamp,
        "version": "futurex-online-live-only",
        "dataset_name": DATASET_NAME,
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "today_context": TODAY_CONTEXT,
        "task_count": len(tasks),
        "tasks": tasks,
        "runs": {},
    }

    for run in RUNS:
        run_dir = out_dir / run.name
        run_dir.mkdir(parents=True, exist_ok=True)
        output_path = run_dir / "predictions.json"
        run_result = run_codex_batch(run, output_path, prompt, api_key)
        run_result["validation"] = validate_predictions(tasks, run_result["predictions"])
        results["runs"][run.name] = run_result
        print(
            f"[{run.name}] duration={run_result['duration_seconds']}s predictions={len(run_result['predictions'])}",
            flush=True,
        )

    results["predictions_identical"] = (
        results["runs"]["base"]["predictions"] == results["runs"]["skill"]["predictions"]
    )
    task_map = {task["id"]: task["title"] for task in tasks}
    base_prediction_map = {
        item["id"]: item["prediction"] for item in results["runs"]["base"]["predictions"]
    }
    skill_prediction_map = {
        item["id"]: item["prediction"] for item in results["runs"]["skill"]["predictions"]
    }
    results["prediction_differences"] = [
        {
            "id": task_id,
            "title": task_map[task_id],
            "base_prediction": base_prediction_map.get(task_id),
            "skill_prediction": skill_prediction_map.get(task_id),
        }
        for task_id in task_map
        if base_prediction_map.get(task_id) != skill_prediction_map.get(task_id)
    ]
    results["duration_delta_seconds"] = round(
        results["runs"]["skill"]["duration_seconds"] - results["runs"]["base"]["duration_seconds"],
        2,
    )

    summary_path = out_dir / "summary.json"
    summary_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved summary to {summary_path}")


if __name__ == "__main__":
    main()
