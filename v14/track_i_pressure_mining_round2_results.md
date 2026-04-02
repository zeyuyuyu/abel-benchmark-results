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

## Case Overview

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

## Full Cases

### v14im2_001 — Which First Pressure Test Separates Financing Stress From Demand Softness?

- Source case: `v14cpi_013`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A distributor note leaves two live stories on the table, and the task is to pick the first stress lever that would most efficiently separate them.

Primary question: What is the first clean arbiter here?
Follow-up question: What downstream readout do you inspect once you run it?

Evidence packet:
- Agent brief (document_excerpt): Rate-sensitive customer verticals have slowed, but service attach and installed-base usage remain stable. Credit spreads widened and management said quote activity was healthy but close timing stretched.
- Commercial snapshot (table): New orders: -4%. Cancellations: +2 points. Service attach: flat. Installed-base usage: flat. HY OAS: +62 bps. Accounts receivable days: +4 days.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `stress financing conditions first`
- Canonical follow-up: `inspect order intake and cancellations`
Evidence summary:
- two live stories remain: financing friction versus genuine demand softness
- the clean separation comes from shocking financing conditions and then reading the downstream order channel
Common failure modes:
- staying at approval-rate or close-timing diagnostics instead of reading order outcomes
- choosing a probe that does not actually separate financing from demand
Canonical answer object:
```json
{
  "label": "B",
  "stress_target": "financing_conditions",
  "readout": "order_intake_and_cancellations"
}
```

Model replies:
- Base primary: `financing approval probe` ✅
- Base follow-up: `approved-quote conversion` ✅
- Skill primary: `financing-term relief test` ✅
- Skill follow-up: `quote-to-close conversion by financing status` ✅

Judge notes: Both primaries press financing conditions; both follow-ups use downstream close/conversion outcomes, which are acceptable order-channel proxies.

### v14im2_002 — Which First Pressure Test Separates Financing Stress From Demand Softness?

- Source case: `v14cpi_013`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A distributor note leaves two live stories on the table, and the task is to pick the first stress lever that would most efficiently separate them.

Primary question: If you had one first probe before writing the note, where do you press?
Follow-up question: What customer outcome actually separates the stories after that probe?

Evidence packet:
- Agent brief (document_excerpt): Rate-sensitive customer verticals have slowed, but service attach and installed-base usage remain stable. Credit spreads widened and management said quote activity was healthy but close timing stretched.
- Commercial snapshot (table): New orders: -4%. Cancellations: +2 points. Service attach: flat. Installed-base usage: flat. HY OAS: +62 bps. Accounts receivable days: +4 days.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `stress financing conditions first`
- Canonical follow-up: `inspect order intake and cancellations`
Evidence summary:
- healthy quote activity with stretched close timing keeps financing friction live
- orders and cancellations are the closest downstream discriminators once financing is stressed
Common failure modes:
- watching financing-process metrics without reading through to orders and cancellations
- jumping straight to margin or receivables despite the live uncertainty being commercial demand
Canonical answer object:
```json
{
  "label": "B",
  "stress_target": "financing_conditions",
  "readout": "order_intake_and_cancellations"
}
```

Model replies:
- Base primary: `financing approval probe` ✅
- Base follow-up: `approved-quote close rates` ✅
- Skill primary: `financing-term relief test` ✅
- Skill follow-up: `close-rate rebound in financed cohorts` ✅

Judge notes: Approval or term-relief probes both fit the financing-condition test, and close-rate/order conversion in financed cohorts is a concrete downstream arbiter.

### v14im2_003 — Fuel Shock Or Demand Weakness: Which Probe Comes First?

- Source case: `v14cpi_014`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

Scenario:
An airline packet leaves cost shock and demand weakness as competing stories, and the task is to choose the first clean pressure test.

Primary question: What lever would you shock first to separate fuel pressure from demand weakness?
Follow-up question: What readout should settle it once you run that stress?

Evidence packet:
- Agent brief (document_excerpt): The stock sold off with energy markets. Forward bookings and capacity plans held steady. Analysts want the first probe that would most quickly separate cost pressure from true demand deterioration.
- Sector snapshot (table): Jet fuel crack: +18%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue: flat. FX: flat.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `stress jet-fuel costs first`
- Canonical follow-up: `inspect unit margin or EPS sensitivity`
Evidence summary:
- forward bookings and unit revenue are stable while fuel moves sharply
- the cleanest first arbiter is the cost lever, with margin or EPS as the direct downstream readout
Common failure modes:
- switching to a fare or demand probe before testing the cost shock
- watching revenue metrics instead of the direct margin or EPS consequence of fuel stress
Canonical answer object:
```json
{
  "label": "A",
  "stress_target": "jet_fuel_costs",
  "readout": "unit_margin_or_eps_sensitivity"
}
```

