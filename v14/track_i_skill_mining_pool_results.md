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

## Case Overview

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

## Full Cases

### v14im_001 — Why Did Margin Miss Despite Revenue Growth?

- Source case: `v14d_013`
- Family: `earnings_driver_analysis`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
An analyst memo, earnings excerpt, and compact KPI table are given for a company that grew revenue but missed margin expectations.

Primary question: What best explains the margin miss?
Follow-up question: What next observable would most strengthen that read?

Evidence packet:
- Earnings excerpt (document_excerpt): Revenue grew 12% year over year, but operating margin missed consensus. Management highlighted a larger-than-expected mix shift into lower-margin hardware and elevated expedited freight costs.
- KPI table (table): Hardware mix: 46% -> 58%. Services mix: 54% -> 42%. Hardware gross margin: 24% -> 18%. Services gross margin: 72% -> 70%. Expedited freight cost as % of revenue: 0.4% -> 2.2%.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `mix shift into lower-margin hardware amplified by freight`
- Canonical follow-up: `watch hardware mix, hardware margin, and freight cost`
Evidence summary:
- revenue growth alone is not a valid margin explanation
- packet supports a causal variable relationship between product mix and margin
Common failure modes:
- answering with generic cost inflation despite no evidence
- treating revenue growth itself as the driver of margin miss
Canonical answer object:
```json
{
  "primary_driver": "mix_shift_into_lower_margin_hardware_amplified_by_freight",
  "supporting_variables": [
    "hardware_mix_up",
    "hardware_gross_margin_down",
    "expedited_freight_cost_up"
  ],
  "confidence": "medium_high"
}
```

Model replies:
- Base primary: `hardware mix shift and freight` ✅
- Base follow-up: `watch mix normalization and freight percent` ✅
- Skill primary: `lower-margin hardware mix shift` ✅
- Skill follow-up: `watch hardware mix and freight percent` ✅

Judge notes: Both primaries capture the lower-margin hardware mix story; the follow-ups name concrete mix/freight observables, even if hardware margin is implicit rather than explicit.

### v14im_002 — Three Plausible Stories, One Dominant Driver

- Source case: `v14d_015`
- Family: `multi_factor_finance_synthesis`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A cross-asset memo includes rates, FX, commodity costs, and company guidance. Several causal stories look plausible.

Primary question: What is the most plausible dominant explanation for the move?
Follow-up question: What uncertainty or metric would you keep live next?

Evidence packet:
- Analyst note (document_excerpt): Management cited three factors for the quarter: a one-point constant-currency headwind, a 40 bps legal reserve, and weaker channel sell-through that pushed inventory days higher.
- Operating summary (table): Revenue miss versus plan: -6%. Constant-currency impact: -1 point. Legal reserve impact on operating margin: -0.4 points. Channel inventory days: +12 days. End-market sell-through: -9%.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `channel inventory correction and weak sell-through`
- Canonical follow-up: `watch sell-through and inventory-days normalization`
Evidence summary:
- dominant driver must explain most of the miss magnitude
- FX and legal reserve are too small to be the main answer
Common failure modes:
- choosing the most familiar macro explanation
- overweighting a one-time legal item that mainly affects margin, not revenue
Canonical answer object:
```json
{
  "primary_driver": "channel_inventory_correction_and_weak_sell_through",
  "supporting_variables": [
    "inventory_days_up",
    "sell_through_down",
    "revenue_miss_much_larger_than_fx_headwind"
  ],
  "confidence": "medium_high"
}
```

Model replies:
- Base primary: `channel inventory overhang` ✅
- Base follow-up: `watch sell-through and inventory days` ✅
- Skill primary: `channel destocking from weak sell-through` ✅
- Skill follow-up: `watch inventory days and sell-through` ✅

Judge notes: All answers align with channel inventory correction tied to weak sell-through, and the follow-ups track the two key discriminators: sell-through and inventory days.

### v14im_003 — Fresh Event, Fast Causal Read

- Source case: `v14d_019`
- Family: `fresh_event_synthesis`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
An unresolved event analysis task asks for a short causal read using current information, with evidence freshness explicitly relevant.

Primary question: What is the most likely causal driver of the move right now?
Follow-up question: What part of the thesis remains uncertain enough not to overstate?

