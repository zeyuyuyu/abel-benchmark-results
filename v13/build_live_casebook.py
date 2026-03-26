#!/usr/bin/env python3
"""Build the v13 live-only finance benchmark package."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

import yfinance as yf
from datasets import load_dataset


ROOT = Path("/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v13")
ARTIFACTS_DIR = ROOT / "artifacts"
QUESTIONS_PATH = ROOT / "questions.json"
GROUND_TRUTH_PATH = ROOT / "ground_truth.json"
CASES_PATH = ROOT / "cases.md"
SPEC_PATH = ROOT / "casebook_spec.md"
REFERENCE_SNAPSHOT_PATH = ARTIFACTS_DIR / "reference_snapshot.json"
FUTUREX_ROWS_PATH = ARTIFACTS_DIR / "futurex_online_rows.json"
MANIFEST_PATH = ARTIFACTS_DIR / "manifest.json"

TODAY_CONTEXT = "March 25, 2026 (GMT+8, Asia/Shanghai)"
RESOLUTION_DATE = "2026-03-31"
DATASET_NAME = "futurex-ai/Futurex-Online"
OFFICIAL_IDS = [
    "69a2e39e5692ef005cdbf2d9",  # S&P 500 Single-Day Gains and Losses (%) in Q1
    "69a2e39e5692ef005cdbf2e9",  # What will KOSPI (^KS11) hit in Q1 2026?
    "69a2e39e5692ef005cdbf2d8",  # Q1 S&P 500 Performance
    "69a2e39e5692ef005cdbf2e8",  # Will KOSPI (KS11) close above __ end of Q1?
    "69a4319df2cb3b006875e9d0",  # What price will Bitcoin hit by March 2026?
    "699c4887d1d3cf005c1e48ad",  # Banxico interest rate decision in March
    "69a2e39e5692ef005cdbf27c",  # Robinhood launches prediction market through MIAXdx by March 31?
]
REFERENCE_SYMBOLS = ["GC=F", "CL=F", "BTC-USD", "ETH-USD", "NVDA", "AMD", "AVGO", "TSM", "TSLA"]

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def round_to_grid(value: float, grid: float, *, mode: str) -> float:
    if mode == "down":
        return math.floor(value / grid) * grid
    if mode == "up":
        return math.ceil(value / grid) * grid
    return round(value / grid) * grid


def fmt_price(value: float, decimals: int = 0) -> str:
    if decimals == 0:
        return f"${value:,.0f}"
    return f"${value:,.{decimals}f}"


def capture_reference_snapshot() -> dict[str, Any]:
    snapshot: dict[str, Any] = {
        "today_context": TODAY_CONTEXT,
        "resolution_date": RESOLUTION_DATE,
        "symbols": {},
    }
    for symbol in REFERENCE_SYMBOLS:
        hist = yf.Ticker(symbol).history(period="20d", interval="1d", auto_adjust=False)
        hist = hist.dropna(subset=["Close"])
        if hist.empty:
            raise RuntimeError(f"No valid history returned for {symbol}")
        row = hist.iloc[-1]
        index = hist.index[-1]
        snapshot["symbols"][symbol] = {
            "symbol": symbol,
            "date": index.date().isoformat(),
            "timezone": str(index.tz),
            "open": round(float(row["Open"]), 4),
            "high": round(float(row["High"]), 4),
            "low": round(float(row["Low"]), 4),
            "close": round(float(row["Close"]), 4),
            "volume": int(row["Volume"]) if not math.isnan(float(row["Volume"])) else None,
        }
    return snapshot


def load_futurex_rows() -> list[dict[str, Any]]:
    dataset = load_dataset(DATASET_NAME, split="train")
    row_map = {row["id"]: row for row in dataset}
    return [row_map[source_id] for source_id in OFFICIAL_IDS]


def official_category(title: str) -> str:
    lower = title.lower()
    if "hit" in lower:
        return "threshold_ladder"
    if "close above" in lower or "performance" in lower:
        return "threshold_truth_set"
    if "decision" in lower or "launches" in lower:
        return "binary_event"
    return "futurex_official"


def build_letter_prompt(question: str, options: list[str], *, end_time: str) -> str:
    option_lines = "\n".join(f"{LETTERS[idx]}.  {text}" for idx, text in enumerate(options))
    return (
        'You are an agent that can predict future events. The event to be predicted: "'
        f"{question} (resolved around {end_time} (GMT+8)). \n"
        f"{option_lines}"
        '"\n'
        "IMPORTANT: Your final answer MUST end with this exact format:\n\n"
        "Your task is to identify all the correct option(s) based on your analysis.\n"
        "Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.\n"
        "Your final answer MUST end with this exact format:\n"
        "listing all correct option(s) you have identified, separated by commas, within the box.\n"
        "For example: \\boxed{A} for a single correct option, or \\boxed{B, C} for multiple correct options.\n\n"
        "Do not use any other format. Do not refuse to make a prediction. Do not say \"I cannot predict the future.\" You must make a clear prediction based on the best data currently available, using the box format specified above."
    )


def build_yes_no_prompt(question: str, *, end_time: str) -> str:
    return (
        'You are an agent that can predict future events. The event to be predicted: "'
        f'{question} (resolved around {end_time} (GMT+8)). " '
        "IMPORTANT: Your final answer MUST end with this exact format: "
        "\\boxed{Yes} or \\boxed{No} "
        "Do not use any other format. Do not refuse to make a prediction. Do not say \"I cannot predict the future.\" "
        "You must make a clear prediction based on the best data currently available, using the box format specified above."
    )


def add_case(
    questions: list[dict[str, Any]],
    ground_truth: list[dict[str, Any]],
    *,
    case_id: str,
    source_type: str,
    title: str,
    category: str,
    pattern: str,
    question: str,
    prompt: str,
    answer_format: str,
    options: list[dict[str, str]] | None,
    end_time: str,
    ground_truth_spec: dict[str, Any],
) -> None:
    questions.append(
        {
            "id": case_id,
            "source_type": source_type,
            "title": title,
            "category": category,
            "futurex_pattern": pattern,
            "question": question,
            "prompt": prompt,
            "answer_format": answer_format,
            "options": options,
            "end_time": end_time,
        }
    )
    ground_truth.append(
        {
            "id": case_id,
            "status": "pending",
            "answer_box": None,
            "answer_tokens": None,
            "resolution_spec": ground_truth_spec,
        }
    )


def build_custom_cases(snapshot: dict[str, Any]) -> list[dict[str, Any]]:
    ref = snapshot["symbols"]
    snapshot_date = ref["NVDA"]["date"]

    gold_close = ref["GC=F"]["close"]
    gold_mid = round_to_grid(gold_close, 50, mode="nearest")
    gold_bounds = [gold_mid - 100, gold_mid - 50, gold_mid, gold_mid + 50]

    eth_close = ref["ETH-USD"]["close"]
    eth_mid = round_to_grid(eth_close, 100, mode="nearest")
    eth_bounds = [eth_mid - 150, eth_mid - 50, eth_mid + 50, eth_mid + 150]

    btc_close = ref["BTC-USD"]["close"]
    btc_base = round_to_grid(btc_close, 1000, mode="nearest")
    btc_thresholds = [btc_base - 3000, btc_base - 1000, btc_base + 1000, btc_base + 4000, btc_base + 9000]

    crude_close = ref["CL=F"]["close"]
    crude_highs = [
        int(round_to_grid(crude_close + 1, 2, mode="up")),
        int(round_to_grid(crude_close + 3, 2, mode="up")),
        int(round_to_grid(crude_close + 6, 5, mode="up")),
    ]
    crude_lows = [
        int(round_to_grid(crude_close - 1, 2, mode="down")),
        int(round_to_grid(crude_close - 3, 2, mode="down")),
        int(round_to_grid(crude_close - 6, 2, mode="down")),
    ]

    nvda_threshold = int(round_to_grid(ref["NVDA"]["close"] * 1.03, 5, mode="up"))
    amd_threshold = int(round_to_grid(ref["AMD"]["close"] * 1.03, 5, mode="up"))

    custom_cases: list[dict[str, Any]] = [
        {
            "title": "What will Gold futures (GC) settle at on the final trading day of March 2026?",
            "category": "month_end_bucket",
            "pattern": "interval bin",
            "question": "What will Gold futures (GC) settle at on the final trading day of March 2026?",
            "answer_format": "boxed_letters",
            "options": [
                f"Gold futures (GC) settle below {fmt_price(gold_bounds[0])}",
                f"Gold futures (GC) settle at least {fmt_price(gold_bounds[0])} but below {fmt_price(gold_bounds[1])}",
                f"Gold futures (GC) settle at least {fmt_price(gold_bounds[1])} but below {fmt_price(gold_bounds[2])}",
                f"Gold futures (GC) settle at least {fmt_price(gold_bounds[2])} but below {fmt_price(gold_bounds[3])}",
                f"Gold futures (GC) settle at least {fmt_price(gold_bounds[3])}",
            ],
            "resolution_spec": {
                "source": "yfinance",
                "method": "close_bucket",
                "symbol": "GC=F",
                "resolution_date": RESOLUTION_DATE,
                "buckets": [
                    {"label": "A", "type": "lt", "value": gold_bounds[0]},
                    {"label": "B", "type": "range", "lower": gold_bounds[0], "upper": gold_bounds[1]},
                    {"label": "C", "type": "range", "lower": gold_bounds[1], "upper": gold_bounds[2]},
                    {"label": "D", "type": "range", "lower": gold_bounds[2], "upper": gold_bounds[3]},
                    {"label": "E", "type": "ge", "value": gold_bounds[3]},
                ],
            },
        },
        {
            "title": "Which of these WTI crude oil futures (CL) levels will trade at any point before March 31, 2026?",
            "category": "hit_levels",
            "pattern": "threshold ladder",
            "question": "Which of these WTI crude oil futures (CL) levels will trade at any point before March 31, 2026?",
            "answer_format": "boxed_letters",
            "options": [
                f"WTI crude oil futures (CL) hit {fmt_price(crude_highs[0])} on the high side before March 31, 2026",
                f"WTI crude oil futures (CL) hit {fmt_price(crude_highs[1])} on the high side before March 31, 2026",
                f"WTI crude oil futures (CL) hit {fmt_price(crude_highs[2])} on the high side before March 31, 2026",
                f"WTI crude oil futures (CL) hit {fmt_price(crude_lows[0])} on the low side before March 31, 2026",
                f"WTI crude oil futures (CL) hit {fmt_price(crude_lows[1])} on the low side before March 31, 2026",
                f"WTI crude oil futures (CL) hit {fmt_price(crude_lows[2])} on the low side before March 31, 2026",
            ],
            "resolution_spec": {
                "source": "yfinance",
                "method": "hit_levels",
                "symbol": "CL=F",
                "start_date": ref["CL=F"]["date"],
                "resolution_date": RESOLUTION_DATE,
                "levels": [
                    {"label": "A", "direction": "high", "value": crude_highs[0]},
                    {"label": "B", "direction": "high", "value": crude_highs[1]},
                    {"label": "C", "direction": "high", "value": crude_highs[2]},
                    {"label": "D", "direction": "low", "value": crude_lows[0]},
                    {"label": "E", "direction": "low", "value": crude_lows[1]},
                    {"label": "F", "direction": "low", "value": crude_lows[2]},
                ],
            },
        },
        {
            "title": "Which of these increasingly bullish claims about Bitcoin will still be true at the March 2026 close?",
            "category": "month_end_thresholds",
            "pattern": "statement-truth set",
            "question": "Which of these increasingly bullish claims about Bitcoin will still be true at the March 2026 close?",
            "answer_format": "boxed_letters",
            "options": [
                f"Bitcoin closes above {fmt_price(btc_thresholds[0])} at the March 2026 close",
                f"Bitcoin closes above {fmt_price(btc_thresholds[1])} at the March 2026 close",
                f"Bitcoin closes above {fmt_price(btc_thresholds[2])} at the March 2026 close",
                f"Bitcoin closes above {fmt_price(btc_thresholds[3])} at the March 2026 close",
                f"Bitcoin closes above {fmt_price(btc_thresholds[4])} at the March 2026 close",
            ],
            "resolution_spec": {
                "source": "yfinance",
                "method": "close_threshold_truths",
                "symbol": "BTC-USD",
                "resolution_date": RESOLUTION_DATE,
                "thresholds": [
                    {"label": "A", "operator": "gt", "value": btc_thresholds[0]},
                    {"label": "B", "operator": "gt", "value": btc_thresholds[1]},
                    {"label": "C", "operator": "gt", "value": btc_thresholds[2]},
                    {"label": "D", "operator": "gt", "value": btc_thresholds[3]},
                    {"label": "E", "operator": "gt", "value": btc_thresholds[4]},
                ],
            },
        },
        {
            "title": "What will Ethereum (ETH-USD) be worth at the March 2026 close?",
            "category": "month_end_bucket",
            "pattern": "interval bin",
            "question": "What will Ethereum (ETH-USD) be worth at the March 2026 close?",
            "answer_format": "boxed_letters",
            "options": [
                f"Ethereum closes below {fmt_price(eth_bounds[0])}",
                f"Ethereum closes at least {fmt_price(eth_bounds[0])} but below {fmt_price(eth_bounds[1])}",
                f"Ethereum closes at least {fmt_price(eth_bounds[1])} but below {fmt_price(eth_bounds[2])}",
                f"Ethereum closes at least {fmt_price(eth_bounds[2])} but below {fmt_price(eth_bounds[3])}",
                f"Ethereum closes at least {fmt_price(eth_bounds[3])}",
            ],
            "resolution_spec": {
                "source": "yfinance",
                "method": "close_bucket",
                "symbol": "ETH-USD",
                "resolution_date": RESOLUTION_DATE,
                "buckets": [
                    {"label": "A", "type": "lt", "value": eth_bounds[0]},
                    {"label": "B", "type": "range", "lower": eth_bounds[0], "upper": eth_bounds[1]},
                    {"label": "C", "type": "range", "lower": eth_bounds[1], "upper": eth_bounds[2]},
                    {"label": "D", "type": "range", "lower": eth_bounds[2], "upper": eth_bounds[3]},
                    {"label": "E", "type": "ge", "value": eth_bounds[3]},
                ],
            },
        },
        {
            "title": "Which semiconductor stock will post the best percentage return from the March 25, 2026 close through the March 31, 2026 close?",
            "category": "winner_market",
            "pattern": "winner market",
            "question": "Which semiconductor stock will post the best percentage return from the March 25, 2026 close through the March 31, 2026 close?",
            "answer_format": "boxed_letters",
            "options": [
                "NVIDIA (NVDA)",
                "AMD (AMD)",
                "Broadcom (AVGO)",
                "Taiwan Semiconductor (TSM)",
            ],
            "resolution_spec": {
                "source": "yfinance",
                "method": "winner_by_return",
                "resolution_date": RESOLUTION_DATE,
                "symbols": {
                    "A": {"symbol": "NVDA", "reference_close": ref["NVDA"]["close"], "reference_date": ref["NVDA"]["date"]},
                    "B": {"symbol": "AMD", "reference_close": ref["AMD"]["close"], "reference_date": ref["AMD"]["date"]},
                    "C": {"symbol": "AVGO", "reference_close": ref["AVGO"]["close"], "reference_date": ref["AVGO"]["date"]},
                    "D": {"symbol": "TSM", "reference_close": ref["TSM"]["close"], "reference_date": ref["TSM"]["date"]},
                },
            },
        },
        {
            "title": "Which of these semiconductor stocks will finish March 2026 above their March 25, 2026 close?",
            "category": "up_membership",
            "pattern": "roster membership",
            "question": "Which of these semiconductor stocks will finish March 2026 above their March 25, 2026 close?",
            "answer_format": "boxed_letters",
            "options": [
                "NVIDIA (NVDA)",
                "AMD (AMD)",
                "Broadcom (AVGO)",
                "Taiwan Semiconductor (TSM)",
            ],
            "resolution_spec": {
                "source": "yfinance",
                "method": "membership_above_reference",
                "resolution_date": RESOLUTION_DATE,
                "symbols": {
                    "A": {"symbol": "NVDA", "reference_close": ref["NVDA"]["close"], "reference_date": ref["NVDA"]["date"]},
                    "B": {"symbol": "AMD", "reference_close": ref["AMD"]["close"], "reference_date": ref["AMD"]["date"]},
                    "C": {"symbol": "AVGO", "reference_close": ref["AVGO"]["close"], "reference_date": ref["AVGO"]["date"]},
                    "D": {"symbol": "TSM", "reference_close": ref["TSM"]["close"], "reference_date": ref["TSM"]["date"]},
                },
            },
        },
        {
            "title": "Which of these risk assets will finish March 2026 above their March 25, 2026 close?",
            "category": "up_membership",
            "pattern": "roster membership",
            "question": "Which of these risk assets will finish March 2026 above their March 25, 2026 close?",
            "answer_format": "boxed_letters",
            "options": [
                "Bitcoin (BTC-USD)",
                "Ethereum (ETH-USD)",
                "Tesla (TSLA)",
                "NVIDIA (NVDA)",
            ],
            "resolution_spec": {
                "source": "yfinance",
                "method": "membership_above_reference",
                "resolution_date": RESOLUTION_DATE,
                "symbols": {
                    "A": {"symbol": "BTC-USD", "reference_close": ref["BTC-USD"]["close"], "reference_date": ref["BTC-USD"]["date"]},
                    "B": {"symbol": "ETH-USD", "reference_close": ref["ETH-USD"]["close"], "reference_date": ref["ETH-USD"]["date"]},
                    "C": {"symbol": "TSLA", "reference_close": ref["TSLA"]["close"], "reference_date": ref["TSLA"]["date"]},
                    "D": {"symbol": "NVDA", "reference_close": ref["NVDA"]["close"], "reference_date": ref["NVDA"]["date"]},
                },
            },
        },
        {
            "title": "Which will post the larger percentage return from the March 25, 2026 close through the March 31, 2026 close?",
            "category": "winner_market",
            "pattern": "winner market",
            "question": "Which will post the larger percentage return from the March 25, 2026 close through the March 31, 2026 close?",
            "answer_format": "boxed_letters",
            "options": [
                "Bitcoin (BTC-USD)",
                "Ethereum (ETH-USD)",
            ],
            "resolution_spec": {
                "source": "yfinance",
                "method": "winner_by_return",
                "resolution_date": RESOLUTION_DATE,
                "symbols": {
                    "A": {"symbol": "BTC-USD", "reference_close": ref["BTC-USD"]["close"], "reference_date": ref["BTC-USD"]["date"]},
                    "B": {"symbol": "ETH-USD", "reference_close": ref["ETH-USD"]["close"], "reference_date": ref["ETH-USD"]["date"]},
                },
            },
        },
        {
            "title": f"Will NVIDIA stock close above {fmt_price(nvda_threshold)} by March 31, 2026?",
            "category": "binary_price_event",
            "pattern": "binary",
            "question": f"Will NVIDIA stock close above {fmt_price(nvda_threshold)} by March 31, 2026?",
            "answer_format": "boxed_yes_no",
            "options": None,
            "resolution_spec": {
                "source": "yfinance",
                "method": "binary_close_threshold",
                "symbol": "NVDA",
                "resolution_date": RESOLUTION_DATE,
                "operator": "gt",
                "value": nvda_threshold,
            },
        },
        {
            "title": f"Will AMD stock close above {fmt_price(amd_threshold)} by March 31, 2026?",
            "category": "binary_price_event",
            "pattern": "binary",
            "question": f"Will AMD stock close above {fmt_price(amd_threshold)} by March 31, 2026?",
            "answer_format": "boxed_yes_no",
            "options": None,
            "resolution_spec": {
                "source": "yfinance",
                "method": "binary_close_threshold",
                "symbol": "AMD",
                "resolution_date": RESOLUTION_DATE,
                "operator": "gt",
                "value": amd_threshold,
            },
        },
    ]

    for case in custom_cases:
        if case["answer_format"] == "boxed_yes_no":
            case["prompt"] = build_yes_no_prompt(case["question"], end_time=RESOLUTION_DATE)
        else:
            case["prompt"] = build_letter_prompt(case["question"], case["options"], end_time=RESOLUTION_DATE)
        case["reference_snapshot_date"] = snapshot_date
    return custom_cases


def render_cases_markdown(questions: list[dict[str, Any]]) -> str:
    lines = [
        "# v13 Live-Only Finance Cases",
        "",
        "This index intentionally excludes answers. Ground truth stays separate in `ground_truth.json` and is backfilled only through third-party resolution rules.",
        "",
        f"Today context: `{TODAY_CONTEXT}`",
        "",
        "| Case ID | Source | Category | End Time | Title |",
        "|---------|--------|----------|----------|-------|",
    ]
    for case in questions:
        lines.append(
            f"| `{case['id']}` | `{case['source_type']}` | `{case['category']}` | `{case['end_time']}` | {case['title']} |"
        )
    return "\n".join(lines) + "\n"


def render_spec_markdown(question_count: int) -> str:
    return "\n".join(
        [
            "# v13 Casebook Spec",
            "",
            "## Goal",
            "",
            "v13 is the first benchmark in this repo that is intentionally designed to avoid collapsing into historical search.",
            "",
            "- It is live-only.",
            "- It does not use Abel itself as ground truth.",
            "- It keeps the benchmark question surface general and finance-facing.",
            "- It compares unrestricted `codex` vs unrestricted `codex + causal-abel`, with normal search allowed for both.",
            "",
            "## Composition",
            "",
            f"- Official current-week `FutureX-Online` finance tasks: `{len(OFFICIAL_IDS)}`",
            f"- Custom `FutureX`-style live market tasks resolved by public price data: `{question_count - len(OFFICIAL_IDS)}`",
            f"- Total cases: `{question_count}`",
            "",
            "## Ground Truth Policy",
            "",
            "- Official `FutureX-Online` cases resolve by matching the same `id` after it lands in `FutureX-Past`.",
            "- Custom live cases resolve through `yfinance` daily data using explicit rules stored in `ground_truth.json`.",
            "- No answer is written into `questions.json`.",
            "- `cases.md` intentionally omits the answer key.",
            "",
            "## Why This Is Better Than FutureX-Past For The Main Benchmark",
            "",
            "- `FutureX-Past` is valuable as historical reference, but it can degrade into after-the-fact search.",
            "- `v13` forces the model to make live forward predictions and wait for later resolution.",
            "- This means any eventual accuracy gap between base and skill is much more meaningful.",
            "",
            "## Artifacts",
            "",
            "- `artifacts/futurex_online_rows.json`: raw official source rows used in the benchmark.",
            "- `artifacts/reference_snapshot.json`: the build-time market reference snapshot for custom live tasks.",
            "- `artifacts/manifest.json`: artifact index.",
            "",
            "## Reproducibility",
            "",
            "- Build package: `python3 /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v13/build_live_casebook.py`",
            "- Run live A/B: `python3 /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v13/test_script.py`",
            "- Backfill scores later: `python3 /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v13/rescore_live.py`",
        ]
    ) + "\n"


def main() -> None:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    official_rows = load_futurex_rows()
    snapshot = capture_reference_snapshot()

    questions: list[dict[str, Any]] = []
    ground_truth: list[dict[str, Any]] = []

    for index, row in enumerate(official_rows, start=1):
        case_id = f"v13_{index:03d}"
        title = row["en_title"]
        add_case(
            questions,
            ground_truth,
            case_id=case_id,
            source_type="futurex_online",
            title=title,
            category=official_category(title),
            pattern="futurex_official",
            question=title,
            prompt=row["prompt"],
            answer_format="boxed_yes_no" if "\\boxed{Yes}" in row["prompt"] else "boxed_letters",
            options=None,
            end_time=row["end_time"],
            ground_truth_spec={
                "source": "futurex_past_backfill",
                "dataset_name": "futurex-ai/Futurex-Past",
                "source_id": row["id"],
                "expected_after": row["end_time"],
                "title": title,
            },
        )

    custom_cases = build_custom_cases(snapshot)
    for offset, case in enumerate(custom_cases, start=len(questions) + 1):
        case_id = f"v13_{offset:03d}"
        options = None
        if case["options"] is not None:
            options = [
                {"label": LETTERS[idx], "text": text}
                for idx, text in enumerate(case["options"])
            ]
        add_case(
            questions,
            ground_truth,
            case_id=case_id,
            source_type="custom_live",
            title=case["title"],
            category=case["category"],
            pattern=case["pattern"],
            question=case["question"],
            prompt=case["prompt"],
            answer_format=case["answer_format"],
            options=options,
            end_time=RESOLUTION_DATE,
            ground_truth_spec=case["resolution_spec"],
        )

    QUESTIONS_PATH.write_text(
        json.dumps(
            {
                "version": "v13-live-only-finance",
                "today_context": TODAY_CONTEXT,
                "question_count": len(questions),
                "cases": questions,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    GROUND_TRUTH_PATH.write_text(
        json.dumps(
            {
                "version": "v13-live-only-finance",
                "today_context": TODAY_CONTEXT,
                "case_count": len(ground_truth),
                "cases": ground_truth,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    CASES_PATH.write_text(render_cases_markdown(questions), encoding="utf-8")
    SPEC_PATH.write_text(render_spec_markdown(len(questions)), encoding="utf-8")
    REFERENCE_SNAPSHOT_PATH.write_text(
        json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    FUTUREX_ROWS_PATH.write_text(
        json.dumps(official_rows, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    MANIFEST_PATH.write_text(
        json.dumps(
            {
                "files": [
                    {"path": "artifacts/futurex_online_rows.json", "description": "Raw official FutureX-Online source rows included in v13."},
                    {"path": "artifacts/reference_snapshot.json", "description": "Build-time market snapshot used to parameterize custom live tasks."},
                    {"path": "questions.json", "description": "Benchmark questions only, with no answer key."},
                    {"path": "ground_truth.json", "description": "Pending answer store plus explicit third-party resolution specs."},
                ]
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Built v13 with {len(questions)} cases.")


if __name__ == "__main__":
    main()
