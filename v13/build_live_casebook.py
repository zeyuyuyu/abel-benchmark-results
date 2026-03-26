#!/usr/bin/env python3
"""Build the v13 live-only finance benchmark package."""

from __future__ import annotations

import json
import math
from datetime import datetime
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
CUSTOM_SEEDS_PATH = ROOT / "llm_custom_case_seeds.json"

TODAY_CONTEXT = "March 26, 2026 (GMT+8, Asia/Shanghai)"
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
TARGET_TOTAL_CASES = 100

ASSET_CONFIGS = {
    "GC=F": {"label": "Gold futures (GC)", "grid": 50},
    "CL=F": {"label": "WTI crude oil futures (CL)", "grid": 2},
    "BTC-USD": {"label": "Bitcoin (BTC-USD)", "grid": 2000},
    "ETH-USD": {"label": "Ethereum (ETH-USD)", "grid": 100},
    "NVDA": {"label": "NVIDIA (NVDA)", "grid": 5},
    "AMD": {"label": "AMD (AMD)", "grid": 5},
    "AVGO": {"label": "Broadcom (AVGO)", "grid": 5},
    "TSM": {"label": "Taiwan Semiconductor (TSM)", "grid": 5},
    "TSLA": {"label": "Tesla (TSLA)", "grid": 10},
    "AAPL": {"label": "Apple (AAPL)", "grid": 5},
    "MSFT": {"label": "Microsoft (MSFT)", "grid": 5},
    "AMZN": {"label": "Amazon (AMZN)", "grid": 5},
    "META": {"label": "Meta (META)", "grid": 10},
    "GOOGL": {"label": "Alphabet (GOOGL)", "grid": 5},
    "QQQ": {"label": "Invesco QQQ Trust (QQQ)", "grid": 5},
    "SPY": {"label": "SPDR S&P 500 ETF (SPY)", "grid": 5},
    "IWM": {"label": "iShares Russell 2000 ETF (IWM)", "grid": 5},
    "SOXX": {"label": "iShares Semiconductor ETF (SOXX)", "grid": 5},
    "XLE": {"label": "Energy Select Sector SPDR Fund (XLE)", "grid": 2},
    "XLF": {"label": "Financial Select Sector SPDR Fund (XLF)", "grid": 2},
    "GLD": {"label": "SPDR Gold Shares (GLD)", "grid": 5},
    "SLV": {"label": "iShares Silver Trust (SLV)", "grid": 1},
    "COIN": {"label": "Coinbase (COIN)", "grid": 5},
    "MSTR": {"label": "Strategy (MSTR)", "grid": 20},
    "XOM": {"label": "Exxon Mobil (XOM)", "grid": 2},
    "CVX": {"label": "Chevron (CVX)", "grid": 2},
    "JPM": {"label": "JPMorgan Chase (JPM)", "grid": 5},
    "GS": {"label": "Goldman Sachs (GS)", "grid": 10},
    "BAC": {"label": "Bank of America (BAC)", "grid": 1},
}

BUCKET_SYMBOLS = [
    "GC=F",
    "CL=F",
    "BTC-USD",
    "ETH-USD",
    "NVDA",
    "AMD",
    "AVGO",
    "TSM",
    "TSLA",
    "AAPL",
    "MSFT",
    "AMZN",
    "META",
    "QQQ",
    "SPY",
]

THRESHOLD_SYMBOLS = [
    "BTC-USD",
    "ETH-USD",
    "NVDA",
    "AMD",
    "TSLA",
    "AAPL",
    "MSFT",
    "AMZN",
    "META",
    "QQQ",
    "SOXX",
    "GLD",
]

HIT_SYMBOLS = [
    "CL=F",
    "GC=F",
    "BTC-USD",
    "ETH-USD",
    "NVDA",
    "AMD",
    "TSLA",
    "QQQ",
    "SPY",
    "SOXX",
    "COIN",
    "MSTR",
]

BINARY_CASE_SPECS = [
    {"symbol": "NVDA", "direction": "gt", "pct": 0.03},
    {"symbol": "AMD", "direction": "gt", "pct": 0.04},
    {"symbol": "AVGO", "direction": "gt", "pct": 0.03},
    {"symbol": "TSM", "direction": "gt", "pct": 0.03},
    {"symbol": "TSLA", "direction": "gt", "pct": 0.05},
    {"symbol": "AAPL", "direction": "gt", "pct": 0.02},
    {"symbol": "MSFT", "direction": "gt", "pct": 0.02},
    {"symbol": "AMZN", "direction": "gt", "pct": 0.03},
    {"symbol": "META", "direction": "gt", "pct": 0.03},
    {"symbol": "QQQ", "direction": "gt", "pct": 0.02},
    {"symbol": "SPY", "direction": "gt", "pct": 0.015},
    {"symbol": "IWM", "direction": "gt", "pct": 0.02},
    {"symbol": "BTC-USD", "direction": "gt", "pct": 0.04},
    {"symbol": "ETH-USD", "direction": "gt", "pct": 0.05},
    {"symbol": "COIN", "direction": "gt", "pct": 0.05},
    {"symbol": "MSTR", "direction": "gt", "pct": 0.06},
    {"symbol": "XLE", "direction": "lt", "pct": 0.03},
    {"symbol": "XLF", "direction": "lt", "pct": 0.02},
]