Evidence packet:
- Snippet 1 (retrieval_bundle): Ocean carriers announced emergency surcharges after a canal disruption forced rerouting on several Asia-Europe lanes.
- Snippet 2 (retrieval_bundle): Freight rate indices jumped sharply over the same two-day window, while retailers said they had not yet repriced goods.
- Snippet 3 (retrieval_bundle): Analysts cautioned that the duration of the rerouting shock remained unclear and could fade if passage normalizes quickly.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `freight-rate spike due to canal disruption and rerouting`
- Canonical follow-up: `duration and persistence of rerouting surcharges remain uncertain`
Evidence summary:
- tests causal synthesis under freshness-sensitive but frozen evidence
- good answers must separate what is likely from what remains unresolved
Common failure modes:
- summarizing headlines without naming a mechanism
- overclaiming a durable earnings effect not supported by the packet
Canonical answer object:
```json
{
  "primary_driver": "freight_rate_spike_due_to_canal_disruption_and_rerouting",
  "uncertainty": "how_long_the_disruption_and_surcharges_will_persist",
  "evidence_used": [
    "Snippet 1",
    "Snippet 2",
    "Snippet 3"
  ]
}
```

Model replies:
- Base primary: `rerouting shock from canal disruption` ✅
- Base follow-up: `watch reopening and retail repricing` ✅
- Skill primary: `rerouting-driven freight capacity shock` ✅
- Skill follow-up: `disruption duration and route normalization` ✅

Judge notes: Both primaries identify canal-disruption-driven rerouting/freight shock; both follow-ups keep the unresolved duration/normalization question live in concrete terms.

### v14im_004 — Build The Event Memo, Not Just The Answer

- Source case: `v14d_020`
- Family: `analyst_workflow_agent`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

Scenario:
The agent receives a short business question but must collect current evidence, decide whether it is enough, and produce an analyst-style memo.

Primary question: What is the best-supported causal explanation for the selloff right now?
Follow-up question: What would you verify next before strengthening that view?

Evidence packet:
- Snippet 1 (retrieval_bundle): A regional bank's shares fell after a policy official commented that deposit competition remains intense for smaller lenders.
- Snippet 2 (retrieval_bundle): The bank's last quarterly filing showed a relatively high share of interest-bearing deposits and rising funding costs.
- Snippet 3 (retrieval_bundle): A rumor about a capital raise circulated online, but no primary-source filing or company statement confirmed it.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `funding-cost and deposit-beta concern`
- Canonical follow-up: `verify uninsured-deposit mix or wholesale-funding dependence`
Evidence summary:
- tests memo-style causal synthesis with verification discipline
- answers should privilege primary-source evidence over rumor
Common failure modes:
- treating the rumor as the main driver
- failing to specify what to verify next
Canonical answer object:
```json
{
  "primary_driver": "funding_cost_and_deposit_beta_concern",
  "next_verification": "verify_insured_vs_uninsured_deposit_mix_and_wholesale_funding_dependence",
  "uncertainty": "the_unconfirmed_capital_raise_rumor_should_not_be_treated_as_established_fact"
}
```

Model replies:
- Base primary: `deposit squeeze, not raise rumor` ✅
- Base follow-up: `check 8-Ks and deposit trends` ❌
- Skill primary: `deposit-competition funding-cost squeeze` ✅
- Skill follow-up: `check filings for capital raise` ❌

Judge notes: Both primaries land on deposit/funding-cost pressure rather than rumor, but neither follow-up verifies the discriminating deposit mix or wholesale-funding dependence the canonical read requires.

### v14im_005 — One Event, Multiple Conflicting Narratives

- Source case: `v14d_021`
- Family: `cross_source_event_integration`
- Exact winner: `skill`
- Base exact: `incorrect`
- Skill exact: `correct`
- Base field score: `1/2`
- Skill field score: `2/2`

Scenario:
A live case includes conflicting media explanations, partial company commentary, and market reaction across related assets.

Primary question: What is the most causally plausible primary driver of the rally?
Follow-up question: What alternative remains live enough to monitor, and how would you monitor it?

