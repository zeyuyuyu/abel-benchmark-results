# v14 Track I Competing Explanations Results

Full Track I run over `16` cases.

## Scoreboard

- Scoring: `LLM semantic judge (gpt-5.4)`

- Base exact raw: `9/16 = 56.25%`
- Skill exact raw: `7/16 = 43.75%`
- Base primary-only: `13/16 = 81.25%`
- Skill primary-only: `10/16 = 62.50%`
- Base follow-up-only: `10/16 = 62.50%`
- Skill follow-up-only: `10/16 = 62.50%`
- Base exact valid outputs: `16/16`
- Skill exact valid outputs: `16/16`
- Base duration: `712.66s`
- Skill duration: `796.09s`

## Per Case

| Case ID | Source | Family | Canonical primary | Base primary | Skill primary | Canonical follow-up | Base follow-up | Skill follow-up | Exact winner |
|---|---|---|---|---|---|---|---|---|---|
| `v14im2_001` | `v14cpi_013` | `pressure_test_design` | `stress financing conditions first` | `financing approval probe` ✅ | `financing-term relief test` ✅ | `inspect order intake and cancellations` | `approved-quote conversion` ✅ | `quote-to-close conversion by financing status` ✅ | `tie` |
| `v14im2_002` | `v14cpi_013` | `pressure_test_design` | `stress financing conditions first` | `financing approval probe` ✅ | `financing-term relief test` ✅ | `inspect order intake and cancellations` | `approved-quote close rates` ✅ | `close-rate rebound in financed cohorts` ✅ | `tie` |
| `v14im2_003` | `v14cpi_014` | `pressure_test_design` | `stress jet-fuel costs first` | `shock jet fuel costs` ✅ | `shock jet fuel crack first` ✅ | `inspect unit margin or EPS sensitivity` | `next unit revenue print` ❌ | `watch forward bookings` ❌ | `tie` |
| `v14im2_004` | `v14cpi_014` | `pressure_test_design` | `stress jet-fuel costs first` | `shock jet fuel costs` ✅ | `shock jet fuel crack first` ✅ | `inspect unit margin or EPS sensitivity` | `next unit revenue print` ❌ | `watch forward bookings` ❌ | `tie` |
| `v14im2_005` | `v14cpi_015` | `pressure_test_design` | `stress customer inventory and build schedules first` | `OEM order pushouts` ✅ | `units versus lithium-linked pricing` ❌ | `inspect shipments and backlog conversion` | `OEM sell-through and inventory days` ❌ | `sell-through and inventory days` ❌ | `tie` |
| `v14im2_006` | `v14cpi_015` | `pressure_test_design` | `stress customer inventory and build schedules first` | `OEM order-release cadence` ✅ | `units versus lithium-linked pricing` ❌ | `inspect shipments and backlog conversion` | `wholesale versus retail sell-through` ✅ | `retail sell-through` ❌ | `base` |
| `v14im2_007` | `v14cpi_016` | `pressure_test_design` | `stress incentive-policy generosity first` | `follow-up latency split` ❌ | `lead-to-appointment by response-time cohort` ❌ | `inspect lead-to-booking conversion` | `lead-to-set conversion` ❌ | `appointment-to-booking on prompt-contact leads` ✅ | `tie` |
| `v14im2_008` | `v14cpi_016` | `pressure_test_design` | `stress incentive-policy generosity first` | `follow-up latency split` ❌ | `lead-to-appointment by response-time cohort` ❌ | `inspect lead-to-booking conversion` | `quote-to-close conversion` ✅ | `appointment-to-booking on prompt-contact leads` ✅ | `tie` |
| `v14im2_009` | `v14cpi_001` | `proxy_family_selection` | `financing conditions and mortgage affordability` | `mortgage affordability friction` ✅ | `mortgage affordability friction` ✅ | `orders stay weak even if rate and credit proxies normalize` | `if traffic and tours roll over` ❌ | `traffic and tours roll over` ❌ | `tie` |
| `v14im2_010` | `v14cpi_001` | `proxy_family_selection` | `orders stay weak even after financing proxies normalize` | `top-of-funnel demand must roll over` ❌ | `top-of-funnel weakens despite stable rates` ❌ | `inspect order intake and cancellations after financing normalization` | `model-home visits and web traffic` ❌ | `model-home visits stay weak` ❌ | `tie` |
| `v14im2_011` | `v14cpi_002` | `proxy_family_selection` | `retail liquidity and alt-beta risk appetite` | `broad alt-liquidity drain` ✅ | `broad alt-liquidity drain` ✅ | `project-specific activity breaks while broad alt liquidity normalizes` | `watch DAU/fees diverge from peers` ✅ | `DAU/fees break versus peers` ✅ | `tie` |
| `v14im2_012` | `v14cpi_002` | `proxy_family_selection` | `project-specific activity breaks while broad alt liquidity normalizes` | `token-specific DAU/fees break` ✅ | `token-specific DAU/fees rollover` ✅ | `compare project activity against broader alt-liquidity normalization` | `compare against gaming-alt peers` ✅ | `compare with gaming-token peers` ✅ | `tie` |
| `v14im2_013` | `v14cpi_006` | `transmission_supportability` | `valuation-duration and refinancing channel` | `duration de-rate via tighter credit` ✅ | `credit-tightening duration de-rate` ✅ | `watch spreads and duration-sensitive peers while company metrics stay intact` | `watch HY spreads versus software basket` ✅ | `watch HY OAS versus software basket` ✅ | `tie` |
| `v14im2_014` | `v14cpi_006` | `transmission_supportability` | `spreads widen and duration-sensitive peers sell off together` | `peer software tracks spreads, not disclosures` ✅ | `basket co-move with clean liquidity` ❌ | `company metrics stay intact while you watch HY spreads and duration-sensitive peers` | `guidance and liquidity stay intact` ✅ | `liquidity and guidance stay intact` ✅ | `base` |
| `v14im2_015` | `v14cpi_008` | `primary_driver_vs_amplifier` | `FDA advisory-panel vote is the primary driver` | `FDA vote primary, squeeze amplifier` ✅ | `FDA vote trigger, squeeze amplifier` ✅ | `keep the primary catalyst separate from squeeze amplification` | `frame short-covering as secondary amplification` ✅ | `describe squeeze as secondary boost` ✅ | `tie` |
| `v14im2_016` | `v14cpi_008` | `primary_driver_vs_amplifier` | `FDA advisory-panel vote is the primary driver while squeeze dynamics amplify` | `AdCom-driven rally, short-covering amplified` ✅ | `AdCom win drove move, shorts amplified` ✅ | `keep the primary catalyst separate from squeeze amplification` | `squeeze narrative stays secondary` ✅ | `keep short-covering secondary` ✅ | `tie` |

## Per-Family

- `pressure_test_design`: base exact `3/8`, skill exact `2/8`
- `primary_driver_vs_amplifier`: base exact `2/2`, skill exact `2/2`
- `proxy_family_selection`: base exact `2/4`, skill exact `2/4`
- `transmission_supportability`: base exact `2/2`, skill exact `1/2`