Model replies:
- Base primary: `shock jet fuel costs` ✅
- Base follow-up: `next unit revenue print` ❌
- Skill primary: `shock jet fuel crack first` ✅
- Skill follow-up: `watch forward bookings` ❌

Judge notes: Both primaries correctly shock the fuel-cost lever; the follow-ups are wrong because revenue/bookings are not the direct margin or EPS readout.

### v14im2_004 — Fuel Shock Or Demand Weakness: Which Probe Comes First?

- Source case: `v14cpi_014`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

Scenario:
An airline packet leaves cost shock and demand weakness as competing stories, and the task is to choose the first clean pressure test.

Primary question: What is the cleanest first arbiter for the airline selloff?
Follow-up question: What number matters most once you run that stress?

Evidence packet:
- Agent brief (document_excerpt): The stock sold off with energy markets. Forward bookings and capacity plans held steady. Analysts want the first probe that would most quickly separate cost pressure from true demand deterioration.
- Sector snapshot (table): Jet fuel crack: +18%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue: flat. FX: flat.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `stress jet-fuel costs first`
- Canonical follow-up: `inspect unit margin or EPS sensitivity`
Evidence summary:
- the packet already leaves demand-side evidence mostly intact
- fuel-cost pressure should be challenged first, then judged on the earnings bridge rather than on bookings chatter
Common failure modes:
- choosing a demand-side arbiter despite stable booking evidence
- tracking close-in yields or PRASM when the canonical downstream readout is margin or EPS sensitivity
Canonical answer object:
```json
{
  "label": "A",
  "stress_target": "jet_fuel_costs",
  "readout": "unit_margin_or_eps_sensitivity"
}
```

Model replies:
- Base primary: `shock jet fuel costs` ✅
- Base follow-up: `next unit revenue print` ❌
- Skill primary: `shock jet fuel crack first` ✅
- Skill follow-up: `watch forward bookings` ❌

Judge notes: Both primaries stay on fuel-cost stress; both follow-ups miss the canonical earnings-bridge readout of unit margin or EPS sensitivity.

### v14im2_005 — EV Supplier Drop: Lithium Pass-Through Or Customer Inventory Reset?

- Source case: `v14cpi_015`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `0/2`

Scenario:
A supplier stock weakens while both upstream commodity and downstream customer signals are moving, and the analyst must pick the first separating probe.

Primary question: What first probe most directly tests inventory reset over lithium pass-through?
Follow-up question: What readout deserves the most weight right after?

Evidence packet:
- Agent brief (document_excerpt): Lithium prices softened, but customer inventory days also rose across two major OEMs. The supplier guides to softer near-term shipments without changing long-run content assumptions.
- Supplier snapshot (table): Lithium spot: -14%. Customer inventory days: +11 days. OEM production schedules: trimmed for next quarter. Supplier gross-margin guide: only modestly lower. Backlog conversion: slowing.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `stress customer inventory and build schedules first`
- Canonical follow-up: `inspect shipments and backlog conversion`
Evidence summary:
- customer inventory days and OEM schedules moved in the same direction as the shipment softness
- shipments and backlog conversion are the most direct downstream readouts of an inventory-reset story
Common failure modes:
- defaulting to the flashier commodity move instead of the downstream shipment path
- using a generic ASP-versus-volume bridge instead of stressing customer inventory and build schedules
Canonical answer object:
```json
{
  "label": "B",
  "stress_target": "customer_inventory_reset",
  "readout": "shipments_and_backlog_conversion"
}
```

Model replies:
- Base primary: `OEM order pushouts` ✅
- Base follow-up: `OEM sell-through and inventory days` ❌
- Skill primary: `units versus lithium-linked pricing` ❌
- Skill follow-up: `sell-through and inventory days` ❌

Judge notes: Base primary matches the OEM schedule/inventory-reset probe; follow-ups miss the shipment/backlog arbiter, and skill stays on lithium pricing.

### v14im2_006 — EV Supplier Drop: Lithium Pass-Through Or Customer Inventory Reset?

