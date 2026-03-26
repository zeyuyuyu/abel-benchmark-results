#!/usr/bin/env python3
"""Run the v13 resolved companion subset for Codex base vs skill."""

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
V13_DIR = REPO_DIR / "v13"
QUESTIONS_PATH = V13_DIR / "resolved_questions.json"
GROUND_TRUTH_PATH = V13_DIR / "resolved_ground_truth.json"
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


def extract_tokens(prediction: str | None) -> list[str]:
    if not prediction or not BOXED_RE.fullmatch(prediction.strip()):
        return []
    inner = prediction.strip()[len("\\boxed{") : -1]
    return sorted(part.strip() for part in inner.split(",") if part.strip())


def build_prompt(cases: list[dict[str, Any]], *, batch_name: str) -> str:
    return (
        "These are categorized resolved companion cases for v13.\n"
        "They are useful for quick scoring and regression checks, but they are not the main live benchmark.\n"
        "Normal search, shell work, and web resources are allowed if helpful.\n"
        "Keep it fast and economical: use at most 1 external tool action total for the whole batch.\n"
        "If the installed `causal-abel` skill is available and relevant, use it, but do not mention the skill in the answer.\n"
        "Do not inspect local benchmark answer keys or ground-truth files.\n"
        "Return only valid JSON with this exact schema:\n"
        "{\n"
        '  "predictions": [\n'
        '    {"id": "v13r_001", "prediction": "\\\\boxed{A}"},\n'
        '    {"id": "v13r_002", "prediction": "\\\\boxed{Yes}"}\n'
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
                    f"Resolved Around: {case['resolved_around']}",
                    f"Expected answer format: {case['answer_format']}",
                    "Prompt:",
                    case["prompt"],
                ]
            )
            for case in cases
        )
    )


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
    batches = [questions[:5], questions[5:10], questions[10:]]

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    out_dir = BENCH_DIR / f"v13-resolved-results-{timestamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

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
            "prediction_map": {},
            "batches": [],
            "duration_seconds": 0.0,
        }

    for batch_index, batch_cases in enumerate(batches, start=1):
        with ThreadPoolExecutor(max_workers=len(RUNS)) as executor:
            future_map = {}
            for run in RUNS:
                state = run_state[run.name]
                future = executor.submit(
                    run_codex_batch,
                    run,
                    batch_name=f"batch_{batch_index}",
                    workspace=state["workspace"],
                    output_path=state["run_dir"] / f"batch_{batch_index}.json",
                    prompt=build_prompt(batch_cases, batch_name=f"batch_{batch_index}"),
                    api_key=api_key,
                )
                future_map[future] = run.name
            for future, run_name in future_map.items():
                batch_result = future.result()
                state = run_state[run_name]
                state["batches"].append(batch_result)
                state["duration_seconds"] += batch_result["duration_seconds"]
                for item in batch_result["predictions"]:
                    state["prediction_map"][item["id"]] = item["prediction"]

    results: dict[str, Any] = {
        "timestamp": timestamp,
        "version": "v13-resolved-companion",
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "case_count": len(questions),
        "runs": {},
        "cases": [],
    }

    for run in RUNS:
        state = run_state[run.name]
        correct = 0
        valid = 0
        category_scores = defaultdict(lambda: {"correct": 0, "case_count": 0})
        for case in questions:
            prediction = state["prediction_map"].get(case["id"])
            if BOXED_RE.fullmatch(prediction or ""):
                valid += 1
            truth_tokens = sorted(truth_map[case["id"]]["answer_tokens"])
            is_correct = extract_tokens(prediction) == truth_tokens
            correct += int(is_correct)
            bucket = category_scores[case["category"]]
            bucket["correct"] += int(is_correct)
            bucket["case_count"] += 1
        results["runs"][run.name] = {
            "correct": correct,
            "accuracy": round(correct / len(questions), 4),
            "valid_prediction_count": valid,
            "duration_seconds": round(state["duration_seconds"], 2),
            "predictions": [
                {"id": case["id"], "prediction": state["prediction_map"].get(case["id"])}
                for case in questions
            ],
            "category_scores": {
                category: {
                    "correct": item["correct"],
                    "case_count": item["case_count"],
                    "accuracy": round(item["correct"] / item["case_count"], 4),
                }
                for category, item in sorted(category_scores.items())
            },
            "batches": state["batches"],
        }

    prediction_diff_count = 0
    for case in questions:
        base_prediction = next(
            item["prediction"] for item in results["runs"]["base"]["predictions"] if item["id"] == case["id"]
        )
        skill_prediction = next(
            item["prediction"] for item in results["runs"]["skill"]["predictions"] if item["id"] == case["id"]
        )
        if base_prediction != skill_prediction:
            prediction_diff_count += 1
        truth = truth_map[case["id"]]
        results["cases"].append(
            {
                "id": case["id"],
                "title": case["title"],
                "category": case["category"],
                "answer_box": truth["answer_box"],
                "base_prediction": base_prediction,
                "skill_prediction": skill_prediction,
                "base_correct": extract_tokens(base_prediction) == sorted(truth["answer_tokens"]),
                "skill_correct": extract_tokens(skill_prediction) == sorted(truth["answer_tokens"]),
            }
        )

    results["summary"] = {
        "prediction_diff_count": prediction_diff_count,
        "base_correct": results["runs"]["base"]["correct"],
        "skill_correct": results["runs"]["skill"]["correct"],
        "base_accuracy": results["runs"]["base"]["accuracy"],
        "skill_accuracy": results["runs"]["skill"]["accuracy"],
        "base_duration_seconds": results["runs"]["base"]["duration_seconds"],
        "skill_duration_seconds": results["runs"]["skill"]["duration_seconds"],
    }

    results_path = V13_DIR / "resolved_results.json"
    report_path = V13_DIR / "resolved_benchmark_report.md"
    results_path.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# v13 Resolved Companion A/B",
        "",
        f"Run timestamp: `{timestamp}`",
        "",
        "| Run | Correct | Accuracy | Valid boxed outputs | Duration (s) |",
        "|-----|---------|----------|---------------------|--------------|",
        f"| `base` | `{results['runs']['base']['correct']}/{len(questions)}` | `{results['runs']['base']['accuracy'] * 100:.2f}%` | `{results['runs']['base']['valid_prediction_count']}/{len(questions)}` | `{results['runs']['base']['duration_seconds']:.2f}` |",
        f"| `skill` | `{results['runs']['skill']['correct']}/{len(questions)}` | `{results['runs']['skill']['accuracy'] * 100:.2f}%` | `{results['runs']['skill']['valid_prediction_count']}/{len(questions)}` | `{results['runs']['skill']['duration_seconds']:.2f}` |",
        "",
        f"- Prediction differences: `{prediction_diff_count}`",
        "",
        "## Per-Case Results",
        "",
        "| Case ID | Category | Answer | Base | Skill |",
        "|---------|----------|--------|------|-------|",
    ]
    for case in results["cases"]:
        lines.append(
            f"| `{case['id']}` | `{case['category']}` | `{case['answer_box']}` | `{case['base_prediction']}` | `{case['skill_prediction']}` |"
        )
    lines.extend(
        [
            "",
            "## Category Scores",
            "",
            "| Category | Base | Skill |",
            "|----------|------|-------|",
        ]
    )
    for category in sorted(results["runs"]["base"]["category_scores"]):
        base_score = results["runs"]["base"]["category_scores"][category]
        skill_score = results["runs"]["skill"]["category_scores"][category]
        lines.append(
            f"| `{category}` | `{base_score['correct']}/{base_score['case_count']}` | `{skill_score['correct']}/{skill_score['case_count']}` |"
        )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(results["summary"], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
