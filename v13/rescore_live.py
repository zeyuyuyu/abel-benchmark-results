#!/usr/bin/env python3
"""Backfill live benchmark ground truth and scores."""

from __future__ import annotations

import ast
import argparse
import json
import math
import re
from functools import lru_cache
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yfinance as yf
from datasets import load_dataset


ROOT = Path(__file__).resolve().parent
RESULTS_PATH = ROOT / "results.json"
GROUND_TRUTH_PATH = ROOT / "ground_truth.json"
REPORT_PATH = ROOT / "benchmark_report.md"
FUTUREX_PAST_DATASET = "futurex-ai/Futurex-Past"
BOXED_RE = re.compile(r"^\\boxed\{(?:Yes|No|[A-Z](?:, ?[A-Z])*)\}$")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def boxed_from_tokens(tokens: list[str]) -> str:
    return "\\boxed{" + ", ".join(tokens) + "}"


def normalize_tokens(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return sorted(str(item).strip() for item in value if str(item).strip())
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return []
        try:
            parsed = ast.literal_eval(stripped)
        except Exception:  # noqa: BLE001
            parsed = stripped
        if isinstance(parsed, list):
            return sorted(str(item).strip() for item in parsed if str(item).strip())
        if parsed in {"Yes", "No"}:
            return [str(parsed)]
        return sorted(part.strip() for part in stripped.split(",") if part.strip())
    return [str(value).strip()]


def extract_prediction_tokens(prediction: str | None) -> list[str]:
    if not prediction or not BOXED_RE.fullmatch(prediction.strip()):
        return []
    inner = prediction.strip()[len("\\boxed{") : -1]
    return sorted(part.strip() for part in inner.split(",") if part.strip())


@lru_cache(maxsize=None)
def fetch_history(symbol: str, start_date: str, end_date: str) -> Any:
    end_dt = datetime.fromisoformat(end_date) + timedelta(days=2)
    hist = yf.Ticker(symbol).history(
        start=start_date,
        end=end_dt.date().isoformat(),
        interval="1d",
        auto_adjust=False,
    )
    return hist.dropna(subset=["Close"])


@lru_cache(maxsize=None)
def fetch_close_on(symbol: str, resolution_date: str) -> float | None:
    hist = fetch_history(symbol, resolution_date, resolution_date)
    if hist.empty:
        return None
    return float(hist.iloc[-1]["Close"])


def resolve_custom(spec: dict[str, Any]) -> tuple[list[str] | None, dict[str, Any] | None]:
    method = spec["method"]
    if method == "close_bucket":
        close_value = fetch_close_on(spec["symbol"], spec["resolution_date"])
        if close_value is None:
            return None, None
        for bucket in spec["buckets"]:
            if bucket["type"] == "lt" and close_value < bucket["value"]:
                return [bucket["label"]], {"close": close_value}
            if bucket["type"] == "ge" and close_value >= bucket["value"]:
                return [bucket["label"]], {"close": close_value}
            if bucket["type"] == "range" and bucket["lower"] <= close_value < bucket["upper"]:
                return [bucket["label"]], {"close": close_value}
        return None, {"close": close_value}

    if method == "close_threshold_truths":
        close_value = fetch_close_on(spec["symbol"], spec["resolution_date"])
        if close_value is None:
            return None, None
        tokens = [
            item["label"]
            for item in spec["thresholds"]
            if item["operator"] == "gt" and close_value > item["value"]
        ]
        return sorted(tokens), {"close": close_value}

    if method == "hit_levels":
        hist = fetch_history(spec["symbol"], spec["start_date"], spec["resolution_date"])
        if hist.empty:
            return None, None
        max_high = float(hist["High"].max())
        min_low = float(hist["Low"].min())
        tokens = []
        for item in spec["levels"]:
            if item["direction"] == "high" and max_high >= item["value"]:
                tokens.append(item["label"])
            if item["direction"] == "low" and min_low <= item["value"]:
                tokens.append(item["label"])
        return sorted(tokens), {"max_high": max_high, "min_low": min_low}

    if method == "winner_by_return":
        outcomes = []
        for label, item in spec["symbols"].items():
            close_value = fetch_close_on(item["symbol"], spec["resolution_date"])
            if close_value is None:
                return None, None
            ref_close = float(item["reference_close"])
            pct_return = (close_value - ref_close) / ref_close
            outcomes.append((pct_return, label, close_value))
        outcomes.sort(reverse=True)
        return [outcomes[0][1]], {
            "returns": {
                label: round(pct, 6)
                for pct, label, _close in outcomes
            }
        }

    if method == "membership_above_reference":
        tokens = []
        closes: dict[str, float] = {}
        for label, item in spec["symbols"].items():
            close_value = fetch_close_on(item["symbol"], spec["resolution_date"])
            if close_value is None:
                return None, None
            closes[label] = close_value
            if close_value > float(item["reference_close"]):
                tokens.append(label)
        return sorted(tokens), {"closes": closes}

    if method == "binary_close_threshold":
        close_value = fetch_close_on(spec["symbol"], spec["resolution_date"])
        if close_value is None:
            return None, None
        outcome = close_value > spec["value"] if spec["operator"] == "gt" else close_value < spec["value"]
        return (["Yes"] if outcome else ["No"]), {"close": close_value}

    raise ValueError(f"Unsupported custom resolution method: {method}")


def resolve_case_spec(
    spec: dict[str, Any],
    *,
    futurex_row_map: dict[str, Any],
) -> tuple[list[str] | None, dict[str, Any] | None]:
    if spec["source"] == "futurex_past_backfill":
        row = futurex_row_map.get(spec["source_id"])
        if row is None:
            return None, None
        return normalize_tokens(row["ground_truth"]), {
            "source_dataset": FUTUREX_PAST_DATASET,
            "source_id": spec["source_id"],
        }
    return resolve_custom(spec)


def backfill_ground_truth_cases(
    cases: list[dict[str, Any]],
    *,
    futurex_row_map: dict[str, Any],
) -> dict[str, int]:
    resolved_count = 0
    pending_count = 0
    for gt_entry in cases:
        resolved_tokens, resolved_meta = resolve_case_spec(
            gt_entry["resolution_spec"],
            futurex_row_map=futurex_row_map,
        )
        if resolved_tokens is None:
            gt_entry["status"] = "pending"
            gt_entry["answer_tokens"] = []
            gt_entry["answer_box"] = None
            gt_entry.pop("resolved_meta", None)
            pending_count += 1
            continue
        gt_entry["status"] = "resolved"
        gt_entry["answer_tokens"] = resolved_tokens
        gt_entry["answer_box"] = boxed_from_tokens(resolved_tokens)
        gt_entry["resolved_meta"] = resolved_meta
        resolved_count += 1
    return {"resolved": resolved_count, "pending": pending_count}


def render_report(results: dict[str, Any]) -> str:
    scoring = results["scoring"]
    lines = [
        "# v13 Live-Only Finance A/B",
        "",
        f"Run timestamp: `{results['timestamp']}`",
        "",
        f"Last rescored: `{scoring['rescored_at']}`",
        "",
        "This benchmark is live-only by design, so unresolved tasks remain pending until third-party sources can settle them.",
        "",
        "| Run | Cases | Valid boxed outputs | Correct on resolved subset | Accuracy on resolved subset | Duration (s) |",
        "|-----|-------|---------------------|----------------------------|-----------------------------|--------------|",
        f"| `base` | `{results['case_count']}` | `{results['runs']['base']['valid_prediction_count']}/{results['case_count']}` | `{scoring['base_correct_count']}/{scoring['resolved_case_count']}` | `{scoring['base_accuracy']}` | `{results['runs']['base']['duration_seconds']:.2f}` |" if scoring["resolved_case_count"] else f"| `base` | `{results['case_count']}` | `{results['runs']['base']['valid_prediction_count']}/{results['case_count']}` | `pending` | `pending` | `{results['runs']['base']['duration_seconds']:.2f}` |",
        f"| `skill` | `{results['case_count']}` | `{results['runs']['skill']['valid_prediction_count']}/{results['case_count']}` | `{scoring['skill_correct_count']}/{scoring['resolved_case_count']}` | `{scoring['skill_accuracy']}` | `{results['runs']['skill']['duration_seconds']:.2f}` |" if scoring["resolved_case_count"] else f"| `skill` | `{results['case_count']}` | `{results['runs']['skill']['valid_prediction_count']}/{results['case_count']}` | `pending` | `pending` | `{results['runs']['skill']['duration_seconds']:.2f}` |",
        "",
        f"- Prediction differences: `{results['summary']['prediction_diff_count']}`",
        f"- Resolved cases: `{scoring['resolved_case_count']}/{results['case_count']}`",
        f"- Pending cases: `{scoring['pending_case_count']}`",
        "",
        "## Per-Case Status",
        "",
        "| Case ID | Source | Ground Truth | Base | Skill | Status |",
        "|---------|--------|--------------|------|-------|--------|",
    ]
    for case in results["cases"]:
        if case.get("resolved"):
            if case["base_correct"] and case["skill_correct"]:
                status = "both correct"
            elif case["base_correct"] and not case["skill_correct"]:
                status = "base only"
            elif not case["base_correct"] and case["skill_correct"]:
                status = "skill only"
            else:
                status = "both incorrect"
        else:
            status = "pending"
        lines.append(
            f"| `{case['id']}` | `{case['source_type']}` | `{case.get('answer_box') or 'pending'}` | `{case.get('base_prediction')}` | `{case.get('skill_prediction')}` | {status} |"
        )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-path", type=Path, default=RESULTS_PATH)
    parser.add_argument("--ground-truth-path", type=Path, default=GROUND_TRUTH_PATH)
    parser.add_argument("--report-path", type=Path, default=REPORT_PATH)
    parser.add_argument("--ground-truth-only", action="store_true")
    parser.add_argument("--skip-backfill", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ground_truth = load_json(args.ground_truth_path)
    if args.skip_backfill:
        backfill_counts = {
            "resolved": sum(1 for item in ground_truth["cases"] if item.get("status") == "resolved"),
            "pending": sum(1 for item in ground_truth["cases"] if item.get("status") != "resolved"),
        }
    else:
        futurex_past = load_dataset(FUTUREX_PAST_DATASET, split="train")
        futurex_row_map = {row["id"]: row for row in futurex_past}
        backfill_counts = backfill_ground_truth_cases(
            ground_truth["cases"],
            futurex_row_map=futurex_row_map,
        )
        write_json(args.ground_truth_path, ground_truth)

    if args.ground_truth_only:
        print(json.dumps(backfill_counts, indent=2, ensure_ascii=False))
        return

    results = load_json(args.results_path)

    base_prediction_map = {item["id"]: item["prediction"] for item in results["runs"]["base"]["predictions"]}
    skill_prediction_map = {item["id"]: item["prediction"] for item in results["runs"]["skill"]["predictions"]}
    gt_map = {item["id"]: item for item in ground_truth["cases"]}

    resolved_count = 0
    base_correct_count = 0
    skill_correct_count = 0

    for case in results["cases"]:
        gt_entry = gt_map[case["id"]]
        resolved_tokens = gt_entry.get("answer_tokens", [])
        case["ground_truth_status"] = gt_entry.get("status", "pending")

        if gt_entry.get("status") == "resolved":
            answer_box = gt_entry["answer_box"]
            case["resolved"] = True
            case["answer_box"] = answer_box
            base_tokens = extract_prediction_tokens(base_prediction_map.get(case["id"]))
            skill_tokens = extract_prediction_tokens(skill_prediction_map.get(case["id"]))
            case["base_prediction"] = base_prediction_map.get(case["id"])
            case["skill_prediction"] = skill_prediction_map.get(case["id"])
            case["base_correct"] = base_tokens == sorted(resolved_tokens)
            case["skill_correct"] = skill_tokens == sorted(resolved_tokens)
            resolved_count += 1
            base_correct_count += int(case["base_correct"])
            skill_correct_count += int(case["skill_correct"])
        else:
            gt_entry["status"] = "pending"
            case["resolved"] = False
            case["answer_box"] = None
            case["base_prediction"] = base_prediction_map.get(case["id"])
            case["skill_prediction"] = skill_prediction_map.get(case["id"])
            case["base_correct"] = None
            case["skill_correct"] = None

    results["scoring"] = {
        "rescored_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "resolved_case_count": resolved_count,
        "pending_case_count": results["case_count"] - resolved_count,
        "base_correct_count": base_correct_count,
        "skill_correct_count": skill_correct_count,
        "base_accuracy": round(base_correct_count / resolved_count, 4) if resolved_count else None,
        "skill_accuracy": round(skill_correct_count / resolved_count, 4) if resolved_count else None,
    }

    write_json(args.results_path, results)
    args.report_path.write_text(render_report(results), encoding="utf-8")
    print(json.dumps(results["scoring"], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