- Source case: `v14cpi_015`
- Family: `pressure_test_design`
- Exact winner: `base`
- Base exact: `correct`
- Skill exact: `incorrect`
- Base field score: `2/2`
- Skill field score: `0/2`

Scenario:
A supplier stock weakens while both upstream commodity and downstream customer signals are moving, and the analyst must pick the first separating probe.

Primary question: Where would you press first if you wanted the fastest separation of the two stories?
Follow-up question: Which downstream number actually arbitrates after that?

Evidence packet:
- Agent brief (document_excerpt): Lithium prices softened, but customer inventory days also rose across two major OEMs. The supplier guides to softer near-term shipments without changing long-run content assumptions.
- Supplier snapshot (table): Lithium spot: -14%. Customer inventory days: +11 days. OEM production schedules: trimmed for next quarter. Supplier gross-margin guide: only modestly lower. Backlog conversion: slowing.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `stress customer inventory and build schedules first`
- Canonical follow-up: `inspect shipments and backlog conversion`
Evidence summary:
- modest margin-guide change does not support a strong lithium pass-through thesis
- the shipment path is more decision-relevant than commodity headlines for this packet
Common failure modes:
- treating lithium as the main story without checking whether backlog conversion is already slowing
- answering with OEM inventory days alone instead of the shipment and backlog readout that follows from the stress
Canonical answer object:
```json
{
  "label": "B",
  "stress_target": "customer_inventory_reset",
  "readout": "shipments_and_backlog_conversion"
}
```

Model replies:
- Base primary: `OEM order-release cadence` ✅
- Base follow-up: `wholesale versus retail sell-through` ✅
- Skill primary: `units versus lithium-linked pricing` ❌
- Skill follow-up: `retail sell-through` ❌

Judge notes: Base primary fits the customer schedule stress, and wholesale versus retail sell-through is a valid downstream shipment-path arbiter; skill remains on lithium/sell-through.

### v14im2_007 — Residential Solar Miss: Policy Step-Down Or Sales Execution?

- Source case: `v14cpi_016`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `0/2`
- Skill field score: `1/2`

Scenario:
The packet leaves policy and execution stories both live, and the evaluation asks for the cleanest first probe to challenge the leading thesis.

Primary question: What first probe most directly challenges the policy step-down thesis?
Follow-up question: What funnel readout matters once you run it?

Evidence packet:
- Agent brief (document_excerpt): Order volume weakened after a state incentive step-down, but channel checks also mention elevated rep turnover and slower lead follow-up times.
- Sales funnel snapshot (table): Lead volume: -3%. Lead-to-booking conversion: -16%. Incentive value: -22%. Sales-rep turnover: +8 points. Follow-up time: slower by 1.4 days.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `stress incentive-policy generosity first`
- Canonical follow-up: `inspect lead-to-booking conversion`
Evidence summary:
- policy generosity fell more than top-of-funnel lead volume, while conversion broke sharply
- lead-to-booking conversion is the key downstream readout once incentive economics are stressed
Common failure modes:
- switching to a sales-execution probe before challenging the policy thesis directly
- watching rep response-time diagnostics instead of the incentive-linked conversion step
Canonical answer object:
```json
{
  "label": "A",
  "stress_target": "incentive_policy_generosity",
  "readout": "lead_to_booking_conversion"
}
```

Model replies:
- Base primary: `follow-up latency split` ❌
- Base follow-up: `lead-to-set conversion` ❌
- Skill primary: `lead-to-appointment by response-time cohort` ❌
- Skill follow-up: `appointment-to-booking on prompt-contact leads` ✅

Judge notes: Both primaries are execution-first rather than policy-generosity probes. Base follow-up stays too early in the funnel; skill follow-up still points to booking conversion.

### v14im2_008 — Residential Solar Miss: Policy Step-Down Or Sales Execution?

- Source case: `v14cpi_016`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

Scenario:
The packet leaves policy and execution stories both live, and the evaluation asks for the cleanest first probe to challenge the leading thesis.

Primary question: If you want one first arbiter between policy economics and execution slippage, what is it?
Follow-up question: What downstream conversion readout earns the most weight after that?

