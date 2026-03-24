#!/usr/bin/env python3
"""Run FutureX financial A/B tests for Codex with and without causal-abel."""

from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
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


PAST_TASK_IDS = [
    "694fd4d0ae81c200695c89cf",  # Bank of Brazil decision in January?
    "695bb4008b62560069adce53",  # Gold (GC) above ___ end of January?
    "695bb4008b62560069adce59",  # What will Crude Oil (CL) settle at in January?
    "695bb4008b62560069adce04",  # What will Opendoor (OPEN) hit in January 2026?
    "695bb4008b62560069adce56",  # What will Crude Oil (CL) hit__ by end of January?
    "695bb4008b62560069adce54",  # What will Gold (GC) settle at in January?
    "6957ba8a03568a006853e82e",  # Tesla hits $400 or $500 first before end of January 2026?
    "6957ba8a03568a006853e82f",  # Nvidia hits 170, 200 or neither first by end of January 2026?
    "69590c18deacd00066876763",  # Will Bitcoin close above USD $100,000 on 31 January 2026 (UTC)?
    "69590c18deacd00066876764",  # Bitcoin below $82K in January?
]

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


def load_selected_tasks(dataset_name: str, ids: list[str], title_field: str) -> list[dict[str, Any]]:
    dataset = load_dataset(dataset_name, split="train")
    rows = {row["id"]: row for row in dataset}
    tasks = []
    for task_id in ids:
        row = rows[task_id]
        tasks.append(
            {
                "id": row["id"],
                "title": row[title_field],
                "prompt": row["prompt"],
                "end_time": row["end_time"],
                "level": row["level"],
                "ground_truth": row.get("ground_truth"),
            }
        )
    return tasks


def boxed_answer_hint(task_prompt: str) -> str:
    if "\\boxed{Yes} or \\boxed{No}" in task_prompt:
        return r"\boxed{Yes}" + " or " + r"\boxed{No}"
    return r"\boxed{A}" + " or " + r"\boxed{B, C}"


