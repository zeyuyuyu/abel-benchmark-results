# v11 Natural-Intent Casebook

Snapshot: `March 25, 2026 (GMT+8)`

These cases are written as questions a normal user might actually ask.
The answer key and grounding are split into `ground_truth.json`, and the original Abel snapshot evidence is saved under `artifacts/`.

## Summary

- Total cases: `40`
- Generation method: `llm_authored_with_live_snapshot`
- Ground truth source: `artifacts/snapshot_facts.json`

## Pattern Counts

| Pattern | Count |
|---------|-------|
| `interval bin` | `6` |
| `roster membership` | `5` |
| `statement-truth set` | `4` |
| `threshold ladder` | `5` |
| `top-k membership` | `2` |
| `winner market` | `18` |

## Cases

| Case ID | Category | Question |
|---------|----------|----------|
| `v11_001` | `directional_bucket` | If you had to bucket AMD's near-term move right now, which range seems most plausible? |
| `v11_002` | `directional_bucket` | If you had to bucket Tesla's near-term move right now, which range seems most plausible? |
| `v11_003` | `directional_bucket` | If you had to bucket Apple's near-term move right now, which range seems most plausible? |
| `v11_004` | `directional_bucket` | If you need a quick Ethereum read right now, which move bucket looks most plausible? |
| `v11_005` | `directional_bucket` | If you need a quick crude oil read right now, which move bucket looks most plausible? |
| `v11_006` | `directional_bucket` | If you need a quick Broadcom read right now, which move bucket looks most plausible? |
| `v11_007` | `directional_thresholds` | Which of these increasingly bullish claims about Apple still hold on a short-term read right now? |
| `v11_008` | `directional_thresholds` | Which of these increasingly bullish claims about Tesla still hold on a short-term read right now? |
| `v11_009` | `directional_thresholds` | Which of these increasingly bullish claims about AMD still hold on a short-term read right now? |
| `v11_010` | `directional_thresholds` | Which of these increasingly bullish claims about Broadcom still hold on a short-term read right now? |
| `v11_011` | `directional_thresholds` | Which of these increasingly bullish claims about Ethereum still hold on a short-term read right now? |
| `v11_012` | `ranking` | Among Nvidia, AMD, Intel, Broadcom, and TSM, which semiconductor name looks strongest right now? |
| `v11_013` | `ranking` | Among Apple, Tesla, Nvidia, and Broadcom, which mega-cap tech name looks strongest right now? |
| `v11_014` | `ranking` | Which three names look strongest right now on a short-term read? |
| `v11_015` | `ranking` | Which three names look weakest right now on a short-term read? |
| `v11_016` | `transmission` | If you wanted one shock anchor to stress-test AMD today, which starting point is most defensible? |
| `v11_017` | `transmission` | If you are trying to explain Nvidia through company channels rather than broad market beta, which names actually look wired in today? |
| `v11_018` | `transmission` | If you were explaining Nvidia to a PM today, which framing is stronger? |
| `v11_019` | `transmission` | Which spillover story is easiest to defend right now? |
| `v11_020` | `transmission` | If you want company names that seem most relevant for following Nvidia today, which basket is the best starting point? |
| `v11_021` | `transmission` | Which of these broad shortcuts look less useful than real company read-throughs for Nvidia right now? |
| `v11_022` | `pressure_test` | You ask for a quick 'what if Nvidia jumps 5%' read on AMD. Which description fits best right now? |
| `v11_023` | `pressure_test` | You ask for the same 'what if' read on AMD, but this time using SOXX as the shock anchor. Which description fits best? |
| `v11_024` | `pressure_test` | Which setup is more likely to fall apart before it becomes a usable downstream scenario? |
| `v11_025` | `pressure_test` | If you want a quick one-hour read-through from Nvidia into AMD, what is closest to the current answer? |
| `v11_026` | `coverage` | If you need a crypto name you can make a more defensible call on right now, which is safer to lean on? |
| `v11_027` | `coverage` | If you need one energy-linked market anchor you can make a defensible call on today, which is the cleanest choice? |
| `v11_028` | `coverage` | Which of these popular shortcuts look weakest if you need a defensible live read right now? |
| `v11_029` | `coverage` | Which of these are easier to support right now with a defensible live read? |
| `v11_030` | `market_story` | Which of these quick takes sound right right now? |
| `v11_031` | `market_story` | Which coverage statements sound right today? |
| `v11_032` | `market_story` | If you want a basket of names that are actually usable for a defensible market read today, which one is best? |
| `v11_033` | `market_story` | If you want one clear leader and one clear laggard from this snapshot, which pair fits best? |
| `v11_034` | `market_story` | Which of these quick cross-name reads sound right right now? |
| `v11_035` | `ranking` | Among Apple, Nvidia, TSM, and crude oil, which looks closest to unchanged right now? |
| `v11_036` | `ranking` | Among Tesla, Intel, Broadcom, and crude oil, which looks under the most pressure right now? |
| `v11_037` | `coverage` | If you need one market handle that is most likely to waste your time today, which is it? |
| `v11_038` | `coverage` | Which of these names are better choices right now than broad shortcut proxies if you need a quick defensible call? |
| `v11_039` | `pressure_test` | Which what-if statements sound right today? |
| `v11_040` | `transmission` | If you are trying to tell a company-specific story around Nvidia, which pair is the least convincing place to start? |

## Files

- Questions: [`questions.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/questions.json)
- Ground Truth: [`ground_truth.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/ground_truth.json)
- Spec: [`casebook_spec.md`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/casebook_spec.md)
- Generator: [`build_natural_intent_casebook.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/build_natural_intent_casebook.py)
- Snapshot Facts: [`snapshot_facts.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/artifacts/snapshot_facts.json)
- Artifact Manifest: [`manifest.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/artifacts/manifest.json)