Evidence packet:
- Agent brief (document_excerpt): Order volume weakened after a state incentive step-down, but channel checks also mention elevated rep turnover and slower lead follow-up times.
- Sales funnel snapshot (table): Lead volume: -3%. Lead-to-booking conversion: -16%. Incentive value: -22%. Sales-rep turnover: +8 points. Follow-up time: slower by 1.4 days.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `stress incentive-policy generosity first`
- Canonical follow-up: `inspect lead-to-booking conversion`
Evidence summary:
- the packet leaves both policy and execution stories live, but the leading thesis is policy step-down
- the right follow-through is to inspect conversion, not just activity or response time
Common failure modes:
- overweighting rep-turnover anecdotes instead of directly testing incentive economics
- staying in process metrics rather than the conversion step that separates the stories
Canonical answer object:
```json
{
  "label": "A",
  "stress_target": "incentive_policy_generosity",
  "readout": "lead_to_booking_conversion"
}
```

Model replies:
- Base primary: `follow-up latency split` ❌
- Base follow-up: `quote-to-close conversion` ✅
- Skill primary: `lead-to-appointment by response-time cohort` ❌
- Skill follow-up: `appointment-to-booking on prompt-contact leads` ✅

Judge notes: Primaries stay on response-time execution. Both follow-ups name concrete downstream conversion reads close enough to the booking-conversion arbiter.

### v14im2_009 — Homebuilder Miss: Funding Stress Or Demand Softness?

- Source case: `v14cpi_001`
- Family: `proxy_family_selection`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

Scenario:
A morning note combines mortgage data, builder credit signals, order metrics, and website activity after a homebuilder stock selloff.

Primary question: What is still the cleaner first read for the homebuilder move?
Follow-up question: What condition would make you revisit that view for real?

Evidence packet:
- Morning note (document_excerpt): The stock fell 11% after management guided to lower near-term orders. Analysts noted no major land or permitting update. Channel checks described buyer hesitation around monthly payments rather than reduced tour activity.
- Market and operating snapshot (table): 30-year mortgage rate: +55 bps over 6 weeks. Mortgage applications: -12%. Builder CDS: +38 bps. Website traffic: -1%. Model-home visits: flat. Cancellation rate: +1.2 points. Backlog burn: stable.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `financing conditions and mortgage affordability`
- Canonical follow-up: `orders stay weak even if rate and credit proxies normalize`
Evidence summary:
- traffic and visits held better than financing-linked proxies
- the main falsifier is not more credit chatter; it is orders staying weak after financing conditions normalize
Common failure modes:
- naming financing pressure but failing to specify the true revisit condition
- monitoring CDS or liquidity headlines instead of the demand outcome after financing normalization
Canonical answer object:
```json
{
  "label": "A",
  "primary_proxy_family": "financing_conditions_and_mortgage_affordability",
  "falsifier": "orders_keep_deteriorating_even_if_rate_and_credit_proxies_normalize"
}
```

Model replies:
- Base primary: `mortgage affordability friction` ✅
- Base follow-up: `if traffic and tours roll over` ❌
- Skill primary: `mortgage affordability friction` ✅
- Skill follow-up: `traffic and tours roll over` ❌

Judge notes: Primary matches the financing/mortgage-affordability read. Follow-up misses the required falsifier: weak orders after rates/credit normalize, not weaker traffic or tours.

### v14im2_010 — Homebuilder Miss: Funding Stress Or Demand Softness?

- Source case: `v14cpi_001`
- Family: `proxy_family_selection`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `0/2`
- Skill field score: `0/2`

Scenario:
A morning note combines mortgage data, builder credit signals, order metrics, and website activity after a homebuilder stock selloff.

Primary question: What would have to happen before you abandon the financing-friction thesis?
Follow-up question: Which commercial readout has to stay weak for that flip?

Evidence packet:
- Morning note (document_excerpt): The stock fell 11% after management guided to lower near-term orders. Analysts noted no major land or permitting update. Channel checks described buyer hesitation around monthly payments rather than reduced tour activity.
- Market and operating snapshot (table): 30-year mortgage rate: +55 bps over 6 weeks. Mortgage applications: -12%. Builder CDS: +38 bps. Website traffic: -1%. Model-home visits: flat. Cancellation rate: +1.2 points. Backlog burn: stable.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `orders stay weak even after financing proxies normalize`
- Canonical follow-up: `inspect order intake and cancellations after financing normalization`
Evidence summary:
- mortgage-rate and credit signals moved much more than traffic or visit activity
- a demand-softness flip requires weak order outcomes even after financing proxies improve
Common failure modes:
- answering with more financing indicators instead of the condition that would falsify the financing thesis
- forgetting to tie the flip condition to orders and cancellations
Canonical answer object:
```json
{
  "label": "A",
  "primary_proxy_family": "financing_conditions_and_mortgage_affordability",
  "falsifier": "orders_keep_deteriorating_even_if_rate_and_credit_proxies_normalize"
}
```

