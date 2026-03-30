# v14 Track G True Live Cases

This markdown materializes the canonical true-live Track G pack.
Questions are visible, but ground truth is intentionally blank until
future third-party resolution arrives.

- Source mirror: `v13/questions.json`
- Case count: `100`

## v13_001 — S&P 500 Single-Day Gains and Losses (%) in Q1

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `futurex_online`
- End time: `2026-03-31`

Question:
```text
S&P 500 Single-Day Gains and Losses (%) in Q1
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "futurex_past_backfill",
  "dataset_name": "futurex-ai/Futurex-Past",
  "source_id": "69a2e39e5692ef005cdbf2d9",
  "expected_after": "2026-03-31",
  "title": "S&P 500 Single-Day Gains and Losses (%) in Q1"
}
```

## v13_002 — What will KOSPI (^KS11) hit in Q1 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `futurex_online`
- End time: `2026-03-31`

Question:
```text
What will KOSPI (^KS11) hit in Q1 2026?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "futurex_past_backfill",
  "dataset_name": "futurex-ai/Futurex-Past",
  "source_id": "69a2e39e5692ef005cdbf2e9",
  "expected_after": "2026-03-31",
  "title": "What will KOSPI (^KS11) hit in Q1 2026?"
}
```

## v13_003 — Q1 S&P 500 Performance

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `futurex_online`
- End time: `2026-03-31`

Question:
```text
Q1 S&P 500 Performance
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "futurex_past_backfill",
  "dataset_name": "futurex-ai/Futurex-Past",
  "source_id": "69a2e39e5692ef005cdbf2d8",
  "expected_after": "2026-03-31",
  "title": "Q1 S&P 500 Performance"
}
```

## v13_004 — Will KOSPI (KS11) close above __ end of Q1?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `futurex_online`
- End time: `2026-03-31`

Question:
```text
Will KOSPI (KS11) close above __ end of Q1?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "futurex_past_backfill",
  "dataset_name": "futurex-ai/Futurex-Past",
  "source_id": "69a2e39e5692ef005cdbf2e8",
  "expected_after": "2026-03-31",
  "title": "Will KOSPI (KS11) close above __ end of Q1?"
}
```

## v13_005 — What price will Bitcoin hit by March 2026? (add your prediction)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `futurex_online`
- End time: `2026-03-31`

Question:
```text
What price will Bitcoin hit by March 2026? (add your prediction)
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "futurex_past_backfill",
  "dataset_name": "futurex-ai/Futurex-Past",
  "source_id": "69a4319df2cb3b006875e9d0",
  "expected_after": "2026-03-31",
  "title": "What price will Bitcoin hit by March 2026? (add your prediction)"
}
```

## v13_006 — Banxico interest rate decision in March

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `futurex_online`
- End time: `2026-03-26`

Question:
```text
Banxico interest rate decision in March
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "futurex_past_backfill",
  "dataset_name": "futurex-ai/Futurex-Past",
  "source_id": "699c4887d1d3cf005c1e48ad",
  "expected_after": "2026-03-26",
  "title": "Banxico interest rate decision in March"
}
```

## v13_007 — Robinhood launches prediction market through MIAXdx by March 31?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `futurex_online`
- End time: `2026-03-31`

Question:
```text
Robinhood launches prediction market through MIAXdx by March 31?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "futurex_past_backfill",
  "dataset_name": "futurex-ai/Futurex-Past",
  "source_id": "69a2e39e5692ef005cdbf27c",
  "expected_after": "2026-03-31",
  "title": "Robinhood launches prediction market through MIAXdx by March 31?"
}
```

## v13_008 — What will Gold futures (GC) close at on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
What will Gold futures (GC) close at on March 31, 2026?
```

Options:
- `A`: Gold futures (GC) closes below $4,350
- `B`: Gold futures (GC) closes at least $4,350 but below $4,400
- `C`: Gold futures (GC) closes at least $4,400 but below $4,450
- `D`: Gold futures (GC) closes at least $4,450 but below $4,500
- `E`: Gold futures (GC) closes at least $4,500

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "GC=F",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 4350
    },
    {
      "label": "B",
      "type": "range",
      "lower": 4350,
      "upper": 4400
    },
    {
      "label": "C",
      "type": "range",
      "lower": 4400,
      "upper": 4450
    },
    {
      "label": "D",
      "type": "range",
      "lower": 4450,
      "upper": 4500
    },
    {
      "label": "E",
      "type": "ge",
      "value": 4500
    }
  ]
}
```

## v13_009 — Where will WTI crude oil futures (CL) settle on the final trading day of March 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Where will WTI crude oil futures (CL) settle on the final trading day of March 2026?
```

Options:
- `A`: WTI crude oil futures (CL) closes below $90
- `B`: WTI crude oil futures (CL) closes at least $90 but below $92
- `C`: WTI crude oil futures (CL) closes at least $92 but below $94
- `D`: WTI crude oil futures (CL) closes at least $94 but below $96
- `E`: WTI crude oil futures (CL) closes at least $96

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "CL=F",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 90
    },
    {
      "label": "B",
      "type": "range",
      "lower": 90,
      "upper": 92
    },
    {
      "label": "C",
      "type": "range",
      "lower": 92,
      "upper": 94
    },
    {
      "label": "D",
      "type": "range",
      "lower": 94,
      "upper": 96
    },
    {
      "label": "E",
      "type": "ge",
      "value": 96
    }
  ]
}
```

## v13_010 — What price range will Bitcoin (BTC-USD) close in on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
What price range will Bitcoin (BTC-USD) close in on March 31, 2026?
```

Options:
- `A`: Bitcoin (BTC-USD) closes below $64,000
- `B`: Bitcoin (BTC-USD) closes at least $64,000 but below $66,000
- `C`: Bitcoin (BTC-USD) closes at least $66,000 but below $68,000
- `D`: Bitcoin (BTC-USD) closes at least $68,000 but below $70,000
- `E`: Bitcoin (BTC-USD) closes at least $70,000

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "BTC-USD",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 64000
    },
    {
      "label": "B",
      "type": "range",
      "lower": 64000,
      "upper": 66000
    },
    {
      "label": "C",
      "type": "range",
      "lower": 66000,
      "upper": 68000
    },
    {
      "label": "D",
      "type": "range",
      "lower": 68000,
      "upper": 70000
    },
    {
      "label": "E",
      "type": "ge",
      "value": 70000
    }
  ]
}
```

## v13_011 — Where will Ethereum (ETH-USD) finish on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Where will Ethereum (ETH-USD) finish on March 31, 2026?
```

Options:
- `A`: Ethereum (ETH-USD) closes below $1,900
- `B`: Ethereum (ETH-USD) closes at least $1,900 but below $2,000
- `C`: Ethereum (ETH-USD) closes at least $2,000 but below $2,100
- `D`: Ethereum (ETH-USD) closes at least $2,100 but below $2,200
- `E`: Ethereum (ETH-USD) closes at least $2,200

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "ETH-USD",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 1900
    },
    {
      "label": "B",
      "type": "range",
      "lower": 1900,
      "upper": 2000
    },
    {
      "label": "C",
      "type": "range",
      "lower": 2000,
      "upper": 2100
    },
    {
      "label": "D",
      "type": "range",
      "lower": 2100,
      "upper": 2200
    },
    {
      "label": "E",
      "type": "ge",
      "value": 2200
    }
  ]
}
```

## v13_012 — What will NVIDIA (NVDA) close at by the end of March 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
What will NVIDIA (NVDA) close at by the end of March 2026?
```

Options:
- `A`: NVIDIA (NVDA) closes below $160
- `B`: NVIDIA (NVDA) closes at least $160 but below $165
- `C`: NVIDIA (NVDA) closes at least $165 but below $170
- `D`: NVIDIA (NVDA) closes at least $170 but below $175
- `E`: NVIDIA (NVDA) closes at least $175

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "NVDA",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 160
    },
    {
      "label": "B",
      "type": "range",
      "lower": 160,
      "upper": 165
    },
    {
      "label": "C",
      "type": "range",
      "lower": 165,
      "upper": 170
    },
    {
      "label": "D",
      "type": "range",
      "lower": 170,
      "upper": 175
    },
    {
      "label": "E",
      "type": "ge",
      "value": 175
    }
  ]
}
```

