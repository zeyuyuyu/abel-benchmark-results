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

## Case Overview

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

## Full Cases

### v14im2r_001 — Fuel Shock Or Demand Weakness: Which Probe Comes First?

- Source case: `v14cpi_014`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `0/2`
- Skill field score: `0/2`

Scenario:
An airline packet leaves cost shock and demand weakness as competing stories, and the task is to choose the first clean pressure test.

Primary question: Which first pressure test most cleanly distinguishes fuel shock from demand weakness?
Follow-up question: What downstream readout should you inspect after that stress?

Evidence packet:
- Agent brief (document_excerpt): The stock sold off with energy markets. Forward bookings and capacity plans held steady. Analysts want the first probe that would most quickly separate cost pressure from true demand deterioration.
- Sector snapshot (table): Jet fuel crack: +18%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue: flat. FX: flat.

Naturalness rationale: Looks like a normal analyst question, but stays close to phrasings that previously surfaced a real skill edge.

Ground truth:
- Canonical primary: `stress jet-fuel costs first`
- Canonical follow-up: `inspect unit margin or EPS sensitivity`
Evidence summary:
- the packet already shows stable demand-side evidence and a large energy move
- margin and EPS sensitivity are the most direct downstream readouts of a fuel-cost stress
Common failure modes:
- choosing a demand-side probe despite the packet already showing stable booking evidence
- picking a variable that is not downstream of the suspected cost channel
Canonical answer object:
```json
{
  "label": "A",
  "stress_target": "jet_fuel_costs",
  "readout": "unit_margin_or_eps_sensitivity"
}
```

Model replies:
- Base primary: `fare pass-through test` ❌
- Base follow-up: `booking elasticity and load factor` ❌
- Skill primary: `fare pass-through test` ❌
- Skill follow-up: `watch close-in booking curve` ❌

Judge notes: Both answers pivot to pricing/demand probes; the canonical test is to stress jet-fuel costs first, then read through to margin or EPS sensitivity, not bookings or close-in demand.

### v14im2r_002 — Fuel Shock Or Demand Weakness: Which Probe Comes First?

- Source case: `v14cpi_014`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `0/2`
- Skill field score: `0/2`

Scenario:
An airline packet leaves cost shock and demand weakness as competing stories, and the task is to choose the first clean pressure test.

Primary question: Which first pressure test most directly separates fuel shock from demand weakness?
Follow-up question: What readout should you inspect once you run that probe?

Evidence packet:
- Agent brief (document_excerpt): The stock sold off with energy markets. Forward bookings and capacity plans held steady. Analysts want the first probe that would most quickly separate cost pressure from true demand deterioration.
- Sector snapshot (table): Jet fuel crack: +18%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue: flat. FX: flat.

Naturalness rationale: Looks like a normal analyst question, but stays close to phrasings that previously surfaced a real skill edge.

Ground truth:
- Canonical primary: `stress jet-fuel costs first`
- Canonical follow-up: `inspect unit margin or EPS sensitivity`
Evidence summary:
- fuel moved sharply while bookings and unit revenue held up
- the direct downstream readout of a fuel-cost stress is margin or EPS sensitivity, not a demand metric
Common failure modes:
- answering with a demand probe before testing the more active fuel channel
- watching PRASM or bookings rather than margin or EPS sensitivity
Canonical answer object:
```json
{
  "label": "A",
  "stress_target": "jet_fuel_costs",
  "readout": "unit_margin_or_eps_sensitivity"
}
```

Model replies:
- Base primary: `fare pass-through test` ❌
- Base follow-up: `booking elasticity and load factor` ❌
- Skill primary: `fare pass-through test` ❌
- Skill follow-up: `watch close-in booking curve` ❌

Judge notes: Fuel is the live channel in the packet, so fare pass-through is the wrong first probe. The follow-ups are demand metrics rather than the required downstream margin/EPS readout of fuel-cost stress.

### v14im2r_003 — Fuel Shock Or Demand Weakness: Which Probe Comes First?

