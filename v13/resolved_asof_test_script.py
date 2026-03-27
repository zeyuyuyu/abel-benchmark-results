#!/usr/bin/env python3
"""Run the v13 resolved as-of subset for Codex base vs skill."""

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


V13_DIR = Path(__file__).resolve().parent
REPO_DIR = V13_DIR.parent
WORKDIR = REPO_DIR.parent
QUESTIONS_PATH = V13_DIR / "resolved_asof_questions.json"
GROUND_TRUTH_PATH = V13_DIR / "resolved_asof_ground_truth.json"
BENCH_DIR = WORKDIR / ".bench"
BASE_HOME = BENCH_DIR / "codex_home_base"
SKILL_HOME = BENCH_DIR / "codex_home_skill"
SKILL_ENV = Path(
    os.getenv(
        "CAUSAL_ABEL_SKILL_ENV",
        str(Path.home() / ".codex/skills/causal-abel/.env.skills"),
    )
)
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
        "These are resolved historical finance cases being evaluated under an as-of search rule.\n"
        "Search is allowed, but you must simulate what was knowable at the time.\n"
        "For each case, do not use or rely on any source published after the listed Search cutoff.\n"
        "Do not use retrospective summaries, later market closes, or later articles that reveal the outcome.\n"
        "If a source date is missing or ambiguous, do not rely on it.\n"
        "Keep it fast and economical: use at most 1 external tool action total for the whole batch.\n"
        "If the installed `causal-abel` skill is available and relevant, use it, but do not mention the skill in the answer.\n"
        "Do not inspect local benchmark answer keys or ground-truth files.\n"
        "Return only valid JSON with this exact schema:\n"
        "{\n"
        '  "predictions": [\n'
        '    {"id": "v13ra_001", "prediction": "\\\\boxed{A}"},\n'
        '    {"id": "v13ra_002", "prediction": "\\\\boxed{Yes}"}\n'
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
                    f"Search cutoff: {case['search_cutoff']}",
                    f"Resolved around: {case['resolved_around']}",
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
    out_dir = BENCH_DIR / f"v13-resolved-asof-results-{timestamp}"
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
        "version": "v13-resolved-asof-subset",
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
            truth = truth_map[case["id"]]
            pred_tokens = extract_tokens(prediction)
            gold_tokens = sorted(truth["answer_tokens"])
            is_valid = bool(pred_tokens)
            is_correct = pred_tokens == gold_tokens
            if is_valid:
                valid += 1
            if is_correct:
                correct += 1
            category_scores[case["category"]]["case_count"] += 1
            if is_correct:
                category_scores[case["category"]]["correct"] += 1

        results["runs"][run.name] = {
            "duration_seconds": round(state["duration_seconds"], 2),
            "valid_case_count": valid,
            "correct_case_count": correct,
            "accuracy": round(correct / len(questions), 4),
            "category_scores": dict(category_scores),
            "batches": state["batches"],
        }

    for case in questions:
        truth = truth_map[case["id"]]
        results["cases"].append(
            {
                "id": case["id"],
                "title": case["title"],
                "category": case["category"],
                "search_cutoff": case["search_cutoff"],
                "answer_box": truth["answer_box"],
                "base_prediction": run_state["base"]["prediction_map"].get(case["id"]),
                "skill_prediction": run_state["skill"]["prediction_map"].get(case["id"]),
            }
        )

    out_path = out_dir / "summary.json"
    out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