## v13_013 — Which range best describes the AMD (AMD) close on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which range best describes the AMD (AMD) close on March 31, 2026?
```

Options:
- `A`: AMD (AMD) closes below $195
- `B`: AMD (AMD) closes at least $195 but below $200
- `C`: AMD (AMD) closes at least $200 but below $205
- `D`: AMD (AMD) closes at least $205 but below $210
- `E`: AMD (AMD) closes at least $210

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "AMD",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 195
    },
    {
      "label": "B",
      "type": "range",
      "lower": 195,
      "upper": 200
    },
    {
      "label": "C",
      "type": "range",
      "lower": 200,
      "upper": 205
    },
    {
      "label": "D",
      "type": "range",
      "lower": 205,
      "upper": 210
    },
    {
      "label": "E",
      "type": "ge",
      "value": 210
    }
  ]
}
```

## v13_014 — What is the most likely closing range for Broadcom (AVGO) on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
What is the most likely closing range for Broadcom (AVGO) on March 31, 2026?
```

Options:
- `A`: Broadcom (AVGO) closes below $300
- `B`: Broadcom (AVGO) closes at least $300 but below $305
- `C`: Broadcom (AVGO) closes at least $305 but below $310
- `D`: Broadcom (AVGO) closes at least $310 but below $315
- `E`: Broadcom (AVGO) closes at least $315

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "AVGO",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 300
    },
    {
      "label": "B",
      "type": "range",
      "lower": 300,
      "upper": 305
    },
    {
      "label": "C",
      "type": "range",
      "lower": 305,
      "upper": 310
    },
    {
      "label": "D",
      "type": "range",
      "lower": 310,
      "upper": 315
    },
    {
      "label": "E",
      "type": "ge",
      "value": 315
    }
  ]
}
```

## v13_015 — Where does Taiwan Semiconductor (TSM) end up at the March 31, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Where does Taiwan Semiconductor (TSM) end up at the March 31, 2026 close?
```

Options:
- `A`: Taiwan Semiconductor (TSM) closes below $315
- `B`: Taiwan Semiconductor (TSM) closes at least $315 but below $320
- `C`: Taiwan Semiconductor (TSM) closes at least $320 but below $325
- `D`: Taiwan Semiconductor (TSM) closes at least $325 but below $330
- `E`: Taiwan Semiconductor (TSM) closes at least $330

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "TSM",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 315
    },
    {
      "label": "B",
      "type": "range",
      "lower": 315,
      "upper": 320
    },
    {
      "label": "C",
      "type": "range",
      "lower": 320,
      "upper": 325
    },
    {
      "label": "D",
      "type": "range",
      "lower": 325,
      "upper": 330
    },
    {
      "label": "E",
      "type": "ge",
      "value": 330
    }
  ]
}
```

## v13_016 — What will the closing price of Tesla (TSLA) be on the final trading day of March 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
What will the closing price of Tesla (TSLA) be on the final trading day of March 2026?
```

Options:
- `A`: Tesla (TSLA) closes below $350
- `B`: Tesla (TSLA) closes at least $350 but below $360
- `C`: Tesla (TSLA) closes at least $360 but below $370
- `D`: Tesla (TSLA) closes at least $370 but below $380
- `E`: Tesla (TSLA) closes at least $380

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "TSLA",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 350
    },
    {
      "label": "B",
      "type": "range",
      "lower": 350,
      "upper": 360
    },
    {
      "label": "C",
      "type": "range",
      "lower": 360,
      "upper": 370
    },
    {
      "label": "D",
      "type": "range",
      "lower": 370,
      "upper": 380
    },
    {
      "label": "E",
      "type": "ge",
      "value": 380
    }
  ]
}
```

## v13_017 — Where will Apple (AAPL) close at month-end on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Where will Apple (AAPL) close at month-end on March 31, 2026?
```

Options:
- `A`: Apple (AAPL) closes below $245
- `B`: Apple (AAPL) closes at least $245 but below $250
- `C`: Apple (AAPL) closes at least $250 but below $255
- `D`: Apple (AAPL) closes at least $255 but below $260
- `E`: Apple (AAPL) closes at least $260

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "AAPL",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 245
    },
    {
      "label": "B",
      "type": "range",
      "lower": 245,
      "upper": 250
    },
    {
      "label": "C",
      "type": "range",
      "lower": 250,
      "upper": 255
    },
    {
      "label": "D",
      "type": "range",
      "lower": 255,
      "upper": 260
    },
    {
      "label": "E",
      "type": "ge",
      "value": 260
    }
  ]
}
```

## v13_018 — Which closing bucket fits Microsoft (MSFT) on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which closing bucket fits Microsoft (MSFT) on March 31, 2026?
```

Options:
- `A`: Microsoft (MSFT) closes below $355
- `B`: Microsoft (MSFT) closes at least $355 but below $360
- `C`: Microsoft (MSFT) closes at least $360 but below $365
- `D`: Microsoft (MSFT) closes at least $365 but below $370
- `E`: Microsoft (MSFT) closes at least $370

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "MSFT",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 355
    },
    {
      "label": "B",
      "type": "range",
      "lower": 355,
      "upper": 360
    },
    {
      "label": "C",
      "type": "range",
      "lower": 360,
      "upper": 365
    },
    {
      "label": "D",
      "type": "range",
      "lower": 365,
      "upper": 370
    },
    {
      "label": "E",
      "type": "ge",
      "value": 370
    }
  ]
}
```

## v13_019 — What closing range does Amazon (AMZN) land in on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
What closing range does Amazon (AMZN) land in on March 31, 2026?
```

Options:
- `A`: Amazon (AMZN) closes below $200
- `B`: Amazon (AMZN) closes at least $200 but below $205
- `C`: Amazon (AMZN) closes at least $205 but below $210
- `D`: Amazon (AMZN) closes at least $210 but below $215
- `E`: Amazon (AMZN) closes at least $215

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "AMZN",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 200
    },
    {
      "label": "B",
      "type": "range",
      "lower": 200,
      "upper": 205
    },
    {
      "label": "C",
      "type": "range",
      "lower": 205,
      "upper": 210
    },
    {
      "label": "D",
      "type": "range",
      "lower": 210,
      "upper": 215
    },
    {
      "label": "E",
      "type": "ge",
      "value": 215
    }
  ]
}
```

## v13_020 — Where will Meta (META) finish at the March 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Where will Meta (META) finish at the March 2026 close?
```

Options:
- `A`: Meta (META) closes below $530
- `B`: Meta (META) closes at least $530 but below $540
- `C`: Meta (META) closes at least $540 but below $550
- `D`: Meta (META) closes at least $550 but below $560
- `E`: Meta (META) closes at least $560

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "META",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 530
    },
    {
      "label": "B",
      "type": "range",
      "lower": 530,
      "upper": 540
    },
    {
      "label": "C",
      "type": "range",
      "lower": 540,
      "upper": 550
    },
    {
      "label": "D",
      "type": "range",
      "lower": 550,
      "upper": 560
    },
    {
      "label": "E",
      "type": "ge",
      "value": 560
    }
  ]
}
```

## v13_021 — What will Invesco QQQ Trust (QQQ) close at on the last trading day of March 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
What will Invesco QQQ Trust (QQQ) close at on the last trading day of March 2026?
```

Options:
- `A`: Invesco QQQ Trust (QQQ) closes below $565
- `B`: Invesco QQQ Trust (QQQ) closes at least $565 but below $570
- `C`: Invesco QQQ Trust (QQQ) closes at least $570 but below $575
- `D`: Invesco QQQ Trust (QQQ) closes at least $575 but below $580
- `E`: Invesco QQQ Trust (QQQ) closes at least $580

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "QQQ",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 565
    },
    {
      "label": "B",
      "type": "range",
      "lower": 565,
      "upper": 570
    },
    {
      "label": "C",
      "type": "range",
      "lower": 570,
      "upper": 575
    },
    {
      "label": "D",
      "type": "range",
      "lower": 575,
      "upper": 580
    },
    {
      "label": "E",
      "type": "ge",
      "value": 580
    }
  ]
}
```