Evidence packet:
- Snippet 1 (retrieval_bundle): A biotech stock rallied after an FDA advisory panel voted in favor of its therapy.
- Snippet 2 (retrieval_bundle): Social media accounts also circulated an acquisition rumor, but no credible outlet confirmed it.
- Snippet 3 (retrieval_bundle): Short interest was elevated heading into the vote, which may have amplified the magnitude of the move.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `positive FDA panel vote improving approval odds`
- Canonical follow-up: `short-squeeze amplification remains possible, so verify timing and short interest`
Evidence summary:
- tests selection among competing narratives
- main event should outrank unsupported rumor, while magnitude amplification remains a valid uncertainty
Common failure modes:
- choosing the rumor because it sounds more dramatic
- ignoring the distinction between driver and amplifier
Canonical answer object:
```json
{
  "primary_driver": "positive_fda_panel_vote_improving_approval_odds",
  "uncertainty": "short_squeeze_dynamics_may_have_amplified_the_move_but_do_not_replace_the_main_causal_event",
  "evidence_used": [
    "Snippet 1",
    "Snippet 3"
  ]
}
```

Model replies:
- Base primary: `FDA panel win, amplified by shorts` ✅
- Base follow-up: `watch SEC filings for buyout confirmation` ❌
- Skill primary: `favorable FDA panel vote` ✅
- Skill follow-up: `watch short-covering and borrow stress` ✅

Judge notes: Both primaries correctly center the FDA panel vote. The base follow-up chases an unsupported buyout rumor, while the skill follow-up monitors squeeze mechanics.

### v14im_006 — Homebuilder Miss: Funding Stress Or Demand Softness?

- Source case: `v14cpi_001`
- Family: `proxy_family_selection`
- Exact winner: `skill`
- Base exact: `incorrect`
- Skill exact: `correct`
- Base field score: `1/2`
- Skill field score: `2/2`

Scenario:
A morning note combines mortgage data, builder credit signals, order metrics, and website activity after a homebuilder stock selloff.

Primary question: Which explanation is cleaner for the move right now?
Follow-up question: What would most directly make you revisit that view?

Evidence packet:
- Morning note (document_excerpt): The stock fell 11% after management guided to lower near-term orders. Analysts noted no major land or permitting update. Channel checks described buyer hesitation around monthly payments rather than reduced tour activity.
- Market and operating snapshot (table): 30-year mortgage rate: +55 bps over 6 weeks. Mortgage applications: -12%. Builder CDS: +38 bps. Website traffic: -1%. Model-home visits: flat. Cancellation rate: +1.2 points. Backlog burn: stable.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `financing conditions and mortgage affordability`
- Canonical follow-up: `if orders stay weak after financing proxies normalize, demand softness gains weight`
Evidence summary:
- mortgage affordability worsened materially while traffic and visits stayed roughly intact
- credit and rate signals moved sharply, which fits hesitation around financing more than collapse in shopper interest
Common failure modes:
- treating a modest cancellation increase as proof of broad demand collapse
- ignoring the sharper movement in mortgage-rate and credit proxies
Canonical answer object:
```json
{
  "label": "A",
  "primary_proxy_family": "financing_conditions_and_mortgage_affordability",
  "falsifier": "orders_keep_deteriorating_even_if_rate_and_credit_proxies_normalize"
}
```

Model replies:
- Base primary: `affordability-driven demand softness` ✅
- Base follow-up: `watch CDS widening or revolver draws` ❌
- Skill primary: `mortgage affordability stress` ✅
- Skill follow-up: `watch tours and traffic weaken` ✅

Judge notes: Affordability and financing stress are the core story; the base primary is close enough because affordability is explicit. Its follow-up watches more funding stress instead of the demand-side evidence that would overturn the view, while the skill follow-up names a concrete demand-side arbiter.

### v14im_007 — Alt-Token Slump: Base-Asset Weakness Or Liquidity Drain?

- Source case: `v14cpi_002`
- Family: `proxy_family_selection`
- Exact winner: `skill`
- Base exact: `incorrect`
- Skill exact: `correct`
- Base field score: `1/2`
- Skill field score: `2/2`

Scenario:
A crypto market packet compares majors, alt-token liquidity, on-chain activity, and exchange conditions after a sharp decline in a gaming token basket.

Primary question: What is the cleaner starting point for the selloff?
Follow-up question: What would most directly falsify that interpretation?

