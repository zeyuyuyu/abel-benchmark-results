#!/usr/bin/env python3
"""Build the v12 general-finance challenge benchmark."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


V12_DIR = Path("/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v12")
ARTIFACTS_DIR = V12_DIR / "artifacts"
SNAPSHOT_FACTS_PATH = ARTIFACTS_DIR / "snapshot_facts.json"

DEFAULT_FACTS = {
    "snapshot_meta": {
        "version": "v12-general-finance-challenge",
        "snapshot_label": "March 25, 2026 (GMT+8)",
        "snapshot_date": "2026-03-25",
        "timezone": "GMT+8",
        "artifacts_manifest": "artifacts/manifest.json",
    },
    "normalized_nodes": {
        "BTC": "BTCUSD_close",
        "ETH": "ETHUSD_close",
    },
    "availability": {
        "AAPL": "ok",
        "AMD": "ok",
        "AVGO": "ok",
        "BTC": "unavailable",
        "CL": "ok",
        "ETH": "ok",
        "GC": "unavailable",
        "NVDA": "ok",
        "QQQ": "unavailable",
        "SOXX": "unavailable",
        "SPY": "unavailable",
        "TSM": "ok",
        "USO": "unavailable",
        "XLE": "unavailable",
    },
    "graph_paths": {
        "AAPL->NVDA": {"connected": True, "path_count": 1},
        "AMD->NVDA": {"connected": True, "path_count": 1},
        "AVGO->NVDA": {"connected": True, "path_count": 1},
        "TSM->NVDA": {"connected": True, "path_count": 1},
        "QQQ->NVDA": {"connected": False, "path_count": 0},
        "SPY->NVDA": {"connected": False, "path_count": 0},
        "SOXX->NVDA": {"connected": False, "path_count": 0},
        "AAPL->AMD": {"connected": True, "path_count": 1},
        "NVDA->AMD": {"connected": True, "path_count": 1},
        "AVGO->AMD": {"connected": True, "path_count": 1},
        "TSM->AMD": {"connected": True, "path_count": 1},
        "QQQ->AMD": {"connected": False, "path_count": 0},
        "SPY->AMD": {"connected": False, "path_count": 0},
        "SOXX->AMD": {"connected": False, "path_count": 0},
        "NVDA->AVGO": {"connected": True, "path_count": 1},
        "AMD->AVGO": {"connected": True, "path_count": 1},
        "NVDA->TSM": {"connected": True, "path_count": 1},
        "AMD->TSM": {"connected": True, "path_count": 1},
    },
    "interventions": {
        "NVDA->AMD": {
            "path_exists": True,
            "intervention_skipped": False,
            "skip_reason": None,
            "error_code": "invalid_intervention",
            "effect_returned": False,
        },
        "SOXX->AMD": {
            "path_exists": False,
            "intervention_skipped": True,
            "skip_reason": "no_directed_path_found",
            "error_code": None,
            "effect_returned": False,
        },
    },
}


def load_facts() -> dict[str, object]:
    if SNAPSHOT_FACTS_PATH.exists():
        return json.loads(SNAPSHOT_FACTS_PATH.read_text(encoding="utf-8"))
    return DEFAULT_FACTS


FACTS = load_facts()
SNAPSHOT = FACTS.get("snapshot_meta", {}).get("snapshot_label", "March 25, 2026 (GMT+8)")
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def build_prompt(question: str, options: list[str]) -> str:
    option_lines = [f"{LETTERS[i]}.  {text}" for i, text in enumerate(options)]
    return (
        "You are helping a user make a market decision. "
        f"Assume today's date is {SNAPSHOT}. "
        "Answer the user's question below by choosing the best option(s).\n\n"
        f"User question: {question}\n"
        + "\n".join(option_lines)
        + "\n\n"
        "Your final answer must be in boxed format only.\n"
        "Use \\boxed{A} for a single option, or \\boxed{B, C} for multiple options.\n"
        "Do not add explanation outside the box."
    )


def availability(alias: str) -> str:
    return str(FACTS["availability"].get(alias, "unavailable"))


def is_available(alias: str) -> bool:
    return availability(alias) == "ok"


def path_connected(key: str) -> bool:
    return bool(FACTS["graph_paths"].get(key, {}).get("connected", False))


def intervention_fact(key: str) -> dict[str, object]:
    return dict(FACTS["interventions"].get(key, {}))


def answer_from_indices(indices: list[int]) -> list[str]:
    return [LETTERS[index] for index in sorted(indices)]


def truth_set_answer(truths: list[bool]) -> list[str]:
    return answer_from_indices([idx for idx, truth in enumerate(truths) if truth])


def single_choice_answer(index: int) -> list[str]:
    return [LETTERS[index]]


QUESTIONS: list[dict[str, object]] = []
GROUND_TRUTH: list[dict[str, object]] = []


def add_case(
    *,
    case_id: str,
    pattern: str,
    category: str,
    question: str,
    options: list[str],
    answer_letters: list[str],
    grounding: dict[str, object],
    why_natural: str,
) -> None:
    labels = LETTERS[: len(options)]
    QUESTIONS.append(
        {
            "id": case_id,
            "futurex_pattern": pattern,
            "category": category,
            "question": question,
            "prompt": build_prompt(question, options),
            "options": [
                {"label": label, "text": text} for label, text in zip(labels, options)
            ],
            "why_this_is_a_natural_user_question": why_natural,
        }
    )
    GROUND_TRUTH.append(
        {
            "id": case_id,
            "category": category,
            "answer_letters": answer_letters,
            "answer_box": "\\boxed{" + ", ".join(answer_letters) + "}",
            "abel_grounding": grounding,
        }
    )


# Proxy and coverage guardrails
add_case(
    case_id="v12_001",
    pattern="winner market",
    category="proxy_selection",
    question="If you need one graph-grounded crypto risk proxy for a meeting right now, which is the safest anchor to lean on?",
    options=[
        "Bitcoin",
        "Ethereum",
        "Both Bitcoin and Ethereum are equally defensible",
        "Neither is safe to lean on",
    ],
    answer_letters=single_choice_answer(1),
    grounding={
        "availability": {"BTC": availability("BTC"), "ETH": availability("ETH")},
        "normalized_nodes": FACTS.get("normalized_nodes", {}),
    },
    why_natural="A PM or trader can naturally ask which crypto proxy is safer to reference in a live discussion.",
)

add_case(
    case_id="v12_002",
    pattern="winner market",
    category="proxy_selection",
    question="If you need one graph-grounded inflation-sensitive commodity anchor today, which is the safest one to lean on?",
    options=[
        "Gold",
        "Crude oil",
        "XLE",
        "Skip this graph for that commodity call",
    ],
    answer_letters=single_choice_answer(1),
    grounding={
        "availability": {"GC": availability("GC"), "CL": availability("CL"), "XLE": availability("XLE")},
    },
    why_natural="This reads like a normal macro desk question about what proxy to trust right now.",
)

add_case(
    case_id="v12_003",
    pattern="winner market",
    category="proxy_selection",
    question="If you want a shortcut stand-in for Nvidia today, which is the least misleading choice?",
    options=[
        "QQQ",
        "SPY",
        "SOXX",
        "Do not use any of those shortcut proxies",
    ],
    answer_letters=single_choice_answer(3),
    grounding={
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in ["QQQ->NVDA", "SPY->NVDA", "SOXX->NVDA"]
        }
    },
    why_natural="Users often ask whether a broad-market shortcut is good enough for a live conversation.",
)

add_case(
    case_id="v12_004",
    pattern="roster membership",
    category="coverage_guardrail",
    question="Which of these shortlists is fully supportable from today's public market graph?",
    options=[
        "Ethereum, crude oil, and Apple",
        "Bitcoin, gold, and SPY",
        "XLE, USO, and SOXX",
        "Bitcoin, Ethereum, and gold",
    ],
    answer_letters=single_choice_answer(0),
    grounding={
        "availability": {
            "ETH": availability("ETH"),
            "CL": availability("CL"),
            "AAPL": availability("AAPL"),
            "BTC": availability("BTC"),
            "GC": availability("GC"),
            "SPY": availability("SPY"),
            "XLE": availability("XLE"),
            "USO": availability("USO"),
            "SOXX": availability("SOXX"),
        }
    },
    why_natural="This is a natural 'which list can I safely present' question for a meeting or note.",
)

add_case(
    case_id="v12_005",
    pattern="statement-truth set",
    category="coverage_guardrail",
    question="Which of these names can you safely present as graph-grounded live reads today?",
    options=[
        "Apple",
        "Nvidia",
        "Ethereum",
        "Crude oil",
        "Bitcoin",
        "Gold",
        "XLE",
        "SOXX",
    ],
    answer_letters=truth_set_answer(
        [
            is_available("AAPL"),
            is_available("NVDA"),
            is_available("ETH"),
            is_available("CL"),
            is_available("BTC"),
            is_available("GC"),
            is_available("XLE"),
            is_available("SOXX"),
        ]
    ),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["AAPL", "NVDA", "ETH", "CL", "BTC", "GC", "XLE", "SOXX"]
        }
    },
    why_natural="This is the kind of filter a live analyst uses before naming concrete assets in a deck or call.",
)

add_case(
    case_id="v12_006",
    pattern="statement-truth set",
    category="coverage_guardrail",
    question='Which of these "obvious market proxies" should make you nervous if someone claims they are graph-grounded live reads today?',
    options=[
        "Bitcoin",
        "Gold",
        "QQQ",
        "SPY",
        "SOXX",
        "XLE",
        "USO",
        "Ethereum",
    ],
    answer_letters=truth_set_answer(
        [
            not is_available("BTC"),
            not is_available("GC"),
            not is_available("QQQ"),
            not is_available("SPY"),
            not is_available("SOXX"),
            not is_available("XLE"),
            not is_available("USO"),
            not is_available("ETH"),
        ]
    ),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["BTC", "GC", "QQQ", "SPY", "SOXX", "XLE", "USO", "ETH"]
        }
    },
    why_natural="The wording stays user-facing while testing whether the model knows which proxies are actually supportable.",
)

# Route membership and shortcut discrimination
add_case(
    case_id="v12_007",
    pattern="statement-truth set",
    category="route_membership",
    question="Which of these names actually show directed paths into Nvidia on today's market map?",
    options=[
        "Apple",
        "AMD",
        "Broadcom",
        "TSM",
        "QQQ",
        "SPY",
        "SOXX",
    ],
    answer_letters=truth_set_answer(
        [
            path_connected("AAPL->NVDA"),
            path_connected("AMD->NVDA"),
            path_connected("AVGO->NVDA"),
            path_connected("TSM->NVDA"),
            path_connected("QQQ->NVDA"),
            path_connected("SPY->NVDA"),
            path_connected("SOXX->NVDA"),
        ]
    ),
    grounding={
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in [
                "AAPL->NVDA",
                "AMD->NVDA",
                "AVGO->NVDA",
                "TSM->NVDA",
                "QQQ->NVDA",
                "SPY->NVDA",
                "SOXX->NVDA",
            ]
        }
    },
    why_natural="A user can naturally ask which names are real live routes into Nvidia rather than placeholders.",
)

add_case(
    case_id="v12_008",
    pattern="statement-truth set",
    category="route_membership",
    question="Which of these names actually show directed paths into AMD on today's market map?",
    options=[
        "Apple",
        "Nvidia",
        "Broadcom",
        "TSM",
        "QQQ",
        "SPY",
        "SOXX",
    ],
    answer_letters=truth_set_answer(
        [
            path_connected("AAPL->AMD"),
            path_connected("NVDA->AMD"),
            path_connected("AVGO->AMD"),
            path_connected("TSM->AMD"),
            path_connected("QQQ->AMD"),
            path_connected("SPY->AMD"),
            path_connected("SOXX->AMD"),
        ]
    ),
    grounding={
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in [
                "AAPL->AMD",
                "NVDA->AMD",
                "AVGO->AMD",
                "TSM->AMD",
                "QQQ->AMD",
                "SPY->AMD",
                "SOXX->AMD",
            ]
        }
    },
    why_natural="This mirrors a real watchlist-building question around AMD spillovers.",
)

add_case(
    case_id="v12_009",
    pattern="roster membership",
    category="route_membership",
    question="If you're building a live watchlist to explain Nvidia through local market structure, which basket is more defensible?",
    options=[
        "Apple, AMD, Broadcom, and TSM",
        "QQQ, SPY, SOXX, and Bitcoin",
        "Gold, XLE, USO, and SPY",
        "Ethereum, Bitcoin, gold, and QQQ",
    ],
    answer_letters=single_choice_answer(0),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["AAPL", "AMD", "AVGO", "TSM", "QQQ", "SPY", "SOXX", "BTC", "GC", "XLE", "USO", "ETH"]
        },
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in ["AAPL->NVDA", "AMD->NVDA", "AVGO->NVDA", "TSM->NVDA", "QQQ->NVDA", "SPY->NVDA", "SOXX->NVDA"]
        },
    },
    why_natural="This is a natural PM question about what should be on the first live monitoring screen.",
)

add_case(
    case_id="v12_010",
    pattern="roster membership",
    category="route_membership",
    question="If you're building a live watchlist to explain AMD through local market structure, which basket is more defensible?",
    options=[
        "Apple, Nvidia, Broadcom, and TSM",
        "QQQ, SPY, SOXX, and Bitcoin",
        "Gold, XLE, USO, and SPY",
        "Ethereum, Bitcoin, gold, and QQQ",
    ],
    answer_letters=single_choice_answer(0),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["AAPL", "NVDA", "AVGO", "TSM", "QQQ", "SPY", "SOXX", "BTC", "GC", "XLE", "USO", "ETH"]
        },
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in ["AAPL->AMD", "NVDA->AMD", "AVGO->AMD", "TSM->AMD", "QQQ->AMD", "SPY->AMD", "SOXX->AMD"]
        },
    },
    why_natural="It stays natural while testing whether the model prefers real local structure over generic placeholders.",
)

add_case(
    case_id="v12_011",
    pattern="statement-truth set",
    category="shortcut_guardrail",
    question='Which of these "obvious shortcut" routes into Nvidia should you actually avoid leaning on today?',
    options=[
        "QQQ",
        "SPY",
        "SOXX",
    ],
    answer_letters=truth_set_answer(
        [
            not path_connected("QQQ->NVDA"),
            not path_connected("SPY->NVDA"),
            not path_connected("SOXX->NVDA"),
        ]
    ),
    grounding={
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in ["QQQ->NVDA", "SPY->NVDA", "SOXX->NVDA"]
        }
    },
    why_natural="Users naturally ask which shortcuts are acceptable and which ones are too sloppy.",
)

add_case(
    case_id="v12_012",
    pattern="statement-truth set",
    category="shortcut_guardrail",
    question='Which of these "obvious shortcut" routes into AMD should you actually avoid leaning on today?',
    options=[
        "QQQ",
        "SPY",
        "SOXX",
    ],
    answer_letters=truth_set_answer(
        [
            not path_connected("QQQ->AMD"),
            not path_connected("SPY->AMD"),
            not path_connected("SOXX->AMD"),
        ]
    ),
    grounding={
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in ["QQQ->AMD", "SPY->AMD", "SOXX->AMD"]
        }
    },
    why_natural="This is a clean guardrail question for anyone building a quick AMD story.",
)

add_case(
    case_id="v12_013",
    pattern="winner market",
    category="market_story",
    question="Which story is better supported today for Nvidia?",
    options=[
        "Local single-name transmission exists while the obvious beta shortcuts look weak",
        "Broad beta proxies are cleaner than single-name routes",
        "Both stories are equally well supported",
        "Neither story has useful support",
    ],
    answer_letters=single_choice_answer(0),
    grounding={
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in ["AAPL->NVDA", "AMD->NVDA", "AVGO->NVDA", "TSM->NVDA", "QQQ->NVDA", "SPY->NVDA", "SOXX->NVDA"]
        }
    },
    why_natural="A strategist could naturally ask whether the better story is local transmission or broad beta.",
)

add_case(
    case_id="v12_014",
    pattern="winner market",
    category="market_story",
    question="Which story is better supported today for AMD?",
    options=[
        "Local single-name transmission exists while the obvious beta shortcuts look weak",
        "Broad beta proxies are cleaner than single-name routes",
        "Both stories are equally well supported",
        "Neither story has useful support",
    ],
    answer_letters=single_choice_answer(0),
    grounding={
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in ["AAPL->AMD", "NVDA->AMD", "AVGO->AMD", "TSM->AMD", "QQQ->AMD", "SPY->AMD", "SOXX->AMD"]
        }
    },
    why_natural="This keeps the question user-facing while still forcing route discrimination.",
)

# Stress and boundary handling
add_case(
    case_id="v12_015",
    pattern="winner market",
    category="stress_boundary",
    question="If you only had bandwidth for one first-pass stress question around AMD today, which is the most defensible place to start?",
    options=[
        "If Nvidia breaks first, what does that mean for AMD?",
        "If SOXX breaks first, what does that mean for AMD?",
        "If SPY breaks first, what does that mean for AMD?",
        "If Bitcoin breaks first, what does that mean for AMD?",
    ],
    answer_letters=single_choice_answer(0),
    grounding={
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in ["NVDA->AMD", "SOXX->AMD", "SPY->AMD"]
        },
        "availability": {"BTC": availability("BTC")},
    },
    why_natural="A live risk discussion often starts with a single 'best first stress question'.",
)

add_case(
    case_id="v12_016",
    pattern="statement-truth set",
    category="stress_boundary",
    question="Which statements are still safe to say about AMD stress tests today?",
    options=[
        "Nvidia is structurally connected to AMD",
        "SOXX is structurally connected to AMD",
        'The graph already gives a clean quantified "push Nvidia, get AMD" estimate',
        "Nvidia is the more defensible first stress lever for AMD than SOXX",
    ],
    answer_letters=truth_set_answer(
        [
            intervention_fact("NVDA->AMD").get("path_exists", False),
            intervention_fact("SOXX->AMD").get("path_exists", False),
            bool(intervention_fact("NVDA->AMD").get("effect_returned", False)),
            intervention_fact("NVDA->AMD").get("path_exists", False)
            and not intervention_fact("SOXX->AMD").get("path_exists", False),
        ]
    ),
    grounding={
        "interventions": {
            "NVDA->AMD": intervention_fact("NVDA->AMD"),
            "SOXX->AMD": intervention_fact("SOXX->AMD"),
        }
    },
    why_natural="A quant or PM can naturally ask which causal claims are safe versus overstated before presenting them.",
)

add_case(
    case_id="v12_017",
    pattern="winner market",
    category="proxy_selection",
    question="If you need one graph-grounded pair-trade lens today, which pair is the cleanest to lean on?",
    options=[
        "Ethereum and crude oil",
        "Bitcoin and gold",
        "SPY and QQQ",
        "XLE and USO",
    ],
    answer_letters=single_choice_answer(0),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["ETH", "CL", "BTC", "GC", "SPY", "QQQ", "XLE", "USO"]
        }
    },
    why_natural="This reads like a real pair-selection question for a fast market discussion.",
)

add_case(
    case_id="v12_018",
    pattern="winner market",
    category="proxy_selection",
    question='If someone insists on a live "broad US equity beta" read from this graph today, what is the safest answer?',
    options=[
        "Lean on QQQ",
        "Lean on SPY",
        "Either is fine",
        "Do not lean on either one",
    ],
    answer_letters=single_choice_answer(3),
    grounding={
        "availability": {"QQQ": availability("QQQ"), "SPY": availability("SPY")},
    },
    why_natural="Users often ask for the least-bad broad beta stand-in, and sometimes the right answer is to decline the shortcut.",
)

add_case(
    case_id="v12_019",
    pattern="statement-truth set",
    category="route_membership",
    question="Which of these names look like real two-way market neighbors of Nvidia today, rather than one-way or placeholder shortcuts?",
    options=[
        "AMD",
        "Broadcom",
        "TSM",
        "QQQ",
        "SPY",
        "SOXX",
    ],
    answer_letters=truth_set_answer(
        [
            path_connected("AMD->NVDA") and path_connected("NVDA->AMD"),
            path_connected("AVGO->NVDA") and path_connected("NVDA->AVGO"),
            path_connected("TSM->NVDA") and path_connected("NVDA->TSM"),
            path_connected("QQQ->NVDA") and False,
            path_connected("SPY->NVDA") and False,
            path_connected("SOXX->NVDA") and False,
        ]
    ),
    grounding={
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in ["AMD->NVDA", "NVDA->AMD", "AVGO->NVDA", "NVDA->AVGO", "TSM->NVDA", "NVDA->TSM", "QQQ->NVDA", "SPY->NVDA", "SOXX->NVDA"]
        }
    },
    why_natural="Two-way neighbor language is natural in a market-monitoring context and harder than one-direction shortcut questions.",
)

add_case(
    case_id="v12_020",
    pattern="statement-truth set",
    category="route_membership",
    question="Which of these names look like real two-way market neighbors of AMD today, rather than one-way or placeholder shortcuts?",
    options=[
        "Nvidia",
        "Broadcom",
        "TSM",
        "QQQ",
        "SPY",
        "SOXX",
    ],
    answer_letters=truth_set_answer(
        [
            path_connected("NVDA->AMD") and path_connected("AMD->NVDA"),
            path_connected("AVGO->AMD") and path_connected("AMD->AVGO"),
            path_connected("TSM->AMD") and path_connected("AMD->TSM"),
            path_connected("QQQ->AMD") and False,
            path_connected("SPY->AMD") and False,
            path_connected("SOXX->AMD") and False,
        ]
    ),
    grounding={
        "path_checks": {
            key: FACTS["graph_paths"][key]
            for key in ["NVDA->AMD", "AMD->NVDA", "AVGO->AMD", "AMD->AVGO", "TSM->AMD", "AMD->TSM", "QQQ->AMD", "SPY->AMD", "SOXX->AMD"]
        }
    },
    why_natural="This mirrors how a trader asks whether two names really belong in the same local monitoring cluster.",
)

add_case(
    case_id="v12_021",
    pattern="winner market",
    category="proxy_selection",
    question="If you need one graph-grounded commodity proxy right now, which is the safest one to cite?",
    options=[
        "Gold",
        "Crude oil",
        "XLE",
        "USO",
    ],
    answer_letters=single_choice_answer(1),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["GC", "CL", "XLE", "USO"]
        }
    },
    why_natural="This is a plain market-facing proxy choice question with no product-internal language.",
)

add_case(
    case_id="v12_022",
    pattern="statement-truth set",
    category="coverage_guardrail",
    question="Which of these names can you safely present as graph-grounded live reads today?",
    options=[
        "Ethereum",
        "Crude oil",
        "Bitcoin",
        "Gold",
    ],
    answer_letters=truth_set_answer(
        [
            is_available("ETH"),
            is_available("CL"),
            is_available("BTC"),
            is_available("GC"),
        ]
    ),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["ETH", "CL", "BTC", "GC"]
        }
    },
    why_natural="A PM can naturally ask which names are safe to quote in a graph-grounded note right now.",
)

add_case(
    case_id="v12_023",
    pattern="statement-truth set",
    category="coverage_guardrail",
    question='Which of these should make you nervous if someone claims they are graph-grounded live reads today?',
    options=[
        "Bitcoin",
        "Gold",
        "Ethereum",
        "Crude oil",
    ],
    answer_letters=truth_set_answer(
        [
            not is_available("BTC"),
            not is_available("GC"),
            not is_available("ETH"),
            not is_available("CL"),
        ]
    ),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["BTC", "GC", "ETH", "CL"]
        }
    },
    why_natural="This is the negative version of a standard supportability question.",
)

add_case(
    case_id="v12_024",
    pattern="winner market",
    category="proxy_selection",
    question="If you need one graph-grounded pair-trade lens today, which pair is the cleanest to lean on?",
    options=[
        "Ethereum and crude oil",
        "Bitcoin and gold",
        "SPY and QQQ",
        "XLE and USO",
    ],
    answer_letters=single_choice_answer(0),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["ETH", "CL", "BTC", "GC", "SPY", "QQQ", "XLE", "USO"]
        }
    },
    why_natural="This keeps the question fully natural while testing whether the model knows which pair is actually supportable.",
)

add_case(
    case_id="v12_025",
    pattern="winner market",
    category="proxy_selection",
    question="If you could keep only one crypto name on a graph-grounded watchlist today, which one survives the filter?",
    options=[
        "Bitcoin",
        "Ethereum",
        "Both Bitcoin and Ethereum",
        "Neither one survives the filter",
    ],
    answer_letters=single_choice_answer(1),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["BTC", "ETH"]
        }
    },
    why_natural="This is a natural watchlist triage question for a trader or PM.",
)

add_case(
    case_id="v12_026",
    pattern="winner market",
    category="proxy_selection",
    question="Which side is easier to defend in a graph-grounded crypto note right now?",
    options=[
        "Bitcoin",
        "Ethereum",
        "Both are equally easy to defend",
        "Neither is easy to defend",
    ],
    answer_letters=single_choice_answer(1),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["BTC", "ETH"]
        }
    },
    why_natural="This sounds like a normal editorial question before sending a market note.",
)

add_case(
    case_id="v12_027",
    pattern="winner market",
    category="coverage_guardrail",
    question="Which statement is safest if you want to stay graph-grounded on crypto today?",
    options=[
        "Bitcoin is supportable right now",
        "Ethereum is supportable right now",
        "Both Bitcoin and Ethereum are supportable right now",
        "Neither Bitcoin nor Ethereum is supportable right now",
    ],
    answer_letters=single_choice_answer(1),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["BTC", "ETH"]
        }
    },
    why_natural="This is a realistic wording for a PM checking how far they can safely go in a live note.",
)

add_case(
    case_id="v12_028",
    pattern="winner market",
    category="coverage_guardrail",
    question="Which name should make you more nervous if someone claims it is a graph-grounded crypto live read today?",
    options=[
        "Bitcoin",
        "Ethereum",
        "Both names should make you equally nervous",
        "Neither name should make you nervous",
    ],
    answer_letters=single_choice_answer(0),
    grounding={
        "availability": {
            alias: availability(alias)
            for alias in ["BTC", "ETH"]
        }
    },
    why_natural="It stays user-facing while probing whether the model can spot the weak crypto anchor.",
)


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    V12_DIR.mkdir(parents=True, exist_ok=True)
    category_counts = Counter(case["category"] for case in QUESTIONS)
    summary = {
        "version": "v12-general-finance-challenge",
        "snapshot_label": SNAPSHOT,
        "case_count": len(QUESTIONS),
        "category_counts": dict(sorted(category_counts.items())),
        "notes": [
            "Natural user-facing finance questions only; no Abel or CAP wording in prompts.",
            "Ground truth is derived from the live Abel snapshot recorded in artifacts/.",
            "This is a targeted challenge set meant to expose routing, proxy-choice, and guardrail differences.",
        ],
    }

    questions_payload = {"summary": summary, "cases": QUESTIONS}
    ground_truth_payload = {"summary": summary, "cases": GROUND_TRUTH}

    write_json(V12_DIR / "questions.json", questions_payload)
    write_json(V12_DIR / "ground_truth.json", ground_truth_payload)

    table_lines = [
        "# v12 Cases",
        "",
        f"Snapshot label: `{SNAPSHOT}`",
        "",
        "| Case ID | Category | Question |",
        "|---------|----------|----------|",
    ]
    for case in QUESTIONS:
        table_lines.append(
            f"| `{case['id']}` | `{case['category']}` | {case['question']} |"
        )
    (V12_DIR / "cases.md").write_text("\n".join(table_lines) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
