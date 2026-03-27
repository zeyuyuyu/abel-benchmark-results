#!/usr/bin/env python3
"""Run the v14 public-dev benchmark as codex-only vs codex+skill."""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import subprocess
import time
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
QUESTIONS_PATH = ROOT / "public_dev_cases.json"
GROUND_TRUTH_PATH = ROOT / "public_dev_ground_truth.json"
RESULTS_PATH = ROOT / "public_dev_results.json"
REPORT_PATH = ROOT / "public_dev_benchmark_report.md"
BENCH_ROOT = ROOT.parent.parent / ".bench"
BASE_HOME = BENCH_ROOT / "codex_home_base"
SKILL_HOME = BENCH_ROOT / "codex_home_skill"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gpt-5.4")
    parser.add_argument("--reasoning-effort", default="low")
    parser.add_argument("--batch-size", type=int, default=3)
    parser.add_argument("--timeout-seconds", type=int, default=600)
    parser.add_argument("--case-ids", nargs="*")
    parser.add_argument("--skip-base", action="store_true")
    parser.add_argument("--skip-skill", action="store_true")
    return parser.parse_args()


def load_cases(case_ids: list[str] | None) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    questions = json.loads(QUESTIONS_PATH.read_text())["cases"]
    ground_truth = {
        case["id"]: case for case in json.loads(GROUND_TRUTH_PATH.read_text())["cases"]
    }
    if case_ids:
        question_map = {case["id"]: case for case in questions}
        missing = [case_id for case_id in case_ids if case_id not in question_map]
        if missing:
            raise SystemExit(f"Unknown case IDs: {', '.join(missing)}")
        questions = [question_map[case_id] for case_id in case_ids]
    return questions, ground_truth


def chunked(items: list[dict[str, Any]], batch_size: int) -> list[list[dict[str, Any]]]:
    return [items[i : i + batch_size] for i in range(0, len(items), batch_size)]


def case_payload(case: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": case["id"],
        "title": case["title"],
        "track": case["track"],
        "scenario": case["scenario"],
        "question": case["question"],
        "options": case.get("options", []),
        "materials": [
            {k: value for k, value in material.items() if k in {"type", "title", "content"}}
            for material in case["instantiated_inputs"]
        ],
        "response_contract": case["response_contract"],
    }


def build_prompt(batch: list[dict[str, Any]]) -> str:
    return (
        "Answer the benchmark cases using ONLY the provided materials. "
        "Do not browse, do not search the web, and do not use outside facts. "
        "If a skill is available and relevant, you may use it silently, but the "
        "answer must still be grounded only in the provided materials. "
        "Return ONLY valid JSON with this schema: "
        '{"predictions":[{"id":"case_id","answer":{...required fields...}}]}. '
        "Do not include markdown fences or extra text. "
        "For categorical fields, prefer compact values instead of long prose when possible. "
        "Cases: "
        + json.dumps([case_payload(case) for case in batch], ensure_ascii=False)
    )