Model replies:
- Base primary: `top-of-funnel demand must roll over` ❌
- Base follow-up: `model-home visits and web traffic` ❌
- Skill primary: `top-of-funnel weakens despite stable rates` ❌
- Skill follow-up: `model-home visits stay weak` ❌

Judge notes: These answers switch to top-of-funnel demand proxies. The canonical flip requires order intake/cancellations staying weak after financing conditions improve.

### v14im2_011 — Alt-Token Slump: Base-Asset Weakness Or Liquidity Drain?

- Source case: `v14cpi_002`
- Family: `proxy_family_selection`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A crypto market packet compares majors, alt-token liquidity, on-chain activity, and exchange conditions after a sharp decline in a gaming token basket.

Primary question: What is still the cleanest starting read for the alt selloff?
Follow-up question: What would actually falsify that read?

Evidence packet:
- Crypto desk note (document_excerpt): BTC and ETH were nearly flat on the day, but gaming and lower-liquidity alt tokens sold off hard. No exploit, governance failure, or delisting notice was reported for the focal token.
- Cross-market snapshot (table): BTC return: +0.3%. ETH return: +0.1%. Alt-token order-book depth: -35%. Perp funding on small tokens: sharply negative. Exchange maintenance on one retail-heavy venue: 2 hours. Game DAU: flat. On-chain fees for the project: flat.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `retail liquidity and alt-beta risk appetite`
- Canonical follow-up: `project-specific activity breaks while broad alt liquidity normalizes`
Evidence summary:
- majors stayed stable while lower-liquidity alt conditions deteriorated sharply
- the true falsifier is project-specific weakness surviving a broader alt-liquidity normalization
Common failure modes:
- giving a broad crypto answer without naming the retail-liquidity and alt-beta channel
- watching BTC or ETH direction instead of the project-specific break that would falsify the broad-liquidity story
Canonical answer object:
```json
{
  "label": "B",
  "primary_proxy_family": "retail_liquidity_and_alt_beta",
  "falsifier": "project_specific_activity_breaks_while_broad_alt_liquidity_normalizes"
}
```

Model replies:
- Base primary: `broad alt-liquidity drain` ✅
- Base follow-up: `watch DAU/fees diverge from peers` ✅
- Skill primary: `broad alt-liquidity drain` ✅
- Skill follow-up: `DAU/fees break versus peers` ✅

Judge notes: Broad alt-liquidity drain is the right first read, and DAU/fees breaking versus peers is a concrete project-specific falsifier consistent with the broad-liquidity story normalizing elsewhere.

### v14im2_012 — Alt-Token Slump: Base-Asset Weakness Or Liquidity Drain?

- Source case: `v14cpi_002`
- Family: `proxy_family_selection`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A crypto market packet compares majors, alt-token liquidity, on-chain activity, and exchange conditions after a sharp decline in a gaming token basket.

Primary question: What single break would push you away from the broad-liquidity story?
Follow-up question: What do you compare it against when checking that break?

Evidence packet:
- Crypto desk note (document_excerpt): BTC and ETH were nearly flat on the day, but gaming and lower-liquidity alt tokens sold off hard. No exploit, governance failure, or delisting notice was reported for the focal token.
- Cross-market snapshot (table): BTC return: +0.3%. ETH return: +0.1%. Alt-token order-book depth: -35%. Perp funding on small tokens: sharply negative. Exchange maintenance on one retail-heavy venue: 2 hours. Game DAU: flat. On-chain fees for the project: flat.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `project-specific activity breaks while broad alt liquidity normalizes`
- Canonical follow-up: `compare project activity against broader alt-liquidity normalization`
Evidence summary:
- project usage was flat in the packet, so a token-specific thesis needs a clear break there
- the comparison set is broader alt-liquidity normalization rather than BTC or ETH direction alone
Common failure modes:
- calling any further alt weakness a falsifier even if broad liquidity is still broken
- using majors as the comparator instead of broader alt-liquidity conditions
Canonical answer object:
```json
{
  "label": "B",
  "primary_proxy_family": "retail_liquidity_and_alt_beta",
  "falsifier": "project_specific_activity_breaks_while_broad_alt_liquidity_normalizes"
}
```

