# v14 Public Dev Benchmark Report

- Timestamp: `2026-03-27T18:02:07.742470+08:00`
- Model: `gpt-5.4`
- Reasoning effort: `low`
- Case count: `21`
- Questions: `/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v14/public_dev_cases.json`
- Ground truth: `/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v14/public_dev_ground_truth.json`
- Detailed case markdown: `public_dev_case_results.md`

## base

- Exact-primary accuracy: `6/21 = 28.57%`
- Weighted average: `44.76%`
- Total duration: `278.22s`

Per track:

- `agentic_live_analysis`: `0/3 = 0.00%`
- `data_grounded_causal_reasoning`: `1/3 = 33.33%`
- `finance_and_business_causal_reasoning`: `0/3 = 0.00%`
- `formal_causality`: `3/3 = 100.00%`
- `graph_and_mechanism`: `1/3 = 33.33%`
- `industrial_intervention_and_estimation`: `0/3 = 0.00%`
- `natural_event_causality`: `1/3 = 33.33%`

## skill

- Exact-primary accuracy: `7/21 = 33.33%`
- Weighted average: `47.86%`
- Total duration: `344.22s`

Per track:

- `agentic_live_analysis`: `0/3 = 0.00%`
- `data_grounded_causal_reasoning`: `1/3 = 33.33%`
- `finance_and_business_causal_reasoning`: `0/3 = 0.00%`
- `formal_causality`: `3/3 = 100.00%`
- `graph_and_mechanism`: `1/3 = 33.33%`
- `industrial_intervention_and_estimation`: `1/3 = 33.33%`
- `natural_event_causality`: `1/3 = 33.33%`

## Comparison

- Exact-primary diff count: `20`
- Differing case IDs: `v14d_001, v14d_002, v14d_003, v14d_005, v14d_006, v14d_007, v14d_008, v14d_009, v14d_010, v14d_011, v14d_012, v14d_013, v14d_014, v14d_015, v14d_016, v14d_017, v14d_018, v14d_019, v14d_020, v14d_021`

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
| `v14d_017` | `industrial_intervention_and_estimation` | `0` | `1` |
| `v14d_018` | `industrial_intervention_and_estimation` | `0` | `0` |
| `v14d_019` | `agentic_live_analysis` | `0` | `0` |
| `v14d_020` | `agentic_live_analysis` | `0` | `0` |
| `v14d_021` | `agentic_live_analysis` | `0` | `0` |
