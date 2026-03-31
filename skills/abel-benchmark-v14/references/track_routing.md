# Track Routing (v14 Benchmark Skill)

## Track G

- `v14-track-g-past-asof`
  - Family: `futurex_style_live_prediction`
  - Regime: `historical_asof_search_cutoff`
  - Questions: `v14/track_g_past_asof_questions.json`
  - Ground truth: `v14/track_g_past_asof_ground_truth.json`
  - Rule: search must not exceed each case's `search_cutoff`

- `v14-track-g-true-live`
  - Family: `futurex_style_live_prediction`
  - Regime: `live_forward_resolution`
  - Questions: `v14/track_g_true_live_questions.json`
  - Ground truth: `v14/track_g_true_live_ground_truth.json`
  - Rule: run prediction now; scoring waits for future resolution

## Track H

- `v14-track-h-causal-ops`
  - Family: `causal_network_operations`
  - Regime: `frozen_evidence_public_dev`
  - Questions: `v14/track_h_causal_ops_questions.json`
  - Ground truth: `v14/track_h_causal_ops_ground_truth.json`
  - Goal: stress direct causal graph operations in analyst language

## Public Index

- `v14-build-public-manifest`
  - Writes:
    - `v14/public_benchmark_manifest.json`
    - `v14/public_benchmark_index.md`
