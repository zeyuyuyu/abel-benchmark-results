from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
V13_ROOT = ROOT.parent / "v13"


def load_v13_live() -> tuple[dict, dict[str, dict]]:
    questions = json.loads((V13_ROOT / "questions.json").read_text())
    truth_items = json.loads((V13_ROOT / "ground_truth.json").read_text())["cases"]
    truth_map = {item["id"]: item for item in truth_items}
    return questions, truth_map


def build() -> tuple[dict, dict, str]:
    questions_doc, truth_map = load_v13_live()
    cases = []
    truths = []

    lines = [
        "# v14 Track G True Live Cases",
        "",
        "This markdown materializes the canonical true-live Track G pack.",
        "Questions are visible, but ground truth is intentionally blank until",
        "future third-party resolution arrives.",
        "",
        f"- Source mirror: `v13/questions.json`",
        f"- Case count: `{questions_doc['question_count']}`",
        "",
    ]

    for case in questions_doc["cases"]:
        truth = truth_map[case["id"]]
        case_obj = {
            "id": case["id"],
            "track": "agentic_live_analysis",
            "task_family": "futurex_style_live_prediction",
            "evaluation_regime": "live_forward_resolution",
            "source_family": ["FutureX-Online" if case.get("source_type") == "futurex_online" else "FutureX-custom-live"],
            "source_type": case.get("source_type"),
            "title": case["title"],
            "category": case.get("category"),
            "futurex_pattern": case.get("futurex_pattern"),
            "question": case["question"],
            "prompt": case.get("prompt"),
            "answer_format": case.get("answer_format"),
            "options": case.get("options", []),
            "end_time": case.get("end_time"),
            "source_casebook": "v13/questions.json",
            "source_case_id": case["id"],
        }
        cases.append(case_obj)

        truths.append(
            {
                "id": case["id"],
                "status": truth.get("status", "pending"),
                "answer_box": None,
                "answer_tokens": [],
                "resolution_spec": truth.get("resolution_spec"),
                "notes": [
                    "Ground truth intentionally blank until forward resolution completes.",
                    "Use the resolution_spec to know where and when the answer should be backfilled.",
                ],
            }
        )

        lines.extend(
            [
                f"## {case['id']} — {case['title']}",
                "",
                f"- Track: `agentic_live_analysis`",
                f"- Task family: `futurex_style_live_prediction`",
                f"- Evaluation regime: `live_forward_resolution`",
                f"- Source type: `{case.get('source_type', 'unknown')}`",
                f"- End time: `{case.get('end_time', 'unknown')}`",
                "",
                "Question:",
                "```text",
                case["question"],
                "```",
                "",
            ]
        )
        if case.get("options"):
            lines.append("Options:")
            for option in case["options"]:
                lines.append(f"- `{option['label']}`: {option['text']}")
            lines.append("")

        lines.extend(
            [
                "Ground truth:",
                "```text",
                "",
                "```",
                "",
                "Resolution spec:",
                "```json",
                json.dumps(truth.get("resolution_spec"), indent=2, ensure_ascii=False),
                "```",
                "",
            ]
        )

    casebook = {
        "version": "v14-track-g-true-live-questions",
        "split": "track_g_true_live",
        "case_count": len(cases),
        "notes": [
            "This pack is the canonical true-live Track G materialization in v14.",
            "All cases use evaluation_regime=live_forward_resolution.",
            "Ground truth must remain blank until forward resolution occurs.",
        ],
        "cases": cases,
    }
    ground_truth = {
        "version": "v14-track-g-true-live-ground-truth",
        "split": "track_g_true_live",
        "case_count": len(truths),
        "notes": [
            "Ground truth is intentionally blank at authoring time.",
            "Only status and resolution_spec are exposed before backfill.",
        ],
        "cases": truths,
    }
    markdown = "\n".join(lines) + "\n"
    return casebook, ground_truth, markdown


def main() -> None:
    casebook, ground_truth, markdown = build()
    (ROOT / "track_g_true_live_questions.json").write_text(
        json.dumps(casebook, indent=2, ensure_ascii=False) + "\n"
    )
    (ROOT / "track_g_true_live_ground_truth.json").write_text(
        json.dumps(ground_truth, indent=2, ensure_ascii=False) + "\n"
    )
    (ROOT / "track_g_true_live_cases.md").write_text(markdown)
    print("wrote", ROOT / "track_g_true_live_questions.json")
    print("wrote", ROOT / "track_g_true_live_ground_truth.json")
    print("wrote", ROOT / "track_g_true_live_cases.md")


if __name__ == "__main__":
    main()
