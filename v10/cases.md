# v10 Natural-Intent Casebook

Snapshot: `March 25, 2026 (GMT+8)`

These cases are written as questions a normal user might actually ask. The answer key is still anchored to the same live snapshot, but the prompts do not expose Abel / CAP internals.

## Summary

- Total cases: `40`
- Generation method: `llm_authored_with_live_snapshot`

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

| Case ID | Category | Answer | Question |
|---------|----------|--------|----------|
| `v10_001` | `directional_bucket` | `\boxed{E}` | If you had to bucket AMD's near-term move right now, which range seems most plausible? |
| `v10_002` | `directional_bucket` | `\boxed{B}` | If you had to bucket Tesla's near-term move right now, which range seems most plausible? |
| `v10_003` | `directional_bucket` | `\boxed{C}` | If you had to bucket Apple's near-term move right now, which range seems most plausible? |
| `v10_004` | `directional_bucket` | `\boxed{B}` | If you need a quick Ethereum read right now, which move bucket looks most plausible? |
| `v10_005` | `directional_bucket` | `\boxed{B}` | If you need a quick crude oil read right now, which move bucket looks most plausible? |
| `v10_006` | `directional_bucket` | `\boxed{A}` | If you need a quick Broadcom read right now, which move bucket looks most plausible? |
| `v10_007` | `directional_thresholds` | `\boxed{A, B, C, D}` | Which of these increasingly bullish claims about Apple still hold on a short-term read right now? |
| `v10_008` | `directional_thresholds` | `\boxed{A, B}` | Which of these increasingly bullish claims about Tesla still hold on a short-term read right now? |
| `v10_009` | `directional_thresholds` | `\boxed{A, B, C, D, E}` | Which of these increasingly bullish claims about AMD still hold on a short-term read right now? |
| `v10_010` | `directional_thresholds` | `\boxed{A}` | Which of these increasingly bullish claims about Broadcom still hold on a short-term read right now? |
| `v10_011` | `directional_thresholds` | `\boxed{A, B}` | Which of these increasingly bullish claims about Ethereum still hold on a short-term read right now? |
| `v10_012` | `ranking` | `\boxed{B}` | Among Nvidia, AMD, Intel, Broadcom, and TSM, which semiconductor name looks strongest right now? |
| `v10_013` | `ranking` | `\boxed{A}` | Among Apple, Tesla, Nvidia, and Broadcom, which mega-cap tech name looks strongest right now? |
| `v10_014` | `ranking` | `\boxed{A, C, D}` | Which three names look strongest right now on a short-term read? |
| `v10_015` | `ranking` | `\boxed{B, E, F}` | Which three names look weakest right now on a short-term read? |
| `v10_016` | `transmission` | `\boxed{A}` | If you wanted one shock anchor to stress-test AMD today, which starting point is most defensible? |
| `v10_017` | `transmission` | `\boxed{A, B}` | If you are trying to explain Nvidia through company channels rather than broad market beta, which names actually look wired in today? |
| `v10_018` | `transmission` | `\boxed{A}` | If you were explaining Nvidia to a PM today, which framing is stronger? |
| `v10_019` | `transmission` | `\boxed{A}` | Which spillover story is easiest to defend right now? |
| `v10_020` | `transmission` | `\boxed{A}` | If you want company names that seem most relevant for following Nvidia today, which basket is the best starting point? |
| `v10_021` | `transmission` | `\boxed{A, B}` | Which of these broad shortcuts look less useful than real company read-throughs for Nvidia right now? |
| `v10_022` | `pressure_test` | `\boxed{B}` | You ask for a quick 'what if Nvidia jumps 5%' read on AMD. Which description fits best right now? |
| `v10_023` | `pressure_test` | `\boxed{B}` | You ask for the same 'what if' read on AMD, but this time using SOXX as the shock anchor. Which description fits best? |
| `v10_024` | `pressure_test` | `\boxed{B}` | Which setup is more likely to fall apart before it becomes a usable downstream scenario? |
| `v10_025` | `pressure_test` | `\boxed{B}` | If you want a quick one-hour read-through from Nvidia into AMD, what is closest to the current answer? |
| `v10_026` | `coverage` | `\boxed{B}` | If you need a crypto name you can make a more defensible call on right now, which is safer to lean on? |
| `v10_027` | `coverage` | `\boxed{A}` | If you need one energy-linked market anchor you can make a defensible call on today, which is the cleanest choice? |
| `v10_028` | `coverage` | `\boxed{A, B, C}` | Which of these popular shortcuts look weakest if you need a defensible live read right now? |
| `v10_029` | `coverage` | `\boxed{A, B, C}` | Which of these are easier to support right now with a defensible live read? |
| `v10_030` | `market_story` | `\boxed{A, B, C}` | Which of these quick takes sound right right now? |
| `v10_031` | `market_story` | `\boxed{A, B}` | Which coverage statements sound right today? |
| `v10_032` | `market_story` | `\boxed{A}` | If you want a basket of names that are actually usable for a defensible market read today, which one is best? |
| `v10_033` | `market_story` | `\boxed{A}` | If you want one clear leader and one clear laggard from this snapshot, which pair fits best? |
| `v10_034` | `market_story` | `\boxed{A, B, D}` | Which of these quick cross-name reads sound right right now? |
| `v10_035` | `ranking` | `\boxed{B}` | Among Apple, Nvidia, TSM, and crude oil, which looks closest to unchanged right now? |
| `v10_036` | `ranking` | `\boxed{C}` | Among Tesla, Intel, Broadcom, and crude oil, which looks under the most pressure right now? |
| `v10_037` | `coverage` | `\boxed{A}` | If you need one market handle that is most likely to waste your time today, which is it? |
| `v10_038` | `coverage` | `\boxed{A, B, C}` | Which of these names are better choices right now than broad shortcut proxies if you need a quick defensible call? |
| `v10_039` | `pressure_test` | `\boxed{A, C, E}` | Which what-if statements sound right today? |
| `v10_040` | `transmission` | `\boxed{A}` | If you are trying to tell a company-specific story around Nvidia, which pair is the least convincing place to start? |

## Files

- Dataset: [`natural_intent_cases.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v10/natural_intent_cases.json)
- Spec: [`casebook_spec.md`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v10/casebook_spec.md)
- Generator: [`build_natural_intent_casebook.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v10/build_natural_intent_casebook.py)