## v13_022 — Which bucket contains the SPDR S&P 500 ETF (SPY) close on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which bucket contains the SPDR S&P 500 ETF (SPY) close on March 31, 2026?
```

Options:
- `A`: SPDR S&P 500 ETF (SPY) closes below $635
- `B`: SPDR S&P 500 ETF (SPY) closes at least $635 but below $640
- `C`: SPDR S&P 500 ETF (SPY) closes at least $640 but below $645
- `D`: SPDR S&P 500 ETF (SPY) closes at least $645 but below $650
- `E`: SPDR S&P 500 ETF (SPY) closes at least $650

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_bucket",
  "symbol": "SPY",
  "resolution_date": "2026-03-31",
  "buckets": [
    {
      "label": "A",
      "type": "lt",
      "value": 635
    },
    {
      "label": "B",
      "type": "range",
      "lower": 635,
      "upper": 640
    },
    {
      "label": "C",
      "type": "range",
      "lower": 640,
      "upper": 645
    },
    {
      "label": "D",
      "type": "range",
      "lower": 645,
      "upper": 650
    },
    {
      "label": "E",
      "type": "ge",
      "value": 650
    }
  ]
}
```

## v13_023 — Which of these statements about the Bitcoin (BTC-USD) close on March 31, 2026 will be true?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these statements about the Bitcoin (BTC-USD) close on March 31, 2026 will be true?
```

Options:
- `A`: Bitcoin (BTC-USD) closes above $64,000 at the March 2026 close
- `B`: Bitcoin (BTC-USD) closes above $66,000 at the March 2026 close
- `C`: Bitcoin (BTC-USD) closes above $68,000 at the March 2026 close
- `D`: Bitcoin (BTC-USD) closes above $70,000 at the March 2026 close
- `E`: Bitcoin (BTC-USD) closes above $72,000 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "BTC-USD",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 64000
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 66000
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 68000
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 70000
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 72000
    }
  ]
}
```

## v13_024 — Which of these Ethereum (ETH-USD) close-above statements still hold at the end of March 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these Ethereum (ETH-USD) close-above statements still hold at the end of March 2026?
```

Options:
- `A`: Ethereum (ETH-USD) closes above $1,900 at the March 2026 close
- `B`: Ethereum (ETH-USD) closes above $2,000 at the March 2026 close
- `C`: Ethereum (ETH-USD) closes above $2,100 at the March 2026 close
- `D`: Ethereum (ETH-USD) closes above $2,200 at the March 2026 close
- `E`: Ethereum (ETH-USD) closes above $2,300 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "ETH-USD",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 1900
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 2000
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 2100
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 2200
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 2300
    }
  ]
}
```

## v13_025 — Which of these claims about NVIDIA (NVDA) on the March 31, 2026 close will be true?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these claims about NVIDIA (NVDA) on the March 31, 2026 close will be true?
```

Options:
- `A`: NVIDIA (NVDA) closes above $160 at the March 2026 close
- `B`: NVIDIA (NVDA) closes above $165 at the March 2026 close
- `C`: NVIDIA (NVDA) closes above $170 at the March 2026 close
- `D`: NVIDIA (NVDA) closes above $175 at the March 2026 close
- `E`: NVIDIA (NVDA) closes above $180 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "NVDA",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 160
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 165
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 170
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 175
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 180
    }
  ]
}
```

## v13_026 — Which of these higher-close outcomes for AMD (AMD) will be true on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these higher-close outcomes for AMD (AMD) will be true on March 31, 2026?
```

Options:
- `A`: AMD (AMD) closes above $195 at the March 2026 close
- `B`: AMD (AMD) closes above $200 at the March 2026 close
- `C`: AMD (AMD) closes above $205 at the March 2026 close
- `D`: AMD (AMD) closes above $210 at the March 2026 close
- `E`: AMD (AMD) closes above $215 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "AMD",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 195
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 200
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 205
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 210
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 215
    }
  ]
}
```

## v13_027 — Which of these Tesla (TSLA) closing thresholds are still met at the March 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these Tesla (TSLA) closing thresholds are still met at the March 2026 close?
```

Options:
- `A`: Tesla (TSLA) closes above $350 at the March 2026 close
- `B`: Tesla (TSLA) closes above $360 at the March 2026 close
- `C`: Tesla (TSLA) closes above $370 at the March 2026 close
- `D`: Tesla (TSLA) closes above $380 at the March 2026 close
- `E`: Tesla (TSLA) closes above $390 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "TSLA",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 350
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 360
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 370
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 380
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 390
    }
  ]
}
```

## v13_028 — Which of these statements about Apple (AAPL) finishing above a level on March 31, 2026 will be true?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these statements about Apple (AAPL) finishing above a level on March 31, 2026 will be true?
```

Options:
- `A`: Apple (AAPL) closes above $245 at the March 2026 close
- `B`: Apple (AAPL) closes above $250 at the March 2026 close
- `C`: Apple (AAPL) closes above $255 at the March 2026 close
- `D`: Apple (AAPL) closes above $260 at the March 2026 close
- `E`: Apple (AAPL) closes above $265 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "AAPL",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 245
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 250
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 255
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 260
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 265
    }
  ]
}
```

## v13_029 — Which of these Microsoft (MSFT) close-above levels remain true at month-end?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these Microsoft (MSFT) close-above levels remain true at month-end?
```

Options:
- `A`: Microsoft (MSFT) closes above $355 at the March 2026 close
- `B`: Microsoft (MSFT) closes above $360 at the March 2026 close
- `C`: Microsoft (MSFT) closes above $365 at the March 2026 close
- `D`: Microsoft (MSFT) closes above $370 at the March 2026 close
- `E`: Microsoft (MSFT) closes above $375 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "MSFT",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 355
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 360
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 365
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 370
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 375
    }
  ]
}
```

## v13_030 — Which of these outcomes for the Amazon (AMZN) close on March 31, 2026 will be true?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these outcomes for the Amazon (AMZN) close on March 31, 2026 will be true?
```

Options:
- `A`: Amazon (AMZN) closes above $200 at the March 2026 close
- `B`: Amazon (AMZN) closes above $205 at the March 2026 close
- `C`: Amazon (AMZN) closes above $210 at the March 2026 close
- `D`: Amazon (AMZN) closes above $215 at the March 2026 close
- `E`: Amazon (AMZN) closes above $220 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "AMZN",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 200
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 205
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 210
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 215
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 220
    }
  ]
}
```

## v13_031 — Which of these stronger month-end close statements about Meta (META) will be true?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these stronger month-end close statements about Meta (META) will be true?
```

Options:
- `A`: Meta (META) closes above $530 at the March 2026 close
- `B`: Meta (META) closes above $540 at the March 2026 close
- `C`: Meta (META) closes above $550 at the March 2026 close
- `D`: Meta (META) closes above $560 at the March 2026 close
- `E`: Meta (META) closes above $570 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "META",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 530
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 540
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 550
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 560
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 570
    }
  ]
}
```

## v13_032 — Which of these Invesco QQQ Trust (QQQ) statements survive the March 31, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these Invesco QQQ Trust (QQQ) statements survive the March 31, 2026 close?
```

Options:
- `A`: Invesco QQQ Trust (QQQ) closes above $565 at the March 2026 close
- `B`: Invesco QQQ Trust (QQQ) closes above $570 at the March 2026 close
- `C`: Invesco QQQ Trust (QQQ) closes above $575 at the March 2026 close
- `D`: Invesco QQQ Trust (QQQ) closes above $580 at the March 2026 close
- `E`: Invesco QQQ Trust (QQQ) closes above $585 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "QQQ",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 565
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 570
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 575
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 580
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 585
    }
  ]
}
```