Model replies:
- Base primary: `token-specific DAU/fees break` ✅
- Base follow-up: `compare against gaming-alt peers` ✅
- Skill primary: `token-specific DAU/fees rollover` ✅
- Skill follow-up: `compare with gaming-token peers` ✅

Judge notes: Token-specific DAU/fees weakness is an acceptable specific version of project activity breaking, and comparing against gaming-alt peers is a reasonable narrower proxy for broader alt-liquidity normalization.

### v14im2_013 — Regional Bank Stress And A Small-Cap SaaS Selloff

- Source case: `v14cpi_006`
- Family: `transmission_supportability`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A software stock trades off during regional-bank stress even though the company has no direct deposit or lending disclosure in the packet.

Primary question: What indirect path best explains the software selloff?
Follow-up question: What market cross-check would strengthen that path most?

Evidence packet:
- Market note (document_excerpt): The company stated that cash is spread across money-center banks and disclosed no unusual financing event. The stock still sold off with other long-duration software names when regional banks weakened.
- Factor snapshot (table): Regional bank ETF: -14%. Small-cap software basket: -9%. HY OAS: +48 bps. Company net cash: positive. Revenue guidance: unchanged.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `valuation-duration and refinancing channel`
- Canonical follow-up: `watch spreads and duration-sensitive peers while company metrics stay intact`
Evidence summary:
- the packet rules out direct deposit problems but keeps a broader financing channel alive
- HY spreads and peer co-movement are the right cross-checks, not direct bank-exposure speculation
Common failure modes:
- denying any path because the company lacks direct bank exposure
- drifting into customer or deposit exposure checks instead of watching spreads and duration-sensitive peers
Canonical answer object:
```json
{
  "label": "C",
  "mechanism": "valuation_duration_and_refinancing_channel",
  "supportability": "supported_but_indirect"
}
```

Model replies:
- Base primary: `duration de-rate via tighter credit` ✅
- Base follow-up: `watch HY spreads versus software basket` ✅
- Skill primary: `credit-tightening duration de-rate` ✅
- Skill follow-up: `watch HY OAS versus software basket` ✅

Judge notes: Both primary answers capture the indirect duration/refinancing channel, and both follow-ups name the right discriminating market cross-check via HY spreads plus software-peer/basket co-move.

### v14im2_014 — Regional Bank Stress And A Small-Cap SaaS Selloff

- Source case: `v14cpi_006`
- Family: `transmission_supportability`
- Exact winner: `base`
- Base exact: `correct`
- Skill exact: `incorrect`
- Base field score: `2/2`
- Skill field score: `1/2`

Scenario:
A software stock trades off during regional-bank stress even though the company has no direct deposit or lending disclosure in the packet.

Primary question: What evidence would make you more confident this is a duration de-rate rather than direct bank exposure?
Follow-up question: What should stay intact if that read is right?

Evidence packet:
- Market note (document_excerpt): The company stated that cash is spread across money-center banks and disclosed no unusual financing event. The stock still sold off with other long-duration software names when regional banks weakened.
- Factor snapshot (table): Regional bank ETF: -14%. Small-cap software basket: -9%. HY OAS: +48 bps. Company net cash: positive. Revenue guidance: unchanged.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `spreads widen and duration-sensitive peers sell off together`
- Canonical follow-up: `company metrics stay intact while you watch HY spreads and duration-sensitive peers`
Evidence summary:
- the canonical read is an indirect financing or valuation channel, not a direct balance-sheet problem
- the confirming pattern is peer and spread behavior alongside intact company fundamentals
Common failure modes:
- looking for direct bank links instead of asking what market evidence would confirm an indirect channel
- forgetting that company metrics should remain intact if the duration-channel explanation is correct
Canonical answer object:
```json
{
  "label": "C",
  "mechanism": "valuation_duration_and_refinancing_channel",
  "supportability": "supported_but_indirect"
}
```

Model replies:
- Base primary: `peer software tracks spreads, not disclosures` ✅
- Base follow-up: `guidance and liquidity stay intact` ✅
- Skill primary: `basket co-move with clean liquidity` ❌
- Skill follow-up: `liquidity and guidance stay intact` ✅

Judge notes: Base primary matches the needed peer-and-spread confirmation pattern; skill primary gets peer co-move and clean liquidity but misses the crucial spread signal. Both follow-ups correctly keep company guidance/liquidity intact.