def normalize_text(value: str) -> str:
    value = value.replace("_", " ").lower()
    value = re.sub(r"[^a-z0-9.\s-]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def text_tokens(value: str) -> set[str]:
    return {token for token in normalize_text(value).split() if token}


def parse_bool(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        norm = normalize_text(value)
        if norm in {"true", "yes"}:
            return True
        if norm in {"false", "no"}:
            return False
    return None


def parse_number(value: Any) -> float | None:
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)
    if isinstance(value, str):
        match = re.search(r"-?\d+(?:\.\d+)?", value)
        if match:
            return float(match.group(0))
    return None


def text_match(predicted: Any, canonical: Any, alternatives: list[Any] | None = None) -> bool:
    values: list[str] = []
    for item in [canonical] + (alternatives or []):
        if isinstance(item, str):
            values.append(item)
    if not isinstance(predicted, str):
        return False
    predicted_norm = normalize_text(predicted)
    predicted_tokens = text_tokens(predicted)
    for value in values:
        value_norm = normalize_text(value)
        if predicted_norm == value_norm or value_norm in predicted_norm or predicted_norm in value_norm:
            return True
        canon_tokens = text_tokens(value)
        if canon_tokens:
            overlap = len(predicted_tokens & canon_tokens) / len(canon_tokens)
            if overlap >= 0.75:
                return True
    return False


def ordered_list_match(predicted: Any, canonical: list[Any]) -> bool:
    if not isinstance(predicted, list):
        return False
    pred_norm = [normalize_text(str(item)) for item in predicted]
    canon_norm = [normalize_text(str(item)) for item in canonical]
    if pred_norm == canon_norm:
        return True
    if len(pred_norm) >= len(canon_norm):
        for start in range(0, len(pred_norm) - len(canon_norm) + 1):
            if pred_norm[start : start + len(canon_norm)] == canon_norm:
                return True
    return False


def unordered_list_match(predicted: Any, canonical: list[Any], alternatives: list[Any] | None = None) -> bool:
    candidate_lists: list[list[Any]] = [canonical]
    if alternatives:
        candidate_lists.extend(item for item in alternatives if isinstance(item, list))
    if not isinstance(predicted, list):
        return False
    pred_norm = sorted(normalize_text(str(item)) for item in predicted)
    for candidate in candidate_lists:
        cand_norm = sorted(normalize_text(str(item)) for item in candidate)
        if pred_norm == cand_norm:
            return True
    return False


def field_match(
    field: str,
    predicted: Any,
    canonical: Any,
    alternatives: list[Any] | None = None,
) -> bool:
    if canonical is None:
        return predicted is None
    if isinstance(canonical, bool):
        return parse_bool(predicted) == canonical
    if isinstance(canonical, (int, float)) and not isinstance(canonical, bool):
        number = parse_number(predicted)
        if number is None:
            return False
        tolerance = 0.15 if field == "estimate" else 1e-6
        return math.isclose(number, float(canonical), abs_tol=tolerance)
    if isinstance(canonical, list):
        if field.endswith("path") or field in {"mechanism_path", "example_path"}:
            return ordered_list_match(predicted, canonical)
        return unordered_list_match(predicted, canonical, alternatives)
    if isinstance(canonical, str):
        if field in {"label"}:
            return isinstance(predicted, str) and normalize_text(predicted) == normalize_text(canonical)
        return text_match(predicted, canonical, alternatives)
    return predicted == canonical


def score_case(
    case: dict[str, Any],
    truth: dict[str, Any],
    prediction: dict[str, Any] | None,
) -> dict[str, Any]:
    canonical = truth["canonical_answer"]
    alternatives = truth.get("accepted_alternatives", [])
    primary_fields = truth["scoring_rubric"]["primary_fields"]
    field_weights = truth["scoring_rubric"]["field_weights"]
    answer = prediction or {}

    field_results: dict[str, bool] = {}
    weighted_score = 0.0
    total_weight = 0.0

    for field, weight in field_weights.items():
        alt_values = [item[field] for item in alternatives if isinstance(item, dict) and field in item]
        matched = field_match(field, answer.get(field), canonical.get(field), alt_values)
        field_results[field] = matched
        total_weight += weight
        if matched:
            weighted_score += weight

    exact_primary = all(field_results.get(field, False) for field in primary_fields)
    return {
        "id": case["id"],
        "title": case["title"],
        "track": case["track"],
        "prediction": answer,
        "canonical_answer": canonical,
        "primary_fields": primary_fields,
        "field_results": field_results,
        "exact_primary_correct": exact_primary,
        "weighted_score": round(weighted_score / total_weight, 4) if total_weight else 0.0,
    }


def parse_output(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"predictions": []}
    raw = path.read_text().strip()
    if not raw:
        return {"predictions": []}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}\s*$", raw, re.DOTALL)
        if not match:
            return {"predictions": []}
        return json.loads(match.group(0))