## v13_033 — Which of these close-above outcomes for iShares Semiconductor ETF (SOXX) will still be true on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these close-above outcomes for iShares Semiconductor ETF (SOXX) will still be true on March 31, 2026?
```

Options:
- `A`: iShares Semiconductor ETF (SOXX) closes above $320 at the March 2026 close
- `B`: iShares Semiconductor ETF (SOXX) closes above $325 at the March 2026 close
- `C`: iShares Semiconductor ETF (SOXX) closes above $330 at the March 2026 close
- `D`: iShares Semiconductor ETF (SOXX) closes above $335 at the March 2026 close
- `E`: iShares Semiconductor ETF (SOXX) closes above $340 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "SOXX",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 320
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 325
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 330
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 335
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 340
    }
  ]
}
```

## v13_034 — Which of these statements about SPDR Gold Shares (GLD) at the March 2026 close end up being true?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these statements about SPDR Gold Shares (GLD) at the March 2026 close end up being true?
```

Options:
- `A`: SPDR Gold Shares (GLD) closes above $390 at the March 2026 close
- `B`: SPDR Gold Shares (GLD) closes above $395 at the March 2026 close
- `C`: SPDR Gold Shares (GLD) closes above $400 at the March 2026 close
- `D`: SPDR Gold Shares (GLD) closes above $405 at the March 2026 close
- `E`: SPDR Gold Shares (GLD) closes above $410 at the March 2026 close

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "close_threshold_truths",
  "symbol": "GLD",
  "resolution_date": "2026-03-31",
  "thresholds": [
    {
      "label": "A",
      "operator": "gt",
      "value": 390
    },
    {
      "label": "B",
      "operator": "gt",
      "value": 395
    },
    {
      "label": "C",
      "operator": "gt",
      "value": 400
    },
    {
      "label": "D",
      "operator": "gt",
      "value": 405
    },
    {
      "label": "E",
      "operator": "gt",
      "value": 410
    }
  ]
}
```

## v13_035 — Which of these WTI crude oil futures (CL) levels will trade before market close on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these WTI crude oil futures (CL) levels will trade before market close on March 31, 2026?
```

Options:
- `A`: WTI crude oil futures (CL) hits $96 on the high side before March 31, 2026
- `B`: WTI crude oil futures (CL) hits $98 on the high side before March 31, 2026
- `C`: WTI crude oil futures (CL) hits $100 on the high side before March 31, 2026
- `D`: WTI crude oil futures (CL) hits $90 on the low side before March 31, 2026
- `E`: WTI crude oil futures (CL) hits $88 on the low side before March 31, 2026
- `F`: WTI crude oil futures (CL) hits $86 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "CL=F",
  "start_date": "2026-03-27",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 96
    },
    {
      "label": "B",
      "direction": "high",
      "value": 98
    },
    {
      "label": "C",
      "direction": "high",
      "value": 100
    },
    {
      "label": "D",
      "direction": "low",
      "value": 90
    },
    {
      "label": "E",
      "direction": "low",
      "value": 88
    },
    {
      "label": "F",
      "direction": "low",
      "value": 86
    }
  ]
}
```

## v13_036 — Which of these price levels will Gold futures (GC) hit before March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these price levels will Gold futures (GC) hit before March 31, 2026?
```

Options:
- `A`: Gold futures (GC) hits $4,500 on the high side before March 31, 2026
- `B`: Gold futures (GC) hits $4,550 on the high side before March 31, 2026
- `C`: Gold futures (GC) hits $4,600 on the high side before March 31, 2026
- `D`: Gold futures (GC) hits $4,350 on the low side before March 31, 2026
- `E`: Gold futures (GC) hits $4,300 on the low side before March 31, 2026
- `F`: Gold futures (GC) hits $4,250 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "GC=F",
  "start_date": "2026-03-27",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 4500
    },
    {
      "label": "B",
      "direction": "high",
      "value": 4550
    },
    {
      "label": "C",
      "direction": "high",
      "value": 4600
    },
    {
      "label": "D",
      "direction": "low",
      "value": 4350
    },
    {
      "label": "E",
      "direction": "low",
      "value": 4300
    },
    {
      "label": "F",
      "direction": "low",
      "value": 4250
    }
  ]
}
```

## v13_037 — Before trading ends on March 31, 2026, which of these levels will Bitcoin (BTC-USD) trade at?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Before trading ends on March 31, 2026, which of these levels will Bitcoin (BTC-USD) trade at?
```

Options:
- `A`: Bitcoin (BTC-USD) hits $72,000 on the high side before March 31, 2026
- `B`: Bitcoin (BTC-USD) hits $74,000 on the high side before March 31, 2026
- `C`: Bitcoin (BTC-USD) hits $76,000 on the high side before March 31, 2026
- `D`: Bitcoin (BTC-USD) hits $66,000 on the low side before March 31, 2026
- `E`: Bitcoin (BTC-USD) hits $64,000 on the low side before March 31, 2026
- `F`: Bitcoin (BTC-USD) hits $62,000 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "BTC-USD",
  "start_date": "2026-03-27",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 72000
    },
    {
      "label": "B",
      "direction": "high",
      "value": 74000
    },
    {
      "label": "C",
      "direction": "high",
      "value": 76000
    },
    {
      "label": "D",
      "direction": "low",
      "value": 66000
    },
    {
      "label": "E",
      "direction": "low",
      "value": 64000
    },
    {
      "label": "F",
      "direction": "low",
      "value": 62000
    }
  ]
}
```

## v13_038 — Which of these Ethereum (ETH-USD) levels get touched before the March 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these Ethereum (ETH-USD) levels get touched before the March 2026 close?
```

Options:
- `A`: Ethereum (ETH-USD) hits $2,200 on the high side before March 31, 2026
- `B`: Ethereum (ETH-USD) hits $2,300 on the high side before March 31, 2026
- `C`: Ethereum (ETH-USD) hits $2,400 on the high side before March 31, 2026
- `D`: Ethereum (ETH-USD) hits $1,900 on the low side before March 31, 2026
- `E`: Ethereum (ETH-USD) hits $1,800 on the low side before March 31, 2026
- `F`: Ethereum (ETH-USD) hits $1,700 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "ETH-USD",
  "start_date": "2026-03-27",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 2200
    },
    {
      "label": "B",
      "direction": "high",
      "value": 2300
    },
    {
      "label": "C",
      "direction": "high",
      "value": 2400
    },
    {
      "label": "D",
      "direction": "low",
      "value": 1900
    },
    {
      "label": "E",
      "direction": "low",
      "value": 1800
    },
    {
      "label": "F",
      "direction": "low",
      "value": 1700
    }
  ]
}
```

## v13_039 — Which of these price marks will NVIDIA (NVDA) reach before March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these price marks will NVIDIA (NVDA) reach before March 31, 2026?
```

Options:
- `A`: NVIDIA (NVDA) hits $180 on the high side before March 31, 2026
- `B`: NVIDIA (NVDA) hits $185 on the high side before March 31, 2026
- `C`: NVIDIA (NVDA) hits $190 on the high side before March 31, 2026
- `D`: NVIDIA (NVDA) hits $165 on the low side before March 31, 2026
- `E`: NVIDIA (NVDA) hits $160 on the low side before March 31, 2026
- `F`: NVIDIA (NVDA) hits $155 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "NVDA",
  "start_date": "2026-03-26",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 180
    },
    {
      "label": "B",
      "direction": "high",
      "value": 185
    },
    {
      "label": "C",
      "direction": "high",
      "value": 190
    },
    {
      "label": "D",
      "direction": "low",
      "value": 165
    },
    {
      "label": "E",
      "direction": "low",
      "value": 160
    },
    {
      "label": "F",
      "direction": "low",
      "value": 155
    }
  ]
}
```