GROUP_SPECS = [
    {"group_label": "semiconductor names", "symbols": ["NVDA", "AMD", "AVGO", "TSM"]},
    {"group_label": "megacap tech names", "symbols": ["AAPL", "MSFT", "AMZN", "META"]},
    {"group_label": "market beta ETFs", "symbols": ["SPY", "QQQ", "IWM"]},
    {"group_label": "crypto assets and proxies", "symbols": ["BTC-USD", "ETH-USD", "COIN", "MSTR"]},
    {"group_label": "energy names", "symbols": ["CL=F", "XLE", "XOM", "CVX"]},
    {"group_label": "financial names", "symbols": ["XLF", "JPM", "GS", "BAC"]},
    {"group_label": "precious-metals names", "symbols": ["GC=F", "GLD", "SLV"]},
    {"group_label": "AI platform names", "symbols": ["NVDA", "MSFT", "META", "AMZN"]},
    {"group_label": "high-beta growth names", "symbols": ["TSLA", "COIN", "MSTR", "SOXX"]},
]

HEAD_TO_HEAD_SPECS = [
    ("BTC-USD", "ETH-USD"),
    ("NVDA", "AMD"),
    ("AAPL", "MSFT"),
    ("AMZN", "META"),
    ("SPY", "QQQ"),
    ("XLE", "XLF"),
    ("GC=F", "CL=F"),
    ("COIN", "MSTR"),
    ("GLD", "SLV"),
    ("SOXX", "QQQ"),
    ("TSLA", "NVDA"),
    ("JPM", "GS"),
    ("XOM", "CVX"),
    ("AAPL", "AMZN"),
    ("META", "GOOGL"),
    ("AVGO", "TSM"),
    ("IWM", "SPY"),
    ("BTC-USD", "COIN"),
]

REFERENCE_SYMBOLS = sorted(ASSET_CONFIGS)

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


def human_date(iso_date: str) -> str:
    return datetime.fromisoformat(iso_date).strftime("%B %d, %Y")


def asset_label(symbol: str) -> str:
    return ASSET_CONFIGS[symbol]["label"]


def asset_grid(symbol: str) -> int:
    return int(ASSET_CONFIGS[symbol]["grid"])


def render_seed_text(seed: dict[str, Any], **context: Any) -> tuple[str, str]:
    title_template = seed.get("title", seed["question"])
    question_template = seed["question"]
    return title_template.format(**context), question_template.format(**context)


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


def load_custom_case_seeds() -> list[dict[str, Any]]:
    payload = json.loads(CUSTOM_SEEDS_PATH.read_text(encoding="utf-8"))
    return payload["cases"]


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


def build_bucket_case(seed: dict[str, Any], ref: dict[str, Any]) -> dict[str, Any]:
    symbol = seed["symbol"]
    close_value = float(ref[symbol]["close"])
    grid = asset_grid(symbol)
    mid = round_to_grid(close_value, grid, mode="nearest")
    bounds = [mid - (2 * grid), mid - grid, mid, mid + grid]
    title, question = render_seed_text(
        seed,
        label=asset_label(symbol),
        resolution_date=human_date(RESOLUTION_DATE),
    )
    return {
        "title": title,
        "category": seed.get("category", "month_end_bucket"),
        "pattern": seed.get("pattern", "interval bin"),
        "question": question,
        "answer_format": "boxed_letters",
        "options": [
            f"{asset_label(symbol)} closes below {fmt_price(bounds[0])}",
            f"{asset_label(symbol)} closes at least {fmt_price(bounds[0])} but below {fmt_price(bounds[1])}",
            f"{asset_label(symbol)} closes at least {fmt_price(bounds[1])} but below {fmt_price(bounds[2])}",
            f"{asset_label(symbol)} closes at least {fmt_price(bounds[2])} but below {fmt_price(bounds[3])}",
            f"{asset_label(symbol)} closes at least {fmt_price(bounds[3])}",
        ],
        "resolution_spec": {
            "source": "yfinance",
            "method": "close_bucket",
            "symbol": symbol,
            "resolution_date": RESOLUTION_DATE,
            "buckets": [
                {"label": "A", "type": "lt", "value": bounds[0]},
                {"label": "B", "type": "range", "lower": bounds[0], "upper": bounds[1]},
                {"label": "C", "type": "range", "lower": bounds[1], "upper": bounds[2]},
                {"label": "D", "type": "range", "lower": bounds[2], "upper": bounds[3]},
                {"label": "E", "type": "ge", "value": bounds[3]},
            ],
        },
    }


