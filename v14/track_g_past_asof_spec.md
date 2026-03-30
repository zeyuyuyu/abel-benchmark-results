# v14 Track G Historical As-Of Spec

## Purpose

This is the canonical full FutureX-Past materialization for Track G under
`historical_asof_search_cutoff`.

## Composition

- Total cases: `244`
- Legacy finance-tagged cases: `15`
- Remaining cases are labeled `category = unlabeled` unless we have prior
  curated category tags.

## Evaluation Rule

- Search is allowed.
- But evidence must be dated on or before each case's `search_cutoff`.
- If source dates are unavailable or ambiguous, they should not be relied on.

## Category Breakdown

- `agriculture_bucket`: `1`
- `central_bank_decision`: `4`
- `commodity_bucket`: `2`
- `commodity_hit_levels`: `1`
- `commodity_thresholds`: `1`
- `crypto_binary`: `2`
- `first_hit`: `2`
- `single_stock_direction`: `1`
- `supply_shock_binary`: `1`
- `unlabeled`: `229`

## Level Breakdown

- `level=1`: `98`
- `level=2`: `106`
- `level=3`: `15`
- `level=4`: `25`

## Files

- `track_g_past_asof_questions.json`
- `track_g_past_asof_ground_truth.json`
- `track_g_past_asof_cases.md`
- `build_track_g_past_asof_pack.py`