## v13_040 — Which of these AMD (AMD) levels trade at any point before market close on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these AMD (AMD) levels trade at any point before market close on March 31, 2026?
```

Options:
- `A`: AMD (AMD) hits $210 on the high side before March 31, 2026
- `B`: AMD (AMD) hits $215 on the high side before March 31, 2026
- `C`: AMD (AMD) hits $220 on the high side before March 31, 2026
- `D`: AMD (AMD) hits $195 on the low side before March 31, 2026
- `E`: AMD (AMD) hits $190 on the low side before March 31, 2026
- `F`: AMD (AMD) hits $185 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "AMD",
  "start_date": "2026-03-26",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 210
    },
    {
      "label": "B",
      "direction": "high",
      "value": 215
    },
    {
      "label": "C",
      "direction": "high",
      "value": 220
    },
    {
      "label": "D",
      "direction": "low",
      "value": 195
    },
    {
      "label": "E",
      "direction": "low",
      "value": 190
    },
    {
      "label": "F",
      "direction": "low",
      "value": 185
    }
  ]
}
```

## v13_041 — Which of these levels does Tesla (TSLA) print before the end of March 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these levels does Tesla (TSLA) print before the end of March 2026?
```

Options:
- `A`: Tesla (TSLA) hits $390 on the high side before March 31, 2026
- `B`: Tesla (TSLA) hits $400 on the high side before March 31, 2026
- `C`: Tesla (TSLA) hits $410 on the high side before March 31, 2026
- `D`: Tesla (TSLA) hits $360 on the low side before March 31, 2026
- `E`: Tesla (TSLA) hits $350 on the low side before March 31, 2026
- `F`: Tesla (TSLA) hits $340 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "TSLA",
  "start_date": "2026-03-26",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 390
    },
    {
      "label": "B",
      "direction": "high",
      "value": 400
    },
    {
      "label": "C",
      "direction": "high",
      "value": 410
    },
    {
      "label": "D",
      "direction": "low",
      "value": 360
    },
    {
      "label": "E",
      "direction": "low",
      "value": 350
    },
    {
      "label": "F",
      "direction": "low",
      "value": 340
    }
  ]
}
```

## v13_042 — Which of these Invesco QQQ Trust (QQQ) prices are traded before March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these Invesco QQQ Trust (QQQ) prices are traded before March 31, 2026?
```

Options:
- `A`: Invesco QQQ Trust (QQQ) hits $580 on the high side before March 31, 2026
- `B`: Invesco QQQ Trust (QQQ) hits $585 on the high side before March 31, 2026
- `C`: Invesco QQQ Trust (QQQ) hits $590 on the high side before March 31, 2026
- `D`: Invesco QQQ Trust (QQQ) hits $565 on the low side before March 31, 2026
- `E`: Invesco QQQ Trust (QQQ) hits $560 on the low side before March 31, 2026
- `F`: Invesco QQQ Trust (QQQ) hits $555 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "QQQ",
  "start_date": "2026-03-26",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 580
    },
    {
      "label": "B",
      "direction": "high",
      "value": 585
    },
    {
      "label": "C",
      "direction": "high",
      "value": 590
    },
    {
      "label": "D",
      "direction": "low",
      "value": 565
    },
    {
      "label": "E",
      "direction": "low",
      "value": 560
    },
    {
      "label": "F",
      "direction": "low",
      "value": 555
    }
  ]
}
```

## v13_043 — Which of these levels will SPDR S&P 500 ETF (SPY) see before the month closes on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these levels will SPDR S&P 500 ETF (SPY) see before the month closes on March 31, 2026?
```

Options:
- `A`: SPDR S&P 500 ETF (SPY) hits $655 on the high side before March 31, 2026
- `B`: SPDR S&P 500 ETF (SPY) hits $660 on the high side before March 31, 2026
- `C`: SPDR S&P 500 ETF (SPY) hits $665 on the high side before March 31, 2026
- `D`: SPDR S&P 500 ETF (SPY) hits $640 on the low side before March 31, 2026
- `E`: SPDR S&P 500 ETF (SPY) hits $635 on the low side before March 31, 2026
- `F`: SPDR S&P 500 ETF (SPY) hits $630 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "SPY",
  "start_date": "2026-03-26",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 655
    },
    {
      "label": "B",
      "direction": "high",
      "value": 660
    },
    {
      "label": "C",
      "direction": "high",
      "value": 665
    },
    {
      "label": "D",
      "direction": "low",
      "value": 640
    },
    {
      "label": "E",
      "direction": "low",
      "value": 635
    },
    {
      "label": "F",
      "direction": "low",
      "value": 630
    }
  ]
}
```

## v13_044 — Which of these iShares Semiconductor ETF (SOXX) levels are reached before the final March close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these iShares Semiconductor ETF (SOXX) levels are reached before the final March close?
```

Options:
- `A`: iShares Semiconductor ETF (SOXX) hits $335 on the high side before March 31, 2026
- `B`: iShares Semiconductor ETF (SOXX) hits $340 on the high side before March 31, 2026
- `C`: iShares Semiconductor ETF (SOXX) hits $345 on the high side before March 31, 2026
- `D`: iShares Semiconductor ETF (SOXX) hits $320 on the low side before March 31, 2026
- `E`: iShares Semiconductor ETF (SOXX) hits $315 on the low side before March 31, 2026
- `F`: iShares Semiconductor ETF (SOXX) hits $310 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "SOXX",
  "start_date": "2026-03-26",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 335
    },
    {
      "label": "B",
      "direction": "high",
      "value": 340
    },
    {
      "label": "C",
      "direction": "high",
      "value": 345
    },
    {
      "label": "D",
      "direction": "low",
      "value": 320
    },
    {
      "label": "E",
      "direction": "low",
      "value": 315
    },
    {
      "label": "F",
      "direction": "low",
      "value": 310
    }
  ]
}
```

## v13_045 — Which of these prices does Coinbase (COIN) trade before March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these prices does Coinbase (COIN) trade before March 31, 2026?
```

Options:
- `A`: Coinbase (COIN) hits $180 on the high side before March 31, 2026
- `B`: Coinbase (COIN) hits $185 on the high side before March 31, 2026
- `C`: Coinbase (COIN) hits $190 on the high side before March 31, 2026
- `D`: Coinbase (COIN) hits $165 on the low side before March 31, 2026
- `E`: Coinbase (COIN) hits $160 on the low side before March 31, 2026
- `F`: Coinbase (COIN) hits $155 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "COIN",
  "start_date": "2026-03-26",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 180
    },
    {
      "label": "B",
      "direction": "high",
      "value": 185
    },
    {
      "label": "C",
      "direction": "high",
      "value": 190
    },
    {
      "label": "D",
      "direction": "low",
      "value": 165
    },
    {
      "label": "E",
      "direction": "low",
      "value": 160
    },
    {
      "label": "F",
      "direction": "low",
      "value": 155
    }
  ]
}
```

## v13_046 — Which of these Strategy (MSTR) levels come into play before March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these Strategy (MSTR) levels come into play before March 31, 2026?
```

Options:
- `A`: Strategy (MSTR) hits $160 on the high side before March 31, 2026
- `B`: Strategy (MSTR) hits $180 on the high side before March 31, 2026
- `C`: Strategy (MSTR) hits $200 on the high side before March 31, 2026
- `D`: Strategy (MSTR) hits $100 on the low side before March 31, 2026
- `E`: Strategy (MSTR) hits $80 on the low side before March 31, 2026
- `F`: Strategy (MSTR) hits $60 on the low side before March 31, 2026

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "hit_levels",
  "symbol": "MSTR",
  "start_date": "2026-03-26",
  "resolution_date": "2026-03-31",
  "levels": [
    {
      "label": "A",
      "direction": "high",
      "value": 160
    },
    {
      "label": "B",
      "direction": "high",
      "value": 180
    },
    {
      "label": "C",
      "direction": "high",
      "value": 200
    },
    {
      "label": "D",
      "direction": "low",
      "value": 100
    },
    {
      "label": "E",
      "direction": "low",
      "value": 80
    },
    {
      "label": "F",
      "direction": "low",
      "value": 60
    }
  ]
}
```

