# v14 Track I Competing Explanations Results

Full Track I run over `17` cases.

## Scoreboard

- Scoring: `LLM semantic judge (gpt-5.4)`

- Base exact raw: `10/17 = 58.82%`
- Skill exact raw: `15/17 = 88.24%`
- Base primary-only: `16/17 = 94.12%`
- Skill primary-only: `16/17 = 94.12%`
- Base follow-up-only: `11/17 = 64.71%`
- Skill follow-up-only: `16/17 = 94.12%`
- Base exact valid outputs: `17/17`
- Skill exact valid outputs: `17/17`
- Base duration: `0.00s`
- Skill duration: `0.00s`

## Per Case

| Case ID | Source | Family | Canonical primary | Base primary | Skill primary | Canonical follow-up | Base follow-up | Skill follow-up | Exact winner |
|---|---|---|---|---|---|---|---|---|---|
| `v14im_001` | `v14d_013` | `earnings_driver_analysis` | `mix shift into lower-margin hardware amplified by freight` | `hardware mix shift and freight` ✅ | `lower-margin hardware mix shift` ✅ | `watch hardware mix, hardware margin, and freight cost` | `watch mix normalization and freight percent` ✅ | `watch hardware mix and freight percent` ✅ | `tie` |
| `v14im_002` | `v14d_015` | `multi_factor_finance_synthesis` | `channel inventory correction and weak sell-through` | `channel inventory overhang` ✅ | `channel destocking from weak sell-through` ✅ | `watch sell-through and inventory-days normalization` | `watch sell-through and inventory days` ✅ | `watch inventory days and sell-through` ✅ | `tie` |
| `v14im_003` | `v14d_019` | `fresh_event_synthesis` | `freight-rate spike due to canal disruption and rerouting` | `rerouting shock from canal disruption` ✅ | `rerouting-driven freight capacity shock` ✅ | `duration and persistence of rerouting surcharges remain uncertain` | `watch reopening and retail repricing` ✅ | `disruption duration and route normalization` ✅ | `tie` |
| `v14im_004` | `v14d_020` | `analyst_workflow_agent` | `funding-cost and deposit-beta concern` | `deposit squeeze, not raise rumor` ✅ | `deposit-competition funding-cost squeeze` ✅ | `verify uninsured-deposit mix or wholesale-funding dependence` | `check 8-Ks and deposit trends` ❌ | `check filings for capital raise` ❌ | `tie` |
| `v14im_005` | `v14d_021` | `cross_source_event_integration` | `positive FDA panel vote improving approval odds` | `FDA panel win, amplified by shorts` ✅ | `favorable FDA panel vote` ✅ | `short-squeeze amplification remains possible, so verify timing and short interest` | `watch SEC filings for buyout confirmation` ❌ | `watch short-covering and borrow stress` ✅ | `skill` |
| `v14im_006` | `v14cpi_001` | `proxy_family_selection` | `financing conditions and mortgage affordability` | `affordability-driven demand softness` ✅ | `mortgage affordability stress` ✅ | `if orders stay weak after financing proxies normalize, demand softness gains weight` | `watch CDS widening or revolver draws` ❌ | `watch tours and traffic weaken` ✅ | `skill` |
| `v14im_007` | `v14cpi_002` | `proxy_family_selection` | `retail liquidity and alt-beta risk appetite` | `alt-liquidity drain` ✅ | `alt liquidity drain` ✅ | `if project-specific activity breaks while broad alt liquidity normalizes` | `watch BTC/ETH break lower` ❌ | `depth normalization without token rebound` ✅ | `skill` |
| `v14im_008` | `v14cpi_003` | `proxy_family_selection` | `fuel and input-cost pressure` | `jet fuel shock` ✅ | `fuel-cost shock` ✅ | `if bookings or unit revenue break while fuel pressure eases` | `watch bookings and unit revenue roll over` ✅ | `bookings and unit revenue weaken` ✅ | `tie` |
| `v14im_009` | `v14cpi_004` | `proxy_family_selection` | `duration pressure and financing conditions` | `duration and factor pressure` ✅ | `duration and credit pressure` ✅ | `if renewal or churn metrics break while rates and credit stabilize` | `watch guidance cuts or churn rise` ✅ | `NRR/churn deterioration or ARR cut` ✅ | `tie` |
| `v14im_010` | `v14cpi_005` | `bridge_noise_rejection` | `soybean rally is bridge noise` | `soybeans are bridge noise` ✅ | `soybeans are bridge noise` ✅ | `watch freight, packaging resin, palm oil, and cocoa instead` | `watch freight, resin, palm oil, cocoa` ✅ | `freight, resin, palm oil, cocoa` ✅ | `tie` |
| `v14im_011` | `v14cpi_006` | `transmission_supportability` | `valuation-duration and refinancing channel` | `long-duration rerating from tighter credit` ✅ | `credit-spread-driven duration derating` ✅ | `watch spreads and duration-sensitive peers while company metrics stay intact` | `watch HY spreads and SaaS correlation` ✅ | `watch HY OAS and nonbank SaaS peers` ✅ | `tie` |
| `v14im_012` | `v14cpi_007` | `transmission_strength_judgment` | `weak near-term pass-through because contracts and cost share limit it` | `minimal near-term margin impact` ✅ | `limited near-term gross-margin impact` ✅ | `verify contract coverage or cost share before promoting the shock` | `check contract reset and pass-through clauses` ✅ | `verify contract volume coverage and reset timing` ✅ | `tie` |
| `v14im_013` | `v14cpi_008` | `primary_driver_vs_amplifier` | `FDA advisory-panel vote is the primary driver while squeeze dynamics amplify` | `FDA catalyst with squeeze amplification` ✅ | `FDA catalyst with short-squeeze amplification` ✅ | `keep primary driver separate from squeeze amplification` | `M&A rumor unverified; squeeze not primary` ✅ | `M&A rumor unconfirmed; extension attribution uncertain` ✅ | `tie` |
| `v14im_014` | `v14cpi_013` | `pressure_test_design` | `stress financing conditions first` | `test financed-vs-cash conversion` ✅ | `financing-term sensitivity on quote conversion` ✅ | `inspect orders and cancellations` | `approval rates and close timing` ❌ | `watch financed conversion and cycle times` ✅ | `skill` |
| `v14im_015` | `v14cpi_014` | `pressure_test_design` | `stress jet-fuel costs first` | `jet-fuel-only margin stress` ✅ | `jet-fuel cost shock test` ✅ | `inspect unit margin or EPS sensitivity` | `watch close-in yields and bookings` ❌ | `watch CASM and margin guide` ✅ | `skill` |
| `v14im_016` | `v14cpi_015` | `pressure_test_design` | `stress customer inventory and build schedules first` | `customer-destock volume stress` ✅ | `OEM inventory reset probe` ✅ | `inspect shipments and backlog conversion` | `watch inventory days and backlog conversion` ✅ | `watch backlog conversion and call-offs` ✅ | `tie` |
| `v14im_017` | `v14cpi_016` | `pressure_test_design` | `stress incentive-policy generosity first` | `fast-follow-up conversion test` ❌ | `same-market speed-to-lead test` ❌ | `inspect lead-to-booking conversion` | `watch close-rate rebound at flat incentives` ✅ | `watch lead-to-booking conversion rebound` ✅ | `tie` |

## Per-Family

- `analyst_workflow_agent`: base exact `0/1`, skill exact `0/1`
- `bridge_noise_rejection`: base exact `1/1`, skill exact `1/1`
- `cross_source_event_integration`: base exact `0/1`, skill exact `1/1`
- `earnings_driver_analysis`: base exact `1/1`, skill exact `1/1`
- `fresh_event_synthesis`: base exact `1/1`, skill exact `1/1`
- `multi_factor_finance_synthesis`: base exact `1/1`, skill exact `1/1`
- `pressure_test_design`: base exact `1/4`, skill exact `3/4`
- `primary_driver_vs_amplifier`: base exact `1/1`, skill exact `1/1`
- `proxy_family_selection`: base exact `2/4`, skill exact `4/4`
- `transmission_strength_judgment`: base exact `1/1`, skill exact `1/1`
- `transmission_supportability`: base exact `1/1`, skill exact `1/1`
