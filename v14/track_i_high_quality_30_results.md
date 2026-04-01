# v14 Track I Competing Explanations Results

Full Track I run over `30` cases.

## Scoreboard

- Scoring: `LLM semantic judge (gpt-5.4)`

- Base exact raw: `19/30 = 63.33%`
- Skill exact raw: `20/30 = 66.67%`
- Base primary-only: `26/30 = 86.67%`
- Skill primary-only: `28/30 = 93.33%`
- Base follow-up-only: `20/30 = 66.67%`
- Skill follow-up-only: `21/30 = 70.00%`
- Base exact valid outputs: `30/30`
- Skill exact valid outputs: `30/30`
- Base duration: `906.46s`
- Skill duration: `794.32s`

## Per Case

| Case ID | Source | Family | Canonical primary | Base primary | Skill primary | Canonical follow-up | Base follow-up | Skill follow-up | Exact winner |
|---|---|---|---|---|---|---|---|---|---|
| `v14im_001` | `v14d_013` | `earnings_driver_analysis` | `mix shift into lower-margin hardware amplified by freight` | `hardware mix shift and freight` ✅ | `hardware mix shift and freight spike` ✅ | `watch hardware mix, hardware margin, and freight cost` | `watch mix normalization and freight percent` ✅ | `watch hardware mix and freight rate` ✅ | `tie` |
| `v14im_002` | `v14d_015` | `multi_factor_finance_synthesis` | `channel inventory correction and weak sell-through` | `channel destocking from weak sell-through` ✅ | `channel destocking from weak sell-through` ✅ | `watch sell-through and inventory-days normalization` | `watch inventory days and sell-through` ✅ | `watch sell-through and inventory days` ✅ | `tie` |
| `v14im_003` | `v14d_019` | `fresh_event_synthesis` | `freight-rate spike due to canal disruption and rerouting` | `shipping rerouting and surcharge shock` ✅ | `canal-rerouting freight shock` ✅ | `duration and persistence of rerouting surcharges remain uncertain` | `watch route normalization and retail repricing` ✅ | `watch disruption duration and normalization` ✅ | `tie` |
| `v14im_004` | `v14d_020` | `analyst_workflow_agent` | `funding-cost and deposit-beta concern` | `deposit-competition funding pressure` ✅ | `deposit-cost pressure, not raise rumor` ✅ | `verify uninsured-deposit mix or wholesale-funding dependence` | `check deposits and any 8-K` ❌ | `verify any primary-source raise filing` ❌ | `tie` |
| `v14im_005` | `v14d_021` | `cross_source_event_integration` | `positive FDA panel vote improving approval odds` | `FDA panel de-risking` ✅ | `positive AdCom vote` ✅ | `short-squeeze amplification remains possible, so verify timing and short interest` | `short squeeze; watch borrow and covering` ✅ | `watch borrow fees and short-covering` ✅ | `tie` |
| `v14im_006` | `v14cpi_001` | `proxy_family_selection` | `financing conditions and mortgage affordability` | `mortgage-rate affordability pressure` ✅ | `rate-driven affordability softness` ✅ | `if orders stay weak after financing proxies normalize, demand softness gains weight` | `watch CDS and liquidity actions` ❌ | `watch peer CDS and land pullbacks` ❌ | `tie` |
| `v14im_007` | `v14cpi_002` | `proxy_family_selection` | `retail liquidity and alt-beta risk appetite` | `alt liquidity drain` ✅ | `alt-liquidity drain` ✅ | `if project-specific activity breaks while broad alt liquidity normalizes` | `watch depth recovery versus BTC/ETH stability` ❌ | `watch BTC/ETH breadth turn negative` ❌ | `tie` |
| `v14im_008` | `v14cpi_003` | `proxy_family_selection` | `fuel and input-cost pressure` | `fuel-cost shock` ✅ | `fuel-cost shock` ✅ | `if bookings or unit revenue break while fuel pressure eases` | `watch forward bookings and unit revenue` ✅ | `watch bookings or unit revenue soften` ✅ | `tie` |
| `v14im_009` | `v14cpi_004` | `proxy_family_selection` | `duration pressure and financing conditions` | `broad duration/risk-off` ✅ | `duration-led factor de-rate` ✅ | `if renewal or churn metrics break while rates and credit stabilize` | `ARR guide cut or churn jump` ✅ | `guidance cut or churn spike` ✅ | `tie` |
| `v14im_010` | `v14cpi_005` | `bridge_noise_rejection` | `soybean rally is bridge noise` | `soybeans` ✅ | `soybeans are bridge noise` ✅ | `watch freight, packaging resin, palm oil, and cocoa instead` | `freight, resin, palm oil, cocoa` ✅ | `watch freight, resin, palm oil, cocoa` ✅ | `tie` |
| `v14im_011` | `v14cpi_006` | `transmission_supportability` | `valuation-duration and refinancing channel` | `tighter financial conditions de-rating` ✅ | `credit-spread risk-off derating` ✅ | `watch spreads and duration-sensitive peers while company metrics stay intact` | `verify bank and SMB customer mix` ❌ | `check customer exposure to regional banks` ❌ | `tie` |
| `v14im_012` | `v14cpi_007` | `transmission_strength_judgment` | `weak near-term pass-through because contracts and cost share limit it` | `minimal near-term margin impact` ✅ | `minimal near-term margin impact` ✅ | `verify contract coverage or cost share before promoting the shock` | `check contract coverage and reset terms` ✅ | `check volume protections and rollover pricing` ✅ | `tie` |
| `v14im_013` | `v14cpi_008` | `primary_driver_vs_amplifier` | `FDA advisory-panel vote is the primary driver while squeeze dynamics amplify` | `FDA panel win, squeeze amplified` ✅ | `FDA catalyst with short-squeeze amplification` ✅ | `keep primary driver separate from squeeze amplification` | `M&A rumor unconfirmed, secondary` ❌ | `keep M&A rumor explicitly unconfirmed` ❌ | `tie` |
| `v14im_014` | `v14cpi_013` | `pressure_test_design` | `stress financing conditions first` | `compare financed vs cash conversion` ✅ | `quote-to-close by financing dependence` ✅ | `inspect orders and cancellations` | `watch approval rates and days-to-close` ❌ | `check approval rates and close timing` ❌ | `tie` |
| `v14im_015` | `v14cpi_014` | `pressure_test_design` | `stress jet-fuel costs first` | `fare pass-through test` ❌ | `fuel-cost stress with bookings fixed` ✅ | `inspect unit margin or EPS sensitivity` | `watch close-in bookings and yields` ❌ | `watch close-in yields and PRASM` ❌ | `tie` |
| `v14im_016` | `v14cpi_015` | `pressure_test_design` | `stress customer inventory and build schedules first` | `ASP-versus-volume bridge` ❌ | `inventory-reset stress with lithium fixed` ✅ | `inspect shipments and backlog conversion` | `watch backlog conversion and OEM inventory days` ✅ | `watch backlog conversion and OEM order releases` ✅ | `skill` |
| `v14im_017` | `v14cpi_016` | `pressure_test_design` | `stress incentive-policy generosity first` | `conversion by response-time cohort` ❌ | `same-incentive follow-up-speed test` ❌ | `inspect lead-to-booking conversion` | `close-rate after response-time normalizes` ❌ | `watch lead-to-booking conversion` ✅ | `tie` |
| `v14im_018` | `v14cpi_009` | `bundled_intervention_supportability` | `no, the price cut is bundled with the sales-comp rewrite in the same weak regions` | `price cut not isolatable` ✅ | `no, bundled price-and-comp treatment` ✅ | `targeted rollout and simultaneous commercial intervention contaminate attribution` | `simultaneous comp-plan rewrite contamination` ✅ | `simultaneous comp-plan contamination` ✅ | `tie` |
| `v14im_019` | `v14cpi_010` | `targeted_rollout_design_choice` | `matched or staggered diff-in-diff event study` | `pre-trend-checked difference-in-differences` ✅ | `difference-in-differences with pre-trends` ✅ | `targeted rollout to high-failure plants and regression to the mean` | `regression to the mean` ✅ | `regression to the mean` ✅ | `tie` |
| `v14im_020` | `v14cpi_011` | `selection_bias_supportability` | `no, selection into prequalified users blocks clean attribution` | `no causal lift estimate` ✅ | `selection-biased, not causal` ✅ | `latent purchase propensity was already higher before treatment` | `selection on unobserved spending appetite` ✅ | `unobserved purchase-propensity confounding` ✅ | `tie` |
| `v14im_021` | `v14cpi_012` | `simultaneous_operations_change` | `no, temporary staffing changed in the same window` | `cannot isolate expedite policy` ✅ | `no clean expedite attribution` ✅ | `the simultaneous staffing change contaminates the effect` | `temp staffing and overtime changes` ✅ | `temp staffing and overtime changes` ✅ | `tie` |
| `v14im_022` | `v14d_009` | `finance_table_causal_interpretation` | `no, pricing and input-cost relief both mattered` | `input-cost hedge, not pricing alone` ✅ | `pricing alone not sufficient` ✅ | `include input-cost relief alongside realized price` | `include commodity-hedge cost relief` ✅ | `hedge-driven input-cost reduction` ✅ | `tie` |
| `v14im_023` | `v14d_010` | `event_chain_attribution` | `distribution-center scanner outage` | `DC scanner outage bottleneck` ✅ | `regional DC scanner outage` ✅ | `weather and port disruption were upstream context, not the final trigger` | `typhoon and port delays secondary` ✅ | `typhoon and port delays secondary` ✅ | `tie` |
| `v14im_024` | `v14d_011` | `causal_vs_temporal_disambiguation` | `morning corporate actions were the driver, not the later interview` | `buyback and guidance raise` ✅ | `buyback and guidance raise` ✅ | `do not over-credit the later interview because it added no new information` | `midday CEO TV recap` ✅ | `midday CEO TV appearance` ✅ | `tie` |
| `v14im_025` | `v14d_012` | `narrative_counterfactual` | `deliveries improve but still finish below plan` | `roughly 14% below plan` ✅ | `about 14% below plan` ✅ | `the later rail disruption would still hold exports back` | `rain-hit rail departures` ✅ | `heavy-rain rail disruption` ✅ | `tie` |
| `v14im_026` | `v14d_014` | `marketing_spend_intervention` | `qualified lead volume falls with only partial efficiency offset` | `near-term volume drop` ✅ | `near-term acquisition volume drop` ✅ | `organic substitution is incomplete in the packet` | `weak organic replacement` ✅ | `only 25% organic replacement` ✅ | `tie` |
| `v14im_027` | `v14d_016` | `manufacturing_sensor_confounder` | `no clean causal claim because maintenance timing and line selection moved too` | `maintenance confound, not temperature alone` ❌ | `maintenance-confounded defect drop` ❌ | `control for maintenance status, line id, and throughput` | `control maintenance timing and throughput` ❌ | `control maintenance timing and throughput` ❌ | `tie` |
| `v14im_028` | `v14d_017` | `staggered_rollout_policy` | `staggered diff-in-diff event study` | `staggered difference-in-differences event study` ✅ | `staggered DiD event study` ✅ | `parallel trends, plus anticipation or spillover risk` | `parallel trends and no anticipation` ✅ | `parallel trends and no anticipation` ✅ | `tie` |
| `v14im_029` | `v14d_008` | `simpsons_paradox_causal_read` | `segment mix shift creates a Simpson's paradox` | `expert-heavy composition shift` ✅ | `composition shift from expert-heavy treatment` ✅ | `within both novice and expert strata the treatment underperformed` | `state aggregate lift is mix-driven` ❌ | `aggregate lift is mix-driven, not causal` ❌ | `tie` |
| `v14im_030` | `v14d_007` | `post_treatment_control_trap` | `no, three-day engagement is post-treatment` | `no, post-treatment mediator` ✅ | `no, post-treatment bad control` ✅ | `conditioning on a post-treatment metric biases the total effect` | `engagement is downstream of treatment` ✅ | `conditions on a downstream mediator` ✅ | `tie` |

