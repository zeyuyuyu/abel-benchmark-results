# v14 Track G FutureX Mapping

## Purpose

This document formally maps the `v13` FutureX-oriented benchmark packs into the
`v14` taxonomy.

The important rule is:

- top-level `v14` tracks are organized by capability
- `FutureX` is treated as a Track G task surface, not as a separate top-level
  benchmark track

So the canonical placement is:

- `track = agentic_live_analysis`
- `task_family = futurex_style_live_prediction`

Within that family, we distinguish two primary evaluation regimes.

## Regime 1: Live Forward Resolution

- `evaluation_regime = live_forward_resolution`
- Source files:
  - `v13/questions.json`
  - `v13/ground_truth.json`
  - `v13/cases.md`
- Case count: `100`

Breakdown:

- official `FutureX-Online` finance cases: `7`
  - id range: `v13_001` -> `v13_007`
- custom live finance cases written in FutureX-style contract form: `93`
  - id range: `v13_008` -> `v13_100`

Why this mapping matters:

- the official subset preserves the external FutureX surface directly
- the custom subset extends the same agentic contract style into a larger
  finance-oriented live benchmark

## Regime 2: Historical As-Of Search Cutoff

- `evaluation_regime = historical_asof_search_cutoff`
- Source files:
  - `v13/resolved_asof_questions.json`
  - `v13/resolved_asof_ground_truth.json`
  - `v13/resolved_asof_cases.md`
- Case count: `15`

This is the canonical historical open-book slice for Track G.

The defining rule is:

- search is allowed
- but evidence must be on or before the case-level `search_cutoff`

Category mix:

- `central_bank_decision`: `4`
- `commodity_bucket`: `2`
- `first_hit`: `2`
- `crypto_binary`: `2`
- `commodity_thresholds`: `1`
- `commodity_hit_levels`: `1`
- `agriculture_bucket`: `1`
- `supply_shock_binary`: `1`
- `single_stock_direction`: `1`

## Related But Non-Primary

There is also a related auxiliary slice:

- `evaluation_regime = historical_resolved_unbounded`
- Source files:
  - `v13/resolved_questions.json`
  - `v13/resolved_ground_truth.json`
  - `v13/resolved_cases.md`

This slice is still useful, but it should not be the primary FutureX-style
score because it is more vulnerable to unrestricted historical leakage.

## Practical Reading

When someone asks “where do the FutureX-style cases live in `v14`?”, the short
answer is:

- `Track G / task_family = futurex_style_live_prediction`

When someone asks “which kind?”, the answer is:

- `live_forward_resolution`
- `historical_asof_search_cutoff`