- Source case: `v14cpi_014`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `0/2`
- Skill field score: `1/2`

Scenario:
An airline packet leaves cost shock and demand weakness as competing stories, and the task is to choose the first clean pressure test.

Primary question: If you only get one first stress, which one best separates fuel shock from demand weakness?
Follow-up question: What downstream number matters most after that stress?

Evidence packet:
- Agent brief (document_excerpt): The stock sold off with energy markets. Forward bookings and capacity plans held steady. Analysts want the first probe that would most quickly separate cost pressure from true demand deterioration.
- Sector snapshot (table): Jet fuel crack: +18%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue: flat. FX: flat.

Naturalness rationale: Looks like a normal analyst question, but stays close to phrasings that previously surfaced a real skill edge.

Ground truth:
- Canonical primary: `stress jet-fuel costs first`
- Canonical follow-up: `inspect unit margin or EPS sensitivity`
Evidence summary:
- energy-linked cost pressure is the live variable in the packet
- the expected downstream consequence of that stress lands in margins or EPS, not in traffic headlines
Common failure modes:
- jumping to close-in demand metrics because they sound more intuitive
- naming a cost shock but failing to follow it through to the right downstream readout
Canonical answer object:
```json
{
  "label": "A",
  "stress_target": "jet_fuel_costs",
  "readout": "unit_margin_or_eps_sensitivity"
}
```

Model replies:
- Base primary: `forward bookings stress` ❌
- Base follow-up: `watch unit revenue` ❌
- Skill primary: `jet fuel crack stress` ✅
- Skill follow-up: `watch fuel CASM` ❌

Judge notes: Base again uses a demand stress and demand readout. Skill primary is equivalent to stressing jet-fuel costs first, but fuel CASM is still a cost-line metric, not the downstream margin or EPS sensitivity the canonical answer requires.

### v14im2r_004 — EV Supplier Drop: Lithium Pass-Through Or Customer Inventory Reset?

- Source case: `v14cpi_015`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A supplier stock weakens while both upstream commodity and downstream customer signals are moving, and the analyst must pick the first separating probe.

Primary question: Which first pressure test best distinguishes lithium pass-through from customer inventory reset?
Follow-up question: What readout should you inspect once you run that probe?

Evidence packet:
- Agent brief (document_excerpt): Lithium prices softened, but customer inventory days also rose across two major OEMs. The supplier guides to softer near-term shipments without changing long-run content assumptions.
- Supplier snapshot (table): Lithium spot: -14%. Customer inventory days: +11 days. OEM production schedules: trimmed for next quarter. Supplier gross-margin guide: only modestly lower. Backlog conversion: slowing.

Naturalness rationale: Looks like a normal analyst question, but stays close to phrasings that previously surfaced a real skill edge.

Ground truth:
- Canonical primary: `stress customer inventory and build schedules first`
- Canonical follow-up: `inspect shipments and backlog conversion`
Evidence summary:
- customer inventory and build schedules are the variables most directly tied to the supplier shipment softness in the packet
- lithium softness alone does not explain a slower backlog conversion nearly as cleanly
Common failure modes:
- defaulting to the flashier commodity move instead of the more direct downstream transmission path
- reading margin before checking the shipment path that actually distinguishes the stories
Canonical answer object:
```json
{
  "label": "B",
  "stress_target": "customer_inventory_reset",
  "readout": "shipments_and_backlog_conversion"
}
```

Model replies:
- Base primary: `customer inventory stress` ✅
- Base follow-up: `watch backlog conversion` ✅
- Skill primary: `customer inventory reset stress` ✅
- Skill follow-up: `watch backlog conversion` ✅

Judge notes: Both answers match the shipment-path story: stress customer inventory/reset first, and backlog conversion is a concrete downstream observable aligned with the canonical shipments/backlog-conversion readout.

### v14im2r_005 — EV Supplier Drop: Lithium Pass-Through Or Customer Inventory Reset?

- Source case: `v14cpi_015`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `0/2`
- Skill field score: `0/2`