## Per-Family

- `analyst_workflow_agent`: base exact `0/1`, skill exact `0/1`
- `bridge_noise_rejection`: base exact `1/1`, skill exact `1/1`
- `bundled_intervention_supportability`: base exact `1/1`, skill exact `1/1`
- `causal_vs_temporal_disambiguation`: base exact `1/1`, skill exact `1/1`
- `cross_source_event_integration`: base exact `1/1`, skill exact `1/1`
- `earnings_driver_analysis`: base exact `1/1`, skill exact `1/1`
- `event_chain_attribution`: base exact `1/1`, skill exact `1/1`
- `finance_table_causal_interpretation`: base exact `1/1`, skill exact `1/1`
- `fresh_event_synthesis`: base exact `1/1`, skill exact `1/1`
- `manufacturing_sensor_confounder`: base exact `0/1`, skill exact `0/1`
- `marketing_spend_intervention`: base exact `1/1`, skill exact `1/1`
- `multi_factor_finance_synthesis`: base exact `1/1`, skill exact `1/1`
- `narrative_counterfactual`: base exact `1/1`, skill exact `1/1`
- `post_treatment_control_trap`: base exact `1/1`, skill exact `1/1`
- `pressure_test_design`: base exact `0/4`, skill exact `1/4`
- `primary_driver_vs_amplifier`: base exact `0/1`, skill exact `0/1`
- `proxy_family_selection`: base exact `2/4`, skill exact `2/4`
- `selection_bias_supportability`: base exact `1/1`, skill exact `1/1`
- `simpsons_paradox_causal_read`: base exact `0/1`, skill exact `0/1`
- `simultaneous_operations_change`: base exact `1/1`, skill exact `1/1`
- `staggered_rollout_policy`: base exact `1/1`, skill exact `1/1`
- `targeted_rollout_design_choice`: base exact `1/1`, skill exact `1/1`
- `transmission_strength_judgment`: base exact `1/1`, skill exact `1/1`
- `transmission_supportability`: base exact `0/1`, skill exact `0/1`
