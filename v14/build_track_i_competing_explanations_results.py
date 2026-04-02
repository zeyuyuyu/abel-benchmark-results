#!/usr/bin/env python3
"""Build repo-facing results for Track I competing-explanations benchmark."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
QUESTIONS_PATH = ROOT / "track_i_competing_explanations_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_i_competing_explanations_ground_truth.json"
OUT_JSON = ROOT / "track_i_competing_explanations_results.json"
OUT_MD = ROOT / "track_i_competing_explanations_results.md"
NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("summary_path", type=Path)
    parser.add_argument("--questions-path", type=Path, default=QUESTIONS_PATH)
    parser.add_argument("--ground-truth-path", type=Path, default=GROUND_TRUTH_PATH)
    parser.add_argument("--out-json", type=Path, default=OUT_JSON)
    parser.add_argument("--out-md", type=Path, default=OUT_MD)
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_text(text: str | None) -> str:
    if text is None:
        return ""
    lowered = text.lower()
    lowered = NON_ALNUM_RE.sub(" ", lowered)
    return " ".join(lowered.split())


def is_valid(prediction: str | None) -> bool:
    return bool(normalize_text(prediction))


def matches_keyword_sets(prediction: str | None, match_any: list[list[list[str]]]) -> bool:
    text = normalize_text(prediction)
    if not text:
        return False
    for keyword_set in match_any:
        if all(any(normalize_text(term) in text for term in group) for group in keyword_set):
            return True
    return False


def mark(pred: str | None, ok: bool) -> str:
    if pred is None:
        return "`None`"
    return f"`{pred}`{' ✅' if ok else ' ❌'}"


def winner_label(row: dict[str, Any]) -> str:
    if row["skill_exact_correct"] and not row["base_exact_correct"]:
        return "skill"
    if row["base_exact_correct"] and not row["skill_exact_correct"]:
        return "base"
    return "tie"


def build_outputs(
    summary: dict[str, Any],
    *,
    questions_path: Path,
    ground_truth_path: Path,
) -> tuple[dict[str, Any], str]:
    questions_payload = load_json(questions_path)
    questions = {case["id"]: case for case in questions_payload["cases"]}
    truths = {case["id"]: case for case in load_json(ground_truth_path)["cases"]}
    judge_meta = summary.get("judge")

    enriched: list[dict[str, Any]] = []
    for row in summary["cases"]:
        q = questions[row["id"]]
        t = truths[row["id"]]
        base_primary = row.get("base_primary_prediction")
        base_followup = row.get("base_followup_prediction")
        skill_primary = row.get("skill_primary_prediction")
        skill_followup = row.get("skill_followup_prediction")
        base_primary_ok = bool(row.get("base_primary_correct")) if "base_primary_correct" in row else matches_keyword_sets(base_primary, t["primary_match_any"])
        base_followup_ok = bool(row.get("base_followup_correct")) if "base_followup_correct" in row else matches_keyword_sets(base_followup, t["followup_match_any"])
        skill_primary_ok = bool(row.get("skill_primary_correct")) if "skill_primary_correct" in row else matches_keyword_sets(skill_primary, t["primary_match_any"])
        skill_followup_ok = bool(row.get("skill_followup_correct")) if "skill_followup_correct" in row else matches_keyword_sets(skill_followup, t["followup_match_any"])
        enriched.append(
            {
                "id": row["id"],
                "title": q["title"],
                "task_family": q["task_family"],
                "source_case_id": q["source_case_id"],
                "scenario": q.get("scenario", ""),
                "question": q.get("question", ""),
                "followup_question": q.get("followup_question", ""),
                "instantiated_inputs": q.get("instantiated_inputs", []),
                "naturalness_rationale": q.get("naturalness_rationale", ""),
                "primary_answer_text": t["primary_answer_text"],
                "followup_answer_text": t["followup_answer_text"],
                "canonical_answer": t.get("canonical_answer"),
                "evidence_summary": t.get("evidence_summary", []),
                "common_failure_modes": t.get("common_failure_modes", []),
                "base_primary_prediction": base_primary,
                "base_followup_prediction": base_followup,
                "skill_primary_prediction": skill_primary,
                "skill_followup_prediction": skill_followup,
                "base_primary_valid": is_valid(base_primary),
                "base_followup_valid": is_valid(base_followup),
                "skill_primary_valid": is_valid(skill_primary),
                "skill_followup_valid": is_valid(skill_followup),
                "base_primary_correct": base_primary_ok,
                "base_followup_correct": base_followup_ok,
                "skill_primary_correct": skill_primary_ok,
                "skill_followup_correct": skill_followup_ok,
                "base_exact_correct": base_primary_ok and base_followup_ok,
                "skill_exact_correct": skill_primary_ok and skill_followup_ok,
                "judge_notes": row.get("judge_notes", ""),
                "exact_winner": "",
            }
        )
        enriched[-1]["exact_winner"] = winner_label(enriched[-1])

    result_json = {
        "timestamp": summary["timestamp"],
        "benchmark": "v14_track_i_competing_explanations",
        "pack_variant": questions_payload.get("pack_variant"),
        "case_count": len(enriched),
        "base": summary["runs"]["base"],
        "skill": summary["runs"]["skill"],
        "cases": enriched,
        "source_summary_path": str(summary.get("source_summary_path", "")),
        "judge": judge_meta,
    }

    total = len(enriched)
    lines = [
        "# v14 Track I Competing Explanations Results",
        "",
        f"Full Track I run over `{total}` cases.",
        "",
        "## Scoreboard",
        "",
    ]
    if judge_meta:
        lines.append(f"- Scoring: `LLM semantic judge ({judge_meta['model']})`")
        lines.append("")
    lines.extend(
        [
        f"- Base exact raw: `{summary['runs']['base']['correct_case_count']}/{total} = {summary['runs']['base']['accuracy']:.2%}`",
        f"- Skill exact raw: `{summary['runs']['skill']['correct_case_count']}/{total} = {summary['runs']['skill']['accuracy']:.2%}`",
        f"- Base primary-only: `{summary['runs']['base']['primary_correct_case_count']}/{total} = {summary['runs']['base']['primary_accuracy']:.2%}`",
        f"- Skill primary-only: `{summary['runs']['skill']['primary_correct_case_count']}/{total} = {summary['runs']['skill']['primary_accuracy']:.2%}`",
        f"- Base follow-up-only: `{summary['runs']['base']['followup_correct_case_count']}/{total} = {summary['runs']['base']['followup_accuracy']:.2%}`",
        f"- Skill follow-up-only: `{summary['runs']['skill']['followup_correct_case_count']}/{total} = {summary['runs']['skill']['followup_accuracy']:.2%}`",
        f"- Base exact valid outputs: `{summary['runs']['base']['valid_case_count']}/{total}`",
        f"- Skill exact valid outputs: `{summary['runs']['skill']['valid_case_count']}/{total}`",
        f"- Base duration: `{summary['runs']['base']['duration_seconds']:.2f}s`",
        f"- Skill duration: `{summary['runs']['skill']['duration_seconds']:.2f}s`",
        "",
        "## Case Overview",
        "",
        "| Case ID | Source | Family | Canonical primary | Base primary | Skill primary | Canonical follow-up | Base follow-up | Skill follow-up | Exact winner |",
        "|---|---|---|---|---|---|---|---|---|---|",
        ]
    )
    for row in enriched:
        lines.append(
            f"| `{row['id']}` | `{row['source_case_id']}` | `{row['task_family']}` | "
            f"`{row['primary_answer_text']}` | {mark(row['base_primary_prediction'], row['base_primary_correct'])} | "
            f"{mark(row['skill_primary_prediction'], row['skill_primary_correct'])} | "
            f"`{row['followup_answer_text']}` | {mark(row['base_followup_prediction'], row['base_followup_correct'])} | "
            f"{mark(row['skill_followup_prediction'], row['skill_followup_correct'])} | `{row['exact_winner']}` |"
        )

    lines.extend(["", "## Full Cases", ""])
    for row in enriched:
        lines.extend(
            [
                f"### {row['id']} — {row['title']}",
                "",
                f"- Source case: `{row['source_case_id']}`",
                f"- Family: `{row['task_family']}`",
                f"- Exact winner: `{row['exact_winner']}`",
                f"- Base exact: `{'correct' if row['base_exact_correct'] else 'incorrect'}`",
                f"- Skill exact: `{'correct' if row['skill_exact_correct'] else 'incorrect'}`",
                f"- Base field score: `{int(row['base_primary_correct']) + int(row['base_followup_correct'])}/2`",
                f"- Skill field score: `{int(row['skill_primary_correct']) + int(row['skill_followup_correct'])}/2`",
                "",
                "Scenario:",
                row["scenario"] or "_None_",
                "",
                f"Primary question: {row['question']}",
                f"Follow-up question: {row['followup_question']}",
                "",
                "Evidence packet:",
            ]
        )
        for item in row["instantiated_inputs"]:
            lines.append(f"- {item['title']} ({item['type']}): {item['content']}")
        if row["naturalness_rationale"]:
            lines.extend(["", f"Naturalness rationale: {row['naturalness_rationale']}"])
        lines.extend(
            [
                "",
                "Ground truth:",
                f"- Canonical primary: `{row['primary_answer_text']}`",
                f"- Canonical follow-up: `{row['followup_answer_text']}`",
            ]
        )
        if row["evidence_summary"]:
            lines.append("Evidence summary:")
            for item in row["evidence_summary"]:
                lines.append(f"- {item}")
        if row["common_failure_modes"]:
            lines.append("Common failure modes:")
            for item in row["common_failure_modes"]:
                lines.append(f"- {item}")
        if row["canonical_answer"] is not None:
            lines.extend(
                [
                    "Canonical answer object:",
                    "```json",
                    json.dumps(row["canonical_answer"], ensure_ascii=False, indent=2),
                    "```",
                ]
            )
        lines.extend(
            [
                "",
                "Model replies:",
                f"- Base primary: {mark(row['base_primary_prediction'], row['base_primary_correct'])}",
                f"- Base follow-up: {mark(row['base_followup_prediction'], row['base_followup_correct'])}",
                f"- Skill primary: {mark(row['skill_primary_prediction'], row['skill_primary_correct'])}",
                f"- Skill follow-up: {mark(row['skill_followup_prediction'], row['skill_followup_correct'])}",
            ]
        )
        if row["judge_notes"]:
            lines.extend(["", f"Judge notes: {row['judge_notes']}"])
        lines.append("")

    lines.extend(["", "## Per-Family", ""])
    for family in sorted(summary["runs"]["base"]["family_scores"]):
        base = summary["runs"]["base"]["family_scores"][family]
        skill = summary["runs"]["skill"]["family_scores"][family]
        lines.append(
            f"- `{family}`: base exact `{base['correct']}/{base['case_count']}`, "
            f"skill exact `{skill['correct']}/{skill['case_count']}`"
        )

    return result_json, "\n".join(lines).rstrip() + "\n"


def main() -> None:
    args = parse_args()
    summary = load_json(args.summary_path)
    summary["source_summary_path"] = args.summary_path.name
    result_json, markdown = build_outputs(
        summary,
        questions_path=args.questions_path,
        ground_truth_path=args.ground_truth_path,
    )
    args.out_json.write_text(json.dumps(result_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.out_md.write_text(markdown, encoding="utf-8")
    print(f"Wrote {args.out_json}")
    print(f"Wrote {args.out_md}")


if __name__ == "__main__":
    main()
