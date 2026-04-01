#!/usr/bin/env python3
"""Build a 30-case high-quality Track I pack."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from build_track_i_skill_mining_pool import build_pack as build_mining_pack
from build_track_i_skill_mining_pool import source_maps


ROOT = Path(__file__).resolve().parent

QUESTIONS_PATH = ROOT / "track_i_high_quality_30_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_i_high_quality_30_ground_truth.json"
CASES_MD_PATH = ROOT / "track_i_high_quality_30_cases.md"
PACK_VARIANT = "track_i_high_quality_30_v1"


EXTRA_CASES = [
    {
        "source_id": "v14cpi_009",
        "id": "v14im_018",
        "primary_question": "Can you cleanly credit the unit-sales move to the price cut?",
        "followup_question": "What contamination would stop you from writing that note cleanly?",
        "primary_answer_text": "no, the price cut is bundled with the sales-comp rewrite in the same weak regions",
        "followup_answer_text": "targeted rollout and simultaneous commercial intervention contaminate attribution",
        "evidence_summary": [
            "the price cut and compensation rewrite happened together in the same weak regions",
            "the packet does not support a price-only causal claim because the commercial interventions were bundled",
        ],
        "common_failure_modes": [
            "pretending the price cut can be isolated despite same-window commercial changes",
            "ignoring that the intervention was targeted into the weakest regions",
        ],
    },
    {
        "source_id": "v14cpi_010",
        "id": "v14im_019",
        "primary_question": "What evaluation read would you trust for the maintenance-model rollout?",
        "followup_question": "What threat are you explicitly defending against?",
        "primary_answer_text": "matched or staggered diff-in-diff event study",
        "followup_answer_text": "targeted rollout to high-failure plants and regression to the mean",
        "evidence_summary": [
            "the rollout started where failures were already worst, so a naive before-after read is not credible",
            "a staggered or matched design is needed to separate treatment from pre-existing plant risk",
        ],
        "common_failure_modes": [
            "using a simple before-after comparison on plants selected for severe prior failures",
            "forgetting regression to the mean when the worst plants are treated first",
        ],
    },
    {
        "source_id": "v14cpi_011",
        "id": "v14im_020",
        "primary_question": "Can you trust the measured purchase-frequency lift from the credit-limit increase?",
        "followup_question": "What makes that read unsafe?",
        "primary_answer_text": "no, selection into prequalified users blocks clean attribution",
        "followup_answer_text": "latent purchase propensity was already higher before treatment",
        "evidence_summary": [
            "credit limits were raised only for users already screened as attractive",
            "the packet leaves a strong selection-on-propensity problem that a raw lift cannot remove",
        ],
        "common_failure_modes": [
            "treating prequalification as harmless rather than the core source of bias",
            "reading the observed lift as causal without addressing baseline user quality",
        ],
    },
    {
        "source_id": "v14cpi_012",
        "id": "v14im_021",
        "primary_question": "Can you cleanly credit the late-shipment improvement to the expedite policy?",
        "followup_question": "What other moving part keeps the read dirty?",
        "primary_answer_text": "no, temporary staffing changed in the same window",
        "followup_answer_text": "the simultaneous staffing change contaminates the effect",
        "evidence_summary": [
            "late shipments fell after the expedite policy, but staffing also changed in the same period",
            "the packet does not support isolating the expedite policy from the operational staffing shift",
        ],
        "common_failure_modes": [
            "equating timing with attribution when multiple warehouse levers moved together",
            "failing to name the simultaneous staffing change as the blocking issue",
        ],
    },
    {
        "source_id": "v14d_009",
        "id": "v14im_022",
        "primary_question": "Was pricing alone enough to explain the margin expansion?",
        "followup_question": "What belongs in the bridge besides pricing?",
        "primary_answer_text": "no, pricing and input-cost relief both mattered",
        "followup_answer_text": "include input-cost relief alongside realized price",
        "evidence_summary": [
            "the table shows pricing and input-cost relief moving in the same direction",
            "the packet supports a mixed explanation, not a pricing-only story",
        ],
        "common_failure_modes": [
            "giving all the credit to pricing just because it is the named intervention",
            "ignoring simultaneous input-cost relief that also improves margin",
        ],
    },
    {
        "source_id": "v14d_010",
        "id": "v14im_023",
        "primary_question": "What actually broke the chain right before stores stocked out?",
        "followup_question": "What earlier story should stay secondary in the memo?",
        "primary_answer_text": "distribution-center scanner outage",
        "followup_answer_text": "weather and port disruption were upstream context, not the final trigger",
        "evidence_summary": [
            "the packet says the immediate operational failure before stockouts was the scanner outage",
            "earlier weather and port issues matter as setup, but they are not the last-step driver",
        ],
        "common_failure_modes": [
            "choosing the biggest upstream headline instead of the direct downstream trigger",
            "retelling the chronology without identifying the immediate mechanism",
        ],
    },
    {
        "source_id": "v14d_011",
        "id": "v14im_024",
        "primary_question": "What is the cleaner causal read on the move?",
        "followup_question": "What headline should not be over-credited?",
        "primary_answer_text": "morning corporate actions were the driver, not the later interview",
        "followup_answer_text": "do not over-credit the later interview because it added no new information",
        "evidence_summary": [
            "the main price move happened before the interview and after the earlier corporate actions",
            "the later interview did not introduce a stronger mechanism than the earlier actions",
        ],
        "common_failure_modes": [
            "crediting the most recent headline despite the timing mismatch",
            "confusing temporal sequence with causal force",
        ],
    },
    {
        "source_id": "v14d_012",
        "id": "v14im_025",
        "primary_question": "If the strike had not happened, where would deliveries most likely have landed?",
        "followup_question": "What would still have kept results below plan?",
        "primary_answer_text": "deliveries improve but still finish below plan",
        "followup_answer_text": "the later rail disruption would still hold exports back",
        "evidence_summary": [
            "removing the strike restores part of the throughput loss but not the later logistics shock",
            "the counterfactual improves the outcome without fully restoring plan",
        ],
        "common_failure_modes": [
            "assuming removal of one disruption fully repairs the chain despite later failures",
            "missing that the packet asks for a partial-improvement counterfactual",
        ],
    },
    {
        "source_id": "v14d_014",
        "id": "v14im_026",
        "primary_question": "What is the near-term read if paid acquisition is cut now?",
        "followup_question": "Why should you not assume efficiency fully offsets it?",
        "primary_answer_text": "qualified lead volume falls with only partial efficiency offset",
        "followup_answer_text": "organic substitution is incomplete in the packet",
        "evidence_summary": [
            "the geo test and memo imply that paid leads do not fully reappear organically",
            "some efficiency gains are plausible, but they do not fully offset the near-term lead loss",
        ],
        "common_failure_modes": [
            "assuming a full efficiency offset with no evidence for complete substitution",
            "focusing on CAC optics while ignoring the lead-volume channel",
        ],
    },
    {
        "source_id": "v14d_016",
        "id": "v14im_027",
        "primary_question": "Can you credit the defect improvement to the temperature change?",
        "followup_question": "What would you need to control for before making that call?",
        "primary_answer_text": "no clean causal claim because maintenance timing and line selection moved too",
        "followup_answer_text": "control for maintenance status, line id, and throughput",
        "evidence_summary": [
            "maintenance timing and treatment assignment changed alongside the temperature policy",
            "the packet does not support a clean estimate without plant and throughput controls",
        ],
        "common_failure_modes": [
            "treating the before-after defect change as causal despite simultaneous maintenance shifts",
            "failing to name the line-selection problem explicitly",
        ],
    },
    {
        "source_id": "v14d_017",
        "id": "v14im_028",
        "primary_question": "What evaluation design is the cleanest read for the staggered rollout?",
        "followup_question": "What assumption or risk should stay explicit?",
        "primary_answer_text": "staggered diff-in-diff event study",
        "followup_answer_text": "parallel trends, plus anticipation or spillover risk",
        "evidence_summary": [
            "regions adopted on different dates, which makes an event-study style design the most credible default",
            "the identifying read still depends on absent-policy trend comparability and limited spillovers",
        ],
        "common_failure_modes": [
            "using a pooled before-after read that throws away the rollout timing information",
            "forgetting anticipation and spillover checks even with the right design family",
        ],
    },
    {
        "source_id": "v14d_008",
        "id": "v14im_029",
        "primary_question": "Why does the aggregate look better if both customer segments got worse?",
        "followup_question": "What point should the note make explicitly?",
        "primary_answer_text": "segment mix shift creates a Simpson's paradox",
        "followup_answer_text": "within both novice and expert strata the treatment underperformed",
        "evidence_summary": [
            "the treated group ended up with more high-converting experts, which distorts the aggregate",
            "within each segment the treatment actually underperformed, so the mix shift drives the top-line lift",
        ],
        "common_failure_modes": [
            "reporting the aggregate lift without opening the segment composition change",
            "missing that both within-stratum effects move against the headline aggregate",
        ],
    },
    {
        "source_id": "v14d_007",
        "id": "v14im_030",
        "primary_question": "Should you control for three-day engagement before calling the experiment?",
        "followup_question": "Why is that the wrong adjustment?",
        "primary_answer_text": "no, three-day engagement is post-treatment",
        "followup_answer_text": "conditioning on a post-treatment metric biases the total effect",
        "evidence_summary": [
            "the engagement metric is measured after treatment assignment, so it sits on or after the treatment path",
            "controlling for it would contaminate the total-effect estimate rather than clean it up",
        ],
        "common_failure_modes": [
            "treating any predictive metric as a safe control without checking measurement timing",
            "confusing post-treatment adjustment with confounder adjustment",
        ],
    },
]


def build_pack() -> tuple[dict[str, Any], dict[str, Any], str]:
    mining_questions, mining_truth, _ = build_mining_pack()
    source_cases, source_truth_map = source_maps()

    questions = [dict(case) for case in mining_questions["cases"]]
    truth_cases = [dict(case) for case in mining_truth["cases"]]

    for recipe in EXTRA_CASES:
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
                "naturalness_rationale": "Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.",
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

    family_counts = Counter(case["task_family"] for case in questions)
    lines = [
        "# Track I High-Quality 30 Pack",
        "",
        f"Pack variant: `{PACK_VARIANT}`.",
        "",
        f"- Case count: `{len(questions)}`",
        f"- Source-backed ground truth count: `{len(truth_cases)}`",
        f"- Unique source cases used: `{len({case['source_case_id'] for case in questions})}`",
        "",
        "This pack extends the 17-case skill-mining pool into a 30-case high-quality set while keeping surfaces natural and source-backed.",
        "",
        "## Family Mix",
        "",
        "| Family | Cases |",
        "|---|---|",
    ]
    for family, count in sorted(family_counts.items()):
        lines.append(f"| `{family}` | `{count}` |")

    for question, truth_case in zip(questions, truth_cases, strict=True):
        lines.extend(
            [
                "",
                f"## {question['id']} — {question['title']}",
                "",
                f"- Source case: `{question['source_case_id']}`",
                f"- Family: `{question['task_family']}`",
                f"- Primary question: {question['question']}",
                f"- Canonical primary answer: `{truth_case['primary_answer_text']}`",
                f"- Follow-up question: {question['followup_question']}",
                f"- Canonical follow-up answer: `{truth_case['followup_answer_text']}`",
            ]
        )

    questions_json = {
        "track": "v14_track_i_high_quality_30",
        "pack_variant": PACK_VARIANT,
        "case_count": len(questions),
        "cases": questions,
    }
    truth_json = {
        "track": "v14_track_i_high_quality_30",
        "pack_variant": PACK_VARIANT,
        "case_count": len(truth_cases),
        "cases": truth_cases,
    }
    return questions_json, truth_json, "\n".join(lines).rstrip() + "\n"


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