## v13_047 — Will NVIDIA (NVDA) close above $180 on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will NVIDIA (NVDA) close above $180 on March 31, 2026?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "NVDA",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 180
}
```

## v13_048 — Will AMD (AMD) finish above $215 at the March 31, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will AMD (AMD) finish above $215 at the March 31, 2026 close?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "AMD",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 215
}
```

## v13_049 — Will Broadcom (AVGO) end March 2026 with a close above $320?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Broadcom (AVGO) end March 2026 with a close above $320?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "AVGO",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 320
}
```

## v13_050 — Will Taiwan Semiconductor (TSM) close through $340 on the final trading day of March 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Taiwan Semiconductor (TSM) close through $340 on the final trading day of March 2026?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "TSM",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 340
}
```

## v13_051 — Will the March 31, 2026 close for Tesla (TSLA) be above $400?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will the March 31, 2026 close for Tesla (TSLA) be above $400?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "TSLA",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 400
}
```

## v13_052 — Will Apple (AAPL) finish the month above $260 on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Apple (AAPL) finish the month above $260 on March 31, 2026?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "AAPL",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 260
}
```

## v13_053 — Will Microsoft (MSFT) close higher than $375 on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Microsoft (MSFT) close higher than $375 on March 31, 2026?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "MSFT",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 375
}
```

## v13_054 — Will Amazon (AMZN) end the March 2026 close above $215?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Amazon (AMZN) end the March 2026 close above $215?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "AMZN",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 215
}
```

## v13_055 — Will Meta (META) settle above $570 on the final trading day of March 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Meta (META) settle above $570 on the final trading day of March 2026?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "META",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 570
}
```

## v13_056 — Will Invesco QQQ Trust (QQQ) close above $590 by month-end on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Invesco QQQ Trust (QQQ) close above $590 by month-end on March 31, 2026?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "QQQ",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 590
}
```

## v13_057 — Will SPDR S&P 500 ETF (SPY) end March 2026 above $655 at the close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will SPDR S&P 500 ETF (SPY) end March 2026 above $655 at the close?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "SPY",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 655
}
```

## v13_058 — Will the final March close for iShares Russell 2000 ETF (IWM) clear $255?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will the final March close for iShares Russell 2000 ETF (IWM) clear $255?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "IWM",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 255
}
```

## v13_059 — Will Bitcoin (BTC-USD) close above $72,000 on the last trading day of March 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Bitcoin (BTC-USD) close above $72,000 on the last trading day of March 2026?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "BTC-USD",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 72000
}
```

## v13_060 — Will Ethereum (ETH-USD) finish above $2,200 by the March 31, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Ethereum (ETH-USD) finish above $2,200 by the March 31, 2026 close?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "ETH-USD",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 2200
}
```

## v13_061 — Will Coinbase (COIN) close north of $185 on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Coinbase (COIN) close north of $185 on March 31, 2026?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "COIN",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 185
}
```

## v13_062 — Will Strategy (MSTR) end March above $160 at the closing bell?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Strategy (MSTR) end March above $160 at the closing bell?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "MSTR",
  "resolution_date": "2026-03-31",
  "operator": "gt",
  "value": 160
}
```

## v13_063 — Will Energy Select Sector SPDR Fund (XLE) close below $58 on March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Energy Select Sector SPDR Fund (XLE) close below $58 on March 31, 2026?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "XLE",
  "resolution_date": "2026-03-31",
  "operator": "lt",
  "value": 58
}
```

## v13_064 — Will Financial Select Sector SPDR Fund (XLF) finish March 2026 with a close below $48?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Will Financial Select Sector SPDR Fund (XLF) finish March 2026 with a close below $48?
```

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "binary_close_threshold",
  "symbol": "XLF",
  "resolution_date": "2026-03-31",
  "operator": "lt",
  "value": 48
}
```

## v13_065 — Which of these semiconductor names posts the best return from the March 26, 2026 close through the March 31, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these semiconductor names posts the best return from the March 26, 2026 close through the March 31, 2026 close?
```

Options:
- `A`: NVIDIA (NVDA)
- `B`: AMD (AMD)
- `C`: Broadcom (AVGO)
- `D`: Taiwan Semiconductor (TSM)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "NVDA",
      "reference_close": 171.24,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "AMD",
      "reference_close": 203.77,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "AVGO",
      "reference_close": 309.415,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "TSM",
      "reference_close": 326.11,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_066 — From the March 26, 2026 close to the March 31, 2026 close, which of these megacap tech names performs best?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
From the March 26, 2026 close to the March 31, 2026 close, which of these megacap tech names performs best?
```

Options:
- `A`: Apple (AAPL)
- `B`: Microsoft (MSFT)
- `C`: Amazon (AMZN)
- `D`: Meta (META)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "AAPL",
      "reference_close": 252.89,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "MSFT",
      "reference_close": 365.97,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "AMZN",
      "reference_close": 207.54,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "META",
      "reference_close": 547.54,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_067 — Which name in this market beta ETFs group has the strongest return from March 26, 2026 through March 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which name in this market beta ETFs group has the strongest return from March 26, 2026 through March 31, 2026?
```

Options:
- `A`: SPDR S&P 500 ETF (SPY)
- `B`: Invesco QQQ Trust (QQQ)
- `C`: iShares Russell 2000 ETF (IWM)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "SPY",
      "reference_close": 645.09,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "QQQ",
      "reference_close": 573.79,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "IWM",
      "reference_close": 247.44,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_068 — Across these crypto assets and proxies, which delivers the best performance from the March 27, 2026 close to the March 31, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Across these crypto assets and proxies, which delivers the best performance from the March 27, 2026 close to the March 31, 2026 close?
```

Options:
- `A`: Bitcoin (BTC-USD)
- `B`: Ethereum (ETH-USD)
- `C`: Coinbase (COIN)
- `D`: Strategy (MSTR)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "BTC-USD",
      "reference_close": 68817.0391,
      "reference_date": "2026-03-27"
    },
    "B": {
      "symbol": "ETH-USD",
      "reference_close": 2064.3914,
      "reference_date": "2026-03-27"
    },
    "C": {
      "symbol": "COIN",
      "reference_close": 173.38,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "MSTR",
      "reference_close": 132.93,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_069 — Which of these energy names gains the most between the March 27, 2026 close and the March 31, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these energy names gains the most between the March 27, 2026 close and the March 31, 2026 close?
```