Evidence packet:
- Crypto desk note (document_excerpt): BTC and ETH were nearly flat on the day, but gaming and lower-liquidity alt tokens sold off hard. No exploit, governance failure, or delisting notice was reported for the focal token.
- Cross-market snapshot (table): BTC return: +0.3%. ETH return: +0.1%. Alt-token order-book depth: -35%. Perp funding on small tokens: sharply negative. Exchange maintenance on one retail-heavy venue: 2 hours. Game DAU: flat. On-chain fees for the project: flat.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `retail liquidity and alt-beta risk appetite`
- Canonical follow-up: `if project-specific activity breaks while broad alt liquidity normalizes`
Evidence summary:
- majors were stable while lower-liquidity books and alt funding deteriorated sharply
- project-specific usage stayed flat, which argues against a token-specific adoption collapse
Common failure modes:
- projecting a broad BTC/ETH narrative onto a move concentrated in low-liquidity alt exposure
- assuming a hack or exploit without evidence packet support
Canonical answer object:
```json
{
  "label": "B",
  "primary_proxy_family": "retail_liquidity_and_alt_beta",
  "falsifier": "project_specific_activity_breaks_while_broad_alt_liquidity_normalizes"
}
```

Model replies:
- Base primary: `alt-liquidity drain` ✅
- Base follow-up: `watch BTC/ETH break lower` ❌
- Skill primary: `alt liquidity drain` ✅
- Skill follow-up: `depth normalization without token rebound` ✅

Judge notes: Alt-liquidity and risk-appetite are the right starting point. BTC/ETH weakness is not the key falsifier, but normalization in liquidity depth without recovery is a valid direct test of the liquidity-drain story.

### v14im_008 — Airline Selloff: Fuel Shock Or Demand Crack?

- Source case: `v14cpi_003`
- Family: `proxy_family_selection`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
An airline equity drawdown arrives alongside a commodity move, while booking and traffic indicators are updated in the same note.

Primary question: What is the cleaner primary read for the airline selloff?
Follow-up question: What would make you change that view first?

Evidence packet:
- Airline sector note (document_excerpt): The stock fell after a sharp move in energy markets. Management did not cut capacity or demand commentary, and no labor disruption was disclosed.
- Operating and market snapshot (table): Jet fuel crack spread: +18%. Front-month crude: +11%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue guidance: flat. Wage agreement updates: none. FX basket: flat.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `fuel and input-cost pressure`
- Canonical follow-up: `if bookings or unit revenue break while fuel pressure eases`
Evidence summary:
- the sharpest moving variables are fuel-linked while bookings and unit-revenue guidance are stable
- there is no evidence packet support for labor or FX being the dominant marginal driver
Common failure modes:
- assuming all airline weakness is demand-driven without checking booking and unit-revenue evidence
- overweighting crude headlines without relating them to the actual airline cost channel
Canonical answer object:
```json
{
  "label": "A",
  "primary_proxy_family": "fuel_and_input_cost_pressure",
  "falsifier": "forward_bookings_or_unit_revenue_break_while_fuel_pressure_eases"
}
```

Model replies:
- Base primary: `jet fuel shock` ✅
- Base follow-up: `watch bookings and unit revenue roll over` ✅
- Skill primary: `fuel-cost shock` ✅
- Skill follow-up: `bookings and unit revenue weaken` ✅

Judge notes: Fuel and input-cost pressure are the clean primary read. Both follow-ups correctly point to bookings and unit revenue weakening as the demand-side signal that would change the view.

### v14im_009 — Small-Cap Software De-Rate: Duration Pressure Or Product Trouble?

- Source case: `v14cpi_004`
- Family: `proxy_family_selection`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A software stock sells off with a broader factor move while company-specific operating metrics are also reported.

Primary question: What is the cleaner explanation for the de-rate?
Follow-up question: What would make you shift toward an idiosyncratic company problem instead?

Evidence packet:
- Software note (document_excerpt): The company reiterated annual ARR guidance and disclosed no outage, product recall, or major customer loss. The stock fell alongside a broader selloff in long-duration software names.
- Factor and operating snapshot (table): High-yield OAS: +75 bps. 10Y real yield: +19 bps. Small-cap software basket: -11%. ARR guidance: unchanged. Net revenue retention: 112% -> 111%. Churn: flat. Major incident count: 0.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `duration pressure and financing conditions`
- Canonical follow-up: `if renewal or churn metrics break while rates and credit stabilize`
Evidence summary:
- macro duration and credit-sensitive software factors moved sharply while company operating metrics were largely intact
- the packet does not contain company-specific failure evidence strong enough to outrank the factor move
Common failure modes:
- inventing product trouble from price action alone
- ignoring the explicit sector-factor de-rating in the evidence packet
Canonical answer object:
```json
{
  "label": "A",
  "primary_proxy_family": "financing_conditions_and_duration_pressure",
  "falsifier": "renewal_or_churn_metrics_break_even_if_credit_and_rate_proxies_stabilize"
}
```

