# v14 Track I Competing Explanations Results

Full Track I run over `8` cases.

## Scoreboard

- Scoring: `LLM semantic judge (gpt-5.4)`

- Base exact raw: `5/8 = 62.50%`
- Skill exact raw: `5/8 = 62.50%`
- Base primary-only: `8/8 = 100.00%`
- Skill primary-only: `8/8 = 100.00%`
- Base follow-up-only: `5/8 = 62.50%`
- Skill follow-up-only: `5/8 = 62.50%`
- Base exact valid outputs: `8/8`
- Skill exact valid outputs: `8/8`
- Base duration: `235.60s`
- Skill duration: `313.42s`

## Per Case

| Case ID | Source | Family | Canonical primary | Base primary | Skill primary | Canonical follow-up | Base follow-up | Skill follow-up | Exact winner |
|---|---|---|---|---|---|---|---|---|---|
| `v14i_001` | `v14d_015` | `multi_factor_finance_synthesis` | `channel inventory correction and weak sell-through` | `weak sell-through driving inventory build` ✅ | `channel destocking` ✅ | `watch sell-through and inventory-days normalization` | `sell-through and inventory days` ✅ | `watch sell-through and inventory days` ✅ | `tie` |
| `v14i_003` | `v14d_020` | `analyst_workflow_agent` | `funding-cost and deposit-beta concern` | `deposit competition squeezing funding costs` ✅ | `deposit-cost pressure` ✅ | `verify uninsured-deposit mix or wholesale-funding dependence` | `primary-source capital raise confirmation` ❌ | `check for capital-raise filings` ❌ | `tie` |
| `v14i_004` | `v14d_021` | `cross_source_event_integration` | `positive FDA panel vote improving approval odds` | `favorable FDA panel vote` ✅ | `positive FDA panel vote` ✅ | `short-squeeze amplification remains possible, so verify timing and short interest` | `watch for credible M&A confirmation` ❌ | `watch credible M&A confirmation` ❌ | `tie` |
| `v14i_005` | `v14cpi_001` | `proxy_family_selection` | `financing conditions and mortgage affordability` | `affordability-driven order softness` ✅ | `affordability-driven demand softness` ✅ | `if orders stay weak after financing proxies normalize, demand softness gains weight` | `watch CDS and land/permitting changes` ❌ | `watch builder CDS and debt access` ❌ | `tie` |
| `v14i_006` | `v14cpi_006` | `transmission_supportability` | `valuation-duration and refinancing channel` | `credit-tightening duration derating` ✅ | `credit-spread multiple compression` ✅ | `watch spreads and duration-sensitive peers while company metrics stay intact` | `watch HY OAS and SaaS peer correlation` ✅ | `watch HY OAS and SaaS peers` ✅ | `tie` |
| `v14i_007` | `v14cpi_003` | `proxy_family_selection` | `fuel and input-cost pressure` | `jet fuel cost shock` ✅ | `fuel-cost squeeze` ✅ | `if bookings or unit revenue break while fuel pressure eases` | `watch bookings and unit revenue guidance` ✅ | `watch bookings and unit revenue` ✅ | `tie` |
| `v14i_008` | `v14cpi_004` | `proxy_family_selection` | `duration pressure and financing conditions` | `duration pressure, not product trouble` ✅ | `duration pressure over product trouble` ✅ | `if renewal or churn metrics break while rates and credit stabilize` | `watch NRR/churn and customer losses` ✅ | `guidance cut or churn spike` ✅ | `tie` |
| `v14i_009` | `v14cpi_007` | `transmission_strength_judgment` | `weak near-term pass-through because contracts and cost share limit it` | `limited near-term margin impact` ✅ | `minimal near-term margin hit` ✅ | `verify contract coverage or cost share before promoting the shock` | `verify contract roll-off and availability` ✅ | `contract rollover and supply availability` ✅ | `tie` |

## Per-Family

- `analyst_workflow_agent`: base exact `0/1`, skill exact `0/1`
- `cross_source_event_integration`: base exact `0/1`, skill exact `0/1`
- `multi_factor_finance_synthesis`: base exact `1/1`, skill exact `1/1`
- `proxy_family_selection`: base exact `2/3`, skill exact `2/3`
- `transmission_strength_judgment`: base exact `1/1`, skill exact `1/1`
- `transmission_supportability`: base exact `1/1`, skill exact `1/1`