### v14im2_015 — Biotech Rally: Primary Driver Or Pure Squeeze?

- Source case: `v14cpi_008`
- Family: `primary_driver_vs_amplifier`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A market-news packet contains a regulatory catalyst, a later rumor, and evidence that short interest may have amplified the move.

Primary question: What distinction has to stay explicit if you do not want to over-credit the squeeze?
Follow-up question: How should the note handle the squeeze without replacing the catalyst?

Evidence packet:
- Event timeline (news_packet): 09:00: FDA advisory panel votes favorably on the therapy. 09:05: stock opens sharply higher. 12:10: an unconfirmed social-media rumor mentions a possible acquisition. Short interest entering the day was 24% of float.
- Intraday move summary (table): Open-to-10am move: +21%. Noon-to-close incremental move: +6%. Borrow fee: elevated. Company filings: no acquisition filing or comment.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `FDA advisory-panel vote is the primary driver`
- Canonical follow-up: `keep the primary catalyst separate from squeeze amplification`
Evidence summary:
- most of the move happened immediately after the regulatory event and before the later rumor
- short interest can explain amplification, but it should not replace the primary catalyst in the note
Common failure modes:
- collapsing primary catalyst and amplifier into one undifferentiated answer
- letting the later rumor dominate the writeup because it sounds more dramatic
Canonical answer object:
```json
{
  "label": "C",
  "primary_driver": "fda_advisory_panel_vote",
  "amplifier": "short_squeeze_dynamics"
}
```

Model replies:
- Base primary: `FDA vote primary, squeeze amplifier` ✅
- Base follow-up: `frame short-covering as secondary amplification` ✅
- Skill primary: `FDA vote trigger, squeeze amplifier` ✅
- Skill follow-up: `describe squeeze as secondary boost` ✅

Judge notes: Both answers keep the FDA advisory-panel vote as the primary driver and treat the squeeze only as secondary amplification.

### v14im2_016 — Biotech Rally: Primary Driver Or Pure Squeeze?

- Source case: `v14cpi_008`
- Family: `primary_driver_vs_amplifier`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A market-news packet contains a regulatory catalyst, a later rumor, and evidence that short interest may have amplified the move.

Primary question: How should the move be phrased so catalyst and amplifier do not get collapsed?
Follow-up question: What should stay secondary even if short-covering mattered?

Evidence packet:
- Event timeline (news_packet): 09:00: FDA advisory panel votes favorably on the therapy. 09:05: stock opens sharply higher. 12:10: an unconfirmed social-media rumor mentions a possible acquisition. Short interest entering the day was 24% of float.
- Intraday move summary (table): Open-to-10am move: +21%. Noon-to-close incremental move: +6%. Borrow fee: elevated. Company filings: no acquisition filing or comment.

Naturalness rationale: Looks like a normal analyst or operator prompt about the first arbiter, the right falsifier, or the observable that should carry the most weight.

Ground truth:
- Canonical primary: `FDA advisory-panel vote is the primary driver while squeeze dynamics amplify`
- Canonical follow-up: `keep the primary catalyst separate from squeeze amplification`
Evidence summary:
- the timing shows the regulatory event came first and explains most of the move
- squeeze dynamics matter as magnitude amplification, not as a replacement causal story
Common failure modes:
- describing the move as a pure squeeze despite the timing evidence
- focusing the follow-up on the rumor rather than on preserving the catalyst-versus-amplifier distinction
Canonical answer object:
```json
{
  "label": "C",
  "primary_driver": "fda_advisory_panel_vote",
  "amplifier": "short_squeeze_dynamics"
}
```

Model replies:
- Base primary: `AdCom-driven rally, short-covering amplified` ✅
- Base follow-up: `squeeze narrative stays secondary` ✅
- Skill primary: `AdCom win drove move, shorts amplified` ✅
- Skill follow-up: `keep short-covering secondary` ✅

Judge notes: Both answers preserve the AdCom/FDA catalyst as primary and keep short-covering explicitly secondary rather than replacing the causal story.


## Per-Family

- `pressure_test_design`: base exact `3/8`, skill exact `2/8`
- `primary_driver_vs_amplifier`: base exact `2/2`, skill exact `2/2`
- `proxy_family_selection`: base exact `2/4`, skill exact `2/4`
- `transmission_supportability`: base exact `2/2`, skill exact `1/2`
