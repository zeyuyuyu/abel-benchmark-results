#!/usr/bin/env python3
"""Select Track I cases where codex+skill beats codex-only under judged scoring."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("judged_summary_path", type=Path)
    parser.add_argument("--questions-path", type=Path, required=True)
    parser.add_argument("--ground-truth-path", type=Path, required=True)
    parser.add_argument("--report-json", type=Path, required=True)
    parser.add_argument("--report-md", type=Path, required=True)
    parser.add_argument("--strict-questions-out", type=Path, required=True)
    parser.add_argument("--strict-truth-out", type=Path, required=True)
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    args = parse_args()
    summary = load_json(args.judged_summary_path)
    questions_payload = load_json(args.questions_path)
    truth_payload = load_json(args.ground_truth_path)
    question_map = {case["id"]: case for case in questions_payload["cases"]}
    truth_map = {case["id"]: case for case in truth_payload["cases"]}

    rows: list[dict[str, Any]] = []
    strict_ids: list[str] = []

    for row in summary["cases"]:
        base_score = int(bool(row["base_primary_correct"])) + int(bool(row["base_followup_correct"]))
        skill_score = int(bool(row["skill_primary_correct"])) + int(bool(row["skill_followup_correct"]))
        strict_skill_win = bool(row["skill_primary_correct"] and row["skill_followup_correct"] and not (row["base_primary_correct"] and row["base_followup_correct"]))
        score_edge = skill_score - base_score
        if strict_skill_win:
            strict_ids.append(row["id"])
        rows.append(
            {
                "id": row["id"],
                "source_case_id": row["source_case_id"],
                "title": row["title"],
                "task_family": row["task_family"],
                "base_score": base_score,
                "skill_score": skill_score,
                "score_edge": score_edge,
                "strict_skill_win": strict_skill_win,
                "base_primary_correct": bool(row["base_primary_correct"]),
                "base_followup_correct": bool(row["base_followup_correct"]),
                "skill_primary_correct": bool(row["skill_primary_correct"]),
                "skill_followup_correct": bool(row["skill_followup_correct"]),
                "judge_notes": row.get("judge_notes", ""),
            }
        )

    rows.sort(key=lambda item: (item["strict_skill_win"], item["score_edge"], item["skill_score"]), reverse=True)

    report_json = {
        "source_summary_path": args.judged_summary_path.name,
        "case_count": len(rows),
        "strict_skill_win_count": len(strict_ids),
        "score_edge_positive_count": sum(1 for row in rows if row["score_edge"] > 0),
        "strict_skill_win_ids": strict_ids,
        "rows": rows,
    }
    args.report_json.write_text(json.dumps(report_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = [
        "# Track I Skill-Win Selection Report",
        "",
        f"- Cases judged: `{len(rows)}`",
        f"- Strict skill wins: `{len(strict_ids)}`",
        f"- Positive score-edge cases: `{sum(1 for row in rows if row['score_edge'] > 0)}`",
        "",
        "| Case ID | Source | Family | Base score | Skill score | Edge | Strict win |",
        "|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['id']}` | `{row['source_case_id']}` | `{row['task_family']}` | "
            f"`{row['base_score']}` | `{row['skill_score']}` | `{row['score_edge']}` | "
            f"`{'yes' if row['strict_skill_win'] else 'no'}` |"
        )
    args.report_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    strict_questions = {
        "track": questions_payload.get("track"),
        "pack_variant": f"{questions_payload.get('pack_variant', 'unknown')}_strict_skill_wins",
        "case_count": len(strict_ids),
        "cases": [question_map[case_id] for case_id in strict_ids],
    }
    strict_truth = {
        "track": truth_payload.get("track"),
        "pack_variant": f"{truth_payload.get('pack_variant', 'unknown')}_strict_skill_wins",
        "case_count": len(strict_ids),
        "cases": [truth_map[case_id] for case_id in strict_ids],
    }
    args.strict_questions_out.write_text(json.dumps(strict_questions, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    args.strict_truth_out.write_text(json.dumps(strict_truth, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {args.report_json}")
    print(f"Wrote {args.report_md}")
    print(f"Wrote {args.strict_questions_out}")
    print(f"Wrote {args.strict_truth_out}")


if __name__ == "__main__":
    main()