Options:
- `A`: WTI crude oil futures (CL)
- `B`: Energy Select Sector SPDR Fund (XLE)
- `C`: Exxon Mobil (XOM)
- `D`: Chevron (CVX)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "CL=F",
      "reference_close": 93.76,
      "reference_date": "2026-03-27"
    },
    "B": {
      "symbol": "XLE",
      "reference_close": 61.52,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "XOM",
      "reference_close": 165.43,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "CVX",
      "reference_close": 207.79,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_070 — From March 26, 2026 through the close on March 31, 2026, which of these financial names leads on return?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
From March 26, 2026 through the close on March 31, 2026, which of these financial names leads on return?
```

Options:
- `A`: Financial Select Sector SPDR Fund (XLF)
- `B`: JPMorgan Chase (JPM)
- `C`: Goldman Sachs (GS)
- `D`: Bank of America (BAC)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "XLF",
      "reference_close": 49.05,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "JPM",
      "reference_close": 291.66,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "GS",
      "reference_close": 822.64,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "BAC",
      "reference_close": 48.24,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_071 — Which of these precious-metals names finishes with the best return from the March 27, 2026 close through month-end?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these precious-metals names finishes with the best return from the March 27, 2026 close through month-end?
```

Options:
- `A`: Gold futures (GC)
- `B`: SPDR Gold Shares (GLD)
- `C`: iShares Silver Trust (SLV)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "GC=F",
      "reference_close": 4440.1001,
      "reference_date": "2026-03-27"
    },
    "B": {
      "symbol": "GLD",
      "reference_close": 400.64,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "SLV",
      "reference_close": 60.77,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_072 — Over the stretch from the March 26, 2026 close to the March 31, 2026 close, which of these AI platform names outperforms?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Over the stretch from the March 26, 2026 close to the March 31, 2026 close, which of these AI platform names outperforms?
```

Options:
- `A`: NVIDIA (NVDA)
- `B`: Microsoft (MSFT)
- `C`: Meta (META)
- `D`: Amazon (AMZN)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "NVDA",
      "reference_close": 171.24,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "MSFT",
      "reference_close": 365.97,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "META",
      "reference_close": 547.54,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "AMZN",
      "reference_close": 207.54,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_073 — Which of these high-beta growth names posts the top return between the March 26, 2026 close and the March 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these high-beta growth names posts the top return between the March 26, 2026 close and the March 2026 close?
```

Options:
- `A`: Tesla (TSLA)
- `B`: Coinbase (COIN)
- `C`: Strategy (MSTR)
- `D`: iShares Semiconductor ETF (SOXX)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "TSLA",
      "reference_close": 372.11,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "COIN",
      "reference_close": 173.38,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "MSTR",
      "reference_close": 132.93,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "SOXX",
      "reference_close": 328.85,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_074 — Which of these semiconductor names close March 31, 2026 above their March 26, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these semiconductor names close March 31, 2026 above their March 26, 2026 close?
```

Options:
- `A`: NVIDIA (NVDA)
- `B`: AMD (AMD)
- `C`: Broadcom (AVGO)
- `D`: Taiwan Semiconductor (TSM)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "membership_above_reference",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "NVDA",
      "reference_close": 171.24,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "AMD",
      "reference_close": 203.77,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "AVGO",
      "reference_close": 309.415,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "TSM",
      "reference_close": 326.11,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_075 — Which of these megacap tech names finish the March 31, 2026 close above their March 26, 2026 level?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these megacap tech names finish the March 31, 2026 close above their March 26, 2026 level?
```

Options:
- `A`: Apple (AAPL)
- `B`: Microsoft (MSFT)
- `C`: Amazon (AMZN)
- `D`: Meta (META)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "membership_above_reference",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "AAPL",
      "reference_close": 252.89,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "MSFT",
      "reference_close": 365.97,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "AMZN",
      "reference_close": 207.54,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "META",
      "reference_close": 547.54,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_076 — By the close on March 31, 2026, which of these market beta ETFs are above their March 26, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
By the close on March 31, 2026, which of these market beta ETFs are above their March 26, 2026 close?
```

Options:
- `A`: SPDR S&P 500 ETF (SPY)
- `B`: Invesco QQQ Trust (QQQ)
- `C`: iShares Russell 2000 ETF (IWM)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "membership_above_reference",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "SPY",
      "reference_close": 645.09,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "QQQ",
      "reference_close": 573.79,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "IWM",
      "reference_close": 247.44,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_077 — Which of these crypto assets and proxies end March 2026 above their March 27, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these crypto assets and proxies end March 2026 above their March 27, 2026 close?
```

Options:
- `A`: Bitcoin (BTC-USD)
- `B`: Ethereum (ETH-USD)
- `C`: Coinbase (COIN)
- `D`: Strategy (MSTR)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "membership_above_reference",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "BTC-USD",
      "reference_close": 68817.0391,
      "reference_date": "2026-03-27"
    },
    "B": {
      "symbol": "ETH-USD",
      "reference_close": 2064.3914,
      "reference_date": "2026-03-27"
    },
    "C": {
      "symbol": "COIN",
      "reference_close": 173.38,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "MSTR",
      "reference_close": 132.93,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_078 — Which names in this energy names group close higher on March 31, 2026 than they did on March 27, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which names in this energy names group close higher on March 31, 2026 than they did on March 27, 2026?
```

Options:
- `A`: WTI crude oil futures (CL)
- `B`: Energy Select Sector SPDR Fund (XLE)
- `C`: Exxon Mobil (XOM)
- `D`: Chevron (CVX)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "membership_above_reference",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "CL=F",
      "reference_close": 93.76,
      "reference_date": "2026-03-27"
    },
    "B": {
      "symbol": "XLE",
      "reference_close": 61.52,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "XOM",
      "reference_close": 165.43,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "CVX",
      "reference_close": 207.79,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_079 — Which of these financial names finish above their March 26, 2026 close by month-end?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these financial names finish above their March 26, 2026 close by month-end?
```

Options:
- `A`: Financial Select Sector SPDR Fund (XLF)
- `B`: JPMorgan Chase (JPM)
- `C`: Goldman Sachs (GS)
- `D`: Bank of America (BAC)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "membership_above_reference",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "XLF",
      "reference_close": 49.05,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "JPM",
      "reference_close": 291.66,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "GS",
      "reference_close": 822.64,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "BAC",
      "reference_close": 48.24,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_080 — At the March 31, 2026 close, which of these precious-metals names are still above their March 27, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
At the March 31, 2026 close, which of these precious-metals names are still above their March 27, 2026 close?
```

Options:
- `A`: Gold futures (GC)
- `B`: SPDR Gold Shares (GLD)
- `C`: iShares Silver Trust (SLV)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "membership_above_reference",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "GC=F",
      "reference_close": 4440.1001,
      "reference_date": "2026-03-27"
    },
    "B": {
      "symbol": "GLD",
      "reference_close": 400.64,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "SLV",
      "reference_close": 60.77,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_081 — Which of these AI platform names close March 2026 above where they closed on March 26, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these AI platform names close March 2026 above where they closed on March 26, 2026?
```

Options:
- `A`: NVIDIA (NVDA)
- `B`: Microsoft (MSFT)
- `C`: Meta (META)
- `D`: Amazon (AMZN)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "membership_above_reference",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "NVDA",
      "reference_close": 171.24,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "MSFT",
      "reference_close": 365.97,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "META",
      "reference_close": 547.54,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "AMZN",
      "reference_close": 207.54,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_082 — Which of these high-beta growth names end the month above their March 26, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which of these high-beta growth names end the month above their March 26, 2026 close?
```

Options:
- `A`: Tesla (TSLA)
- `B`: Coinbase (COIN)
- `C`: Strategy (MSTR)
- `D`: iShares Semiconductor ETF (SOXX)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "membership_above_reference",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "TSLA",
      "reference_close": 372.11,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "COIN",
      "reference_close": 173.38,
      "reference_date": "2026-03-26"
    },
    "C": {
      "symbol": "MSTR",
      "reference_close": 132.93,
      "reference_date": "2026-03-26"
    },
    "D": {
      "symbol": "SOXX",
      "reference_close": 328.85,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_083 — Which performs better from the March 27, 2026 close through the March 31, 2026 close: Bitcoin (BTC-USD) or Ethereum (ETH-USD)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which performs better from the March 27, 2026 close through the March 31, 2026 close: Bitcoin (BTC-USD) or Ethereum (ETH-USD)?
```

Options:
- `A`: Bitcoin (BTC-USD)
- `B`: Ethereum (ETH-USD)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "BTC-USD",
      "reference_close": 68817.0391,
      "reference_date": "2026-03-27"
    },
    "B": {
      "symbol": "ETH-USD",
      "reference_close": 2064.3914,
      "reference_date": "2026-03-27"
    }
  }
}
```

## v13_084 — From the March 26, 2026 close to the March 31, 2026 close, which has the stronger return: NVIDIA (NVDA) or AMD (AMD)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
From the March 26, 2026 close to the March 31, 2026 close, which has the stronger return: NVIDIA (NVDA) or AMD (AMD)?
```

Options:
- `A`: NVIDIA (NVDA)
- `B`: AMD (AMD)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "NVDA",
      "reference_close": 171.24,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "AMD",
      "reference_close": 203.77,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_085 — Which outperforms between March 26, 2026 and the close on March 31, 2026: Apple (AAPL) or Microsoft (MSFT)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which outperforms between March 26, 2026 and the close on March 31, 2026: Apple (AAPL) or Microsoft (MSFT)?