def run_batches(
    mode_name: str,
    codex_home: Path,
    batches: list[list[dict[str, Any]]],
    model: str,
    reasoning_effort: str,
    timeout_seconds: int,
    workdir: Path,
) -> dict[str, Any]:
    raw_dir = workdir / mode_name
    raw_dir.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)

    prediction_map: dict[str, dict[str, Any]] = {}
    batch_logs: list[dict[str, Any]] = []
    total_duration = 0.0

    for index, batch in enumerate(batches, start=1):
        output_path = raw_dir / f"batch_{index}.json"
        prompt = build_prompt(batch)
        cmd = [
            "codex",
            "exec",
            "--skip-git-repo-check",
            "-C",
            str(workdir),
            "-s",
            "danger-full-access",
            "-m",
            model,
            "-c",
            f'reasoning_effort="{reasoning_effort}"',
            "--color",
            "never",
            "-o",
            str(output_path),
            prompt,
        ]
        started = time.time()
        result = subprocess.run(
            cmd,
            cwd=workdir,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
        duration = round(time.time() - started, 2)
        total_duration += duration
        parsed = parse_output(output_path)
        for item in parsed.get("predictions", []):
            if isinstance(item, dict) and "id" in item:
                prediction_map[item["id"]] = item.get("answer", {})
        batch_logs.append(
            {
                "batch_index": index,
                "case_ids": [case["id"] for case in batch],
                "duration_seconds": duration,
                "returncode": result.returncode,
                "stderr_tail": result.stderr[-500:],
                "output_path": str(output_path),
            }
        )

    return {
        "mode": mode_name,
        "codex_home": str(codex_home),
        "total_duration_seconds": round(total_duration, 2),
        "predictions": prediction_map,
        "batch_logs": batch_logs,
    }


def build_summary(mode_result: dict[str, Any], cases: list[dict[str, Any]], truth_map: dict[str, Any]) -> dict[str, Any]:
    scored_cases = [
        score_case(case, truth_map[case["id"]], mode_result["predictions"].get(case["id"]))
        for case in cases
    ]
    exact_correct = sum(1 for item in scored_cases if item["exact_primary_correct"])
    weighted_average = round(
        sum(item["weighted_score"] for item in scored_cases) / len(scored_cases), 4
    )
    per_track: dict[str, dict[str, Any]] = defaultdict(lambda: {"correct": 0, "total": 0})
    for item in scored_cases:
        per_track[item["track"]]["total"] += 1
        if item["exact_primary_correct"]:
            per_track[item["track"]]["correct"] += 1
    return {
        "summary": {
            "exact_primary_correct": exact_correct,
            "case_count": len(scored_cases),
            "exact_primary_accuracy": round(exact_correct / len(scored_cases), 4),
            "weighted_average": weighted_average,
            "total_duration_seconds": mode_result["total_duration_seconds"],
            "per_track": {
                track: {
                    **stats,
                    "accuracy": round(stats["correct"] / stats["total"], 4) if stats["total"] else 0.0,
                }
                for track, stats in per_track.items()
            },
        },
        "cases": scored_cases,
        "batch_logs": mode_result["batch_logs"],
    }


def render_report(results: dict[str, Any]) -> str:
    lines = [
        "# v14 Public Dev Benchmark Report",
        "",
        f"- Timestamp: `{results['timestamp']}`",
        f"- Model: `{results['model']}`",
        f"- Reasoning effort: `{results['reasoning_effort']}`",
        f"- Case count: `{results['case_count']}`",
        f"- Questions: `{QUESTIONS_PATH}`",
        f"- Ground truth: `{GROUND_TRUTH_PATH}`",
        "",
    ]
    for mode_name in ["base", "skill"]:
        if mode_name not in results["runs"]:
            continue
        summary = results["runs"][mode_name]["summary"]
        lines.extend(
            [
                f"## {mode_name}",
                "",
                f"- Exact-primary accuracy: `{summary['exact_primary_correct']}/{summary['case_count']} = {summary['exact_primary_accuracy']:.2%}`",
                f"- Weighted average: `{summary['weighted_average']:.2%}`",
                f"- Total duration: `{summary['total_duration_seconds']:.2f}s`",
                "",
                "Per track:",
                "",
            ]
        )
        for track, stats in sorted(summary["per_track"].items()):
            lines.append(
                f"- `{track}`: `{stats['correct']}/{stats['total']} = {stats['accuracy']:.2%}`"
            )
        lines.append("")

    if "comparison" in results:
        comparison = results["comparison"]
        lines.extend(
            [
                "## Comparison",
                "",
                f"- Exact-primary diff count: `{comparison['prediction_diff_count']}`",
                f"- Differing case IDs: `{', '.join(comparison['differing_case_ids']) or 'none'}`",
                "",
            ]
        )

    lines.extend(["## Case Table", ""])
    header = "| Case ID | Track | Base | Skill |"
    separator = "|---|---|---:|---:|"
    lines.extend([header, separator])
    base_cases = {case["id"]: case for case in results["runs"].get("base", {}).get("cases", [])}
    skill_cases = {case["id"]: case for case in results["runs"].get("skill", {}).get("cases", [])}
    for case_id in [case["id"] for case in results["cases"]]:
        base_mark = "n/a"
        skill_mark = "n/a"
        if case_id in base_cases:
            base_mark = "1" if base_cases[case_id]["exact_primary_correct"] else "0"
        if case_id in skill_cases:
            skill_mark = "1" if skill_cases[case_id]["exact_primary_correct"] else "0"
        track = next(case["track"] for case in results["cases"] if case["id"] == case_id)
        lines.append(f"| `{case_id}` | `{track}` | `{base_mark}` | `{skill_mark}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    cases, truth_map = load_cases(args.case_ids)
    batches = chunked(cases, args.batch_size)
    bench_dir = BENCH_ROOT / f"v14-public-dev-results-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    bench_dir.mkdir(parents=True, exist_ok=True)

    results: dict[str, Any] = {
        "timestamp": datetime.now().astimezone().isoformat(),
        "version": "v14",
        "benchmark": "public_dev",
        "model": args.model,
        "reasoning_effort": args.reasoning_effort,
        "case_count": len(cases),
        "cases": [{"id": case["id"], "title": case["title"], "track": case["track"]} for case in cases],
        "runs": {},
        "bench_dir": str(bench_dir),
    }

    if not args.skip_base:
        base_result = run_batches(
            "base",
            BASE_HOME,
            batches,
            args.model,
            args.reasoning_effort,
            args.timeout_seconds,
            bench_dir,
        )
        results["runs"]["base"] = build_summary(base_result, cases, truth_map)

    if not args.skip_skill:
        skill_result = run_batches(
            "skill",
            SKILL_HOME,
            batches,
            args.model,
            args.reasoning_effort,
            args.timeout_seconds,
            bench_dir,
        )
        results["runs"]["skill"] = build_summary(skill_result, cases, truth_map)

    if "base" in results["runs"] and "skill" in results["runs"]:
        base_predictions = {
            case["id"]: case["prediction"] for case in results["runs"]["base"]["cases"]
        }
        skill_predictions = {
            case["id"]: case["prediction"] for case in results["runs"]["skill"]["cases"]
        }
        differing_case_ids = [
            case["id"] for case in cases if base_predictions.get(case["id"]) != skill_predictions.get(case["id"])
        ]
        results["comparison"] = {
            "prediction_diff_count": len(differing_case_ids),
            "differing_case_ids": differing_case_ids,
        }

    RESULTS_PATH.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n")
    REPORT_PATH.write_text(render_report(results))
    print(f"wrote {RESULTS_PATH}")
    print(f"wrote {REPORT_PATH}")


if __name__ == "__main__":
    main()