Model replies:
- Base primary: `duration and factor pressure` ✅
- Base follow-up: `watch guidance cuts or churn rise` ✅
- Skill primary: `duration and credit pressure` ✅
- Skill follow-up: `NRR/churn deterioration or ARR cut` ✅

Judge notes: Both primaries match the macro duration/credit-factor de-rate over product trouble. Both follow-ups get credit for concrete retention/demand-break signals like churn or NRR deterioration, even though they omit the explicit macro-stabilization qualifier.

### v14im_010 — Soybean Rally And Snack-Maker Weakness

- Source case: `v14cpi_005`
- Family: `bridge_noise_rejection`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A consumer staples note lists several moving commodities, but only some sit on the company’s true cost path.

Primary question: Which candidate driver is most likely bridge noise rather than the core transmission channel?
Follow-up question: Which costs deserve attention instead if you want the cleaner transmission path?

Evidence packet:
- Staples note (document_excerpt): The stock traded lower after a basket of agricultural commodities moved higher. Management commentary emphasizes freight, packaging resin, palm oil, and cocoa as the main variable costs.
- Cost exposure snapshot (table): Soybeans: +9%. Palm oil: +4%. Cocoa: +6%. Packaging resin: +7%. Freight surcharge impact: +110 bps to COGS. Soy exposure in the focal brand mix: not material.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `soybean rally is bridge noise`
- Canonical follow-up: `watch freight, packaging resin, palm oil, and cocoa instead`
Evidence summary:
- the note explicitly says soy is not a material input for the focal brand mix
- freight, resin, palm oil, and cocoa all sit more directly on the company cost path
Common failure modes:
- equating any agricultural headline with causal relevance to a food stock
- picking the most visible market move instead of the cleanest company-specific transmission channel
Canonical answer object:
```json
{
  "label": "A",
  "bridge_noise": "soybean_rally",
  "rationale_tag": "company_cost_structure_does_not_run_through_soybeans"
}
```

Model replies:
- Base primary: `soybeans are bridge noise` ✅
- Base follow-up: `watch freight, resin, palm oil, cocoa` ✅
- Skill primary: `soybeans are bridge noise` ✅
- Skill follow-up: `freight, resin, palm oil, cocoa` ✅

Judge notes: Both candidates correctly reject soy as bridge noise and point to the cleaner direct cost channels: freight, resin, palm oil, and cocoa.

### v14im_011 — Regional Bank Stress And A Small-Cap SaaS Selloff

- Source case: `v14cpi_006`
- Family: `transmission_supportability`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A software stock trades off during regional-bank stress even though the company has no direct deposit or lending disclosure in the packet.

Primary question: What is the most supportable transmission path from the bank stress to the software move?
Follow-up question: What additional evidence would most strengthen or weaken that path?

Evidence packet:
- Market note (document_excerpt): The company stated that cash is spread across money-center banks and disclosed no unusual financing event. The stock still sold off with other long-duration software names when regional banks weakened.
- Factor snapshot (table): Regional bank ETF: -14%. Small-cap software basket: -9%. HY OAS: +48 bps. Company net cash: positive. Revenue guidance: unchanged.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `valuation-duration and refinancing channel`
- Canonical follow-up: `watch spreads and duration-sensitive peers while company metrics stay intact`
Evidence summary:
- the packet rules out direct deposit exposure, but a broader risk and financing channel remains plausible
- high-yield spreads widened and duration-sensitive software names sold off together
Common failure modes:
- assuming no path simply because the company lacks direct bank exposure
- inventing a balance-sheet crisis despite the explicit net-cash note
Canonical answer object:
```json
{
  "label": "C",
  "mechanism": "valuation_duration_and_refinancing_channel",
  "supportability": "supported_but_indirect"
}
```

Model replies:
- Base primary: `long-duration rerating from tighter credit` ✅
- Base follow-up: `watch HY spreads and SaaS correlation` ✅
- Skill primary: `credit-spread-driven duration derating` ✅
- Skill follow-up: `watch HY OAS and nonbank SaaS peers` ✅