```

Options:
- `A`: Apple (AAPL)
- `B`: Microsoft (MSFT)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "AAPL",
      "reference_close": 252.89,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "MSFT",
      "reference_close": 365.97,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_086 — Which posts the better return from the March 26, 2026 close through month-end: Amazon (AMZN) or Meta (META)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which posts the better return from the March 26, 2026 close through month-end: Amazon (AMZN) or Meta (META)?
```

Options:
- `A`: Amazon (AMZN)
- `B`: Meta (META)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "AMZN",
      "reference_close": 207.54,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "META",
      "reference_close": 547.54,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_087 — Between SPDR S&P 500 ETF (SPY) and Invesco QQQ Trust (QQQ), which does better from the March 26, 2026 close to the March 31, 2026 close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Between SPDR S&P 500 ETF (SPY) and Invesco QQQ Trust (QQQ), which does better from the March 26, 2026 close to the March 31, 2026 close?
```

Options:
- `A`: SPDR S&P 500 ETF (SPY)
- `B`: Invesco QQQ Trust (QQQ)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "SPY",
      "reference_close": 645.09,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "QQQ",
      "reference_close": 573.79,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_088 — Which has the higher return over the stretch from March 26, 2026 to March 31, 2026: Energy Select Sector SPDR Fund (XLE) or Financial Select Sector SPDR Fund (XLF)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which has the higher return over the stretch from March 26, 2026 to March 31, 2026: Energy Select Sector SPDR Fund (XLE) or Financial Select Sector SPDR Fund (XLF)?
```

Options:
- `A`: Energy Select Sector SPDR Fund (XLE)
- `B`: Financial Select Sector SPDR Fund (XLF)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "XLE",
      "reference_close": 61.52,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "XLF",
      "reference_close": 49.05,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_089 — From the March 27, 2026 close through the final March close, which performs better: Gold futures (GC) or WTI crude oil futures (CL)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
From the March 27, 2026 close through the final March close, which performs better: Gold futures (GC) or WTI crude oil futures (CL)?
```

Options:
- `A`: Gold futures (GC)
- `B`: WTI crude oil futures (CL)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "GC=F",
      "reference_close": 4440.1001,
      "reference_date": "2026-03-27"
    },
    "B": {
      "symbol": "CL=F",
      "reference_close": 93.76,
      "reference_date": "2026-03-27"
    }
  }
}
```

## v13_090 — Which wins on return between the March 26, 2026 close and the March 31, 2026 close: Coinbase (COIN) or Strategy (MSTR)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which wins on return between the March 26, 2026 close and the March 31, 2026 close: Coinbase (COIN) or Strategy (MSTR)?
```

Options:
- `A`: Coinbase (COIN)
- `B`: Strategy (MSTR)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "COIN",
      "reference_close": 173.38,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "MSTR",
      "reference_close": 132.93,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_091 — Which finishes stronger from the March 26, 2026 close through March 31, 2026: SPDR Gold Shares (GLD) or iShares Silver Trust (SLV)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which finishes stronger from the March 26, 2026 close through March 31, 2026: SPDR Gold Shares (GLD) or iShares Silver Trust (SLV)?
```

Options:
- `A`: SPDR Gold Shares (GLD)
- `B`: iShares Silver Trust (SLV)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "GLD",
      "reference_close": 400.64,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "SLV",
      "reference_close": 60.77,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_092 — Which has the better move from March 26, 2026 to the March 2026 close: iShares Semiconductor ETF (SOXX) or Invesco QQQ Trust (QQQ)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which has the better move from March 26, 2026 to the March 2026 close: iShares Semiconductor ETF (SOXX) or Invesco QQQ Trust (QQQ)?
```

Options:
- `A`: iShares Semiconductor ETF (SOXX)
- `B`: Invesco QQQ Trust (QQQ)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "SOXX",
      "reference_close": 328.85,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "QQQ",
      "reference_close": 573.79,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_093 — Between the March 26, 2026 close and the March 31, 2026 close, which outperforms: Tesla (TSLA) or NVIDIA (NVDA)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Between the March 26, 2026 close and the March 31, 2026 close, which outperforms: Tesla (TSLA) or NVIDIA (NVDA)?
```

Options:
- `A`: Tesla (TSLA)
- `B`: NVIDIA (NVDA)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "TSLA",
      "reference_close": 372.11,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "NVDA",
      "reference_close": 171.24,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_094 — Which posts the stronger return into month-end: JPMorgan Chase (JPM) or Goldman Sachs (GS)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which posts the stronger return into month-end: JPMorgan Chase (JPM) or Goldman Sachs (GS)?
```

Options:
- `A`: JPMorgan Chase (JPM)
- `B`: Goldman Sachs (GS)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "JPM",
      "reference_close": 291.66,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "GS",
      "reference_close": 822.64,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_095 — Which ends the period from March 26, 2026 through March 31, 2026 with the better return: Exxon Mobil (XOM) or Chevron (CVX)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which ends the period from March 26, 2026 through March 31, 2026 with the better return: Exxon Mobil (XOM) or Chevron (CVX)?
```

Options:
- `A`: Exxon Mobil (XOM)
- `B`: Chevron (CVX)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "XOM",
      "reference_close": 165.43,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "CVX",
      "reference_close": 207.79,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_096 — Which does better from the March 26, 2026 close to the close on March 31, 2026: Apple (AAPL) or Amazon (AMZN)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which does better from the March 26, 2026 close to the close on March 31, 2026: Apple (AAPL) or Amazon (AMZN)?
```

Options:
- `A`: Apple (AAPL)
- `B`: Amazon (AMZN)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "AAPL",
      "reference_close": 252.89,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "AMZN",
      "reference_close": 207.54,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_097 — From March 26, 2026 through the March 2026 close, which leads on return: Meta (META) or Alphabet (GOOGL)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
From March 26, 2026 through the March 2026 close, which leads on return: Meta (META) or Alphabet (GOOGL)?
```

Options:
- `A`: Meta (META)
- `B`: Alphabet (GOOGL)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "META",
      "reference_close": 547.54,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "GOOGL",
      "reference_close": 280.92,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_098 — Which has the edge from the March 26, 2026 close through the March 31, 2026 close: Broadcom (AVGO) or Taiwan Semiconductor (TSM)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which has the edge from the March 26, 2026 close through the March 31, 2026 close: Broadcom (AVGO) or Taiwan Semiconductor (TSM)?
```

Options:
- `A`: Broadcom (AVGO)
- `B`: Taiwan Semiconductor (TSM)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "AVGO",
      "reference_close": 309.415,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "TSM",
      "reference_close": 326.11,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_099 — Which outperforms over the run from March 26, 2026 to March 31, 2026: iShares Russell 2000 ETF (IWM) or SPDR S&P 500 ETF (SPY)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which outperforms over the run from March 26, 2026 to March 31, 2026: iShares Russell 2000 ETF (IWM) or SPDR S&P 500 ETF (SPY)?
```

Options:
- `A`: iShares Russell 2000 ETF (IWM)
- `B`: SPDR S&P 500 ETF (SPY)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "IWM",
      "reference_close": 247.44,
      "reference_date": "2026-03-26"
    },
    "B": {
      "symbol": "SPY",
      "reference_close": 645.09,
      "reference_date": "2026-03-26"
    }
  }
}
```

## v13_100 — Which closes out the period with the better return, Bitcoin (BTC-USD) or Coinbase (COIN)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`
- Source type: `custom_live`
- End time: `2026-03-31`

Question:
```text
Which closes out the period with the better return, Bitcoin (BTC-USD) or Coinbase (COIN)?
```

Options:
- `A`: Bitcoin (BTC-USD)
- `B`: Coinbase (COIN)

Ground truth:
```text

```

Resolution spec:
```json
{
  "source": "yfinance",
  "method": "winner_by_return",
  "resolution_date": "2026-03-31",
  "symbols": {
    "A": {
      "symbol": "BTC-USD",
      "reference_close": 68817.0391,
      "reference_date": "2026-03-27"
    },
    "B": {
      "symbol": "COIN",
      "reference_close": 173.38,
      "reference_date": "2026-03-26"
    }
  }
}
```

