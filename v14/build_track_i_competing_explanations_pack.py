#!/usr/bin/env python3
"""Build a curated Track I competing-explanations pack."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent

PUBLIC_CASES_PATH = ROOT / "public_dev_cases.json"
PUBLIC_TRUTH_PATH = ROOT / "public_dev_ground_truth.json"
SOURCE_CASES_PATH = ROOT / "causal_proxy_intervention_cases.json"
SOURCE_TRUTH_PATH = ROOT / "causal_proxy_intervention_ground_truth.json"

QUESTIONS_PATH = ROOT / "track_i_competing_explanations_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_i_competing_explanations_ground_truth.json"
CASES_MD_PATH = ROOT / "track_i_competing_explanations_cases.md"
PACK_VARIANT = "track_i_market_only_frozen_v1"


CURATED_CASES = [
    {
        "source_id": "v14d_015",
        "id": "v14i_001",
        "primary_question": "What is the most plausible dominant explanation for the move?",
        "followup_question": "What is the most important next verification or uncertainty to keep live?",
        "primary_answer_text": "channel inventory correction and weak sell-through",
        "primary_match_any": [
            [["inventory correction", "channel correction", "channel inventory"]],
            [["sell-through", "sell through"], ["inventory"]],
        ],
        "followup_answer_text": "watch sell-through and inventory-days normalization",
        "followup_match_any": [
            [["sell-through", "sell through"], ["inventory days", "inventory"]],
            [["inventory days"], ["normalize", "normalization", "improve"]],
            [["sell-through", "sell through"], ["recover", "improve"]],
        ],
    },
    {
        "source_id": "v14d_020",
        "id": "v14i_003",
        "primary_question": "What is the best-supported causal explanation for the selloff right now?",
        "followup_question": "What would you verify next before strengthening that view?",
        "primary_answer_text": "funding-cost and deposit-beta concern",
        "primary_match_any": [
            [["funding"], ["deposit", "beta", "competition"]],
            [["deposit beta", "deposit competition"], ["funding", "cost"]],
        ],
        "followup_answer_text": "verify uninsured-deposit mix or wholesale-funding dependence",
        "followup_match_any": [
            [["uninsured", "insured"], ["deposit"]],
            [["wholesale"], ["funding"]],
        ],
    },
    {
        "source_id": "v14d_021",
        "id": "v14i_004",
        "primary_question": "What is the most causally plausible primary driver of the rally?",
        "followup_question": "What uncertainty or alternative is still live enough to monitor?",
        "primary_answer_text": "positive FDA panel vote improving approval odds",
        "primary_match_any": [
            [["fda"], ["panel", "vote", "advisory"], ["approval", "odds", "therapy"]],
            [["panel vote", "advisory panel"], ["approval"]],
        ],
        "followup_answer_text": "short-squeeze amplification remains possible, so verify timing and short interest",
        "followup_match_any": [
            [["short interest", "short-interest", "borrow fee", "borrow fees", "borrow"], ["timing", "amplif", "amplifier"]],
            [["borrow fee", "borrow fees"], ["short", "squeeze"]],
        ],
    },
    {
        "source_id": "v14cpi_001",
        "id": "v14i_005",
        "primary_question": "Which explanation is cleaner for the move right now?",
        "followup_question": "What would make you revisit that view first?",
        "primary_answer_text": "financing conditions and mortgage affordability",
        "primary_match_any": [
            [["mortgage"], ["afford", "rate"]],
            [["financing"], ["afford", "conditions", "rates"]],
        ],
        "followup_answer_text": "if orders stay weak after financing proxies normalize, demand softness gains weight",
        "followup_match_any": [
            [["orders"], ["normalize", "normalise", "improve", "ease"], ["rate", "credit", "financing"]],
            [["demand"], ["orders"], ["stay weak", "remain weak", "keep deteriorating", "keep weakening"]],
        ],
    },
    {
        "source_id": "v14cpi_006",
        "id": "v14i_006",
        "primary_question": "What is the most supportable transmission path from the bank stress to the software move?",
        "followup_question": "What additional evidence would most strengthen or weaken that path?",
        "primary_answer_text": "valuation-duration and refinancing channel",
        "primary_match_any": [
            [["duration", "valuation"], ["refinanc", "spread", "credit"]],
            [["refinanc"], ["duration", "multiple", "valuation"]],
        ],
        "followup_answer_text": "watch spreads and duration-sensitive peers while company metrics stay intact",
        "followup_match_any": [
            [["spread", "credit"], ["duration", "peer", "basket"]],
            [["duration"], ["peer", "basket", "software"]],
        ],
    },
    {
        "source_id": "v14cpi_003",
        "id": "v14i_007",
        "primary_question": "What is the cleaner primary read for the airline selloff?",
        "followup_question": "What would make you change that view first?",
        "primary_answer_text": "fuel and input-cost pressure",
        "primary_match_any": [
            [["fuel"], ["cost", "input"]],
            [["crude"], ["fuel", "cost"]],
        ],
        "followup_answer_text": "if bookings or unit revenue break while fuel pressure eases",
        "followup_match_any": [
            [["bookings", "unit revenue", "unit-revenue"], ["fuel", "crude"], ["ease", "eases", "normalize", "normalise"]],
            [["bookings", "unit revenue", "unit-revenue"], ["break", "weaken", "fall"]],
        ],
    },
    {
        "source_id": "v14cpi_004",
        "id": "v14i_008",
        "primary_question": "What is the cleaner explanation for the de-rate?",
        "followup_question": "What would make you shift toward an idiosyncratic company problem instead?",
        "primary_answer_text": "duration pressure and financing conditions",
        "primary_match_any": [
            [["duration", "rate", "yield"], ["pressure", "financing", "credit"]],
            [["financing", "credit"], ["duration", "multiple", "rate"]],
        ],
        "followup_answer_text": "if renewal or churn metrics break while rates and credit stabilize",
        "followup_match_any": [
            [["renewal", "churn"], ["rate", "credit"], ["stabil", "normalize", "normalise"]],
            [["renewal", "churn"], ["break", "weaken", "deteriorate"]],
        ],
    },
    {
        "source_id": "v14cpi_007",
        "id": "v14i_009",
        "primary_question": "How much should the commodity shock matter near-term for the EV maker?",
        "followup_question": "What would you verify before promoting it into a bigger thesis?",
        "primary_answer_text": "weak near-term pass-through because contracts and cost share limit it",
        "primary_match_any": [
            [["weak", "limited", "modest"], ["near term", "near-term", "short term", "short-term"]],
            [["contract"], ["cost share"]],
        ],
        "followup_answer_text": "verify contract coverage or cost share before promoting the shock",
        "followup_match_any": [
            [["contract", "coverage"], ["cost share"]],
            [["cost share"], ["contract", "coverage"]],
        ],
    },
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_maps() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    cases = {}
    truth = {}
    for case in load_json(PUBLIC_CASES_PATH)["cases"]:
        cases[case["id"]] = case
    for case in load_json(SOURCE_CASES_PATH)["cases"]:
        cases[case["id"]] = case
    for case in load_json(PUBLIC_TRUTH_PATH)["cases"]:
        truth[case["id"]] = case
    for case in load_json(SOURCE_TRUTH_PATH)["cases"]:
        truth[case["id"]] = case
    return cases, truth


def build_pack() -> tuple[dict[str, Any], dict[str, Any], str]:
    source_cases, source_truth = source_maps()

    questions: list[dict[str, Any]] = []
    truth_cases: list[dict[str, Any]] = []
    markdown_lines = [
        "# v14 Track I Competing Explanations Cases",
        "",
        f"Frozen pack variant: `{PACK_VARIANT}`.",
        "",
        "Curated market-only analyst-style cases designed to avoid obvious skill-shaped prompts.",
        "",
    ]

    for recipe in CURATED_CASES:
        case = source_cases[recipe["source_id"]]
        truth = source_truth[recipe["source_id"]]
        question_row = {
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
            "naturalness_rationale": (
                "Looks like a normal analyst disagreement about explanations and what to verify next, "
                "rather than a graph or skill operation."
            ),
            "source_truth_summary": truth["evidence_summary"],
        }
        truth_row = {
            "id": recipe["id"],
            "source_case_id": recipe["source_id"],
            "primary_answer_text": recipe["primary_answer_text"],
            "primary_match_any": recipe["primary_match_any"],
            "followup_answer_text": recipe["followup_answer_text"],
            "followup_match_any": recipe["followup_match_any"],
            "canonical_answer": truth["canonical_answer"],
            "evidence_summary": truth["evidence_summary"],
            "common_failure_modes": truth["common_failure_modes"],
        }
        questions.append(question_row)
        truth_cases.append(truth_row)

        markdown_lines.extend(
            [
                f"## {recipe['id']} — {case['title']}",
                "",
                f"- Source case: `{recipe['source_id']}`",
                f"- Family: `{case['task_family']}`",
                f"- Primary question: {recipe['primary_question']}",
                f"- Canonical primary answer: `{recipe['primary_answer_text']}`",
                f"- Follow-up question: {recipe['followup_question']}",
                f"- Canonical follow-up answer: `{recipe['followup_answer_text']}`",
                "- Inputs:",
            ]
        )
        for item in case["instantiated_inputs"]:
            markdown_lines.append(f"  - `{item['type']}` — {item['title']}")
            markdown_lines.append(f"    - {item['content']}")
        markdown_lines.append("")

    questions_json = {"track": "v14_track_i_competing_explanations", "case_count": len(questions), "cases": questions}
    questions_json["pack_variant"] = PACK_VARIANT
    truth_json = {"track": "v14_track_i_competing_explanations", "case_count": len(truth_cases), "cases": truth_cases}
    truth_json["pack_variant"] = PACK_VARIANT
    return questions_json, truth_json, "\n".join(markdown_lines).rstrip() + "\n"


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
