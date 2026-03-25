#!/usr/bin/env python3
"""Build the v10 natural-intent benchmark casebook."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


V10_DIR = Path("/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v10")
SNAPSHOT = "March 25, 2026 (GMT+8)"

FACTS = {
    "observe_pct": {
        "AAPL": 0.09639149017599172,
        "TSLA": -0.2406296289655383,
        "AMD": 0.20931723421453704,
        "NVDA": 0.04359642834965821,
        "INTC": -0.14087294122588326,
        "AVGO": -0.42783624749264547,
        "TSM": -0.06885487621693929,
        "CL": -0.1050836626590292,
        "ETH": -0.1634334446580476,
    },
    "graph_paths": {
        "NVDA->AMD": {"connected": True, "path_count": 1},
        "SOXX->AMD": {"connected": False, "path_count": 0},
        "AVGO->NVDA": {"connected": True, "path_count": 1},
        "TSM->NVDA": {"connected": True, "path_count": 1},
        "AMD->NVDA": {"connected": True, "path_count": 1},
        "QQQ->NVDA": {"connected": False, "path_count": 0},
        "SPY->NVDA": {"connected": False, "path_count": 0},
        "BTC->ETH": {"connected": False, "path_count": 0},
        "XLK->AAPL": {"connected": False, "path_count": 0},
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
    "counterfactuals": {
        "NVDA->AMD": {
            "status": "ok",
            "reachable": False,
            "effect_support": "no_structural_path",
            "path_count": 0,
            "preview_only": True,
        },
        "SOXX->AMD": {
            "status": "error",
            "error_code": "node_not_found",
        },
    },
    "availability": {
        "SOXX": "unavailable",
        "QQQ": "unavailable",
        "SPY": "unavailable",
        "BTC": "unavailable",
        "GC": "unavailable",
        "GLD": "unavailable",
        "AAPL": "ok",
        "NVDA": "ok",
        "ETH": "ok",
        "CL": "ok",
        "XLE": "unavailable",
        "USO": "unavailable",
    },
}


def build_prompt(question: str, options: list[str]) -> str:
    labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    option_lines = [f"{labels[i]}.  {text}" for i, text in enumerate(options)]
    return (
        "You are helping a user make a market call. "
        f"Assume today's date is {SNAPSHOT}. "
        "Answer the user's question below by choosing the best option(s).\n\n"
        f"User question: {question}\n"
        + "\n".join(option_lines)
        + "\n\n"
        "Your final answer must be in boxed format only.\n"
        "Use \\boxed{A} for a single option, or \\boxed{B, C} for multiple options.\n"
        "Do not add explanation outside the box."
    )


CASES: list[dict[str, object]] = []


def add_case(
    case_id: str,
    pattern: str,
    category: str,
    question: str,
    options: list[str],
    answer_letters: list[str],
    grounding: dict[str, object],
    why_natural: str,
) -> None:
    labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[: len(options)])
    CASES.append(
        {
            "id": case_id,
            "futurex_pattern": pattern,
            "category": category,
            "question": question,
            "prompt": build_prompt(question, options),
            "options": [
                {"label": label, "text": text} for label, text in zip(labels, options)
            ],
            "answer_letters": answer_letters,
            "answer_box": "\\boxed{" + ", ".join(answer_letters) + "}",
            "abel_grounding": grounding,
            "why_this_is_a_natural_user_question": why_natural,
        }
    )


# Directional buckets
add_case(
    "v10_001",
    "interval bin",
    "directional_bucket",
    "If you had to bucket AMD's near-term move right now, which range seems most plausible?",
    [
        "Down more than 0.30%",
        "Down between 0.10% and 0.30%",
        "Roughly flat, within +/-0.10%",
        "Up between 0.10% and 0.20%",
        "Up at least 0.20%",
    ],
    ["E"],
    {"asset": "AMD", "prediction_pct": FACTS["observe_pct"]["AMD"], "backing_node": "AMD_close"},
    "A trader or PM could naturally ask for a bucketed near-term move.",
)
add_case(
    "v10_002",
    "interval bin",
    "directional_bucket",
    "If you had to bucket Tesla's near-term move right now, which range seems most plausible?",
    [
        "Down more than 0.30%",
        "Down between 0.10% and 0.30%",
        "Roughly flat, within +/-0.10%",
        "Up between 0.10% and 0.20%",
        "Up at least 0.20%",
    ],
    ["B"],
    {"asset": "TSLA", "prediction_pct": FACTS["observe_pct"]["TSLA"], "backing_node": "TSLA_close"},
    "This is a normal market-read question with no tool-internal phrasing.",
)
add_case(
    "v10_003",
    "interval bin",
    "directional_bucket",
    "If you had to bucket Apple's near-term move right now, which range seems most plausible?",
    [
        "Down more than 0.30%",
        "Down between 0.10% and 0.30%",
        "Roughly flat, within +/-0.10%",
        "Up between 0.10% and 0.20%",
        "Up at least 0.20%",
    ],
    ["C"],
    {"asset": "AAPL", "prediction_pct": FACTS["observe_pct"]["AAPL"], "backing_node": "AAPL_close"},
    "A user can naturally ask for a quick bucket rather than a precise point forecast.",
)
add_case(
    "v10_004",
    "interval bin",
    "directional_bucket",
    "If you need a quick Ethereum read right now, which move bucket looks most plausible?",
    [
        "Down more than 0.30%",
        "Down between 0.10% and 0.30%",
        "Roughly flat, within +/-0.10%",
        "Up between 0.10% and 0.20%",
        "Up at least 0.20%",
    ],
    ["B"],
    {"asset": "ETH", "prediction_pct": FACTS["observe_pct"]["ETH"], "backing_node": "ETHUSD_close"},
    "Crypto users ask this kind of bucketed directional question all the time.",
)
add_case(
    "v10_005",
    "interval bin",
    "directional_bucket",
    "If you need a quick crude oil read right now, which move bucket looks most plausible?",
    [
        "Down more than 0.30%",
        "Down between 0.10% and 0.30%",
        "Roughly flat, within +/-0.10%",
        "Up between 0.10% and 0.20%",
        "Up at least 0.20%",
    ],
    ["B"],
    {"asset": "CL", "prediction_pct": FACTS["observe_pct"]["CL"], "backing_node": "CL_close"},
    "This is a natural energy-market framing rather than an internal tool query.",
)
add_case(
    "v10_006",
    "interval bin",
    "directional_bucket",
    "If you need a quick Broadcom read right now, which move bucket looks most plausible?",
    [
        "Down more than 0.30%",
        "Down between 0.10% and 0.30%",
        "Roughly flat, within +/-0.10%",
        "Up between 0.10% and 0.20%",
        "Up at least 0.20%",
    ],
    ["A"],
    {"asset": "AVGO", "prediction_pct": FACTS["observe_pct"]["AVGO"], "backing_node": "AVGO_close"},
    "It is normal to ask for a rough short-term move bucket on a single name.",
)

# Threshold ladders
add_case(
    "v10_007",
    "threshold ladder",
    "directional_thresholds",
    "Which of these increasingly bullish claims about Apple still hold on a short-term read right now?",
    [
        "Apple is not worse than -0.50%",
        "Apple is not worse than -0.30%",
        "Apple is not worse than -0.10%",
        "Apple is at least flat",
        "Apple is up at least 0.10%",
    ],
    ["A", "B", "C", "D"],
    {"asset": "AAPL", "prediction_pct": FACTS["observe_pct"]["AAPL"], "backing_node": "AAPL_close"},
    "This keeps FutureX's monotonic threshold style but makes it read like a human analyst question.",
)
add_case(
    "v10_008",
    "threshold ladder",
    "directional_thresholds",
    "Which of these increasingly bullish claims about Tesla still hold on a short-term read right now?",
    [
        "Tesla is not worse than -0.50%",
        "Tesla is not worse than -0.30%",
        "Tesla is not worse than -0.10%",
        "Tesla is at least flat",
        "Tesla is up at least 0.10%",
    ],
    ["A", "B"],
    {"asset": "TSLA", "prediction_pct": FACTS["observe_pct"]["TSLA"], "backing_node": "TSLA_close"},
    "This is still a natural user question: how much damage is already implied?",
)
add_case(
    "v10_009",
    "threshold ladder",
    "directional_thresholds",
    "Which of these increasingly bullish claims about AMD still hold on a short-term read right now?",
    [
        "AMD is not worse than -0.50%",
        "AMD is not worse than -0.30%",
        "AMD is not worse than -0.10%",
        "AMD is at least flat",
        "AMD is up at least 0.10%",
    ],
    ["A", "B", "C", "D", "E"],
    {"asset": "AMD", "prediction_pct": FACTS["observe_pct"]["AMD"], "backing_node": "AMD_close"},
    "A user can naturally ask how many bullish thresholds are still alive right now.",
)
add_case(
    "v10_010",
    "threshold ladder",
    "directional_thresholds",
    "Which of these increasingly bullish claims about Broadcom still hold on a short-term read right now?",
    [
        "Broadcom is not worse than -0.50%",
        "Broadcom is not worse than -0.30%",
        "Broadcom is not worse than -0.10%",
        "Broadcom is at least flat",
        "Broadcom is up at least 0.10%",
    ],
    ["A"],
    {"asset": "AVGO", "prediction_pct": FACTS["observe_pct"]["AVGO"], "backing_node": "AVGO_close"},
    "The threshold framing stays natural while still producing an exact-scored answer.",
)
add_case(
    "v10_011",
    "threshold ladder",
    "directional_thresholds",
    "Which of these increasingly bullish claims about Ethereum still hold on a short-term read right now?",
    [
        "Ethereum is not worse than -0.50%",
        "Ethereum is not worse than -0.30%",
        "Ethereum is not worse than -0.10%",
        "Ethereum is at least flat",
        "Ethereum is up at least 0.10%",
    ],
    ["A", "B"],
    {"asset": "ETH", "prediction_pct": FACTS["observe_pct"]["ETH"], "backing_node": "ETHUSD_close"},
    "This is a natural crypto question that indirectly benefits from the latest skill normalization.",
)

# Ranking
add_case(
    "v10_012",
    "winner market",
    "ranking",
    "Among Nvidia, AMD, Intel, Broadcom, and TSM, which semiconductor name looks strongest right now?",
    ["Nvidia", "AMD", "Intel", "Broadcom", "TSM"],
    ["B"],
    {
        "basket": ["NVDA", "AMD", "INTC", "AVGO", "TSM"],
        "prediction_pct": {k: FACTS["observe_pct"][k] for k in ["NVDA", "AMD", "INTC", "AVGO", "TSM"]},
    },
    "Picking the strongest name in a known basket is a normal user task.",
)
add_case(
    "v10_013",
    "winner market",
    "ranking",
    "Among Apple, Tesla, Nvidia, and Broadcom, which mega-cap tech name looks strongest right now?",
    ["Apple", "Tesla", "Nvidia", "Broadcom"],
    ["A"],
    {
        "basket": ["AAPL", "TSLA", "NVDA", "AVGO"],
        "prediction_pct": {k: FACTS["observe_pct"][k] for k in ["AAPL", "TSLA", "NVDA", "AVGO"]},
    },
    "A PM or trader could naturally ask which large-cap tech name leads the tape.",
)
add_case(
    "v10_014",
    "top-k membership",
    "ranking",
    "Which three names look strongest right now on a short-term read?",
    ["Apple", "Tesla", "AMD", "Nvidia", "Intel", "Broadcom", "TSM"],
    ["A", "C", "D"],
    {
        "top3": ["AMD", "AAPL", "NVDA"],
        "prediction_pct": {k: FACTS["observe_pct"][k] for k in ["AAPL", "TSLA", "AMD", "NVDA", "INTC", "AVGO", "TSM"]},
    },
    "Top-3 membership is a classic benchmark shape and also a plausible natural question.",
)
add_case(
    "v10_015",
    "top-k membership",
    "ranking",
    "Which three names look weakest right now on a short-term read?",
    ["Apple", "Tesla", "AMD", "Nvidia", "Intel", "Broadcom", "TSM", "Crude oil"],
    ["B", "E", "F"],
    {
        "bottom3": ["AVGO", "TSLA", "INTC"],
        "prediction_pct": {k: FACTS["observe_pct"][k] for k in ["AAPL", "TSLA", "AMD", "NVDA", "INTC", "AVGO", "TSM", "CL"]},
    },
    "This is the natural inverse of a 'who looks strongest' question.",
)

# Transmission / routing
add_case(
    "v10_016",
    "winner market",
    "transmission",
    "If you wanted one shock anchor to stress-test AMD today, which starting point is most defensible?",
    ["Nvidia", "SOXX", "QQQ", "SPY"],
    ["A"],
    {
        "relevant_paths": {
            "NVDA->AMD": FACTS["graph_paths"]["NVDA->AMD"],
            "SOXX->AMD": FACTS["graph_paths"]["SOXX->AMD"],
        },
        "intervention_support": FACTS["interventions"]["NVDA->AMD"],
    },
    "Analysts naturally ask which anchor is the cleanest way to stress-test a downstream name.",
)
add_case(
    "v10_017",
    "roster membership",
    "transmission",
    "If you are trying to explain Nvidia through company channels rather than broad market beta, which names actually look wired in today?",
    ["Broadcom", "TSM", "QQQ", "SPY"],
    ["A", "B"],
    {
        "relevant_paths": {
            "AVGO->NVDA": FACTS["graph_paths"]["AVGO->NVDA"],
            "TSM->NVDA": FACTS["graph_paths"]["TSM->NVDA"],
            "QQQ->NVDA": FACTS["graph_paths"]["QQQ->NVDA"],
            "SPY->NVDA": FACTS["graph_paths"]["SPY->NVDA"],
        }
    },
    "This is a normal 'what's really feeding into this name' question.",
)
add_case(
    "v10_018",
    "winner market",
    "transmission",
    "If you were explaining Nvidia to a PM today, which framing is stronger?",
    [
        "Company-level semiconductor channels like Broadcom and TSM",
        "Broad index beta through QQQ and SPY",
        "Both frames are equally strong",
        "Neither frame has meaningful support",
    ],
    ["A"],
    {
        "upstream_company_routes": ["AVGO->NVDA", "TSM->NVDA"],
        "broad_beta_routes": ["QQQ->NVDA", "SPY->NVDA"],
    },
    "This is still a normal explanatory question, not an internal graph query.",
)
add_case(
    "v10_019",
    "winner market",
    "transmission",
    "Which spillover story is easiest to defend right now?",
    [
        "Nvidia into AMD",
        "SOXX into AMD",
        "Bitcoin into Ethereum",
        "XLK into Apple",
    ],
    ["A"],
    {
        "path_snapshot": {
            "NVDA->AMD": FACTS["graph_paths"]["NVDA->AMD"],
            "SOXX->AMD": FACTS["graph_paths"]["SOXX->AMD"],
            "BTC->ETH": FACTS["graph_paths"]["BTC->ETH"],
            "XLK->AAPL": FACTS["graph_paths"]["XLK->AAPL"],
        }
    },
    "A user could naturally ask which causal spillover story is most grounded today.",
)
add_case(
    "v10_020",
    "winner market",
    "transmission",
    "If you want company names that seem most relevant for following Nvidia today, which basket is the best starting point?",
    [
        "Broadcom, TSM, and AMD",
        "SOXX, QQQ, and SPY",
        "Apple, crude oil, and Ethereum",
        "None of these baskets look meaningfully connected",
    ],
    ["A"],
    {
        "supporting_paths": {
            "AVGO->NVDA": FACTS["graph_paths"]["AVGO->NVDA"],
            "TSM->NVDA": FACTS["graph_paths"]["TSM->NVDA"],
            "AMD->NVDA": FACTS["graph_paths"]["AMD->NVDA"],
        }
    },
    "It asks for a sensible starting basket, which is how a real analyst might phrase the problem.",
)
add_case(
    "v10_021",
    "roster membership",
    "transmission",
    "Which of these broad shortcuts look less useful than real company read-throughs for Nvidia right now?",
    ["QQQ", "SPY", "Broadcom", "TSM"],
    ["A", "B"],
    {
        "broad_routes": {
            "QQQ->NVDA": FACTS["graph_paths"]["QQQ->NVDA"],
            "SPY->NVDA": FACTS["graph_paths"]["SPY->NVDA"],
        },
        "company_routes": {
            "AVGO->NVDA": FACTS["graph_paths"]["AVGO->NVDA"],
            "TSM->NVDA": FACTS["graph_paths"]["TSM->NVDA"],
        },
    },
    "This is a natural 'which shortcuts are actually bad anchors' question.",
)

# Pressure tests / what-if
add_case(
    "v10_022",
    "winner market",
    "pressure_test",
    "You ask for a quick 'what if Nvidia jumps 5%' read on AMD. Which description fits best right now?",
    [
        "You get a clean quantified downstream scenario",
        "There is a reason to care, but you still do not get a clean quantified read-through",
        "There is clearly no link at all",
        "The setup is missing the target entirely",
    ],
    ["B"],
    {
        "intervention": FACTS["interventions"]["NVDA->AMD"],
        "counterfactual": FACTS["counterfactuals"]["NVDA->AMD"],
    },
    "A user can naturally ask for a quick what-if on a familiar pair like Nvidia and AMD.",
)
add_case(
    "v10_023",
    "winner market",
    "pressure_test",
    "You ask for the same 'what if' read on AMD, but this time using SOXX as the shock anchor. Which description fits best?",
    [
        "You get a clean quantified downstream scenario",
        "The setup breaks before you get a usable downstream scenario",
        "It behaves the same way as the Nvidia case",
        "It routes cleanly through broad index beta",
    ],
    ["B"],
    {
        "intervention": FACTS["interventions"]["SOXX->AMD"],
        "counterfactual": FACTS["counterfactuals"]["SOXX->AMD"],
    },
    "This is still a normal user question about whether a what-if read is usable.",
)
add_case(
    "v10_024",
    "winner market",
    "pressure_test",
    "Which setup is more likely to fall apart before it becomes a usable downstream scenario?",
    ["Nvidia into AMD", "SOXX into AMD", "Both", "Neither"],
    ["B"],
    {
        "intervention_nvda": FACTS["interventions"]["NVDA->AMD"],
        "intervention_soxx": FACTS["interventions"]["SOXX->AMD"],
    },
    "Users often want to know which scenario is worth trying at all.",
)
add_case(
    "v10_025",
    "winner market",
    "pressure_test",
    "If you want a quick one-hour read-through from Nvidia into AMD, what is closest to the current answer?",
    [
        "A clear reachable scenario",
        "A preview that stays disconnected or unsupported",
        "A hard target-missing error",
        "A strong upside estimate",
    ],
    ["B"],
    {"counterfactual": FACTS["counterfactuals"]["NVDA->AMD"]},
    "This is a plausible user-facing way to ask for a quick preview without naming internal verbs.",
)

# Coverage / supportability
add_case(
    "v10_026",
    "winner market",
    "coverage",
    "If you need a crypto name you can make a more defensible call on right now, which is safer to lean on?",
    ["Bitcoin", "Ethereum", "Both are equally grounded", "Neither is grounded enough"],
    ["B"],
    {
        "availability": {
            "BTC": FACTS["availability"]["BTC"],
            "ETH": FACTS["availability"]["ETH"],
        }
    },
    "A normal user could absolutely ask which of two assets is more supportable right now.",
)
add_case(
    "v10_027",
    "winner market",
    "coverage",
    "If you need one energy-linked market anchor you can make a defensible call on today, which is the cleanest choice?",
    ["Crude oil", "XLE", "USO", "Gold"],
    ["A"],
    {
        "availability": {
            "CL": FACTS["availability"]["CL"],
            "XLE": FACTS["availability"]["XLE"],
            "USO": FACTS["availability"]["USO"],
            "GC": FACTS["availability"]["GC"],
        }
    },
    "This is a natural coverage-selection question, not an internal availability query.",
)
add_case(
    "v10_028",
    "roster membership",
    "coverage",
    "Which of these popular shortcuts look weakest if you need a defensible live read right now?",
    ["SOXX", "QQQ", "SPY", "Nvidia", "Apple"],
    ["A", "B", "C"],
    {
        "availability": {
            "SOXX": FACTS["availability"]["SOXX"],
            "QQQ": FACTS["availability"]["QQQ"],
            "SPY": FACTS["availability"]["SPY"],
            "NVDA": FACTS["availability"]["NVDA"],
            "AAPL": FACTS["availability"]["AAPL"],
        }
    },
    "Users naturally ask which shortcuts are weak anchors today.",
)
add_case(
    "v10_029",
    "roster membership",
    "coverage",
    "Which of these are easier to support right now with a defensible live read?",
    ["Ethereum", "Apple", "Nvidia", "SOXX", "Bitcoin"],
    ["A", "B", "C"],
    {
        "availability": {
            "ETH": FACTS["availability"]["ETH"],
            "AAPL": FACTS["availability"]["AAPL"],
            "NVDA": FACTS["availability"]["NVDA"],
            "SOXX": FACTS["availability"]["SOXX"],
            "BTC": FACTS["availability"]["BTC"],
        }
    },
    "This is the natural positive version of the same supportability question.",
)
add_case(
    "v10_030",
    "statement-truth set",
    "market_story",
    "Which of these quick takes sound right right now?",
    [
        "AMD looks stronger than Nvidia",
        "Apple looks stronger than Tesla",
        "Broadcom looks weaker than Intel",
        "TSM looks stronger than AMD",
        "Crude oil looks stronger than Apple",
    ],
    ["A", "B", "C"],
    {
        "comparison_set": {
            "AMD": FACTS["observe_pct"]["AMD"],
            "NVDA": FACTS["observe_pct"]["NVDA"],
            "AAPL": FACTS["observe_pct"]["AAPL"],
            "TSLA": FACTS["observe_pct"]["TSLA"],
            "AVGO": FACTS["observe_pct"]["AVGO"],
            "INTC": FACTS["observe_pct"]["INTC"],
            "TSM": FACTS["observe_pct"]["TSM"],
            "CL": FACTS["observe_pct"]["CL"],
        }
    },
    "This asks for natural comparative takes instead of raw internal facts.",
)
add_case(
    "v10_031",
    "statement-truth set",
    "market_story",
    "Which coverage statements sound right today?",
    [
        "Ethereum is easier to ground than Bitcoin",
        "Crude oil is easier to ground than XLE",
        "SOXX is easier to ground than Nvidia",
        "QQQ is easier to ground than Apple",
        "Broad index shortcuts are the cleanest anchors today",
    ],
    ["A", "B"],
    {
        "availability": FACTS["availability"],
    },
    "A user can naturally ask which market handles are more trustworthy right now.",
)
add_case(
    "v10_032",
    "winner market",
    "market_story",
    "If you want a basket of names that are actually usable for a defensible market read today, which one is best?",
    [
        "Apple, Nvidia, and Ethereum",
        "SOXX, QQQ, and SPY",
        "Both baskets are equally usable",
        "Neither basket is usable enough",
    ],
    ["A"],
    {
        "availability": {
            "AAPL": FACTS["availability"]["AAPL"],
            "NVDA": FACTS["availability"]["NVDA"],
            "ETH": FACTS["availability"]["ETH"],
            "SOXX": FACTS["availability"]["SOXX"],
            "QQQ": FACTS["availability"]["QQQ"],
            "SPY": FACTS["availability"]["SPY"],
        }
    },
    "This is a basket-selection question, which is a very common user framing.",
)
add_case(
    "v10_033",
    "winner market",
    "market_story",
    "If you want one clear leader and one clear laggard from this snapshot, which pair fits best?",
    [
        "AMD and Broadcom",
        "Nvidia and Apple",
        "TSM and AMD",
        "Intel and crude oil",
    ],
    ["A"],
    {
        "prediction_pct": {
            "AMD": FACTS["observe_pct"]["AMD"],
            "AVGO": FACTS["observe_pct"]["AVGO"],
            "NVDA": FACTS["observe_pct"]["NVDA"],
            "AAPL": FACTS["observe_pct"]["AAPL"],
            "TSM": FACTS["observe_pct"]["TSM"],
            "INTC": FACTS["observe_pct"]["INTC"],
            "CL": FACTS["observe_pct"]["CL"],
        }
    },
    "A PM could naturally ask for the cleanest leader-laggard pair in a snapshot.",
)
add_case(
    "v10_034",
    "statement-truth set",
    "market_story",
    "Which of these quick cross-name reads sound right right now?",
    [
        "Nvidia looks stronger than TSM",
        "Crude oil looks stronger than Intel",
        "Apple looks weaker than Nvidia",
        "Tesla looks stronger than Broadcom",
        "Ethereum looks stronger than Apple",
    ],
    ["A", "B", "D"],
    {
        "comparison_set": {
            "NVDA": FACTS["observe_pct"]["NVDA"],
            "TSM": FACTS["observe_pct"]["TSM"],
            "CL": FACTS["observe_pct"]["CL"],
            "INTC": FACTS["observe_pct"]["INTC"],
            "AAPL": FACTS["observe_pct"]["AAPL"],
            "TSLA": FACTS["observe_pct"]["TSLA"],
            "AVGO": FACTS["observe_pct"]["AVGO"],
            "ETH": FACTS["observe_pct"]["ETH"],
        }
    },
    "This keeps the FutureX-style truth-set format but makes it feel like a normal trading-desk comparison.",
)
add_case(
    "v10_035",
    "winner market",
    "ranking",
    "Among Apple, Nvidia, TSM, and crude oil, which looks closest to unchanged right now?",
    ["Apple", "Nvidia", "TSM", "Crude oil"],
    ["B"],
    {
        "basket": ["AAPL", "NVDA", "TSM", "CL"],
        "prediction_pct": {
            "AAPL": FACTS["observe_pct"]["AAPL"],
            "NVDA": FACTS["observe_pct"]["NVDA"],
            "TSM": FACTS["observe_pct"]["TSM"],
            "CL": FACTS["observe_pct"]["CL"],
        },
        "absolute_move_order": ["NVDA", "TSM", "AAPL", "CL"],
    },
    "Asking which name is closest to flat is a very normal market snapshot question.",
)
add_case(
    "v10_036",
    "winner market",
    "ranking",
    "Among Tesla, Intel, Broadcom, and crude oil, which looks under the most pressure right now?",
    ["Tesla", "Intel", "Broadcom", "Crude oil"],
    ["C"],
    {
        "basket": ["TSLA", "INTC", "AVGO", "CL"],
        "prediction_pct": {
            "TSLA": FACTS["observe_pct"]["TSLA"],
            "INTC": FACTS["observe_pct"]["INTC"],
            "AVGO": FACTS["observe_pct"]["AVGO"],
            "CL": FACTS["observe_pct"]["CL"],
        },
    },
    "This is the bearish mirror of a standard 'what looks strongest' question.",
)
add_case(
    "v10_037",
    "winner market",
    "coverage",
    "If you need one market handle that is most likely to waste your time today, which is it?",
    ["SOXX", "Apple", "Nvidia", "Ethereum"],
    ["A"],
    {
        "availability": {
            "SOXX": FACTS["availability"]["SOXX"],
            "AAPL": FACTS["availability"]["AAPL"],
            "NVDA": FACTS["availability"]["NVDA"],
            "ETH": FACTS["availability"]["ETH"],
        }
    },
    "Users often ask which candidate handle is least worth leaning on before doing more work.",
)
add_case(
    "v10_038",
    "roster membership",
    "coverage",
    "Which of these names are better choices right now than broad shortcut proxies if you need a quick defensible call?",
    ["Apple", "Nvidia", "Ethereum", "QQQ", "SPY"],
    ["A", "B", "C"],
    {
        "availability": {
            "AAPL": FACTS["availability"]["AAPL"],
            "NVDA": FACTS["availability"]["NVDA"],
            "ETH": FACTS["availability"]["ETH"],
            "QQQ": FACTS["availability"]["QQQ"],
            "SPY": FACTS["availability"]["SPY"],
        }
    },
    "This is a natural watchlist-prioritization question rather than an internal availability check.",
)
add_case(
    "v10_039",
    "statement-truth set",
    "pressure_test",
    "Which what-if statements sound right today?",
    [
        "Nvidia is at least worth checking as a shock anchor for AMD",
        "SOXX is a cleaner shock anchor for AMD than Nvidia",
        "The Nvidia-to-AMD what-if is easier to motivate than the SOXX-to-AMD one",
        "Both setups give equally clean quantified downstream outputs",
        "The SOXX-to-AMD setup can fall apart before it becomes usable",
    ],
    ["A", "C", "E"],
    {
        "intervention_nvda": FACTS["interventions"]["NVDA->AMD"],
        "intervention_soxx": FACTS["interventions"]["SOXX->AMD"],
        "counterfactual_nvda": FACTS["counterfactuals"]["NVDA->AMD"],
    },
    "A real user could plausibly ask which scenario is even worth putting on the whiteboard.",
)
add_case(
    "v10_040",
    "winner market",
    "transmission",
    "If you are trying to tell a company-specific story around Nvidia, which pair is the least convincing place to start?",
    [
        "QQQ and SPY",
        "Broadcom and TSM",
        "Broadcom and AMD",
        "TSM and AMD",
    ],
    ["A"],
    {
        "broad_routes": {
            "QQQ->NVDA": FACTS["graph_paths"]["QQQ->NVDA"],
            "SPY->NVDA": FACTS["graph_paths"]["SPY->NVDA"],
        },
        "company_routes": {
            "AVGO->NVDA": FACTS["graph_paths"]["AVGO->NVDA"],
            "TSM->NVDA": FACTS["graph_paths"]["TSM->NVDA"],
            "AMD->NVDA": FACTS["graph_paths"]["AMD->NVDA"],
        },
    },
    "It is natural to ask which explanatory starting point is least persuasive before committing to a story.",
)


def write_outputs() -> None:
    V10_DIR.mkdir(parents=True, exist_ok=True)
    summary = {
        "version": "v10-natural-intent-casebook",
        "generation_method": "llm_authored_with_live_snapshot",
        "snapshot_date": "2026-03-25",
        "timezone": "GMT+8",
        "case_count": len(CASES),
        "pattern_counts": dict(
            sorted(Counter(case["futurex_pattern"] for case in CASES).items())
        ),
        "category_counts": dict(
            sorted(Counter(case["category"] for case in CASES).items())
        ),
    }
    payload = {
        "summary": summary,
        "cases": CASES,
    }
    (V10_DIR / "natural_intent_cases.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    lines = [
        "# v10 Natural-Intent Casebook",
        "",
        f"Snapshot: `{SNAPSHOT}`",
        "",
        "These cases are written as questions a normal user might actually ask. The answer key is still anchored to the same live snapshot, but the prompts do not expose Abel / CAP internals.",
        "",
        "## Summary",
        "",
        f"- Total cases: `{summary['case_count']}`",
        f"- Generation method: `{summary['generation_method']}`",
        "",
        "## Pattern Counts",
        "",
        "| Pattern | Count |",
        "|---------|-------|",
    ]
    for pattern, count in summary["pattern_counts"].items():
        lines.append(f"| `{pattern}` | `{count}` |")
    lines.extend(
        [
            "",
            "## Cases",
            "",
            "| Case ID | Category | Answer | Question |",
            "|---------|----------|--------|----------|",
        ]
    )
    for case in CASES:
        lines.append(
            f"| `{case['id']}` | `{case['category']}` | `{case['answer_box']}` | {case['question']} |"
        )
    lines.extend(
        [
            "",
            "## Files",
            "",
            "- Dataset: [`natural_intent_cases.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v10/natural_intent_cases.json)",
            "- Spec: [`casebook_spec.md`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v10/casebook_spec.md)",
            "- Generator: [`build_natural_intent_casebook.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v10/build_natural_intent_casebook.py)",
        ]
    )
    (V10_DIR / "cases.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    write_outputs()
