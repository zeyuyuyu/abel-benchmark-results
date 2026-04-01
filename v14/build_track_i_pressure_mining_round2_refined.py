#!/usr/bin/env python3
"""Build a refined pressure-test mining mini-pool near known positive phrasings."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from build_track_i_skill_mining_pool import source_maps


ROOT = Path(__file__).resolve().parent

QUESTIONS_PATH = ROOT / "track_i_pressure_mining_round2_refined_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_i_pressure_mining_round2_refined_ground_truth.json"
CASES_MD_PATH = ROOT / "track_i_pressure_mining_round2_refined_cases.md"
PACK_VARIANT = "track_i_pressure_mining_round2_refined_v1"


CURATED_CASES = [
    {
        "source_id": "v14cpi_014",
        "id": "v14im2r_001",
        "primary_question": "Which first pressure test most cleanly distinguishes fuel shock from demand weakness?",
        "followup_question": "What downstream readout should you inspect after that stress?",
        "primary_answer_text": "stress jet-fuel costs first",
        "followup_answer_text": "inspect unit margin or EPS sensitivity",
        "evidence_summary": [
            "the packet already shows stable demand-side evidence and a large energy move",
            "margin and EPS sensitivity are the most direct downstream readouts of a fuel-cost stress",
        ],
        "common_failure_modes": [
            "choosing a demand-side probe despite the packet already showing stable booking evidence",
            "picking a variable that is not downstream of the suspected cost channel",
        ],
    },
    {
        "source_id": "v14cpi_014",
        "id": "v14im2r_002",
        "primary_question": "Which first pressure test most directly separates fuel shock from demand weakness?",
        "followup_question": "What readout should you inspect once you run that probe?",
        "primary_answer_text": "stress jet-fuel costs first",
        "followup_answer_text": "inspect unit margin or EPS sensitivity",
        "evidence_summary": [
            "fuel moved sharply while bookings and unit revenue held up",
            "the direct downstream readout of a fuel-cost stress is margin or EPS sensitivity, not a demand metric",
        ],
        "common_failure_modes": [
            "answering with a demand probe before testing the more active fuel channel",
            "watching PRASM or bookings rather than margin or EPS sensitivity",
        ],
    },
    {
        "source_id": "v14cpi_014",
        "id": "v14im2r_003",
        "primary_question": "If you only get one first stress, which one best separates fuel shock from demand weakness?",
        "followup_question": "What downstream number matters most after that stress?",
        "primary_answer_text": "stress jet-fuel costs first",
        "followup_answer_text": "inspect unit margin or EPS sensitivity",
        "evidence_summary": [
            "energy-linked cost pressure is the live variable in the packet",
            "the expected downstream consequence of that stress lands in margins or EPS, not in traffic headlines",
        ],
        "common_failure_modes": [
            "jumping to close-in demand metrics because they sound more intuitive",
            "naming a cost shock but failing to follow it through to the right downstream readout",
        ],
    },
    {
        "source_id": "v14cpi_015",
        "id": "v14im2r_004",
        "primary_question": "Which first pressure test best distinguishes lithium pass-through from customer inventory reset?",
        "followup_question": "What readout should you inspect once you run that probe?",
        "primary_answer_text": "stress customer inventory and build schedules first",
        "followup_answer_text": "inspect shipments and backlog conversion",
        "evidence_summary": [
            "customer inventory and build schedules are the variables most directly tied to the supplier shipment softness in the packet",
            "lithium softness alone does not explain a slower backlog conversion nearly as cleanly",
        ],
        "common_failure_modes": [
            "defaulting to the flashier commodity move instead of the more direct downstream transmission path",
            "reading margin before checking the shipment path that actually distinguishes the stories",
        ],
    },
    {
        "source_id": "v14cpi_015",
        "id": "v14im2r_005",
        "primary_question": "Which first pressure test most directly separates lithium pass-through from customer inventory reset?",
        "followup_question": "What readout should matter most once you run that probe?",
        "primary_answer_text": "stress customer inventory and build schedules first",
        "followup_answer_text": "inspect shipments and backlog conversion",
        "evidence_summary": [
            "backlog conversion is already slowing while margin guidance is only modestly lower",
            "that pattern points first to customer schedule and inventory stress rather than to commodity pass-through",
        ],
        "common_failure_modes": [
            "choosing a lithium or ASP bridge before testing customer schedules",
            "stopping at inventory days alone instead of reading through to shipments and backlog conversion",
        ],
    },
    {
        "source_id": "v14cpi_015",
        "id": "v14im2r_006",
        "primary_question": "What first probe most cleanly separates lithium pass-through from customer inventory reset?",
        "followup_question": "What downstream shipment readout deserves the most weight after that?",
        "primary_answer_text": "stress customer inventory and build schedules first",
        "followup_answer_text": "inspect shipments and backlog conversion",
        "evidence_summary": [
            "the shipment path is the cleanest place to discriminate these stories",
            "customer schedule and inventory stress should show up in shipments and backlog conversion faster than in margin",
        ],
        "common_failure_modes": [
            "letting the commodity headline dominate despite a clearer downstream shipment signal",
            "answering with a generic sell-through monitor rather than the shipment and backlog path",
        ],
    },
    {
        "source_id": "v14cpi_016",
        "id": "v14im2r_007",
        "primary_question": "Which pressure test most directly challenges the thesis that policy incentive step-down is the main driver?",
        "followup_question": "What readout matters most once you stress that lever?",
        "primary_answer_text": "stress incentive-policy generosity first",
        "followup_answer_text": "inspect lead-to-booking conversion",
        "evidence_summary": [
            "the leading thesis is specifically about incentive generosity, so the cleanest challenge is to stress that lever and inspect the conversion step most directly tied to purchase economics",
            "lead volume moved far less than conversion, which makes the conversion readout more decision-relevant than top-of-funnel traffic",
        ],
        "common_failure_modes": [
            "choosing a lever unrelated to the stated uncertainty",
            "looking at margin instead of the funnel step most exposed to incentive economics",
        ],
    },
    {
        "source_id": "v14cpi_016",
        "id": "v14im2r_008",
        "primary_question": "What first pressure test most directly challenges the policy-step-down story?",
        "followup_question": "Which downstream readout matters most once you run it?",
        "primary_answer_text": "stress incentive-policy generosity first",
        "followup_answer_text": "inspect lead-to-booking conversion",
        "evidence_summary": [
            "the packet leaves policy and execution both live, but the leading claim is policy economics",
            "lead-to-booking conversion is the funnel step most exposed to that lever",
        ],
        "common_failure_modes": [
            "jumping straight to rep-speed or turnover diagnostics instead of challenging the policy thesis",
            "watching lead flow rather than the conversion step where incentive economics should bite",
        ],
    },
    {
        "source_id": "v14cpi_016",
        "id": "v14im2r_009",
        "primary_question": "If policy economics is the leading thesis, what is the cleanest first probe to challenge it?",
        "followup_question": "What funnel readout should you inspect once you do?",
        "primary_answer_text": "stress incentive-policy generosity first",
        "followup_answer_text": "inspect lead-to-booking conversion",
        "evidence_summary": [
            "incentive value dropped much more than lead volume, while conversion weakened sharply",
            "the natural downstream arbiter is conversion rather than response-time anecdotes",
        ],
        "common_failure_modes": [
            "treating rep-turnover chatter as the first probe despite the leading policy thesis",
            "stopping at follow-up speed instead of inspecting lead-to-booking conversion",
        ],
    },
    {
        "source_id": "v14cpi_013",
        "id": "v14im2r_010",
        "primary_question": "Which first pressure test separates financing stress from demand softness?",
        "followup_question": "What readout should you inspect once you run that probe?",
        "primary_answer_text": "stress financing conditions first",
        "followup_answer_text": "inspect order intake and cancellations",
        "evidence_summary": [
            "the open causal split is financing friction versus true demand softness",
            "orders and cancellations are the closest downstream variables for distinguishing the two stories after stressing financing conditions",
        ],
        "common_failure_modes": [
            "choosing a lever unrelated to the live uncertainty",
            "looking at approval rates and close timing instead of downstream order outcomes",
        ],
    },
]


def build_pack() -> tuple[dict[str, Any], dict[str, Any], str]:
    source_cases, source_truth_map = source_maps()
    questions: list[dict[str, Any]] = []
    truth_cases: list[dict[str, Any]] = []
    lines = [
        "# Track I Pressure Mining Round 2 Refined",
        "",
        f"Candidate pool variant: `{PACK_VARIANT}`.",
        "",
        "Refined mini-pool built close to previously positive `pressure_test_design` phrasings rather than farther-abstraction arbiter prompts.",
        "",
    ]

    for recipe in CURATED_CASES:
        case = source_cases[recipe["source_id"]]
        source_truth = source_truth_map[recipe["source_id"]]
        questions.append(
            {
                "id": recipe["id"],
                "source_case_id": recipe["source_id"],
                "title": case["title"],
                "track": "competing_explanations",
                "task_family": case["task_family"],
                "scenario": case["scenario"],
                "question": recipe["primary_question"],
                "followup_question": recipe["followup_question"],
                "prompt_style": case["prompt_style"],
                "instantiated_inputs": case["instantiated_inputs"],
                "naturalness_rationale": "Looks like a normal analyst question, but stays close to phrasings that previously surfaced a real skill edge.",
                "source_truth_summary": recipe["evidence_summary"],
            }
        )
        truth_cases.append(
            {
                "id": recipe["id"],
                "source_case_id": recipe["source_id"],
                "primary_answer_text": recipe["primary_answer_text"],
                "followup_answer_text": recipe["followup_answer_text"],
                "canonical_answer": source_truth["canonical_answer"],
                "evidence_summary": recipe["evidence_summary"],
                "common_failure_modes": recipe["common_failure_modes"],
            }
        )
        lines.extend(
            [
                f"## {recipe['id']} — {case['title']}",
                "",
                f"- Source case: `{recipe['source_id']}`",
                f"- Family: `{case['task_family']}`",
                f"- Primary question: {recipe['primary_question']}",
                f"- Canonical primary answer: `{recipe['primary_answer_text']}`",
                f"- Follow-up question: {recipe['followup_question']}",
                f"- Canonical follow-up answer: `{recipe['followup_answer_text']}`",
                "",
            ]
        )

    return (
        {
            "track": "v14_track_i_pressure_mining_round2_refined",
            "pack_variant": PACK_VARIANT,
            "case_count": len(questions),
            "cases": questions,
        },
        {
            "track": "v14_track_i_pressure_mining_round2_refined",
            "pack_variant": PACK_VARIANT,
            "case_count": len(truth_cases),
            "cases": truth_cases,
        },
        "\n".join(lines).rstrip() + "\n",
    )


def main() -> None:
    questions_json, truth_json, markdown = build_pack()
    QUESTIONS_PATH.write_text(json.dumps(questions_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    GROUND_TRUTH_PATH.write_text(json.dumps(truth_json, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    CASES_MD_PATH.write_text(markdown, encoding="utf-8")
    print(f"Wrote {QUESTIONS_PATH}")
    print(f"Wrote {GROUND_TRUTH_PATH}")
    print(f"Wrote {CASES_MD_PATH}")


if __name__ == "__main__":
    main()
