#!/usr/bin/env python3
"""Build repo-facing results for the v14 Track G past-asof benchmark."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
QUESTIONS_PATH = ROOT / "track_g_past_asof_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_g_past_asof_ground_truth.json"
OUT_JSON = ROOT / "track_g_past_asof_results.json"
OUT_MD = ROOT / "track_g_past_asof_results.md"
BOXED_RE = re.compile(r"^\\boxed\{(?P<inner>.*)\}$", re.DOTALL)
LETTER_TOKEN_RE = re.compile(r"^[A-Z]$")
LETTER_LIST_RE = re.compile(r"^[A-Z](?:, ?[A-Z])*$")
COMPACT_LETTER_LIST_RE = re.compile(r"^[A-Z]{2,}$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("summary_path", type=Path)
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_token(token: str) -> str:
    return re.sub(r"\s+", " ", token.strip())


def extract_prediction_tokens(prediction: str | None, gold_tokens: list[str]) -> list[str]:
    if not prediction:
        return []
    match = BOXED_RE.fullmatch(prediction.strip())
    if not match:
        return []

    inner = normalize_token(match.group("inner"))
    normalized_gold = [normalize_token(token) for token in gold_tokens]
    if not normalized_gold:
        return []
    if len(normalized_gold) == 1:
        return [inner]

    if all(LETTER_TOKEN_RE.fullmatch(token) for token in normalized_gold):
        if LETTER_LIST_RE.fullmatch(inner):
            return sorted(part.strip() for part in inner.split(",") if part.strip())
        if COMPACT_LETTER_LIST_RE.fullmatch(inner) and len(inner) == len(normalized_gold):
            return sorted(list(inner))

    parts = [normalize_token(part) for part in inner.split(",")]
    if len(parts) != len(normalized_gold):
        return []
    return sorted(parts)


def mark(prediction: str | None, correct: bool) -> str:
    if prediction is None:
        return "`None`"
    suffix = " ✅" if correct else " ❌"
    return f"`{prediction}`{suffix}"


def build_outputs(summary: dict[str, Any]) -> tuple[dict[str, Any], str]:
    questions = {item["id"]: item for item in load_json(QUESTIONS_PATH)["cases"]}
    truth = {item["id"]: item for item in load_json(GROUND_TRUTH_PATH)["cases"]}

    enriched_cases: list[dict[str, Any]] = []
    for case in summary["cases"]:
        q = questions[case["id"]]
        t = truth[case["id"]]
        base_prediction = case.get("base_prediction")
        skill_prediction = case.get("skill_prediction")
        answer_box = t["answer_box"]
        gold_tokens = sorted(normalize_token(token) for token in t["answer_tokens"])
        base_tokens = extract_prediction_tokens(base_prediction, t["answer_tokens"])
        skill_tokens = extract_prediction_tokens(skill_prediction, t["answer_tokens"])
        base_correct = base_tokens == gold_tokens
        skill_correct = skill_tokens == gold_tokens
        enriched_cases.append(
            {
                "id": case["id"],
                "title": q["title"],
                "category": q["category"],
                "search_cutoff": q["search_cutoff"],
                "answer_box": answer_box,
                "base_prediction": base_prediction,
                "skill_prediction": skill_prediction,
                "base_correct": base_correct,
                "skill_correct": skill_correct,
                "base_valid": bool(base_tokens),
                "skill_valid": bool(skill_tokens),
            }
        )

    run_summaries: dict[str, dict[str, Any]] = {}
    for run_name in ("base", "skill"):
        correct_key = f"{run_name}_correct"
        valid_key = f"{run_name}_valid"
        category_scores: dict[str, dict[str, int]] = {}
        for case in enriched_cases:
            stats = category_scores.setdefault(case["category"], {"correct": 0, "case_count": 0})
            stats["case_count"] += 1
            if case[correct_key]:
                stats["correct"] += 1
        correct_case_count = sum(1 for case in enriched_cases if case[correct_key])
        valid_case_count = sum(1 for case in enriched_cases if case[valid_key])
        run_summaries[run_name] = {
            "correct_case_count": correct_case_count,
            "valid_case_count": valid_case_count,
            "accuracy": round(correct_case_count / len(enriched_cases), 4),
            "duration_seconds": summary["runs"][run_name]["duration_seconds"],
            "category_scores": category_scores,
        }

    result_json = {
        "timestamp": summary["timestamp"],
        "benchmark": "v14_track_g_past_asof",
        "case_count": len(enriched_cases),
        "base": run_summaries["base"],
        "skill": run_summaries["skill"],
        "cases": enriched_cases,
        "source_summary_path": str(summary.get("source_summary_path", "")),
    }

    total = len(enriched_cases)
    lines = [
        "# v14 Track G Past-As-Of Results",
        "",
        f"Full `historical_asof_search_cutoff` run over the {total}-case Track G pack.",
        "",
        f"- Base: `{run_summaries['base']['correct_case_count']}/{total} = {run_summaries['base']['accuracy']:.2%}`",
        f"- Skill: `{run_summaries['skill']['correct_case_count']}/{total} = {run_summaries['skill']['accuracy']:.2%}`",
        f"- Base valid outputs: `{run_summaries['base']['valid_case_count']}/{total}`",
        f"- Skill valid outputs: `{run_summaries['skill']['valid_case_count']}/{total}`",
        f"- Base duration: `{run_summaries['base']['duration_seconds']:.2f}s`",
        f"- Skill duration: `{run_summaries['skill']['duration_seconds']:.2f}s`",
        "",
        "| Case ID | Category | Cutoff | Ground truth | Base | Skill | Notes |",
        "|---|---|---|---|---|---|---|",
    ]
    for case in enriched_cases:
        notes: list[str] = []
        if not case["base_valid"]:
            notes.append("base_invalid_or_missing")
        if not case["skill_valid"]:
            notes.append("skill_invalid_or_missing")
        if not notes:
            notes.append("completed")
        lines.append(
            f"| `{case['id']}` | `{case['category']}` | `{case['search_cutoff']}` | "
            f"`{case['answer_box']}` | {mark(case['base_prediction'], case['base_correct'])} | "
            f"{mark(case['skill_prediction'], case['skill_correct'])} | {', '.join(notes)} |"
        )

    lines.extend(["", "## Per-Category", ""])
    for category in sorted(run_summaries["base"]["category_scores"]):
        base_stats = run_summaries["base"]["category_scores"][category]
        skill_stats = run_summaries["skill"]["category_scores"][category]
        lines.append(
            f"- `{category}`: base `{base_stats['correct']}/{base_stats['case_count']}`, "
            f"skill `{skill_stats['correct']}/{skill_stats['case_count']}`"
        )

    for case in enriched_cases:
        lines.extend(
            [
                "",
                f"## {case['id']} — {case['title']}",
                "",
                f"- Category: `{case['category']}`",
                f"- Search cutoff: `{case['search_cutoff']}`",
                f"- Ground truth: `{case['answer_box']}`",
                f"- `codex only`: {mark(case['base_prediction'], case['base_correct'])}",
                f"- `codex + skill`: {mark(case['skill_prediction'], case['skill_correct'])}",
            ]
        )

    return result_json, "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    summary = load_json(args.summary_path)
    summary["source_summary_path"] = args.summary_path.name
    result_json, markdown = build_outputs(summary)
    OUT_JSON.write_text(json.dumps(result_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUT_MD.write_text(markdown, encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
