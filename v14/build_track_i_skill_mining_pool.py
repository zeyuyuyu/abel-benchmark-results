#!/usr/bin/env python3
"""Build a broad natural candidate pool for Track I skill mining."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent

PUBLIC_CASES_PATH = ROOT / "public_dev_cases.json"
PUBLIC_TRUTH_PATH = ROOT / "public_dev_ground_truth.json"
SOURCE_CASES_PATH = ROOT / "causal_proxy_intervention_cases.json"
SOURCE_TRUTH_PATH = ROOT / "causal_proxy_intervention_ground_truth.json"

QUESTIONS_PATH = ROOT / "track_i_skill_mining_pool_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_i_skill_mining_pool_ground_truth.json"
CASES_MD_PATH = ROOT / "track_i_skill_mining_pool_cases.md"
PACK_VARIANT = "track_i_skill_mining_pool_v1"


CURATED_CASES = [
    {
        "source_id": "v14d_013",
        "id": "v14im_001",
        "primary_question": "What best explains the margin miss?",
        "followup_question": "What next observable would most strengthen that read?",
        "primary_answer_text": "mix shift into lower-margin hardware amplified by freight",
        "followup_answer_text": "watch hardware mix, hardware margin, and freight cost",
        "evidence_summary": [
            "revenue growth alone is not a valid margin explanation",
            "packet supports a causal variable relationship between product mix and margin",
        ],
        "common_failure_modes": [
            "answering with generic cost inflation despite no evidence",
            "treating revenue growth itself as the driver of margin miss",
        ],
    },
    {
        "source_id": "v14d_015",
        "id": "v14im_002",
        "primary_question": "What is the most plausible dominant explanation for the move?",
        "followup_question": "What uncertainty or metric would you keep live next?",
        "primary_answer_text": "channel inventory correction and weak sell-through",
        "followup_answer_text": "watch sell-through and inventory-days normalization",
        "evidence_summary": [
            "dominant driver must explain most of the miss magnitude",
            "FX and legal reserve are too small to be the main answer",
        ],
        "common_failure_modes": [
            "choosing the most familiar macro explanation",
            "overweighting a one-time legal item that mainly affects margin, not revenue",
        ],
    },
    {
        "source_id": "v14d_019",
        "id": "v14im_003",
        "primary_question": "What is the most likely causal driver of the move right now?",
        "followup_question": "What part of the thesis remains uncertain enough not to overstate?",
        "primary_answer_text": "freight-rate spike due to canal disruption and rerouting",
        "followup_answer_text": "duration and persistence of rerouting surcharges remain uncertain",
        "evidence_summary": [
            "tests causal synthesis under freshness-sensitive but frozen evidence",
            "good answers must separate what is likely from what remains unresolved",
        ],
        "common_failure_modes": [
            "summarizing headlines without naming a mechanism",
            "overclaiming a durable earnings effect not supported by the packet",
        ],
    },
    {
        "source_id": "v14d_020",
        "id": "v14im_004",
        "primary_question": "What is the best-supported causal explanation for the selloff right now?",
        "followup_question": "What would you verify next before strengthening that view?",
        "primary_answer_text": "funding-cost and deposit-beta concern",
        "followup_answer_text": "verify uninsured-deposit mix or wholesale-funding dependence",
        "evidence_summary": [
            "tests memo-style causal synthesis with verification discipline",
            "answers should privilege primary-source evidence over rumor",
        ],
        "common_failure_modes": [
            "treating the rumor as the main driver",
            "failing to specify what to verify next",
        ],
    },
    {
        "source_id": "v14d_021",
        "id": "v14im_005",
        "primary_question": "What is the most causally plausible primary driver of the rally?",
        "followup_question": "What alternative remains live enough to monitor, and how would you monitor it?",
        "primary_answer_text": "positive FDA panel vote improving approval odds",
        "followup_answer_text": "short-squeeze amplification remains possible, so verify timing and short interest",
        "evidence_summary": [
            "tests selection among competing narratives",
            "main event should outrank unsupported rumor, while magnitude amplification remains a valid uncertainty",
        ],
        "common_failure_modes": [
            "choosing the rumor because it sounds more dramatic",
            "ignoring the distinction between driver and amplifier",
        ],
    },
    {
        "source_id": "v14cpi_001",
        "id": "v14im_006",
        "primary_question": "Which explanation is cleaner for the move right now?",
        "followup_question": "What would most directly make you revisit that view?",
        "primary_answer_text": "financing conditions and mortgage affordability",
        "followup_answer_text": "if orders stay weak after financing proxies normalize, demand softness gains weight",
        "evidence_summary": [
            "mortgage affordability worsened materially while traffic and visits stayed roughly intact",
            "credit and rate signals moved sharply, which fits hesitation around financing more than collapse in shopper interest",
        ],
        "common_failure_modes": [
            "treating a modest cancellation increase as proof of broad demand collapse",
            "ignoring the sharper movement in mortgage-rate and credit proxies",
        ],
    },
    {
        "source_id": "v14cpi_002",
        "id": "v14im_007",
        "primary_question": "What is the cleaner starting point for the selloff?",
        "followup_question": "What would most directly falsify that interpretation?",
        "primary_answer_text": "retail liquidity and alt-beta risk appetite",
        "followup_answer_text": "if project-specific activity breaks while broad alt liquidity normalizes",
        "evidence_summary": [
            "majors were stable while lower-liquidity books and alt funding deteriorated sharply",
            "project-specific usage stayed flat, which argues against a token-specific adoption collapse",
        ],
        "common_failure_modes": [
            "projecting a broad BTC/ETH narrative onto a move concentrated in low-liquidity alt exposure",
            "assuming a hack or exploit without evidence packet support",
        ],
    },
    {
        "source_id": "v14cpi_003",
        "id": "v14im_008",
        "primary_question": "What is the cleaner primary read for the airline selloff?",
        "followup_question": "What would make you change that view first?",
        "primary_answer_text": "fuel and input-cost pressure",
        "followup_answer_text": "if bookings or unit revenue break while fuel pressure eases",
        "evidence_summary": [
            "the sharpest moving variables are fuel-linked while bookings and unit-revenue guidance are stable",
            "there is no evidence packet support for labor or FX being the dominant marginal driver",
        ],
        "common_failure_modes": [
            "assuming all airline weakness is demand-driven without checking booking and unit-revenue evidence",
            "overweighting crude headlines without relating them to the actual airline cost channel",
        ],
    },
    {
        "source_id": "v14cpi_004",
        "id": "v14im_009",
        "primary_question": "What is the cleaner explanation for the de-rate?",
        "followup_question": "What would make you shift toward an idiosyncratic company problem instead?",
        "primary_answer_text": "duration pressure and financing conditions",
        "followup_answer_text": "if renewal or churn metrics break while rates and credit stabilize",
        "evidence_summary": [
            "macro duration and credit-sensitive software factors moved sharply while company operating metrics were largely intact",
            "the packet does not contain company-specific failure evidence strong enough to outrank the factor move",
        ],
        "common_failure_modes": [
            "inventing product trouble from price action alone",
            "ignoring the explicit sector-factor de-rating in the evidence packet",
        ],
    },
    {
        "source_id": "v14cpi_005",
        "id": "v14im_010",
        "primary_question": "Which candidate driver is most likely bridge noise rather than the core transmission channel?",
        "followup_question": "Which costs deserve attention instead if you want the cleaner transmission path?",
        "primary_answer_text": "soybean rally is bridge noise",
        "followup_answer_text": "watch freight, packaging resin, palm oil, and cocoa instead",
        "evidence_summary": [
            "the note explicitly says soy is not a material input for the focal brand mix",
            "freight, resin, palm oil, and cocoa all sit more directly on the company cost path",
        ],
        "common_failure_modes": [
            "equating any agricultural headline with causal relevance to a food stock",
            "picking the most visible market move instead of the cleanest company-specific transmission channel",
        ],
    },
    {
        "source_id": "v14cpi_006",
        "id": "v14im_011",
        "primary_question": "What is the most supportable transmission path from the bank stress to the software move?",
        "followup_question": "What additional evidence would most strengthen or weaken that path?",
        "primary_answer_text": "valuation-duration and refinancing channel",
        "followup_answer_text": "watch spreads and duration-sensitive peers while company metrics stay intact",
        "evidence_summary": [
            "the packet rules out direct deposit exposure, but a broader risk and financing channel remains plausible",
            "high-yield spreads widened and duration-sensitive software names sold off together",
        ],
        "common_failure_modes": [
            "assuming no path simply because the company lacks direct bank exposure",
            "inventing a balance-sheet crisis despite the explicit net-cash note",
        ],
    },
    {
        "source_id": "v14cpi_007",
        "id": "v14im_012",
        "primary_question": "How much should the commodity shock matter near-term for the EV maker?",
        "followup_question": "What would you verify before promoting it into a bigger thesis?",
        "primary_answer_text": "weak near-term pass-through because contracts and cost share limit it",
        "followup_answer_text": "verify contract coverage or cost share before promoting the shock",
        "evidence_summary": [
            "the cost share is small and the contract coverage delays pass-through",
            "the packet explicitly points to larger variable exposures elsewhere in the cost stack",
        ],
        "common_failure_modes": [
            "overweighting the most dramatic commodity headline without checking cost share and contract timing",
            "calling the move impossible to assess despite clear packet constraints",
        ],
    },
    {
        "source_id": "v14cpi_008",
        "id": "v14im_013",
        "primary_question": "Which explanation best fits the move without overstating the evidence?",
        "followup_question": "What distinction or uncertainty should you keep explicit in the note?",
        "primary_answer_text": "FDA advisory-panel vote is the primary driver while squeeze dynamics amplify",
        "followup_answer_text": "keep primary driver separate from squeeze amplification",
        "evidence_summary": [
            "most of the move occurred immediately after the regulatory event and before the rumor appeared",
            "short interest can explain amplification without replacing the primary catalyst",
        ],
        "common_failure_modes": [
            "treating the later rumor as primary despite the timing mismatch",
            "collapsing primary driver and amplifier into the same answer",
        ],
    },
    {
        "source_id": "v14cpi_013",
        "id": "v14im_014",
        "primary_question": "Which first pressure test would best separate financing stress from demand softness?",
        "followup_question": "What readout should you inspect once you run that probe?",
        "primary_answer_text": "stress financing conditions first",
        "followup_answer_text": "inspect orders and cancellations",
        "evidence_summary": [
            "the open causal split is financing friction versus true demand softness",
            "orders and cancellations are the closest downstream variables for distinguishing the two stories after stressing financing conditions",
        ],
        "common_failure_modes": [
            "choosing a lever unrelated to the live uncertainty",
            "looking at margin before testing the order-flow channel that actually separates the stories",
        ],
    },
    {
        "source_id": "v14cpi_014",
        "id": "v14im_015",
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
        "source_id": "v14cpi_015",
        "id": "v14im_016",
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
        "source_id": "v14cpi_016",
        "id": "v14im_017",
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
    source_cases, source_truth_map = source_maps()
    questions: list[dict[str, Any]] = []
    truth_cases: list[dict[str, Any]] = []
    lines = [
        "# Track I Skill Mining Pool",
        "",
        f"Candidate pool variant: `{PACK_VARIANT}`.",
        "",
        "These cases are natural market or business causal-read surfaces used for mining cases where `codex + skill` materially beats `codex only`.",
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
                "naturalness_rationale": "Looks like a normal analyst question about what is driving a move and what to inspect next.",
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
            "track": "v14_track_i_skill_mining_pool",
            "pack_variant": PACK_VARIANT,
            "case_count": len(questions),
            "cases": questions,
        },
        {
            "track": "v14_track_i_skill_mining_pool",
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