def build_threshold_case(seed: dict[str, Any], ref: dict[str, Any]) -> dict[str, Any]:
    symbol = seed["symbol"]
    close_value = float(ref[symbol]["close"])
    grid = asset_grid(symbol)
    base = round_to_grid(close_value, grid, mode="nearest")
    thresholds = [base - (2 * grid), base - grid, base, base + grid, base + (2 * grid)]
    title, question = render_seed_text(
        seed,
        label=asset_label(symbol),
        resolution_date=human_date(RESOLUTION_DATE),
    )
    return {
        "title": title,
        "category": seed.get("category", "month_end_thresholds"),
        "pattern": seed.get("pattern", "statement-truth set"),
        "question": question,
        "answer_format": "boxed_letters",
        "options": [
            f"{asset_label(symbol)} closes above {fmt_price(threshold)} at the March 2026 close"
            for threshold in thresholds
        ],
        "resolution_spec": {
            "source": "yfinance",
            "method": "close_threshold_truths",
            "symbol": symbol,
            "resolution_date": RESOLUTION_DATE,
            "thresholds": [
                {"label": LETTERS[idx], "operator": "gt", "value": threshold}
                for idx, threshold in enumerate(thresholds)
            ],
        },
    }


def build_hit_levels_case(seed: dict[str, Any], ref: dict[str, Any]) -> dict[str, Any]:
    symbol = seed["symbol"]
    close_value = float(ref[symbol]["close"])
    grid = asset_grid(symbol)
    highs = [round_to_grid(close_value + (grid * step), grid, mode="up") for step in (1, 2, 3)]
    lows = [round_to_grid(close_value - (grid * step), grid, mode="down") for step in (1, 2, 3)]
    title, question = render_seed_text(
        seed,
        label=asset_label(symbol),
        resolution_date=human_date(RESOLUTION_DATE),
    )
    return {
        "title": title,
        "category": seed.get("category", "hit_levels"),
        "pattern": seed.get("pattern", "threshold ladder"),
        "question": question,
        "answer_format": "boxed_letters",
        "options": [
            f"{asset_label(symbol)} hits {fmt_price(level)} on the high side before March 31, 2026" for level in highs
        ]
        + [
            f"{asset_label(symbol)} hits {fmt_price(level)} on the low side before March 31, 2026" for level in lows
        ],
        "resolution_spec": {
            "source": "yfinance",
            "method": "hit_levels",
            "symbol": symbol,
            "start_date": ref[symbol]["date"],
            "resolution_date": RESOLUTION_DATE,
            "levels": [
                {"label": LETTERS[idx], "direction": "high", "value": level}
                for idx, level in enumerate(highs)
            ]
            + [
                {"label": LETTERS[idx + len(highs)], "direction": "low", "value": level}
                for idx, level in enumerate(lows)
            ],
        },
    }


def build_binary_case(seed: dict[str, Any], ref: dict[str, Any]) -> dict[str, Any]:
    symbol = seed["symbol"]
    direction = seed["direction"]
    pct = seed["pct"]
    close_value = float(ref[symbol]["close"])
    grid = asset_grid(symbol)
    if direction == "gt":
        threshold = round_to_grid(close_value * (1 + pct), grid, mode="up")
    else:
        threshold = round_to_grid(close_value * (1 - pct), grid, mode="down")
    title, question = render_seed_text(
        seed,
        label=asset_label(symbol),
        threshold=fmt_price(threshold),
        resolution_date=human_date(RESOLUTION_DATE),
    )
    return {
        "title": title,
        "category": seed.get("category", "binary_price_event"),
        "pattern": seed.get("pattern", "binary"),
        "question": question,
        "answer_format": "boxed_yes_no",
        "options": None,
        "resolution_spec": {
            "source": "yfinance",
            "method": "binary_close_threshold",
            "symbol": symbol,
            "resolution_date": RESOLUTION_DATE,
            "operator": direction,
            "value": threshold,
        },
    }


def build_winner_case(seed: dict[str, Any], ref: dict[str, Any]) -> dict[str, Any]:
    symbols = seed["symbols"]
    snapshot_date = human_date(max(ref[symbol]["date"] for symbol in symbols))
    title, question = render_seed_text(
        seed,
        group_label=seed.get("group_label", "assets"),
        snapshot_date=snapshot_date,
        resolution_date=human_date(RESOLUTION_DATE),
    )
    return {
        "title": title,
        "category": seed.get("category", "winner_market"),
        "pattern": seed.get("pattern", "winner market"),
        "question": question,
        "answer_format": "boxed_letters",
        "options": [asset_label(symbol) for symbol in symbols],
        "resolution_spec": {
            "source": "yfinance",
            "method": "winner_by_return",
            "resolution_date": RESOLUTION_DATE,
            "symbols": {
                LETTERS[idx]: {
                    "symbol": symbol,
                    "reference_close": ref[symbol]["close"],
                    "reference_date": ref[symbol]["date"],
                }
                for idx, symbol in enumerate(symbols)
            },
        },
    }