Scenario:
A supplier stock weakens while both upstream commodity and downstream customer signals are moving, and the analyst must pick the first separating probe.

Primary question: Which first pressure test most directly separates lithium pass-through from customer inventory reset?
Follow-up question: What readout should matter most once you run that probe?

Evidence packet:
- Agent brief (document_excerpt): Lithium prices softened, but customer inventory days also rose across two major OEMs. The supplier guides to softer near-term shipments without changing long-run content assumptions.
- Supplier snapshot (table): Lithium spot: -14%. Customer inventory days: +11 days. OEM production schedules: trimmed for next quarter. Supplier gross-margin guide: only modestly lower. Backlog conversion: slowing.

Naturalness rationale: Looks like a normal analyst question, but stays close to phrasings that previously surfaced a real skill edge.

Ground truth:
- Canonical primary: `stress customer inventory and build schedules first`
- Canonical follow-up: `inspect shipments and backlog conversion`
Evidence summary:
- backlog conversion is already slowing while margin guidance is only modestly lower
- that pattern points first to customer schedule and inventory stress rather than to commodity pass-through
Common failure modes:
- choosing a lithium or ASP bridge before testing customer schedules
- stopping at inventory days alone instead of reading through to shipments and backlog conversion
Canonical answer object:
```json
{
  "label": "B",
  "stress_target": "customer_inventory_reset",
  "readout": "shipments_and_backlog_conversion"
}
```

Model replies:
- Base primary: `volume-price bridge on shipments` ❌
- Base follow-up: `OEM sell-through and inventory days` ❌
- Skill primary: `unit shipments versus lithium-linked ASP` ❌
- Skill follow-up: `OEM sell-through and inventory days` ❌

Judge notes: Base and skill primaries jump to shipment/ASP diagnostics instead of first stressing customer inventory and build schedules. Both follow-ups stop at sell-through/inventory monitoring rather than the discriminating shipments and backlog-conversion readout.

### v14im2r_006 — EV Supplier Drop: Lithium Pass-Through Or Customer Inventory Reset?

- Source case: `v14cpi_015`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `0/2`
- Skill field score: `0/2`

Scenario:
A supplier stock weakens while both upstream commodity and downstream customer signals are moving, and the analyst must pick the first separating probe.

Primary question: What first probe most cleanly separates lithium pass-through from customer inventory reset?
Follow-up question: What downstream shipment readout deserves the most weight after that?

Evidence packet:
- Agent brief (document_excerpt): Lithium prices softened, but customer inventory days also rose across two major OEMs. The supplier guides to softer near-term shipments without changing long-run content assumptions.
- Supplier snapshot (table): Lithium spot: -14%. Customer inventory days: +11 days. OEM production schedules: trimmed for next quarter. Supplier gross-margin guide: only modestly lower. Backlog conversion: slowing.

Naturalness rationale: Looks like a normal analyst question, but stays close to phrasings that previously surfaced a real skill edge.

Ground truth:
- Canonical primary: `stress customer inventory and build schedules first`
- Canonical follow-up: `inspect shipments and backlog conversion`
Evidence summary:
- the shipment path is the cleanest place to discriminate these stories
- customer schedule and inventory stress should show up in shipments and backlog conversion faster than in margin
Common failure modes:
- letting the commodity headline dominate despite a clearer downstream shipment signal
- answering with a generic sell-through monitor rather than the shipment and backlog path
Canonical answer object:
```json
{
  "label": "B",
  "stress_target": "customer_inventory_reset",
  "readout": "shipments_and_backlog_conversion"
}
```

Model replies:
- Base primary: `volume-price bridge on shipments` ❌
- Base follow-up: `OEM wholesales versus sell-through` ❌
- Skill primary: `unit shipments versus lithium-linked ASP` ❌
- Skill follow-up: `OEM sell-through and inventory days` ❌

Judge notes: Shipment path matters here, but the first probe still needs to stress customer schedules and inventory, not a shipment price bridge. Both follow-ups miss the required shipments plus backlog-conversion path.

### v14im2r_007 — Residential Solar Miss: Policy Step-Down Or Sales Execution?

