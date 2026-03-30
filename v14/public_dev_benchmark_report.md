# v14 Public Dev Benchmark Report

- Timestamp: `2026-03-30T10:07:24.699666+08:00`
- Model: `gpt-5.4`
- Reasoning effort: `low`
- Case count: `25`
- Questions: `public_dev_cases.json`
- Ground truth: `public_dev_ground_truth.json`
- Detailed case markdown: `public_dev_case_results.md`

## base

- Exact-primary accuracy: `6/25 = 24.00%`
- Weighted average: `45.20%`
- Total duration: `361.25s`

Per track:

- `agentic_live_analysis`: `0/7 = 0.00%`
- `data_grounded_causal_reasoning`: `1/3 = 33.33%`
- `finance_and_business_causal_reasoning`: `0/3 = 0.00%`
- `formal_causality`: `3/3 = 100.00%`
- `graph_and_mechanism`: `1/3 = 33.33%`
- `industrial_intervention_and_estimation`: `0/3 = 0.00%`
- `natural_event_causality`: `1/3 = 33.33%`

## skill

- Exact-primary accuracy: `6/25 = 24.00%`
- Weighted average: `46.60%`
- Total duration: `468.47s`

Per track:

- `agentic_live_analysis`: `0/7 = 0.00%`
- `data_grounded_causal_reasoning`: `1/3 = 33.33%`
- `finance_and_business_causal_reasoning`: `0/3 = 0.00%`
- `formal_causality`: `3/3 = 100.00%`
- `graph_and_mechanism`: `1/3 = 33.33%`
- `industrial_intervention_and_estimation`: `0/3 = 0.00%`
- `natural_event_causality`: `1/3 = 33.33%`

## Comparison

- Exact-primary diff count: `24`
- Differing case IDs: `v14d_001, v14d_002, v14d_003, v14d_005, v14d_006, v14d_007, v14d_008, v14d_009, v14d_010, v14d_011, v14d_012, v14d_013, v14d_014, v14d_015, v14d_016, v14d_017, v14d_018, v14d_019, v14d_020, v14d_021, v14d_022, v14d_023, v14d_024, v14d_025`

## Case Table

| Case ID | Track | Base | Skill |
|---|---|---:|---:|
| `v14d_001` | `formal_causality` | `1` | `1` |
| `v14d_002` | `formal_causality` | `1` | `1` |
| `v14d_003` | `formal_causality` | `1` | `1` |
| `v14d_004` | `graph_and_mechanism` | `0` | `0` |
| `v14d_005` | `graph_and_mechanism` | `0` | `0` |
| `v14d_006` | `graph_and_mechanism` | `1` | `1` |
| `v14d_007` | `data_grounded_causal_reasoning` | `1` | `1` |
| `v14d_008` | `data_grounded_causal_reasoning` | `0` | `0` |
| `v14d_009` | `data_grounded_causal_reasoning` | `0` | `0` |
| `v14d_010` | `natural_event_causality` | `1` | `1` |
| `v14d_011` | `natural_event_causality` | `0` | `0` |
| `v14d_012` | `natural_event_causality` | `0` | `0` |
| `v14d_013` | `finance_and_business_causal_reasoning` | `0` | `0` |
| `v14d_014` | `finance_and_business_causal_reasoning` | `0` | `0` |
| `v14d_015` | `finance_and_business_causal_reasoning` | `0` | `0` |
| `v14d_016` | `industrial_intervention_and_estimation` | `0` | `0` |
| `v14d_017` | `industrial_intervention_and_estimation` | `0` | `0` |
| `v14d_018` | `industrial_intervention_and_estimation` | `0` | `0` |
| `v14d_019` | `agentic_live_analysis` | `0` | `0` |
| `v14d_020` | `agentic_live_analysis` | `0` | `0` |
| `v14d_021` | `agentic_live_analysis` | `0` | `0` |
| `v14d_022` | `agentic_live_analysis` | `0` | `0` |
| `v14d_023` | `agentic_live_analysis` | `0` | `0` |
| `v14d_024` | `agentic_live_analysis` | `0` | `0` |
| `v14d_025` | `agentic_live_analysis` | `0` | `0` |
