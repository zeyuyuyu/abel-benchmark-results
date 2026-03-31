# v14 Track H Causal Ops Results

Full Track H run over `24` cases.

- Base raw: `16/24 = 66.67%`
- Skill raw: `21/24 = 87.50%`
- Base valid outputs: `18/24`
- Skill valid outputs: `21/24`
- Base duration: `6899.45s`
- Skill duration: `6445.91s`

## Valid-Only (Both Sides Valid)

- Cases used: `18`
- Base: `16/18` = 88.89%
- Skill: `18/18` = 100.00%

| Case ID | Family | Ground truth | Base | Skill |
|---|---|---|---|---|
| `v14h_001` | `cross_asset_upside_selection` | `\boxed{D}` | `\boxed{A}` ❌ | `\boxed{D}` ✅ |
| `v14h_002` | `cross_asset_upside_selection` | `\boxed{A}` | `\boxed{C}` ❌ | `\boxed{A}` ✅ |
| `v14h_003` | `cross_asset_upside_selection` | `\boxed{D}` | `\boxed{D}` ✅ | `\boxed{D}` ✅ |
| `v14h_004` | `cross_asset_upside_selection` | `\boxed{C}` | `\boxed{C}` ✅ | `\boxed{C}` ✅ |
| `v14h_005` | `cross_asset_upside_selection` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ |
| `v14h_006` | `cross_asset_upside_selection` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ |
| `v14h_007` | `direct_parent_identification` | `\boxed{D}` | `None` | `\boxed{D}` ✅ |
| `v14h_008` | `direct_parent_identification` | `\boxed{C}` | `None` | `\boxed{C}` ✅ |
| `v14h_009` | `direct_parent_identification` | `\boxed{C}` | `None` | `\boxed{C}` ✅ |
| `v14h_010` | `direct_parent_identification` | `\boxed{D}` | `\boxed{D}` ✅ | `\boxed{D}` ✅ |
| `v14h_011` | `direct_parent_identification` | `\boxed{D}` | `\boxed{D}` ✅ | `\boxed{D}` ✅ |
| `v14h_012` | `direct_parent_identification` | `\boxed{C}` | `\boxed{C}` ✅ | `\boxed{C}` ✅ |
| `v14h_013` | `markov_role_classification` | `\boxed{A}` | `None` | `None` |
| `v14h_014` | `markov_role_classification` | `\boxed{A}` | `None` | `None` |
| `v14h_015` | `markov_role_classification` | `\boxed{A}` | `None` | `None` |
| `v14h_016` | `markov_role_classification` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ |
| `v14h_017` | `markov_role_classification` | `\boxed{A}` | `\boxed{A}` ✅ | `\boxed{A}` ✅ |
| `v14h_018` | `markov_role_classification` | `\boxed{A}` | `\boxed{A}` ✅ | `\boxed{A}` ✅ |
| `v14h_019` | `directed_path_reachability` | `\boxed{A}` | `\boxed{A}` ✅ | `\boxed{A}` ✅ |
| `v14h_020` | `directed_path_reachability` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ |
| `v14h_021` | `directed_path_reachability` | `\boxed{A}` | `\boxed{A}` ✅ | `\boxed{A}` ✅ |
| `v14h_022` | `directed_path_reachability` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ |
| `v14h_023` | `directed_path_reachability` | `\boxed{A}` | `\boxed{A}` ✅ | `\boxed{A}` ✅ |
| `v14h_024` | `directed_path_reachability` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ |

## Per-Family

- `cross_asset_upside_selection`: base `4/6`, skill `6/6`
- `direct_parent_identification`: base `3/6`, skill `6/6`
- `directed_path_reachability`: base `6/6`, skill `6/6`
- `markov_role_classification`: base `3/6`, skill `3/6`
