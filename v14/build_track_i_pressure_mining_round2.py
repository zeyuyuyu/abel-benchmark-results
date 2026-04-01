#!/usr/bin/env python3
"""Build a focused second-round Track I mining pack."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from build_track_i_skill_mining_pool import source_maps


ROOT = Path(__file__).resolve().parent

QUESTIONS_PATH = ROOT / "track_i_pressure_mining_round2_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_i_pressure_mining_round2_ground_truth.json"
CASES_MD_PATH = ROOT / "track_i_pressure_mining_round2_cases.md"
PACK_VARIANT = "track_i_pressure_mining_round2_v1"


CURATED_CASES = [
    {
        "source_id": "v14cpi_013",
        "id": "v14im2_001",
        "primary_question": "What is the first clean arbiter here?",
        "followup_question": "What downstream readout do you inspect once you run it?",
        "primary_answer_text": "stress financing conditions first",
        "followup_answer_text": "inspect order intake and cancellations",
        "evidence_summary": [
            "two live stories remain: financing friction versus genuine demand softness",
            "the clean separation comes from shocking financing conditions and then reading the downstream order channel",
        ],
        "common_failure_modes": [
            "staying at approval-rate or close-timing diagnostics instead of reading order outcomes",
            "choosing a probe that does not actually separate financing from demand",
        ],
    },
    {
        "source_id": "v14cpi_013",
        "id": "v14im2_002",
        "primary_question": "If you had one first probe before writing the note, where do you press?",
        "followup_question": "What customer outcome actually separates the stories after that probe?",
        "primary_answer_text": "stress financing conditions first",
        "followup_answer_text": "inspect order intake and cancellations",
        "evidence_summary": [
            "healthy quote activity with stretched close timing keeps financing friction live",
            "orders and cancellations are the closest downstream discriminators once financing is stressed",
        ],
        "common_failure_modes": [
            "watching financing-process metrics without reading through to orders and cancellations",
            "jumping straight to margin or receivables despite the live uncertainty being commercial demand",
        ],
    },
    {
        "source_id": "v14cpi_014",
        "id": "v14im2_003",
        "primary_question": "What lever would you shock first to separate fuel pressure from demand weakness?",
        "followup_question": "What readout should settle it once you run that stress?",
        "primary_answer_text": "stress jet-fuel costs first",
        "followup_answer_text": "inspect unit margin or EPS sensitivity",
        "evidence_summary": [
            "forward bookings and unit revenue are stable while fuel moves sharply",
            "the cleanest first arbiter is the cost lever, with margin or EPS as the direct downstream readout",
        ],
        "common_failure_modes": [
            "switching to a fare or demand probe before testing the cost shock",
            "watching revenue metrics instead of the direct margin or EPS consequence of fuel stress",
        ],
    },
    {
        "source_id": "v14cpi_014",
        "id": "v14im2_004",
        "primary_question": "What is the cleanest first arbiter for the airline selloff?",
        "followup_question": "What number matters most once you run that stress?",
        "primary_answer_text": "stress jet-fuel costs first",
        "followup_answer_text": "inspect unit margin or EPS sensitivity",
        "evidence_summary": [
            "the packet already leaves demand-side evidence mostly intact",
            "fuel-cost pressure should be challenged first, then judged on the earnings bridge rather than on bookings chatter",
        ],
        "common_failure_modes": [
            "choosing a demand-side arbiter despite stable booking evidence",
            "tracking close-in yields or PRASM when the canonical downstream readout is margin or EPS sensitivity",
        ],
    },
    {
        "source_id": "v14cpi_015",
        "id": "v14im2_005",
        "primary_question": "What first probe most directly tests inventory reset over lithium pass-through?",
        "followup_question": "What readout deserves the most weight right after?",
        "primary_answer_text": "stress customer inventory and build schedules first",
        "followup_answer_text": "inspect shipments and backlog conversion",
        "evidence_summary": [
            "customer inventory days and OEM schedules moved in the same direction as the shipment softness",
            "shipments and backlog conversion are the most direct downstream readouts of an inventory-reset story",
        ],
        "common_failure_modes": [
            "defaulting to the flashier commodity move instead of the downstream shipment path",
            "using a generic ASP-versus-volume bridge instead of stressing customer inventory and build schedules",
        ],
    },
    {
        "source_id": "v14cpi_015",
        "id": "v14im2_006",
        "primary_question": "Where would you press first if you wanted the fastest separation of the two stories?",
        "followup_question": "Which downstream number actually arbitrates after that?",
        "primary_answer_text": "stress customer inventory and build schedules first",
        "followup_answer_text": "inspect shipments and backlog conversion",
        "evidence_summary": [
            "modest margin-guide change does not support a strong lithium pass-through thesis",
            "the shipment path is more decision-relevant than commodity headlines for this packet",
        ],
        "common_failure_modes": [
            "treating lithium as the main story without checking whether backlog conversion is already slowing",
            "answering with OEM inventory days alone instead of the shipment and backlog readout that follows from the stress",
        ],
    },
    {
        "source_id": "v14cpi_016",
        "id": "v14im2_007",
        "primary_question": "What first probe most directly challenges the policy step-down thesis?",
        "followup_question": "What funnel readout matters once you run it?",
        "primary_answer_text": "stress incentive-policy generosity first",
        "followup_answer_text": "inspect lead-to-booking conversion",
        "evidence_summary": [
            "policy generosity fell more than top-of-funnel lead volume, while conversion broke sharply",
            "lead-to-booking conversion is the key downstream readout once incentive economics are stressed",
        ],
        "common_failure_modes": [
            "switching to a sales-execution probe before challenging the policy thesis directly",
            "watching rep response-time diagnostics instead of the incentive-linked conversion step",
        ],
    },
    {
        "source_id": "v14cpi_016",
        "id": "v14im2_008",
        "primary_question": "If you want one first arbiter between policy economics and execution slippage, what is it?",
        "followup_question": "What downstream conversion readout earns the most weight after that?",
        "primary_answer_text": "stress incentive-policy generosity first",
        "followup_answer_text": "inspect lead-to-booking conversion",
        "evidence_summary": [
            "the packet leaves both policy and execution stories live, but the leading thesis is policy step-down",
            "the right follow-through is to inspect conversion, not just activity or response time",
        ],
        "common_failure_modes": [
            "overweighting rep-turnover anecdotes instead of directly testing incentive economics",
            "staying in process metrics rather than the conversion step that separates the stories",
        ],
    },
    {
        "source_id": "v14cpi_001",
        "id": "v14im2_009",
        "primary_question": "What is still the cleaner first read for the homebuilder move?",
        "followup_question": "What condition would make you revisit that view for real?",
        "primary_answer_text": "financing conditions and mortgage affordability",
        "followup_answer_text": "orders stay weak even if rate and credit proxies normalize",
        "evidence_summary": [
            "traffic and visits held better than financing-linked proxies",
            "the main falsifier is not more credit chatter; it is orders staying weak after financing conditions normalize",
        ],
        "common_failure_modes": [
            "naming financing pressure but failing to specify the true revisit condition",
            "monitoring CDS or liquidity headlines instead of the demand outcome after financing normalization",
        ],
    },
    {
        "source_id": "v14cpi_001",
        "id": "v14im2_010",
        "primary_question": "What would have to happen before you abandon the financing-friction thesis?",
        "followup_question": "Which commercial readout has to stay weak for that flip?",
        "primary_answer_text": "orders stay weak even after financing proxies normalize",
        "followup_answer_text": "inspect order intake and cancellations after financing normalization",
        "evidence_summary": [
            "mortgage-rate and credit signals moved much more than traffic or visit activity",
            "a demand-softness flip requires weak order outcomes even after financing proxies improve",
        ],
        "common_failure_modes": [
            "answering with more financing indicators instead of the condition that would falsify the financing thesis",
            "forgetting to tie the flip condition to orders and cancellations",
        ],
    },
    {
        "source_id": "v14cpi_002",
        "id": "v14im2_011",
        "primary_question": "What is still the cleanest starting read for the alt selloff?",
        "followup_question": "What would actually falsify that read?",
        "primary_answer_text": "retail liquidity and alt-beta risk appetite",
        "followup_answer_text": "project-specific activity breaks while broad alt liquidity normalizes",
        "evidence_summary": [
            "majors stayed stable while lower-liquidity alt conditions deteriorated sharply",
            "the true falsifier is project-specific weakness surviving a broader alt-liquidity normalization",
        ],
        "common_failure_modes": [
            "giving a broad crypto answer without naming the retail-liquidity and alt-beta channel",
            "watching BTC or ETH direction instead of the project-specific break that would falsify the broad-liquidity story",
        ],
    },
    {
        "source_id": "v14cpi_002",
        "id": "v14im2_012",
        "primary_question": "What single break would push you away from the broad-liquidity story?",
        "followup_question": "What do you compare it against when checking that break?",
        "primary_answer_text": "project-specific activity breaks while broad alt liquidity normalizes",
        "followup_answer_text": "compare project activity against broader alt-liquidity normalization",
        "evidence_summary": [
            "project usage was flat in the packet, so a token-specific thesis needs a clear break there",
            "the comparison set is broader alt-liquidity normalization rather than BTC or ETH direction alone",
        ],
        "common_failure_modes": [
            "calling any further alt weakness a falsifier even if broad liquidity is still broken",
            "using majors as the comparator instead of broader alt-liquidity conditions",
        ],
    },
    {
        "source_id": "v14cpi_006",
        "id": "v14im2_013",
        "primary_question": "What indirect path best explains the software selloff?",
        "followup_question": "What market cross-check would strengthen that path most?",
        "primary_answer_text": "valuation-duration and refinancing channel",
        "followup_answer_text": "watch spreads and duration-sensitive peers while company metrics stay intact",
        "evidence_summary": [
            "the packet rules out direct deposit problems but keeps a broader financing channel alive",
            "HY spreads and peer co-movement are the right cross-checks, not direct bank-exposure speculation",
        ],
        "common_failure_modes": [
            "denying any path because the company lacks direct bank exposure",
            "drifting into customer or deposit exposure checks instead of watching spreads and duration-sensitive peers",
        ],
    },
    {
        "source_id": "v14cpi_006",
        "id": "v14im2_014",
        "primary_question": "What evidence would make you more confident this is a duration de-rate rather than direct bank exposure?",
        "followup_question": "What should stay intact if that read is right?",
        "primary_answer_text": "spreads widen and duration-sensitive peers sell off together",
        "followup_answer_text": "company metrics stay intact while you watch HY spreads and duration-sensitive peers",
        "evidence_summary": [
            "the canonical read is an indirect financing or valuation channel, not a direct balance-sheet problem",
            "the confirming pattern is peer and spread behavior alongside intact company fundamentals",
        ],
        "common_failure_modes": [
            "looking for direct bank links instead of asking what market evidence would confirm an indirect channel",
            "forgetting that company metrics should remain intact if the duration-channel explanation is correct",
        ],
    },
    {
        "source_id": "v14cpi_008",
        "id": "v14im2_015",
        "primary_question": "What distinction has to stay explicit if you do not want to over-credit the squeeze?",
        "followup_question": "How should the note handle the squeeze without replacing the catalyst?",
        "primary_answer_text": "FDA advisory-panel vote is the primary driver",
        "followup_answer_text": "keep the primary catalyst separate from squeeze amplification",
        "evidence_summary": [
            "most of the move happened immediately after the regulatory event and before the later rumor",
            "short interest can explain amplification, but it should not replace the primary catalyst in the note",
        ],
        "common_failure_modes": [
            "collapsing primary catalyst and amplifier into one undifferentiated answer",
            "letting the later rumor dominate the writeup because it sounds more dramatic",
        ],
    },
    {
        "source_id": "v14cpi_008",
        "id": "v14im2_016",
        "primary_question": "How should the move be phrased so catalyst and amplifier do not get collapsed?",
        "followup_question": "What should stay secondary even if short-covering mattered?",
        "primary_answer_text": "FDA advisory-panel vote is the primary driver while squeeze dynamics amplify",
        "followup_answer_text": "keep the primary catalyst separate from squeeze amplification",
        "evidence_summary": [
            "the timing shows the regulatory event came first and explains most of the move",
            "squeeze dynamics matter as magnitude amplification, not as a replacement causal story",
        ],
        "common_failure_modes": [
            "describing the move as a pure squeeze despite the timing evidence",
            "focusing the follow-up on the rumor rather than on preserving the catalyst-versus-amplifier distinction",
        ],
    },
]


def build_pack() -> tuple[dict[str, Any], dict[str, Any], str]:
    source_cases, source_truth_map = source_maps()
    questions: list[dict[str, Any]] = []
    truth_cases: list[dict[str, Any]] = []
    lines = [
        "# Track I Pressure Mining Round 2",
        "",
        f"Candidate pool variant: `{PACK_VARIANT}`.",
        "",
        "Focused second-round mining around `pressure_test_design` and adjacent families that naturally expose first-probe, discriminating-readout, and catalyst-vs-amplifier reasoning.",
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
                "naturalness_rationale": "Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.",
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
            "track": "v14_track_i_pressure_mining_round2",
            "pack_variant": PACK_VARIANT,
            "case_count": len(questions),
            "cases": questions,
        },
        {
            "track": "v14_track_i_pressure_mining_round2",
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