Judge notes: Both primaries identify the broader valuation-duration/refinancing channel rather than direct bank exposure. Both follow-ups name the key arbitrating observables on that path: HY spreads and duration-sensitive SaaS peer behavior.

### v14im_012 — Rare-Earth Spike Into EV Gross Margin

- Source case: `v14cpi_007`
- Family: `transmission_strength_judgment`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A commodity shock looks intuitively relevant, but the evidence packet includes cost-share and contracting details that constrain near-term transmission.

Primary question: How much should the commodity shock matter near-term for the EV maker?
Follow-up question: What would you verify before promoting it into a bigger thesis?

Evidence packet:
- Supply-chain note (document_excerpt): Rare-earth spot prices jumped after export restrictions. The automaker’s procurement note says the focal materials are covered by fixed contracts for the next two quarters.
- Cost-structure snapshot (table): Rare-earth component share of COGS: 1.2%. Fixed-price coverage horizon: 2 quarters. Battery metals and logistics remain the larger variable exposures.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `weak near-term pass-through because contracts and cost share limit it`
- Canonical follow-up: `verify contract coverage or cost share before promoting the shock`
Evidence summary:
- the cost share is small and the contract coverage delays pass-through
- the packet explicitly points to larger variable exposures elsewhere in the cost stack
Common failure modes:
- overweighting the most dramatic commodity headline without checking cost share and contract timing
- calling the move impossible to assess despite clear packet constraints
Canonical answer object:
```json
{
  "label": "C",
  "transmission_strength": "weak_near_term",
  "blocking_factor": "fixed_contracts_and_low_cost_share"
}
```

Model replies:
- Base primary: `minimal near-term margin impact` ✅
- Base follow-up: `check contract reset and pass-through clauses` ✅
- Skill primary: `limited near-term gross-margin impact` ✅
- Skill follow-up: `verify contract volume coverage and reset timing` ✅

Judge notes: Both primaries correctly say the rare-earth shock should have limited near-term margin impact. Both follow-ups focus on the right verification area before upgrading the thesis: contract coverage/reset timing and pass-through mechanics.

### v14im_013 — Biotech Rally: Primary Driver Or Pure Squeeze?

- Source case: `v14cpi_008`
- Family: `primary_driver_vs_amplifier`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A market-news packet contains a regulatory catalyst, a later rumor, and evidence that short interest may have amplified the move.

Primary question: Which explanation best fits the move without overstating the evidence?
Follow-up question: What distinction or uncertainty should you keep explicit in the note?

Evidence packet:
- Event timeline (news_packet): 09:00: FDA advisory panel votes favorably on the therapy. 09:05: stock opens sharply higher. 12:10: an unconfirmed social-media rumor mentions a possible acquisition. Short interest entering the day was 24% of float.
- Intraday move summary (table): Open-to-10am move: +21%. Noon-to-close incremental move: +6%. Borrow fee: elevated. Company filings: no acquisition filing or comment.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `FDA advisory-panel vote is the primary driver while squeeze dynamics amplify`
- Canonical follow-up: `keep primary driver separate from squeeze amplification`
Evidence summary:
- most of the move occurred immediately after the regulatory event and before the rumor appeared
- short interest can explain amplification without replacing the primary catalyst
Common failure modes:
- treating the later rumor as primary despite the timing mismatch
- collapsing primary driver and amplifier into the same answer
Canonical answer object:
```json
{
  "label": "C",
  "primary_driver": "fda_advisory_panel_vote",
  "amplifier": "short_squeeze_dynamics"
}
```

Model replies:
- Base primary: `FDA catalyst with squeeze amplification` ✅
- Base follow-up: `M&A rumor unverified; squeeze not primary` ✅
- Skill primary: `FDA catalyst with short-squeeze amplification` ✅
- Skill follow-up: `M&A rumor unconfirmed; extension attribution uncertain` ✅

Judge notes: Both primaries keep the FDA event as the main catalyst with squeeze as amplifier; both follow-ups preserve attribution discipline rather than promoting the later rumor to primary cause.

### v14im_014 — Which First Pressure Test Separates Financing Stress From Demand Softness?

- Source case: `v14cpi_013`
- Family: `pressure_test_design`
- Exact winner: `skill`
- Base exact: `incorrect`
- Skill exact: `correct`
- Base field score: `1/2`
- Skill field score: `2/2`

