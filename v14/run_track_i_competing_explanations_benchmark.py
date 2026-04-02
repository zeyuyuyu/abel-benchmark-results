#!/usr/bin/env python3
"""Run Track I competing-explanations benchmark for Codex base vs skill."""

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
QUESTIONS_PATH = V14_DIR / "track_i_competing_explanations_questions.json"
GROUND_TRUTH_PATH = V14_DIR / "track_i_competing_explanations_ground_truth.json"
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
NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


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
    parser.add_argument("--batch-size", type=int, default=2)
    parser.add_argument("--case-ids", nargs="*")
    parser.add_argument("--timeout-seconds", type=int, default=TIMEOUT_SECONDS)
    parser.add_argument("--questions-path", type=Path, default=QUESTIONS_PATH)
    parser.add_argument("--ground-truth-path", type=Path, default=GROUND_TRUTH_PATH)
    parser.add_argument("--benchmark-slug", default="v14-track-i-competing-explanations")
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


def normalize_text(text: str | None) -> str:
    if text is None:
        return ""
    lowered = text.lower()
    lowered = NON_ALNUM_RE.sub(" ", lowered)
    return " ".join(lowered.split())


def is_valid_prediction(prediction: str | None) -> bool:
    return bool(normalize_text(prediction))


def matches_keyword_sets(prediction: str | None, match_any: list[list[list[str]]]) -> bool:
    text = normalize_text(prediction)
    if not text:
        return False
    for keyword_set in match_any:
        if all(any(normalize_text(term) in text for term in group) for group in keyword_set):
            return True
    return False


def field_is_correct(prediction: str | None, truth: dict[str, Any], field_prefix: str) -> bool:
    match_key = f"{field_prefix}_match_any"
    if match_key in truth:
        return matches_keyword_sets(prediction, truth[match_key])

    answer_key = f"{field_prefix}_answer_text"
    canonical = normalize_text(truth.get(answer_key))
    observed = normalize_text(prediction)
    if not canonical or not observed:
        return False
    return canonical in observed or observed in canonical