- Source case: `v14cpi_016`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

Scenario:
The packet leaves policy and execution stories both live, and the evaluation asks for the cleanest first probe to challenge the leading thesis.

Primary question: Which pressure test most directly challenges the thesis that policy incentive step-down is the main driver?
Follow-up question: What readout matters most once you stress that lever?

Evidence packet:
- Agent brief (document_excerpt): Order volume weakened after a state incentive step-down, but channel checks also mention elevated rep turnover and slower lead follow-up times.
- Sales funnel snapshot (table): Lead volume: -3%. Lead-to-booking conversion: -16%. Incentive value: -22%. Sales-rep turnover: +8 points. Follow-up time: slower by 1.4 days.

Naturalness rationale: Looks like a normal analyst question, but stays close to phrasings that previously surfaced a real skill edge.

Ground truth:
- Canonical primary: `stress incentive-policy generosity first`
- Canonical follow-up: `inspect lead-to-booking conversion`
Evidence summary:
- the leading thesis is specifically about incentive generosity, so the cleanest challenge is to stress that lever and inspect the conversion step most directly tied to purchase economics
- lead volume moved far less than conversion, which makes the conversion readout more decision-relevant than top-of-funnel traffic
Common failure modes:
- choosing a lever unrelated to the stated uncertainty
- looking at margin instead of the funnel step most exposed to incentive economics
Canonical answer object:
```json
{
  "label": "A",
  "stress_target": "incentive_policy_generosity",
  "readout": "lead_to_booking_conversion"
}
```

Model replies:
- Base primary: `same-state fast-follow-up test` ❌
- Base follow-up: `lead-to-booking conversion lift` ✅
- Skill primary: `same-incentive conversion by follow-up speed` ❌
- Skill follow-up: `new-lead booking conversion recovery` ✅

Judge notes: Both primaries test sales follow-up speed/execution rather than incentive-policy generosity, so they miss the canonical lever. Both follow-ups correctly target booking conversion as the key downstream readout.

### v14im2r_008 — Residential Solar Miss: Policy Step-Down Or Sales Execution?

- Source case: `v14cpi_016`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

Scenario:
The packet leaves policy and execution stories both live, and the evaluation asks for the cleanest first probe to challenge the leading thesis.

Primary question: What first pressure test most directly challenges the policy-step-down story?
Follow-up question: Which downstream readout matters most once you run it?

Evidence packet:
- Agent brief (document_excerpt): Order volume weakened after a state incentive step-down, but channel checks also mention elevated rep turnover and slower lead follow-up times.
- Sales funnel snapshot (table): Lead volume: -3%. Lead-to-booking conversion: -16%. Incentive value: -22%. Sales-rep turnover: +8 points. Follow-up time: slower by 1.4 days.

Naturalness rationale: Looks like a normal analyst question, but stays close to phrasings that previously surfaced a real skill edge.

Ground truth:
- Canonical primary: `stress incentive-policy generosity first`
- Canonical follow-up: `inspect lead-to-booking conversion`
Evidence summary:
- the packet leaves policy and execution both live, but the leading claim is policy economics
- lead-to-booking conversion is the funnel step most exposed to that lever
Common failure modes:
- jumping straight to rep-speed or turnover diagnostics instead of challenging the policy thesis
- watching lead flow rather than the conversion step where incentive economics should bite
Canonical answer object:
```json
{
  "label": "A",
  "stress_target": "incentive_policy_generosity",
  "readout": "lead_to_booking_conversion"
}
```

Model replies:
- Base primary: `same-state fast-follow-up test` ❌
- Base follow-up: `lead-to-booking conversion lift` ✅
- Skill primary: `same-incentive conversion by follow-up speed` ❌
- Skill follow-up: `new-lead booking conversion recovery` ✅

Judge notes: Both primaries focus on execution-speed diagnostics instead of first stressing incentive generosity. Both follow-ups are acceptable because they read through to lead-to-booking conversion.

### v14im2r_009 — Residential Solar Miss: Policy Step-Down Or Sales Execution?

