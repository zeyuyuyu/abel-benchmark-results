#!/usr/bin/env python3
"""LLM-judge Track I competing-explanations outputs against frozen ground truth."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import time
from copy import deepcopy
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
REPO_DIR = ROOT.parent
WORKDIR = REPO_DIR.parent
QUESTIONS_PATH = ROOT / "track_i_competing_explanations_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_i_competing_explanations_ground_truth.json"
BENCH_DIR = WORKDIR / ".bench"
JUDGE_HOME = BENCH_DIR / "codex_home_base"
MODEL = "gpt-5.4"
REASONING_EFFORT = "low"
TIMEOUT_SECONDS = 1800


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("summary_path", type=Path)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--timeout-seconds", type=int, default=TIMEOUT_SECONDS)
    parser.add_argument("--output-path", type=Path)
    parser.add_argument("--questions-path", type=Path, default=QUESTIONS_PATH)
    parser.add_argument("--ground-truth-path", type=Path, default=GROUND_TRUTH_PATH)
    return parser.parse_args()


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


def is_valid_prediction(prediction: str | None) -> bool:
    return bool(prediction and prediction.strip())


def build_prompt(batch: list[dict[str, Any]]) -> str:
    parts = [
        "You are judging benchmark answers for realistic market causal-read cases.",
        "Score each candidate independently against the canonical answer.",
        "Use semantic equivalence, not wording overlap.",
        "Accept a narrower or more specific phrase if it preserves the same dominant causal story.",
        "Accept a follow-up if it names a concrete next observable or uncertainty that directly arbitrates the canonical story, even when phrased differently.",
        "Do not give credit for generic monitoring if the canonical follow-up requires a discriminating observable.",
        "Do not compare base and skill to each other; judge each on its own merits.",
        "Return only valid JSON with this exact schema:",
        "{",
        '  "judgments": [',
        '    {',
        '      "id": "v14i_001",',
        '      "base_primary_correct": true,',
        '      "base_followup_correct": false,',
        '      "skill_primary_correct": true,',
        '      "skill_followup_correct": true,',
        '      "notes": "short rationale"',
        "    }",
        "  ]",
        "}",
        "No markdown fences. No extra prose.",
        "",
    ]
    for case in batch:
        parts.extend(
            [
                f"Case ID: {case['id']}",
                f"Title: {case['title']}",
                f"Task family: {case['task_family']}",
                f"Primary question: {case['question']}",
                f"Follow-up question: {case['followup_question']}",
                "Evidence summary:",
            ]
        )
        for line in case["evidence_summary"]:
            parts.append(f"- {line}")
        parts.extend(
            [
                "Common failure modes:",
            ]
        )
        for line in case["common_failure_modes"]:
            parts.append(f"- {line}")
        parts.extend(
            [
                f"Canonical primary answer: {case['primary_answer_text']}",
                f"Canonical follow-up answer: {case['followup_answer_text']}",
                f"Base primary prediction: {case['base_primary_prediction'] or 'None'}",
                f"Base follow-up prediction: {case['base_followup_prediction'] or 'None'}",
                f"Skill primary prediction: {case['skill_primary_prediction'] or 'None'}",
                f"Skill follow-up prediction: {case['skill_followup_prediction'] or 'None'}",
                "",
            ]
        )
    return "\n".join(parts).strip() + "\n"


def run_judge(batch: list[dict[str, Any]], *, output_path: Path, timeout_seconds: int) -> dict[str, Any]:
    prompt = build_prompt(batch)
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
    env["CODEX_HOME"] = str(JUDGE_HOME)
    started = time.time()
    timed_out = False
    timeout = timeout_seconds if timeout_seconds > 0 else None
    try:
        completed = subprocess.run(
            cmd,
            cwd=WORKDIR,
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
    raw_output = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
    parsed = None
    parse_error = None
    try:
        parsed = parse_json_payload(raw_output)
    except Exception as exc:  # noqa: BLE001
        parse_error = str(exc)
    return {
        "returncode": returncode,
        "timed_out": timed_out,
        "duration_seconds": round(time.time() - started, 2),
        "stdout": stdout,
        "stderr": stderr,
        "raw_output": raw_output,
        "parsed_output": parsed,
        "parse_error": parse_error,
    }


def recompute_run_metrics(summary: dict[str, Any], run_name: str) -> dict[str, Any]:
    valid = 0
    primary_valid = 0
    followup_valid = 0
    primary_correct = 0
    followup_correct = 0
    exact_correct = 0
    family_scores: dict[str, dict[str, int]] = {}

    for row in summary["cases"]:
        primary_prediction = row.get(f"{run_name}_primary_prediction")
        followup_prediction = row.get(f"{run_name}_followup_prediction")
        primary_is_valid = is_valid_prediction(primary_prediction)
        followup_is_valid = is_valid_prediction(followup_prediction)
        primary_is_correct = bool(row.get(f"{run_name}_primary_correct"))
        followup_is_correct = bool(row.get(f"{run_name}_followup_correct"))
        exact_is_correct = primary_is_correct and followup_is_correct

        if primary_is_valid:
            primary_valid += 1
        if followup_is_valid:
            followup_valid += 1
        if primary_is_valid and followup_is_valid:
            valid += 1
        if primary_is_correct:
            primary_correct += 1
        if followup_is_correct:
            followup_correct += 1
        if exact_is_correct:
            exact_correct += 1

        family = row["task_family"]
        family_scores.setdefault(family, {"correct": 0, "case_count": 0})
        family_scores[family]["case_count"] += 1
        if exact_is_correct:
            family_scores[family]["correct"] += 1

    case_count = len(summary["cases"])
    prior = summary["runs"][run_name]
    return {
        "duration_seconds": prior["duration_seconds"],
        "valid_case_count": valid,
        "correct_case_count": exact_correct,
        "accuracy": round(exact_correct / case_count, 4),
        "primary_valid_case_count": primary_valid,
        "followup_valid_case_count": followup_valid,
        "primary_correct_case_count": primary_correct,
        "followup_correct_case_count": followup_correct,
        "primary_accuracy": round(primary_correct / case_count, 4),
        "followup_accuracy": round(followup_correct / case_count, 4),
        "exact_valid_rate": round(valid / case_count, 4),
        "family_scores": family_scores,
        "batches": prior["batches"],
    }


def main() -> None:
    args = parse_args()
    summary = load_json(args.summary_path)
    questions = {case["id"]: case for case in load_json(args.questions_path)["cases"]}
    truths = {case["id"]: case for case in load_json(args.ground_truth_path)["cases"]}

    cases_for_judge: list[dict[str, Any]] = []
    for row in summary["cases"]:
        question = questions[row["id"]]
        truth = truths[row["id"]]
        cases_for_judge.append(
            {
                "id": row["id"],
                "title": row["title"],
                "task_family": row["task_family"],
                "question": question["question"],
                "followup_question": question["followup_question"],
                "evidence_summary": truth["evidence_summary"],
                "common_failure_modes": truth["common_failure_modes"],
                "primary_answer_text": truth["primary_answer_text"],
                "followup_answer_text": truth["followup_answer_text"],
                "base_primary_prediction": row.get("base_primary_prediction"),
                "base_followup_prediction": row.get("base_followup_prediction"),
                "skill_primary_prediction": row.get("skill_primary_prediction"),
                "skill_followup_prediction": row.get("skill_followup_prediction"),
            }
        )

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    output_path = args.output_path or args.summary_path.with_name(f"{args.summary_path.stem}_llm_judged.json")
    judge_dir = output_path.parent / f"track_i_judge_artifacts_{timestamp}"
    judge_dir.mkdir(parents=True, exist_ok=True)

    judgments: dict[str, dict[str, Any]] = {}
    judge_batches: list[dict[str, Any]] = []
    for batch_index in range(0, len(cases_for_judge), args.batch_size):
        batch = cases_for_judge[batch_index : batch_index + args.batch_size]
        artifact_path = judge_dir / f"judge_batch_{batch_index // args.batch_size + 1}.json"
        result = run_judge(batch, output_path=artifact_path, timeout_seconds=args.timeout_seconds)
        judge_batches.append(result)
        parsed = result.get("parsed_output")
        if not isinstance(parsed, dict):
            raise SystemExit(f"Judge parse failed for batch {artifact_path.name}: {result['parse_error']}")
        for item in parsed.get("judgments", []):
            if not isinstance(item, dict) or "id" not in item:
                continue
            judgments[str(item["id"])] = item

    judged_summary = deepcopy(summary)
    judged_summary["source_summary_path"] = str(args.summary_path)
    judged_summary["judge"] = {
        "method": "llm_semantic_compare",
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "batch_size": args.batch_size,
        "artifact_dir": str(judge_dir),
        "questions_path": str(args.questions_path),
        "ground_truth_path": str(args.ground_truth_path),
        "batches": judge_batches,
    }
    judged_summary["raw_runs_before_llm_judge"] = deepcopy(summary["runs"])

    for row in judged_summary["cases"]:
        judgment = judgments.get(row["id"])
        if judgment is None:
            raise SystemExit(f"Missing judgment for case {row['id']}")
        row["base_primary_correct"] = bool(judgment.get("base_primary_correct"))
        row["base_followup_correct"] = bool(judgment.get("base_followup_correct"))
        row["skill_primary_correct"] = bool(judgment.get("skill_primary_correct"))
        row["skill_followup_correct"] = bool(judgment.get("skill_followup_correct"))
        row["judge_notes"] = str(judgment.get("notes", "")).strip()

    judged_summary["runs"]["base"] = recompute_run_metrics(judged_summary, "base")
    judged_summary["runs"]["skill"] = recompute_run_metrics(judged_summary, "skill")

    output_path.write_text(json.dumps(judged_summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
