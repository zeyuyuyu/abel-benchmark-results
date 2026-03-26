#!/usr/bin/env python3
"""Run the v13 live-only finance benchmark for Codex base vs skill."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Any


WORKDIR = Path("/Users/zeyu/Documents/bach_private_cache")
REPO_DIR = WORKDIR / "abel-benchmark-results"
V13_DIR = REPO_DIR / "v13"
QUESTIONS_PATH = V13_DIR / "questions.json"
GROUND_TRUTH_PATH = V13_DIR / "ground_truth.json"
BENCH_DIR = WORKDIR / ".bench"
BASE_HOME = BENCH_DIR / "codex_home_base"
SKILL_HOME = BENCH_DIR / "codex_home_skill"
SKILL_ENV = Path("/Users/zeyu/.codex/skills/causal-abel/.env.skills")
MODEL = "gpt-5.4"
REASONING_EFFORT = "low"
TIMEOUT_SECONDS = 1800
BOXED_RE = re.compile(r"^\\boxed\{(?:Yes|No|[A-Z](?:, ?[A-Z])*)\}$")


@dataclass(frozen=True)
class RunConfig:
    name: str
    codex_home: Path


RUNS = [
    RunConfig(name="base", codex_home=BASE_HOME),
    RunConfig(name="skill", codex_home=SKILL_HOME),
]


def resolve_api_key() -> str:
    direct = os.getenv("ABEL_API_KEY", "").strip()
    if direct:
        return direct
    if SKILL_ENV.exists():
        for raw in SKILL_ENV.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            if key.strip() == "ABEL_API_KEY":
                return value.strip().strip('"').strip("'")
    raise SystemExit("Missing ABEL_API_KEY in environment and causal-abel .env.skills")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


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


def build_prompt(cases: list[dict[str, Any]], *, batch_name: str) -> str:
    return (
        "These are v13 live-only finance benchmark cases.\n"
        "They are intentionally unresolved as of March 25, 2026 (GMT+8), so do not treat them as historical lookup questions.\n"
        "This is an unrestricted comparison: normal search, shell work, and web resources are allowed if helpful.\n"
        "If the installed `causal-abel` skill is available and relevant, use it, but do not mention the skill in the answer.\n"
        "Do not inspect local benchmark answer keys, local ground-truth files, or repository artifacts.\n"
        "Return only valid JSON with this exact schema:\n"
        "{\n"
        '  "predictions": [\n'
        '    {"id": "v13_001", "prediction": "\\\\boxed{A}"},\n'
        '    {"id": "v13_002", "prediction": "\\\\boxed{Yes}"}\n'
        "  ]\n"
        "}\n"
        "Do not include markdown fences or prose.\n\n"
        f"Batch: {batch_name}\n\n"
        + "\n\n".join(
            "\n".join(
                [
                    f"Case ID: {case['id']}",
                    f"Title: {case['title']}",
                    f"Category: {case['category']}",
                    f"End Time: {case['end_time']}",
                    f"Expected answer format: {case['answer_format']}",
                    "Prompt:",
                    case["prompt"],
                ]
            )
            for case in cases
        )
    )


def validate_predictions(cases: list[dict[str, Any]], predictions: list[dict[str, str]]) -> dict[str, Any]:
    case_ids = [case["id"] for case in cases]
    prediction_map = {item["id"]: item["prediction"] for item in predictions}
    missing_case_ids = [case_id for case_id in case_ids if case_id not in prediction_map]
    extra_case_ids = sorted(case_id for case_id in prediction_map if case_id not in set(case_ids))
    invalid_predictions = [
        item for item in predictions if not BOXED_RE.fullmatch(str(item["prediction"]).strip())
    ]
    return {
        "case_count_expected": len(cases),
        "prediction_count_returned": len(predictions),
        "valid_prediction_count": len(predictions) - len(invalid_predictions),
        "all_cases_returned": not missing_case_ids and not extra_case_ids,
        "all_predictions_valid": not invalid_predictions,
        "missing_case_ids": missing_case_ids,
        "extra_case_ids": extra_case_ids,
        "invalid_predictions": invalid_predictions,
    }


def run_codex_batch(
    run: RunConfig,
    *,
    batch_name: str,
    workspace: Path,
    output_path: Path,
    prompt: str,
    api_key: str,
) -> dict[str, Any]:
    cmd = [
        "codex",
        "exec",
        "--skip-git-repo-check",
        "-C",
        str(workspace),
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
        cwd=workspace,
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
    predictions: list[dict[str, str]] = []
    if isinstance(parsed, dict):
        for item in parsed.get("predictions", []):
            if isinstance(item, dict) and "id" in item and "prediction" in item:
                predictions.append(
                    {
                        "id": str(item["id"]),
                        "prediction": str(item["prediction"]).strip(),
                    }
                )
    return {
        "batch_name": batch_name,
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
    api_key = resolve_api_key()
    questions = load_json(QUESTIONS_PATH)["cases"]
    truth_map = {item["id"]: item for item in load_json(GROUND_TRUTH_PATH)["cases"]}
    batches = [
        questions[:7],
        questions[7:12],
        questions[12:],
    ]

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    out_dir = BENCH_DIR / f"v13-live-only-results-{timestamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    results: dict[str, Any] = {
        "timestamp": timestamp,
        "version": "v13-live-only-finance",
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "today_context": "March 25, 2026 (GMT+8, Asia/Shanghai)",
        "case_count": len(questions),
        "cases": [
            {
                "id": case["id"],
                "title": case["title"],
                "category": case["category"],
                "source_type": case["source_type"],
                "end_time": case["end_time"],
                "ground_truth_status": truth_map[case["id"]]["status"],
            }
            for case in questions
        ],
        "runs": {},
        "scoring": {
            "resolved_case_count": 0,
            "pending_case_count": len(questions),
            "base_correct_count": 0,
            "skill_correct_count": 0,
            "base_accuracy": None,
            "skill_accuracy": None,
        },
    }

    run_state: dict[str, dict[str, Any]] = {}
    for run in RUNS:
        run_dir = out_dir / run.name
        workspace = run_dir / "workspace"
        if workspace.exists():
            shutil.rmtree(workspace)
        workspace.mkdir(parents=True, exist_ok=True)
        run_state[run.name] = {
            "run_dir": run_dir,
            "workspace": workspace,
            "total_duration": 0.0,
            "prediction_map": {},
            "batches": [],
        }

    for batch_index, batch_cases in enumerate(batches, start=1):
        with ThreadPoolExecutor(max_workers=len(RUNS)) as executor:
            future_map = {}
            for run in RUNS:
                state = run_state[run.name]
                output_path = state["run_dir"] / f"batch_{batch_index}.json"
                future = executor.submit(
                    run_codex_batch,
                    run,
                    batch_name=f"batch_{batch_index}",
                    workspace=state["workspace"],
                    output_path=output_path,
                    prompt=build_prompt(batch_cases, batch_name=f"batch_{batch_index}"),
                    api_key=api_key,
                )
                future_map[future] = run.name
            for future, run_name in future_map.items():
                batch_result = future.result()
                batch_result["validation"] = validate_predictions(batch_cases, batch_result["predictions"])
                state = run_state[run_name]
                state["batches"].append(batch_result)
                state["total_duration"] += batch_result["duration_seconds"]
                for item in batch_result["predictions"]:
                    state["prediction_map"][item["id"]] = item["prediction"]

    for run in RUNS:
        state = run_state[run.name]
        prediction_map = state["prediction_map"]
        valid_outputs = sum(
            1 for prediction in prediction_map.values() if BOXED_RE.fullmatch(prediction)
        )
        results["runs"][run.name] = {
            "duration_seconds": round(state["total_duration"], 2),
            "prediction_count": len(prediction_map),
            "valid_prediction_count": valid_outputs,
            "predictions": [
                {"id": case["id"], "prediction": prediction_map.get(case["id"])}
                for case in questions
            ],
            "batches": state["batches"],
        }

    prediction_diff_count = 0
    for case in results["cases"]:
        base_prediction = next(
            (item["prediction"] for item in results["runs"]["base"]["predictions"] if item["id"] == case["id"]),
            None,
        )
        skill_prediction = next(
            (item["prediction"] for item in results["runs"]["skill"]["predictions"] if item["id"] == case["id"]),
            None,
        )
        case["base_prediction"] = base_prediction
        case["skill_prediction"] = skill_prediction
        if base_prediction != skill_prediction:
            prediction_diff_count += 1

    results["summary"] = {
        "prediction_diff_count": prediction_diff_count,
        "base_duration_seconds": results["runs"]["base"]["duration_seconds"],
        "skill_duration_seconds": results["runs"]["skill"]["duration_seconds"],
        "base_valid_prediction_count": results["runs"]["base"]["valid_prediction_count"],
        "skill_valid_prediction_count": results["runs"]["skill"]["valid_prediction_count"],
    }

    (out_dir / "summary.full.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (V13_DIR / "results.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# v13 Live-Only Finance A/B",
        "",
        f"Run timestamp: `{timestamp}`",
        "",
        "Ground truth is intentionally still pending for this live benchmark. Use `rescore_live.py` after the cases resolve.",
        "",
        "| Run | Cases | Valid boxed outputs | Duration (s) |",
        "|-----|-------|---------------------|--------------|",
        f"| `base` | `{len(questions)}` | `{results['runs']['base']['valid_prediction_count']}/{len(questions)}` | `{results['runs']['base']['duration_seconds']:.2f}` |",
        f"| `skill` | `{len(questions)}` | `{results['runs']['skill']['valid_prediction_count']}/{len(questions)}` | `{results['runs']['skill']['duration_seconds']:.2f}` |",
        "",
        f"- Prediction differences: `{prediction_diff_count}`",
        "",
        "## Per-Case Predictions",
        "",
        "| Case ID | Source | Base | Skill |",
        "|---------|--------|------|-------|",
    ]
    for case in results["cases"]:
        lines.append(
            f"| `{case['id']}` | `{case['source_type']}` | `{case['base_prediction']}` | `{case['skill_prediction']}` |"
        )
    (V13_DIR / "benchmark_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps(results["summary"], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
