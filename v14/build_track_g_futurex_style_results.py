#!/usr/bin/env python3
"""Build repo-facing results for the 4-case Track G FutureX-style subset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
BENCH = ROOT.parent.parent / ".bench" / "v14-track-g-futurex-results-20260330-102819"
SUMMARY_PATH = BENCH / "summary.json"
CASES_PATH = ROOT / "public_dev_cases.json"
GROUND_TRUTH_PATH = ROOT / "public_dev_ground_truth.json"
OUT_JSON = ROOT / "track_g_futurex_style_results.json"
OUT_MD = ROOT / "track_g_futurex_style_results.md"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def build_payload() -> dict[str, Any]:
    summary = load_json(SUMMARY_PATH)
    case_map = {case["id"]: case for case in load_json(CASES_PATH)["cases"]}
    gt_map = {case["id"]: case for case in load_json(GROUND_TRUTH_PATH)["cases"]}
    base_map = {case["id"]: case for case in summary["runs"]["base"]["cases"]}
    skill_map = {case["id"]: case for case in summary["runs"]["skill"]["cases"]}

    cases = []
    for item in summary["cases"]:
        case = case_map[item["id"]]
        gt = gt_map[item["id"]]
        base = base_map[item["id"]]
        skill = skill_map[item["id"]]
        cases.append(
            {
                "id": item["id"],
                "title": item["title"],
                "track": item["track"],
                "evaluation_regime": item["evaluation_regime"],
                "task_family": item["task_family"],
                "scenario": case["scenario"],
                "question": case["question"],
                "instantiated_inputs": case["instantiated_inputs"],
                "options": case["options"],
                "canonical_answer": gt["canonical_answer"],
                "evidence_summary": gt["evidence_summary"],
                "common_failure_modes": gt["common_failure_modes"],
                "base_prediction": base["prediction"],
                "base_field_results": base["field_results"],
                "base_exact_primary_correct": base["exact_primary_correct"],
                "base_weighted_score": base["weighted_score"],
                "skill_prediction": skill["prediction"],
                "skill_field_results": skill["field_results"],
                "skill_exact_primary_correct": skill["exact_primary_correct"],
                "skill_weighted_score": skill["weighted_score"],
            }
        )

    return {
        "benchmark": summary["benchmark"],
        "timestamp": summary["timestamp"],
        "model": summary["model"],
        "reasoning_effort": summary["reasoning_effort"],
        "case_count": summary["case_count"],
        "comparison": summary["comparison"],
        "runs": {
            "base": summary["runs"]["base"]["summary"],
            "skill": summary["runs"]["skill"]["summary"],
        },
        "cases": cases,
    }


def build_markdown(payload: dict[str, Any]) -> str:
    lines = [
        "# v14 Track G FutureX-Style Subset",
        "",
        f"Run timestamp: `{payload['timestamp']}`",
        f"Case count: `{payload['case_count']}`",
        f"Prediction differences: `{payload['comparison']['prediction_diff_count']}`",
        "",
        "| Run | Exact-primary | Weighted average | Duration (s) |",
        "|-----|---------------|------------------|--------------|",
        f"| `base` | `{payload['runs']['base']['exact_primary_correct']}/{payload['runs']['base']['case_count']}` | `{payload['runs']['base']['weighted_average']:.4f}` | `{payload['runs']['base']['total_duration_seconds']:.2f}` |",
        f"| `skill` | `{payload['runs']['skill']['exact_primary_correct']}/{payload['runs']['skill']['case_count']}` | `{payload['runs']['skill']['weighted_average']:.4f}` | `{payload['runs']['skill']['total_duration_seconds']:.2f}` |",
        "",
        "## Per-Case Status",
        "",
        "| Case ID | Canonical Label | Base Exact | Skill Exact | Base Weighted | Skill Weighted |",
        "|---------|-----------------|------------|-------------|---------------|----------------|",
    ]

    for case in payload["cases"]:
        lines.append(
            f"| `{case['id']}` | `{case['canonical_answer']['label']}` | "
            f"`{int(case['base_exact_primary_correct'])}` | `{int(case['skill_exact_primary_correct'])}` | "
            f"`{case['base_weighted_score']:.2f}` | `{case['skill_weighted_score']:.2f}` |"
        )

    lines.extend(["", "## Full Cases", ""])
    for case in payload["cases"]:
        lines.extend(
            [
                f"### {case['id']} — {case['title']}",
                "",
                f"- Track: `{case['track']}`",
                f"- Evaluation regime: `{case['evaluation_regime']}`",
                f"- Task family: `{case['task_family']}`",
                "",
                f"Scenario: {case['scenario']}",
                "",
                f"Question: {case['question']}",
                "",
                "Inputs:",
            ]
        )
        for item in case["instantiated_inputs"]:
            lines.append(f"- {item['title']}: {item['content']}")
        lines.extend(["", "Options:"])
        for option in case["options"]:
            lines.append(f"- `{option['label']}`: {option['text']}")
        lines.extend(
            [
                "",
                "Ground truth canonical answer:",
                "",
                "```json",
                json.dumps(case["canonical_answer"], ensure_ascii=False, indent=2),
                "```",
                "",
                "Evidence summary:",
            ]
        )
        for item in case["evidence_summary"]:
            lines.append(f"- {item}")
        lines.extend(["", "Common failure modes:"])
        for item in case["common_failure_modes"]:
            lines.append(f"- {item}")
        lines.extend(
            [
                "",
                f"Base prediction: `{json.dumps(case['base_prediction'], ensure_ascii=False)}`",
                f"Base field results: `{json.dumps(case['base_field_results'], ensure_ascii=False)}`",
                f"Base exact-primary: `{int(case['base_exact_primary_correct'])}` | weighted `{case['base_weighted_score']:.2f}`",
                "",
                f"Skill prediction: `{json.dumps(case['skill_prediction'], ensure_ascii=False)}`",
                f"Skill field results: `{json.dumps(case['skill_field_results'], ensure_ascii=False)}`",
                f"Skill exact-primary: `{int(case['skill_exact_primary_correct'])}` | weighted `{case['skill_weighted_score']:.2f}`",
                "",
            ]
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    payload = build_payload()
    write_json(OUT_JSON, payload)
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