Scenario:
A distributor note leaves two live stories on the table, and the task is to pick the first stress lever that would most efficiently separate them.

Primary question: Which first pressure test would best separate financing stress from demand softness?
Follow-up question: What readout should you inspect once you run that probe?

Evidence packet:
- Agent brief (document_excerpt): Rate-sensitive customer verticals have slowed, but service attach and installed-base usage remain stable. Credit spreads widened and management said quote activity was healthy but close timing stretched.
- Commercial snapshot (table): New orders: -4%. Cancellations: +2 points. Service attach: flat. Installed-base usage: flat. HY OAS: +62 bps. Accounts receivable days: +4 days.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

Ground truth:
- Canonical primary: `stress financing conditions first`
- Canonical follow-up: `inspect orders and cancellations`
Evidence summary:
- the open causal split is financing friction versus true demand softness
- orders and cancellations are the closest downstream variables for distinguishing the two stories after stressing financing conditions
Common failure modes:
- choosing a lever unrelated to the live uncertainty
- looking at margin before testing the order-flow channel that actually separates the stories
Canonical answer object:
```json
{
  "label": "B",
  "stress_target": "financing_conditions",
  "readout": "order_intake_and_cancellations"
}
```

Model replies:
- Base primary: `test financed-vs-cash conversion` ✅
- Base follow-up: `approval rates and close timing` ❌
- Skill primary: `financing-term sensitivity on quote conversion` ✅
- Skill follow-up: `watch financed conversion and cycle times` ✅

Judge notes: Both primaries stay focused on financing as the first probe. Base follow-up leans on financing-process metrics instead of the downstream order-flow discriminator; skill follow-up's financed conversion is close enough to the canonical readout.

### v14im_015 — Fuel Shock Or Demand Weakness: Which Probe Comes First?

- Source case: `v14cpi_014`
- Family: `pressure_test_design`
- Exact winner: `skill`
- Base exact: `incorrect`
- Skill exact: `correct`
- Base field score: `1/2`
- Skill field score: `2/2`

Scenario:
An airline packet leaves cost shock and demand weakness as competing stories, and the task is to choose the first clean pressure test.

Primary question: Which first pressure test most cleanly distinguishes fuel shock from demand weakness?
Follow-up question: What downstream readout should you inspect after that stress?

Evidence packet:
- Agent brief (document_excerpt): The stock sold off with energy markets. Forward bookings and capacity plans held steady. Analysts want the first probe that would most quickly separate cost pressure from true demand deterioration.
- Sector snapshot (table): Jet fuel crack: +18%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue: flat. FX: flat.

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

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
- Base primary: `jet-fuel-only margin stress` ✅
- Base follow-up: `watch close-in yields and bookings` ❌
- Skill primary: `jet-fuel cost shock test` ✅
- Skill follow-up: `watch CASM and margin guide` ✅

Judge notes: Both primaries correctly stress fuel costs first. Base follow-up incorrectly shifts to demand-side indicators, while skill follow-up stays on cost-side unit-economics sensitivity.

### v14im_016 — EV Supplier Drop: Lithium Pass-Through Or Customer Inventory Reset?

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

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

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
- Base primary: `customer-destock volume stress` ✅
- Base follow-up: `watch inventory days and backlog conversion` ✅
- Skill primary: `OEM inventory reset probe` ✅
- Skill follow-up: `watch backlog conversion and call-offs` ✅

Judge notes: Both primaries focus on customer inventory reset/build effects rather than lithium. Both follow-ups stay on the shipment-path distinction, with backlog conversion directly matching the canonical readout.

### v14im_017 — Residential Solar Miss: Policy Step-Down Or Sales Execution?

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

Naturalness rationale: Looks like a normal analyst question about what is driving a move and what to inspect next.

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
- Base primary: `fast-follow-up conversion test` ❌
- Base follow-up: `watch close-rate rebound at flat incentives` ✅
- Skill primary: `same-market speed-to-lead test` ❌
- Skill follow-up: `watch lead-to-booking conversion rebound` ✅

Judge notes: Primary must stress incentive-policy generosity; both primary candidates switch to sales-execution levers instead. Both follow-ups point to the key conversion readout, with skill matching canon directly and base using close-rate as the same core observable.


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