- Source case: `v14cpi_016`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

Scenario:
The packet leaves policy and execution stories both live, and the evaluation asks for the cleanest first probe to challenge the leading thesis.

Primary question: If policy economics is the leading thesis, what is the cleanest first probe to challenge it?
Follow-up question: What funnel readout should you inspect once you do?

Evidence packet:
- Agent brief (document_excerpt): Order volume weakened after a state incentive step-down, but channel checks also mention elevated rep turnover and slower lead follow-up times.
- Sales funnel snapshot (table): Lead volume: -3%. Lead-to-booking conversion: -16%. Incentive value: -22%. Sales-rep turnover: +8 points. Follow-up time: slower by 1.4 days.

Naturalness rationale: Looks like a normal analyst question, but stays close to phrasings that previously surfaced a real skill edge.

Ground truth:
- Canonical primary: `stress incentive-policy generosity first`
- Canonical follow-up: `inspect lead-to-booking conversion`
Evidence summary:
- incentive value dropped much more than lead volume, while conversion weakened sharply
- the natural downstream arbiter is conversion rather than response-time anecdotes
Common failure modes:
- treating rep-turnover chatter as the first probe despite the leading policy thesis
- stopping at follow-up speed instead of inspecting lead-to-booking conversion
Canonical answer object:
```json
{
  "label": "A",
  "stress_target": "incentive_policy_generosity",
  "readout": "lead_to_booking_conversion"
}
```

Model replies:
- Base primary: `same-market follow-up-lag split` ❌
- Base follow-up: `lead-to-booking by response-time bucket` ✅
- Skill primary: `same-state follow-up-speed cohort split` ❌
- Skill follow-up: `lead-to-booking by response-lag bucket` ✅

Judge notes: Both primary answers switch to sales follow-up speed/lag instead of first stressing policy generosity. Both follow-ups still point to the right arbiter, lead-to-booking conversion, just segmented by response lag.

### v14im2r_010 — Which First Pressure Test Separates Financing Stress From Demand Softness?

- Source case: `v14cpi_013`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `0/2`
- Skill field score: `0/2`

Scenario:
A distributor note leaves two live stories on the table, and the task is to pick the first stress lever that would most efficiently separate them.

Primary question: Which first pressure test separates financing stress from demand softness?
Follow-up question: What readout should you inspect once you run that probe?

Evidence packet:
- Agent brief (document_excerpt): Rate-sensitive customer verticals have slowed, but service attach and installed-base usage remain stable. Credit spreads widened and management said quote activity was healthy but close timing stretched.
- Commercial snapshot (table): New orders: -4%. Cancellations: +2 points. Service attach: flat. Installed-base usage: flat. HY OAS: +62 bps. Accounts receivable days: +4 days.

Naturalness rationale: Looks like a normal analyst question, but stays close to phrasings that previously surfaced a real skill edge.

Ground truth:
- Canonical primary: `stress financing conditions first`
- Canonical follow-up: `inspect order intake and cancellations`
Evidence summary:
- the open causal split is financing friction versus true demand softness
- orders and cancellations are the closest downstream variables for distinguishing the two stories after stressing financing conditions
Common failure modes:
- choosing a lever unrelated to the live uncertainty
- looking at approval rates and close timing instead of downstream order outcomes
Canonical answer object:
```json
{
  "label": "B",
  "stress_target": "financing_conditions",
  "readout": "order_intake_and_cancellations"
}
```

Model replies:
- Base primary: `financed-vs-cash close-rate split` ❌
- Base follow-up: `quote-to-close lag by financing type` ❌
- Skill primary: `financed-vs-cash quote-to-close split` ❌
- Skill follow-up: `quote-to-close days by financing cohort` ❌

Judge notes: Both primary answers use financed-vs-cash splits rather than a direct financing-condition stress test. Both follow-ups focus on quote-to-close timing, not the required downstream order intake and cancellations.


## Per-Family

- `pressure_test_design`: base exact `1/10`, skill exact `1/10`
