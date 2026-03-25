# v9 FutureX-Style LLM Casebook

Snapshot: `2026-03-25 (GMT+8)`

This casebook is LLM-authored, but each answer key is anchored to a live Abel CAP snapshot after updating the local skill to `1.0.7`.

## Summary

- Total cases: `36`
- Generation method: `llm_authored_with_live_snapshot`
- Skill version target: `1.0.7`

## Pattern Counts

| FutureX Pattern | Count |
|-----------------|-------|
| `interval bin` | `9` |
| `roster membership` | `9` |
| `statement-truth set` | `8` |
| `threshold ladder` | `6` |
| `top-k membership` | `2` |
| `winner market` | `2` |

## Cases

| Case ID | Pattern | Category | Answer |
|---------|---------|----------|--------|
| `fxcausal_001` | `interval bin` | `observe_prediction` | `\boxed{C}` |
| `fxcausal_002` | `interval bin` | `observe_prediction` | `\boxed{B}` |
| `fxcausal_003` | `interval bin` | `observe_prediction` | `\boxed{E}` |
| `fxcausal_004` | `interval bin` | `observe_prediction` | `\boxed{C}` |
| `fxcausal_005` | `interval bin` | `observe_prediction` | `\boxed{B}` |
| `fxcausal_006` | `interval bin` | `observe_prediction` | `\boxed{A}` |
| `fxcausal_007` | `interval bin` | `observe_prediction` | `\boxed{B}` |
| `fxcausal_008` | `interval bin` | `observe_prediction` | `\boxed{B}` |
| `fxcausal_009` | `threshold ladder` | `observe_prediction` | `\boxed{A, B, C, D}` |
| `fxcausal_010` | `threshold ladder` | `observe_prediction` | `\boxed{A, B}` |
| `fxcausal_011` | `threshold ladder` | `observe_prediction` | `\boxed{A, B, C, D, E}` |
| `fxcausal_012` | `threshold ladder` | `observe_prediction` | `\boxed{A}` |
| `fxcausal_013` | `threshold ladder` | `observe_prediction` | `\boxed{A, B}` |
| `fxcausal_014` | `threshold ladder` | `observe_prediction` | `\boxed{A, B}` |
| `fxcausal_015` | `winner market` | `observe_ranking` | `\boxed{B}` |
| `fxcausal_016` | `winner market` | `observe_ranking` | `\boxed{A}` |
| `fxcausal_017` | `top-k membership` | `observe_ranking` | `\boxed{A, C, D}` |
| `fxcausal_018` | `top-k membership` | `observe_ranking` | `\boxed{B, E, F}` |
| `fxcausal_019` | `roster membership` | `observe_drivers` | `\boxed{A, B, C}` |
| `fxcausal_020` | `roster membership` | `observe_drivers` | `\boxed{A, B, C}` |
| `fxcausal_021` | `roster membership` | `graph_neighbors` | `\boxed{A, B, C}` |
| `fxcausal_022` | `roster membership` | `graph_neighbors` | `\boxed{A, B, C}` |
| `fxcausal_023` | `roster membership` | `observe_drivers` | `\boxed{A}` |
| `fxcausal_024` | `roster membership` | `graph_neighbors` | `\boxed{A, B, C}` |
| `fxcausal_025` | `statement-truth set` | `graph_paths` | `\boxed{A, C, E}` |
| `fxcausal_026` | `statement-truth set` | `graph_paths` | `\boxed{A}` |
| `fxcausal_027` | `statement-truth set` | `intervention` | `\boxed{A, D}` |
| `fxcausal_028` | `statement-truth set` | `intervention` | `\boxed{B, C}` |
| `fxcausal_029` | `statement-truth set` | `counterfactual_preview` | `\boxed{A, B, C, D}` |
| `fxcausal_030` | `statement-truth set` | `counterfactual_preview` | `\boxed{A}` |
| `fxcausal_031` | `roster membership` | `observation_availability` | `\boxed{A, B, C}` |
| `fxcausal_032` | `roster membership` | `observation_availability` | `\boxed{A, C, D}` |
| `fxcausal_033` | `roster membership` | `observation_availability` | `\boxed{C, D, E}` |
| `fxcausal_034` | `statement-truth set` | `normalization_and_crypto` | `\boxed{A, B}` |
| `fxcausal_035` | `statement-truth set` | `normalization_and_crypto` | `\boxed{A, B, D}` |
| `fxcausal_036` | `interval bin` | `observe_prediction` | `\boxed{C}` |

## Files

- Dataset: [`futurex_style_cases.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v9/futurex_style_cases.json)
- Spec: [`casebook_spec.md`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v9/casebook_spec.md)
