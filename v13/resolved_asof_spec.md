# v13 Resolved As-Of Spec

## Purpose

This subset keeps the convenience of resolved `FutureX-Past` questions while imposing an explicit as-of search rule.

- The cases are historical and immediately scoreable.
- Search is allowed.
- But evidence must be constrained to each case's `search_cutoff`.
- This subset is better than unrestricted historical search when the goal is to simulate decision-time reasoning.

## Composition

- Total cases: `15`
- Same 15 categorized `FutureX-Past` finance cases used in the resolved companion.
- Each case adds `search_cutoff` and `search_cutoff_source` metadata.

## Files

- `resolved_asof_questions.json`
- `resolved_asof_ground_truth.json`
- `resolved_asof_cases.md`
- `resolved_asof_test_script.py`

## Evaluation Rule

- If the benchmark runner uses search, it should reject sources dated after the case cutoff.
- If a source date is unavailable or ambiguous, it should not be relied on.