def build_prompt(cases: list[dict[str, Any]], *, batch_name: str) -> str:
    parts = [
        "You are evaluating realistic analyst-style market causal-read cases.",
        "Treat each case as a real analyst question about what is driving a company, sector, or cross-asset move and what next observable would arbitrate among explanations.",
        "These cases are intentionally written to look like normal market analysis, not graph queries.",
        "Use the evidence packet in each case. Do not inspect local benchmark files or answer keys.",
        "The packet may be incomplete. If two explanations remain plausibly live, do the minimum extra verification needed to choose the better-calibrated answer.",
        "You may use tools if truly needed.",
        "Prefer verification targets that directly arbitrate among causal stories, not generic rumor-watching or price-watching.",
        "For each case, return one short primary answer phrase and one short follow-up answer phrase.",
        "Keep each phrase concise, ideally 2-10 words, not a full sentence.",
        "Return only valid JSON with this exact schema:",
        "{",
        '  "predictions": [',
        '    {"id": "v14i_001", "primary_prediction": "inventory correction", "followup_prediction": "watch sell-through and inventory days"}',
        "  ]",
        "}",
        "No markdown fences. No extra prose.",
        "",
        f"Batch: {batch_name}",
        "",
    ]
    for case in cases:
        parts.append(f"Case ID: {case['id']}")
        parts.append(f"Title: {case['title']}")
        parts.append(f"Family: {case['task_family']}")
        parts.append(f"Scenario: {case['scenario']}")
        parts.append(f"Primary question: {case['question']}")
        parts.append("Evidence packet:")
        for item in case["instantiated_inputs"]:
            parts.append(f"- {item['title']} ({item['type']}): {item['content']}")
        parts.append(f"Follow-up question: {case['followup_question']}")
        parts.append("")
    return "\n".join(parts).strip() + "\n"


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
    timeout = timeout_seconds if timeout_seconds > 0 else None
    try:
        completed = subprocess.run(
            cmd,
            cwd=workspace,
            capture_output=True,
            text=True,
            env=env,
            timeout=timeout,
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
            if (
                isinstance(item, dict)
                and "id" in item
                and "primary_prediction" in item
                and "followup_prediction" in item
            ):
                predictions.append(
                    {
                        "id": str(item["id"]),
                        "primary_prediction": str(item["primary_prediction"]).strip(),
                        "followup_prediction": str(item["followup_prediction"]).strip(),
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
    questions = load_json(args.questions_path)["cases"]
    if args.case_ids:
        case_map = {item["id"]: item for item in questions}
        missing = [case_id for case_id in args.case_ids if case_id not in case_map]
        if missing:
            raise SystemExit(f"Unknown case IDs: {', '.join(missing)}")
        questions = [case_map[case_id] for case_id in args.case_ids]
    truth_map = {item["id"]: item for item in load_json(args.ground_truth_path)["cases"]}
    batches = [questions[i : i + args.batch_size] for i in range(0, len(questions), args.batch_size)]

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    out_dir = BENCH_DIR / f"{args.benchmark_slug}-results-{timestamp}"
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
        print(f"[track-i-competing-explanations] batch {batch_index}/{total_batches} (cases={len(batch_cases)})", flush=True)
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
                    state["prediction_map"][item["id"]] = {
                        "primary_prediction": item.get("primary_prediction"),
                        "followup_prediction": item.get("followup_prediction"),
                    }
        print(f"[track-i-competing-explanations] completed batch {batch_index}/{total_batches}", flush=True)

    results: dict[str, Any] = {
        "timestamp": timestamp,
        "version": args.benchmark_slug,
        "questions_path": args.questions_path.name,
        "ground_truth_path": args.ground_truth_path.name,
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "timeout_seconds": args.timeout_seconds,
        "case_count": len(questions),
        "runs": {},
        "cases": [],
    }

    for run in RUNS:
        state = run_state[run.name]
        correct = 0
        valid = 0
        primary_correct = 0
        followup_correct = 0
        primary_valid = 0
        followup_valid = 0
        family_scores = defaultdict(lambda: {"correct": 0, "case_count": 0})
        for case in questions:
            prediction = state["prediction_map"].get(case["id"], {})
            truth = truth_map[case["id"]]
            primary_prediction = prediction.get("primary_prediction")
            followup_prediction = prediction.get("followup_prediction")
            primary_is_valid = is_valid_prediction(primary_prediction)
            followup_is_valid = is_valid_prediction(followup_prediction)
            primary_is_correct = field_is_correct(primary_prediction, truth, "primary")
            followup_is_correct = field_is_correct(followup_prediction, truth, "followup")
            is_valid = primary_is_valid and followup_is_valid
            is_correct = primary_is_correct and followup_is_correct
            if primary_is_valid:
                primary_valid += 1
            if followup_is_valid:
                followup_valid += 1
            if is_valid:
                valid += 1
            if primary_is_correct:
                primary_correct += 1
            if followup_is_correct:
                followup_correct += 1
            if is_correct:
                correct += 1
            family_scores[case["task_family"]]["case_count"] += 1
            if is_correct:
                family_scores[case["task_family"]]["correct"] += 1
        results["runs"][run.name] = {
            "duration_seconds": round(state["duration_seconds"], 2),
            "valid_case_count": valid,
            "correct_case_count": correct,
            "accuracy": round(correct / len(questions), 4),
            "primary_valid_case_count": primary_valid,
            "followup_valid_case_count": followup_valid,
            "primary_correct_case_count": primary_correct,
            "followup_correct_case_count": followup_correct,
            "primary_accuracy": round(primary_correct / len(questions), 4),
            "followup_accuracy": round(followup_correct / len(questions), 4),
            "exact_valid_rate": round(valid / len(questions), 4),
            "family_scores": dict(family_scores),
            "batches": state["batches"],
        }

    for case in questions:
        truth = truth_map[case["id"]]
        base_prediction = run_state["base"]["prediction_map"].get(case["id"], {})
        skill_prediction = run_state["skill"]["prediction_map"].get(case["id"], {})
        results["cases"].append(
            {
                "id": case["id"],
                "title": case["title"],
                "task_family": case["task_family"],
                "primary_answer_text": truth["primary_answer_text"],
                "followup_answer_text": truth["followup_answer_text"],
                "base_primary_prediction": base_prediction.get("primary_prediction"),
                "base_followup_prediction": base_prediction.get("followup_prediction"),
                "skill_primary_prediction": skill_prediction.get("primary_prediction"),
                "skill_followup_prediction": skill_prediction.get("followup_prediction"),
                "source_case_id": case["source_case_id"],
            }
        )

    out_path = out_dir / "summary.json"
    out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
