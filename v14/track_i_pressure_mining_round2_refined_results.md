# v14 Track I Competing Explanations Results

Full Track I run over `10` cases.

## Scoreboard

- Scoring: `LLM semantic judge (gpt-5.4)`

- Base exact raw: `1/10 = 10.00%`
- Skill exact raw: `1/10 = 10.00%`
- Base primary-only: `1/10 = 10.00%`
- Skill primary-only: `2/10 = 20.00%`
- Base follow-up-only: `4/10 = 40.00%`
- Skill follow-up-only: `4/10 = 40.00%`
- Base exact valid outputs: `10/10`
- Skill exact valid outputs: `10/10`
- Base duration: `518.14s`
- Skill duration: `467.56s`

## Per Case

| Case ID | Source | Family | Canonical primary | Base primary | Skill primary | Canonical follow-up | Base follow-up | Skill follow-up | Exact winner |
|---|---|---|---|---|---|---|---|---|---|
| `v14im2r_001` | `v14cpi_014` | `pressure_test_design` | `stress jet-fuel costs first` | `fare pass-through test` ❌ | `fare pass-through test` ❌ | `inspect unit margin or EPS sensitivity` | `booking elasticity and load factor` ❌ | `watch close-in booking curve` ❌ | `tie` |
| `v14im2r_002` | `v14cpi_014` | `pressure_test_design` | `stress jet-fuel costs first` | `fare pass-through test` ❌ | `fare pass-through test` ❌ | `inspect unit margin or EPS sensitivity` | `booking elasticity and load factor` ❌ | `watch close-in booking curve` ❌ | `tie` |
| `v14im2r_003` | `v14cpi_014` | `pressure_test_design` | `stress jet-fuel costs first` | `forward bookings stress` ❌ | `jet fuel crack stress` ✅ | `inspect unit margin or EPS sensitivity` | `watch unit revenue` ❌ | `watch fuel CASM` ❌ | `tie` |
| `v14im2r_004` | `v14cpi_015` | `pressure_test_design` | `stress customer inventory and build schedules first` | `customer inventory stress` ✅ | `customer inventory reset stress` ✅ | `inspect shipments and backlog conversion` | `watch backlog conversion` ✅ | `watch backlog conversion` ✅ | `tie` |
| `v14im2r_005` | `v14cpi_015` | `pressure_test_design` | `stress customer inventory and build schedules first` | `volume-price bridge on shipments` ❌ | `unit shipments versus lithium-linked ASP` ❌ | `inspect shipments and backlog conversion` | `OEM sell-through and inventory days` ❌ | `OEM sell-through and inventory days` ❌ | `tie` |
| `v14im2r_006` | `v14cpi_015` | `pressure_test_design` | `stress customer inventory and build schedules first` | `volume-price bridge on shipments` ❌ | `unit shipments versus lithium-linked ASP` ❌ | `inspect shipments and backlog conversion` | `OEM wholesales versus sell-through` ❌ | `OEM sell-through and inventory days` ❌ | `tie` |
| `v14im2r_007` | `v14cpi_016` | `pressure_test_design` | `stress incentive-policy generosity first` | `same-state fast-follow-up test` ❌ | `same-incentive conversion by follow-up speed` ❌ | `inspect lead-to-booking conversion` | `lead-to-booking conversion lift` ✅ | `new-lead booking conversion recovery` ✅ | `tie` |
| `v14im2r_008` | `v14cpi_016` | `pressure_test_design` | `stress incentive-policy generosity first` | `same-state fast-follow-up test` ❌ | `same-incentive conversion by follow-up speed` ❌ | `inspect lead-to-booking conversion` | `lead-to-booking conversion lift` ✅ | `new-lead booking conversion recovery` ✅ | `tie` |
| `v14im2r_009` | `v14cpi_016` | `pressure_test_design` | `stress incentive-policy generosity first` | `same-market follow-up-lag split` ❌ | `same-state follow-up-speed cohort split` ❌ | `inspect lead-to-booking conversion` | `lead-to-booking by response-time bucket` ✅ | `lead-to-booking by response-lag bucket` ✅ | `tie` |
| `v14im2r_010` | `v14cpi_013` | `pressure_test_design` | `stress financing conditions first` | `financed-vs-cash close-rate split` ❌ | `financed-vs-cash quote-to-close split` ❌ | `inspect order intake and cancellations` | `quote-to-close lag by financing type` ❌ | `quote-to-close days by financing cohort` ❌ | `tie` |

## Per-Family

- `pressure_test_design`: base exact `1/10`, skill exact `1/10`
