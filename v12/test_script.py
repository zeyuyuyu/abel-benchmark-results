#!/usr/bin/env python3
"""Run the v12 general-finance challenge for Codex base vs skill."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from typing import Any


WORKDIR = Path("/Users/zeyu/Documents/bach_private_cache")
REPO_DIR = WORKDIR / "abel-benchmark-results"
BENCH_DIR = WORKDIR / ".bench"
BASE_HOME = BENCH_DIR / "codex_home_base"
SKILL_HOME = BENCH_DIR / "codex_home_skill"
SKILL_ENV = Path("/Users/zeyu/.codex/skills/causal-abel/.env.skills")
V12_DIR = REPO_DIR / "v12"
QUESTIONS_PATH = V12_DIR / "questions.json"
GROUND_TRUTH_PATH = V12_DIR / "ground_truth.json"
MODEL = "gpt-5.4"
REASONING_EFFORT = "low"
TIMEOUT_SECONDS = 1800
BOXED_RE = re.compile(r"^\\boxed\{[A-Z](?:, ?[A-Z])*\}$")


@dataclass(frozen=True)
class RunConfig:
    name: str
    codex_home: Path


RUNS = [
    RunConfig(name="base", codex_home=BASE_HOME),
    RunConfig(name="skill", codex_home=SKILL_HOME),
]

ACTIVE_CASE_IDS = [
    "v12_001",
    "v12_025",
    "v12_026",
    "v12_027",
    "v12_028",
]

BATCHES = [
    ["v12_001", "v12_025", "v12_026", "v12_027", "v12_028"],
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
                candidate = value.strip().strip('"').strip("'")
                if candidate:
                    return candidate
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


def normalize_boxed(text: str | None) -> tuple[str, ...] | None:
    if not text:
        return None
    stripped = text.strip()
    if not BOXED_RE.fullmatch(stripped):
        return None
    inner = stripped[len("\\boxed{") : -1]
    parts = [part.strip() for part in inner.split(",") if part.strip()]
    return tuple(sorted(parts))


def build_prompt(cases: list[dict[str, Any]], run_name: str) -> str:
    tool_policy = (
        "Use the tools and skills available to you if they are genuinely relevant. "
        "You may use ordinary web or market search if helpful. "
        "Keep it fast and economical: use at most 2 external tool actions total for the whole batch. "
        "Do not inspect local benchmark artifacts, local answer files, or repository ground-truth files. "
        "Treat the benchmark as closed-book with respect to local answer keys."
    )
    intro = (
        "These are v12 general-finance challenge cases for Abel skill evaluation. "
        "Each case is written as a natural market question. "
        "Answer them as if today is March 25, 2026 (GMT+8). "
        f"{tool_policy}\n\n"
        "Return only valid JSON with this exact schema:\n"
        "{\n"
        '  "predictions": [\n'
        '    {"id": "v12_001", "prediction": "\\\\boxed{A}"},\n'
        '    {"id": "v12_002", "prediction": "\\\\boxed{B, C}"}\n'
        "  ]\n"
        "}\n"
        "Do not include markdown fences or any prose outside the JSON.\n"
        "Every prediction must be a boxed letter answer using only the provided option labels.\n"
    )
    sections = []
    for case in cases:
        option_lines = "\n".join(
            f"{option['label']}. {option['text']}" for option in case["options"]
        )
        sections.append(
            "\n".join(
                [
                    f"Case ID: {case['id']}",
                    f"Category: {case['category']}",
                    f"Question: {case['question']}",
                    "Options:",
                    option_lines,
                ]
            )
        )
    return intro + "\n\n".join(sections)


def validate_predictions(cases: list[dict[str, Any]], predictions: list[dict[str, str]]) -> dict[str, Any]:
    case_ids = [case["id"] for case in cases]
    case_id_set = set(case_ids)
    prediction_map = {item["id"]: item["prediction"] for item in predictions}
    missing_case_ids = [case_id for case_id in case_ids if case_id not in prediction_map]
    extra_case_ids = sorted(case_id for case_id in prediction_map if case_id not in case_id_set)
    invalid_predictions = [
        item for item in predictions if normalize_boxed(item["prediction"]) is None
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
    predictions = []
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
    questions = load_json(QUESTIONS_PATH)
    ground_truth = load_json(GROUND_TRUTH_PATH)
    question_map = {case["id"]: case for case in questions["cases"]}
    truth_map = {case["id"]: case for case in ground_truth["cases"]}
    all_cases = [question_map[case_id] for case_id in ACTIVE_CASE_IDS]

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    out_dir = BENCH_DIR / f"v12-general-finance-results-{timestamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    results: dict[str, Any] = {
        "timestamp": timestamp,
        "version": "v12-general-finance-challenge-high-signal-subset",
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "case_count": len(all_cases),
        "active_case_ids": ACTIVE_CASE_IDS,
        "questions_path": str(QUESTIONS_PATH),
        "ground_truth_path": str(GROUND_TRUTH_PATH),
        "runs": {},
        "cases": [],
    }

    run_predictions: dict[str, dict[str, Any]] = {}
    run_state: dict[str, dict[str, Any]] = {}
    for run in RUNS:
        run_dir = out_dir / run.name
        workspace = run_dir / "workspace"
        if workspace.exists():
            shutil.rmtree(workspace)
        workspace.mkdir(parents=True, exist_ok=True)
        run_state[run.name] = {
            "run": run,
            "run_dir": run_dir,
            "workspace": workspace,
            "batch_summaries": [],
            "prediction_map": {},
            "total_duration": 0.0,
            "all_valid": True,
        }

    for batch_index, batch_case_ids in enumerate(BATCHES, start=1):
        batch_cases = [question_map[case_id] for case_id in batch_case_ids]
        with ThreadPoolExecutor(max_workers=len(RUNS)) as executor:
            future_map = {}
            for run in RUNS:
                state = run_state[run.name]
                output_path = state["run_dir"] / f"batch_{batch_index}.json"
                prompt = build_prompt(batch_cases, run.name)
                future = executor.submit(
                    run_codex_batch,
                    run,
                    f"batch_{batch_index}",
                    state["workspace"],
                    output_path,
                    prompt,
                    api_key,
                )
                future_map[future] = run.name
            for future, run_name in future_map.items():
                batch_result = future.result()
                validation = validate_predictions(batch_cases, batch_result["predictions"])
                batch_result["validation"] = validation
                state = run_state[run_name]
                state["batch_summaries"].append(batch_result)
                state["total_duration"] += batch_result["duration_seconds"]
                state["all_valid"] = (
                    state["all_valid"]
                    and validation["all_predictions_valid"]
                    and validation["all_cases_returned"]
                )
                for item in batch_result["predictions"]:
                    state["prediction_map"][item["id"]] = item["prediction"]

    for run in RUNS:
        state = run_state[run.name]
        prediction_map = state["prediction_map"]
        category_scores = defaultdict(lambda: {"correct": 0, "case_count": 0})
        correct = 0
        valid_boxed_outputs = 0
        missing_case_ids: list[str] = []

        for case in all_cases:
            case_id = case["id"]
            prediction = prediction_map.get(case_id)
            normalized_prediction = normalize_boxed(prediction)
            normalized_truth = normalize_boxed(truth_map[case_id]["answer_box"])
            is_correct = normalized_prediction == normalized_truth
            if prediction is None:
                missing_case_ids.append(case_id)
            correct += int(is_correct)
            valid_boxed_outputs += int(normalized_prediction is not None)
            bucket = category_scores[case["category"]]
            bucket["correct"] += int(is_correct)
            bucket["case_count"] += 1

        results["runs"][run.name] = {
            "correct": correct,
            "case_count": len(all_cases),
            "accuracy": round(correct / len(all_cases), 4),
            "valid_boxed_outputs": valid_boxed_outputs,
            "duration_seconds": round(state["total_duration"], 2),
            "all_batches_valid": state["all_valid"],
            "missing_case_ids": missing_case_ids,
            "category_scores": {
                category: {
                    "correct": score["correct"],
                    "case_count": score["case_count"],
                    "accuracy": round(score["correct"] / score["case_count"], 4),
                }
                for category, score in sorted(category_scores.items())
            },
            "batches": state["batch_summaries"],
        }
        run_predictions[run.name] = prediction_map

    prediction_diff_count = 0
    for case in all_cases:
        case_id = case["id"]
        answer_box = truth_map[case_id]["answer_box"]
        base_prediction = run_predictions["base"].get(case_id)
        skill_prediction = run_predictions["skill"].get(case_id)
        if base_prediction != skill_prediction:
            prediction_diff_count += 1
        results["cases"].append(
            {
                "id": case_id,
                "category": case["category"],
                "question": case["question"],
                "answer_box": answer_box,
                "base_prediction": base_prediction,
                "skill_prediction": skill_prediction,
                "base_correct": normalize_boxed(base_prediction) == normalize_boxed(answer_box),
                "skill_correct": normalize_boxed(skill_prediction) == normalize_boxed(answer_box),
            }
        )

    results["summary"] = {
        "prediction_diff_count": prediction_diff_count,
        "base_accuracy": results["runs"]["base"]["accuracy"],
        "skill_accuracy": results["runs"]["skill"]["accuracy"],
        "base_correct": results["runs"]["base"]["correct"],
        "skill_correct": results["runs"]["skill"]["correct"],
        "base_duration_seconds": results["runs"]["base"]["duration_seconds"],
        "skill_duration_seconds": results["runs"]["skill"]["duration_seconds"],
    }

    (out_dir / "summary.full.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (V12_DIR / "results.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# v12 A/B Results",
        "",
        f"Run timestamp: `{timestamp}`",
        "",
        "## Summary",
        "",
        "| Run | Correct | Accuracy | Valid Boxed Outputs | Duration (s) |",
        "|-----|---------|----------|---------------------|--------------|",
        f"| `base` | `{results['runs']['base']['correct']}/{len(all_cases)}` | `{results['runs']['base']['accuracy'] * 100:.2f}%` | `{results['runs']['base']['valid_boxed_outputs']}/{len(all_cases)}` | `{results['runs']['base']['duration_seconds']:.2f}` |",
        f"| `skill` | `{results['runs']['skill']['correct']}/{len(all_cases)}` | `{results['runs']['skill']['accuracy'] * 100:.2f}%` | `{results['runs']['skill']['valid_boxed_outputs']}/{len(all_cases)}` | `{results['runs']['skill']['duration_seconds']:.2f}` |",
        "",
        f"- Prediction differences: `{prediction_diff_count}`",
        "",
        "## Cases",
        "",
        "| Case ID | Answer | Base | Skill |",
        "|---------|--------|------|-------|",
    ]
    for case in results["cases"]:
        lines.append(
            f"| `{case['id']}` | `{case['answer_box']}` | `{case['base_prediction']}` | `{case['skill_prediction']}` |"
        )
    (V12_DIR / "benchmark_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps(results["summary"], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
