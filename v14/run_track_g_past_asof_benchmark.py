#!/usr/bin/env python3
"""Run v14 Track G past-asof benchmark for Codex base vs skill."""

from __future__ import annotations

import argparse
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


V14_DIR = Path(__file__).resolve().parent
REPO_DIR = V14_DIR.parent
WORKDIR = REPO_DIR.parent
QUESTIONS_PATH = V14_DIR / "track_g_past_asof_questions.json"
GROUND_TRUTH_PATH = V14_DIR / "track_g_past_asof_ground_truth.json"
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--case-ids", nargs="*")
    parser.add_argument("--timeout-seconds", type=int, default=TIMEOUT_SECONDS)
    return parser.parse_args()


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


def coerce_text(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value


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


def compact_case_prompt(prompt: str) -> str:
    if "IMPORTANT:" in prompt:
        prompt = prompt.split("IMPORTANT:", 1)[0].rstrip()
    return prompt.strip()


def build_prompt(cases: list[dict[str, Any]], *, batch_name: str) -> str:
    return (
        "These are resolved historical prediction cases being evaluated under an as-of search rule.\n"
        "Search is allowed, but you must simulate what was knowable at the time.\n"
        "For each case, do not use or rely on any source published after the listed Search cutoff.\n"
        "Do not use retrospective summaries, later closes, or later articles that reveal the outcome.\n"
        "If a source date is missing or ambiguous, do not rely on it.\n"
        "Keep it fast and economical: use minimal external tool actions.\n"
        "These are mostly historical as-of lookup and mapping tasks, not direct Abel graph tasks.\n"
        "If the installed `causal-abel` skill is available, only use it when a case is genuinely about causal drivers, paths, or interventions; otherwise ignore it.\n"
        "Do not inspect local benchmark answer keys or ground-truth files.\n"
        "Return only valid JSON with this exact schema:\n"
        "{\n"
        '  "predictions": [\n'
        '    {"id": "v14ga_0001", "prediction": "\\\\boxed{A}"},\n'
        '    {"id": "v14ga_0002", "prediction": "\\\\boxed{Yes}"}\n'
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
                    compact_case_prompt(case["prompt"]),
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
    timeout_seconds: int,
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
    timed_out = False
    try:
        completed = subprocess.run(
            cmd,
            cwd=workspace,
            capture_output=True,
            text=True,
            env=env,
            timeout=timeout_seconds,
            check=False,
        )
        returncode = completed.returncode
        stdout = completed.stdout[-4000:]
        stderr = completed.stderr[-4000:]
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        returncode = 124
        stdout = coerce_text(exc.stdout)[-4000:]
        stderr = (coerce_text(exc.stderr) + "\nTIMEOUT")[-4000:]
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
        "returncode": returncode,
        "timed_out": timed_out,
        "duration_seconds": duration,
        "stdout": stdout,
        "stderr": stderr,
        "raw_output": raw_output,
        "parsed_output": parsed,
        "parse_error": parse_error,
        "predictions": predictions,
    }


def main() -> None:
    args = parse_args()
    api_key = resolve_api_key()
    questions = load_json(QUESTIONS_PATH)["cases"]
    if args.case_ids:
        case_map = {item["id"]: item for item in questions}
        missing = [case_id for case_id in args.case_ids if case_id not in case_map]
        if missing:
            raise SystemExit(f"Unknown case IDs: {', '.join(missing)}")
        questions = [case_map[case_id] for case_id in args.case_ids]
    truth_map = {item["id"]: item for item in load_json(GROUND_TRUTH_PATH)["cases"]}
    batches = [
        questions[i : i + args.batch_size] for i in range(0, len(questions), args.batch_size)
    ]

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    out_dir = BENCH_DIR / f"v14-track-g-past-asof-results-{timestamp}"
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

    total_batches = len(batches)
    for batch_index, batch_cases in enumerate(batches, start=1):
        print(
            f"[track-g-past-asof] batch {batch_index}/{total_batches} "
            f"(cases={len(batch_cases)})",
            flush=True,
        )
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
                    timeout_seconds=args.timeout_seconds,
                )
                future_map[future] = run.name
            for future, run_name in future_map.items():
                batch_result = future.result()
                state = run_state[run_name]
                state["batches"].append(batch_result)
                state["duration_seconds"] += batch_result["duration_seconds"]
                for item in batch_result["predictions"]:
                    state["prediction_map"][item["id"]] = item["prediction"]
        print(f"[track-g-past-asof] completed batch {batch_index}/{total_batches}", flush=True)

    results: dict[str, Any] = {
        "timestamp": timestamp,
        "version": "v14-track-g-past-asof",
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