def build_membership_case(seed: dict[str, Any], ref: dict[str, Any]) -> dict[str, Any]:
    symbols = seed["symbols"]
    snapshot_date = human_date(max(ref[symbol]["date"] for symbol in symbols))
    title, question = render_seed_text(
        seed,
        group_label=seed.get("group_label", "assets"),
        snapshot_date=snapshot_date,
        resolution_date=human_date(RESOLUTION_DATE),
    )
    return {
        "title": title,
        "category": seed.get("category", "up_membership"),
        "pattern": seed.get("pattern", "roster membership"),
        "question": question,
        "answer_format": "boxed_letters",
        "options": [asset_label(symbol) for symbol in symbols],
        "resolution_spec": {
            "source": "yfinance",
            "method": "membership_above_reference",
            "resolution_date": RESOLUTION_DATE,
            "symbols": {
                LETTERS[idx]: {
                    "symbol": symbol,
                    "reference_close": ref[symbol]["close"],
                    "reference_date": ref[symbol]["date"],
                }
                for idx, symbol in enumerate(symbols)
            },
        },
    }


def build_head_to_head_case(seed: dict[str, Any], ref: dict[str, Any]) -> dict[str, Any]:
    left = seed["symbols"][0]
    right = seed["symbols"][1]
    snapshot_date = human_date(max(ref[left]["date"], ref[right]["date"]))
    title, question = render_seed_text(
        seed,
        left_label=asset_label(left),
        right_label=asset_label(right),
        snapshot_date=snapshot_date,
        resolution_date=human_date(RESOLUTION_DATE),
    )
    return {
        "title": title,
        "category": seed.get("category", "head_to_head"),
        "pattern": seed.get("pattern", "winner market"),
        "question": question,
        "answer_format": "boxed_letters",
        "options": [asset_label(left), asset_label(right)],
        "resolution_spec": {
            "source": "yfinance",
            "method": "winner_by_return",
            "resolution_date": RESOLUTION_DATE,
            "symbols": {
                "A": {
                    "symbol": left,
                    "reference_close": ref[left]["close"],
                    "reference_date": ref[left]["date"],
                },
                "B": {
                    "symbol": right,
                    "reference_close": ref[right]["close"],
                    "reference_date": ref[right]["date"],
                },
            },
        },
    }


def build_custom_cases(snapshot: dict[str, Any]) -> list[dict[str, Any]]:
    ref = snapshot["symbols"]
    seeds = load_custom_case_seeds()

    custom_cases: list[dict[str, Any]] = []
    for seed in seeds:
        kind = seed["kind"]
        if kind == "close_bucket":
            custom_cases.append(build_bucket_case(seed, ref))
        elif kind == "close_threshold_truths":
            custom_cases.append(build_threshold_case(seed, ref))
        elif kind == "hit_levels":
            custom_cases.append(build_hit_levels_case(seed, ref))
        elif kind == "binary_close_threshold":
            custom_cases.append(build_binary_case(seed, ref))
        elif kind == "winner_by_return":
            if len(seed["symbols"]) == 2:
                custom_cases.append(build_head_to_head_case(seed, ref))
            else:
                custom_cases.append(build_winner_case(seed, ref))
        elif kind == "membership_above_reference":
            custom_cases.append(build_membership_case(seed, ref))
        else:
            raise ValueError(f"Unsupported custom seed kind: {kind}")

    expected_custom_count = TARGET_TOTAL_CASES - len(OFFICIAL_IDS)
    if len(custom_cases) != expected_custom_count:
        raise RuntimeError(
            f"Expected {expected_custom_count} custom cases, but built {len(custom_cases)}"
        )

    for case in custom_cases:
        if case["answer_format"] == "boxed_yes_no":
            case["prompt"] = build_yes_no_prompt(case["question"], end_time=RESOLUTION_DATE)
        else:
            case["prompt"] = build_letter_prompt(case["question"], case["options"], end_time=RESOLUTION_DATE)
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
            "- Each custom live question is authored in a separate LLM-written seed file, not generated from a repeated prompt template at build time.",
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
            "- `llm_custom_case_seeds.json`: individually written custom live question surfaces used by the builder.",
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
                    {"path": "llm_custom_case_seeds.json", "description": "LLM-authored custom live question seeds used to build the 93 non-official cases."},
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
