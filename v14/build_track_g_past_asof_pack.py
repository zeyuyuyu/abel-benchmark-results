from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
V13_ROOT = ROOT.parent / "v13"


def load_v13_asof() -> tuple[dict, dict[str, dict]]:
    questions = json.loads((V13_ROOT / "resolved_asof_questions.json").read_text())
    truth_items = json.loads((V13_ROOT / "resolved_asof_ground_truth.json").read_text())["cases"]
    truth_map = {item["id"]: item for item in truth_items}
    return questions, truth_map


def build() -> tuple[dict, dict, str]:
    questions_doc, truth_map = load_v13_asof()
    cases = []
    truths = []

    lines = [
        "# v14 Track G Historical As-Of Cases",
        "",
        "This markdown materializes the canonical Track G historical as-of pack.",
        "Search is allowed, but it must not use sources later than each case's",
        "`search_cutoff`.",
        "",
        f"- Source mirror: `v13/resolved_asof_questions.json`",
        f"- Case count: `{questions_doc['question_count']}`",
        "",
    ]

    for case in questions_doc["cases"]:
        truth = truth_map[case["id"]]
        case_obj = {
            "id": case["id"],
            "track": "agentic_live_analysis",
            "task_family": "futurex_style_live_prediction",
            "evaluation_regime": "historical_asof_search_cutoff",
            "source_family": ["FutureX-Past"],
            "title": case["title"],
            "category": case.get("category"),
            "futurex_pattern": case.get("futurex_pattern"),
            "prompt": case["prompt"],
            "answer_format": case.get("answer_format"),
            "resolved_around": case.get("resolved_around"),
            "search_cutoff": case.get("search_cutoff"),
            "search_cutoff_source": case.get("search_cutoff_source"),
            "usage_policy": case.get("usage_policy"),
            "source_casebook": "v13/resolved_asof_questions.json",
            "source_case_id": case["id"],
            "source_id": case.get("source_id"),
        }
        cases.append(case_obj)

        truths.append(
            {
                "id": case["id"],
                "title": truth.get("title"),
                "category": truth.get("category"),
                "answer_box": truth.get("answer_box"),
                "answer_tokens": truth.get("answer_tokens", []),
                "resolved_around": truth.get("resolved_around"),
                "search_cutoff": truth.get("search_cutoff"),
                "search_cutoff_source": truth.get("search_cutoff_source"),
                "source_dataset": truth.get("source_dataset"),
                "source_id": truth.get("source_id"),
            }
        )

        lines.extend(
            [
                f"## {case['id']} — {case['title']}",
                "",
                f"- Track: `agentic_live_analysis`",
                f"- Task family: `futurex_style_live_prediction`",
                f"- Evaluation regime: `historical_asof_search_cutoff`",
                f"- Category: `{case.get('category', 'unknown')}`",
                f"- Search cutoff: `{case.get('search_cutoff', 'unknown')}`",
                f"- Search cutoff source: `{case.get('search_cutoff_source', 'unknown')}`",
                f"- Resolved around: `{case.get('resolved_around', 'unknown')}`",
                "",
                "Prompt:",
                "```text",
                case["prompt"],
                "```",
                "",
                "Usage policy:",
                "```json",
                json.dumps(case.get("usage_policy"), indent=2, ensure_ascii=False),
                "```",
                "",
                "Ground truth:",
                "```json",
                json.dumps(
                    {
                        "answer_box": truth.get("answer_box"),
                        "answer_tokens": truth.get("answer_tokens", []),
                    },
                    indent=2,
                    ensure_ascii=False,
                ),
                "```",
                "",
            ]
        )

    casebook = {
        "version": "v14-track-g-past-asof-questions",
        "split": "track_g_past_asof",
        "case_count": len(cases),
        "notes": [
            "This pack is the canonical historical as-of Track G materialization in v14.",
            "All cases use evaluation_regime=historical_asof_search_cutoff.",
            "Search is allowed, but evidence must respect each case-level search_cutoff.",
        ],
        "cases": cases,
    }
    ground_truth = {
        "version": "v14-track-g-past-asof-ground-truth",
        "split": "track_g_past_asof",
        "case_count": len(truths),
        "notes": [
            "Answers are immediately available because these are historical as-of cases.",
            "The key protocol is time-bounded search, not hidden forward resolution.",
        ],
        "cases": truths,
    }
    markdown = "\n".join(lines) + "\n"
    return casebook, ground_truth, markdown


def main() -> None:
    casebook, ground_truth, markdown = build()
    (ROOT / "track_g_past_asof_questions.json").write_text(
        json.dumps(casebook, indent=2, ensure_ascii=False) + "\n"
    )
    (ROOT / "track_g_past_asof_ground_truth.json").write_text(
        json.dumps(ground_truth, indent=2, ensure_ascii=False) + "\n"
    )
    (ROOT / "track_g_past_asof_cases.md").write_text(markdown)
    print("wrote", ROOT / "track_g_past_asof_questions.json")
    print("wrote", ROOT / "track_g_past_asof_ground_truth.json")
    print("wrote", ROOT / "track_g_past_asof_cases.md")


if __name__ == "__main__":
    main()
