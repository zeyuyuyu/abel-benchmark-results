# v14 Track G Historical As-Of Spec

## Purpose

This pack is the canonical `v14` materialization of Track G historical
`FutureX-Past` cases under a strict time-bounded search protocol.

## Source

This pack mirrors the current `v13` historical as-of benchmark:

- source questions: `v13/resolved_asof_questions.json`
- source answers: `v13/resolved_asof_ground_truth.json`

## Files

- `track_g_past_asof_questions.json`
- `track_g_past_asof_ground_truth.json`
- `track_g_past_asof_cases.md`

## Evaluation Rule

- Search is allowed.
- But evidence must be dated on or before the case-level `search_cutoff`.
- If source dates are unclear, they should not be relied on.

## Why This Exists

`public_dev` only contains a small number of Track G exemplars.

This pack is different:

- it is the full current historical as-of slice
- it preserves the category mix from `v13 resolved_asof`
- it is the correct materialized `v14` pack for
  `evaluation_regime = historical_asof_search_cutoff`

## Current Count

- mirrored historical as-of cases: `15`
