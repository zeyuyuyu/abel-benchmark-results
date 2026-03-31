# v14 Track H Benchmark Report (2026-03-31)

Run summary for `Track H: causal_network_operations` using:

- Questions: `v14/track_h_causal_ops_questions.json`
- Ground truth: `v14/track_h_causal_ops_ground_truth.json`
- Harness output: `.bench/v14-track-h-causal-ops-results-20260331-175131/summary.json`
- Repo result files:
  - `v14/track_h_causal_ops_results.json`
  - `v14/track_h_causal_ops_results.md`

## Headline A/B

- Case count: `24`
- Codex only (raw): `16/24 = 66.67%`
- Codex + skill (raw): `21/24 = 87.50%`
- Absolute gain: `+20.83pp`

## Validity and Runtime

- Base valid outputs: `18/24`
- Skill valid outputs: `21/24`
- Base runtime: `6899.45s`
- Skill runtime: `6445.91s`

Valid-only (both sides valid):

- Cases used: `18`
- Base: `16/18 = 88.89%`
- Skill: `18/18 = 100.00%`

## Family Breakdown

- `cross_asset_upside_selection`: base `4/6`, skill `6/6`
- `direct_parent_identification`: base `3/6`, skill `6/6`
- `markov_role_classification`: base `3/6`, skill `3/6`
- `directed_path_reachability`: base `6/6`, skill `6/6`

## Takeaway

This run shows clear separation on Track H. The largest observed gain is in
graph-structured upstream driver identification, where skill-assisted runs
improve both accuracy and answer-format validity.