def build_batch_prompt(dataset_label: str, tasks: list[dict[str, Any]], mode: str) -> str:
    mode_text = {
        "past": (
            "These are retrospective FutureX-Past financial tasks. "
            "Treat this as a static QA benchmark using information available today."
        ),
        "online": (
            "These are unresolved current-week FutureX-Online financial tasks. "
            f"Assume today's date is {TODAY_CONTEXT}. Make the best live predictions you can as of that date."
        ),
    }[mode]
    intro = (
        f"{mode_text} "
        "Use tools, shell, and web-accessible resources if helpful. "
        "If the specialized installed skill `causal-abel` is available and useful for market or macro questions, use it. "
        "For each task, preserve the required FutureX answer format inside a JSON object. "
        "Return only valid JSON. No markdown fences, no prose before or after the JSON.\n\n"
        "Output schema:\n"
        "{\n"
        '  "predictions": [\n'
        '    {"id": "task-id", "prediction": "\\\\boxed{...}"}\n'
        "  ]\n"
        "}\n\n"
        f"Dataset label: {dataset_label}\n"
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


def extract_boxed_content(prediction: str) -> str:
    match = re.search(r"\\boxed\{([^}]*)\}", prediction)
    if match:
        return match.group(1).strip()
    return prediction.strip()


def normalize_prediction_tokens(prediction: str) -> list[str]:
    content = extract_boxed_content(prediction)
    if not content:
        return []
    parts = [part.strip() for part in content.split(",")]
    normalized = []
    for part in parts:
        if part:
            normalized.append(part.lower())
    return sorted(normalized)


def normalize_ground_truth(ground_truth: str) -> list[str]:
    parsed = ast.literal_eval(ground_truth)
    if isinstance(parsed, list):
        return sorted(str(item).strip().lower() for item in parsed if str(item).strip())
    return [str(parsed).strip().lower()]


def run_codex_batch(
    run: RunConfig,
    output_path: Path,
    prompt: str,
    api_key: str,
) -> dict[str, Any]:
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
    parse_error = None
    parsed = None
    try:
        parsed = parse_json_payload(raw_output)
    except Exception as exc:  # noqa: BLE001
        parse_error = str(exc)
    return {
        "returncode": completed.returncode,
        "duration_seconds": duration,
        "stdout": completed.stdout[-4000:],
        "stderr": completed.stderr[-4000:],
        "raw_output": raw_output,
        "parsed_output": parsed,
        "parse_error": parse_error,
    }


def score_past_tasks(tasks: list[dict[str, Any]], parsed_output: dict[str, Any] | None) -> dict[str, Any]:
    prediction_map: dict[str, str] = {}
    if isinstance(parsed_output, dict):
        for item in parsed_output.get("predictions", []):
            if isinstance(item, dict) and "id" in item and "prediction" in item:
                prediction_map[str(item["id"])] = str(item["prediction"])

    results = []
    total_correct = 0
    for task in tasks:
        prediction = prediction_map.get(task["id"], "")
        actual = normalize_prediction_tokens(prediction)
        expected = normalize_ground_truth(task["ground_truth"])
        correct = actual == expected
        total_correct += int(correct)
        results.append(
            {
                "id": task["id"],
                "title": task["title"],
                "prediction": prediction,
                "expected_ground_truth": task["ground_truth"],
                "expected_tokens": expected,
                "actual_tokens": actual,
                "correct": correct,
            }
        )
    return {
        "correct": total_correct,
        "total": len(tasks),
        "accuracy": round(total_correct / len(tasks), 4) if tasks else 0.0,
        "tasks": results,
    }


def materialize_subset_files(out_dir: Path, past_tasks: list[dict[str, Any]], online_tasks: list[dict[str, Any]]) -> None:
    (out_dir / "futurex_past_financial_subset.json").write_text(
        json.dumps(past_tasks, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (out_dir / "futurex_online_financial_subset.json").write_text(
        json.dumps(online_tasks, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def main() -> None:
    api_key = require_env("ABEL_API_KEY")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    out_dir = BENCH_DIR / f"futurex-results-{timestamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    past_tasks = load_selected_tasks("futurex-ai/Futurex-Past", PAST_TASK_IDS, "title")
    online_tasks = load_selected_tasks("futurex-ai/Futurex-Online", ONLINE_TASK_IDS, "en_title")
    materialize_subset_files(out_dir, past_tasks, online_tasks)

    prompts = {
        "past": build_batch_prompt("FutureX-Past financial subset", past_tasks, "past"),
        "online": build_batch_prompt("FutureX-Online financial subset", online_tasks, "online"),
    }

    results: dict[str, Any] = {
        "timestamp": timestamp,
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "today_context": TODAY_CONTEXT,
        "subset_sizes": {"past": len(past_tasks), "online": len(online_tasks)},
        "runs": {"past": {}, "online": {}},
    }

    for dataset_key in ["past", "online"]:
        dataset_dir = out_dir / dataset_key
        dataset_dir.mkdir(parents=True, exist_ok=True)
        for run in RUNS:
            output_path = dataset_dir / f"{run.name}.json"
            run_result = run_codex_batch(run, output_path, prompts[dataset_key], api_key)
            entry: dict[str, Any] = {"result": run_result}
            if dataset_key == "past":
                entry["score"] = score_past_tasks(past_tasks, run_result["parsed_output"])
            else:
                prediction_items = []
                if isinstance(run_result["parsed_output"], dict):
                    for item in run_result["parsed_output"].get("predictions", []):
                        if isinstance(item, dict) and "id" in item and "prediction" in item:
                            prediction_items.append(
                                {
                                    "id": str(item["id"]),
                                    "prediction": str(item["prediction"]),
                                }
                            )
                entry["predictions"] = prediction_items
            results["runs"][dataset_key][run.name] = entry
            print(
                f"[{dataset_key}/{run.name}] duration={run_result['duration_seconds']}s",
                flush=True,
            )
            if dataset_key == "past":
                score = entry["score"]
                print(
                    f"[{dataset_key}/{run.name}] accuracy={score['correct']}/{score['total']}",
                    flush=True,
                )

    summary_path = out_dir / "summary.json"
    summary_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved summary to {summary_path}")


if __name__ == "__main__":
    main()
