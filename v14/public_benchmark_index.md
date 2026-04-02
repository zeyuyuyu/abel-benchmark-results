# v14 Public Benchmark Index

This file marks the `v14` benchmark as a **public benchmark suite**.

- Scope: `v14`
- Visibility: `public`
- Generated from: `build_public_benchmark_manifest.py`

## Public Rules

- `historical_asof_search_cutoff` cases allow search, but search must not use evidence after each case's `search_cutoff` timestamp.
- `live_forward_resolution` cases are unresolved by design; answer keys remain blank until third-party resolution.
- Public dev packs can include answer keys for reproducible A/B development and harness debugging.

## Pack Index

| Pack | Track | Regime | Cases | Truth Ready | Questions | Ground Truth | Cases Markdown | Results |
|---|---|---|---:|---:|---|---|---|---|
| `public_dev_seed_pack` | `multi_track_public_dev` | `frozen_evidence_public_dev` | 25 | 25/25 | `v14/public_dev_cases.json` | `v14/public_dev_ground_truth.json` | `v14/public_dev_case_results.md` | `v14/public_dev_benchmark_report.md` |
| `causal_proxy_intervention` | `multi_track_public_dev` | `frozen_evidence_public_dev` | 16 | 16/16 | `v14/causal_proxy_intervention_cases.json` | `v14/causal_proxy_intervention_ground_truth.json` | `v14/causal_proxy_intervention_cases.md` | - |
| `track_g_true_live` | `agentic_live_analysis` | `live_forward_resolution` | 100 | 93/100 | `v14/track_g_true_live_questions.json` | `v14/track_g_true_live_ground_truth.json` | `v14/track_g_true_live_cases.md` | - |
| `track_g_past_asof` | `agentic_live_analysis` | `historical_asof_search_cutoff` | 244 | 244/244 | `v14/track_g_past_asof_questions.json` | `v14/track_g_past_asof_ground_truth.json` | `v14/track_g_past_asof_cases.md` | `v14/track_g_past_asof_results.md` |
| `track_h_causal_ops` | `causal_network_operations` | `frozen_evidence_public_dev` | 24 | 24/24 | `v14/track_h_causal_ops_questions.json` | `v14/track_h_causal_ops_ground_truth.json` | `v14/track_h_causal_ops_cases.md` | `v14/track_h_causal_ops_results.md` |

## Quick Commands

```bash
cd "$(git rev-parse --show-toplevel)"
python3 v14/build_public_benchmark_manifest.py
python3 scripts/run_benchmark.py check-skill
python3 scripts/run_benchmark.py v14-track-g-past-asof
python3 scripts/run_benchmark.py v14-track-g-true-live
```
