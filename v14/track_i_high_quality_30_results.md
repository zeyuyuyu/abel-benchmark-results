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

## Case Overview

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
- Skill primary: `hardware mix shift and freight spike` ✅
- Skill follow-up: `watch hardware mix and freight rate` ✅

Judge notes: Both primaries match the lower-margin hardware mix plus freight story; both follow-ups name concrete mix/freight observables, though the base is less explicit on hardware margin.

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
- Base primary: `channel destocking from weak sell-through` ✅
- Base follow-up: `watch inventory days and sell-through` ✅
- Skill primary: `channel destocking from weak sell-through` ✅
- Skill follow-up: `watch sell-through and inventory days` ✅

Judge notes: All predictions align with the dominant channel inventory correction driven by weak sell-through and the right confirming metrics.

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
- Base primary: `shipping rerouting and surcharge shock` ✅
- Base follow-up: `watch route normalization and retail repricing` ✅
- Skill primary: `canal-rerouting freight shock` ✅
- Skill follow-up: `watch disruption duration and normalization` ✅

Judge notes: Both primaries capture a rerouting-driven freight shock. The skill follow-up states the duration uncertainty directly; the base is still acceptable because route normalization tests that same persistence question.

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
- Base primary: `deposit-competition funding pressure` ✅
- Base follow-up: `check deposits and any 8-K` ❌
- Skill primary: `deposit-cost pressure, not raise rumor` ✅
- Skill follow-up: `verify any primary-source raise filing` ❌

Judge notes: Both primaries capture funding/deposit-cost pressure rather than the rumor. Both follow-ups miss the discriminating verification target of uninsured-deposit mix or wholesale-funding dependence and instead point to generic deposits/filings or rumor checks.

### v14im_005 — One Event, Multiple Conflicting Narratives

- Source case: `v14d_021`
- Family: `cross_source_event_integration`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
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
- Base primary: `FDA panel de-risking` ✅
- Base follow-up: `short squeeze; watch borrow and covering` ✅
- Skill primary: `positive AdCom vote` ✅
- Skill follow-up: `watch borrow fees and short-covering` ✅

Judge notes: Both primaries match FDA-panel de-risking, and both follow-ups concretely test short-squeeze amplification through borrow/covering signals.

### v14im_006 — Homebuilder Miss: Funding Stress Or Demand Softness?

- Source case: `v14cpi_001`
- Family: `proxy_family_selection`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

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
- Base primary: `mortgage-rate affordability pressure` ✅
- Base follow-up: `watch CDS and liquidity actions` ❌
- Skill primary: `rate-driven affordability softness` ✅
- Skill follow-up: `watch peer CDS and land pullbacks` ❌

Judge notes: Both primaries fit financing and affordability pressure, but neither follow-up gives the key revisit condition of orders staying weak after financing proxies normalize.

### v14im_007 — Alt-Token Slump: Base-Asset Weakness Or Liquidity Drain?

- Source case: `v14cpi_002`
- Family: `proxy_family_selection`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

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
- Base primary: `alt liquidity drain` ✅
- Base follow-up: `watch depth recovery versus BTC/ETH stability` ❌
- Skill primary: `alt-liquidity drain` ✅
- Skill follow-up: `watch BTC/ETH breadth turn negative` ❌

Judge notes: Both primaries correctly center alt-liquidity and risk appetite, but both follow-ups miss the discriminating falsifier of project-specific activity breaking while broader alt liquidity normalizes.

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
- Base primary: `fuel-cost shock` ✅
- Base follow-up: `watch forward bookings and unit revenue` ✅
- Skill primary: `fuel-cost shock` ✅
- Skill follow-up: `watch bookings or unit revenue soften` ✅

Judge notes: Both primaries match fuel and input-cost pressure, and both follow-ups correctly point to bookings or unit revenue as the demand-side observable that would challenge that view.

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
- Base primary: `broad duration/risk-off` ✅
- Base follow-up: `ARR guide cut or churn jump` ✅
- Skill primary: `duration-led factor de-rate` ✅
- Skill follow-up: `guidance cut or churn spike` ✅

Judge notes: Primary answers match the macro duration/financing-factor de-rate. The follow-ups use concrete company-metric breaks like churn/guidance deterioration, which are close enough to the canonical renewal/churn test.

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
- Base primary: `soybeans` ✅
- Base follow-up: `freight, resin, palm oil, cocoa` ✅
- Skill primary: `soybeans are bridge noise` ✅
- Skill follow-up: `watch freight, resin, palm oil, cocoa` ✅

Judge notes: Both answers correctly treat the soybean move as irrelevant bridge noise and point to the direct cost-path inputs instead.

### v14im_011 — Regional Bank Stress And A Small-Cap SaaS Selloff

- Source case: `v14cpi_006`
- Family: `transmission_supportability`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

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
- Base primary: `tighter financial conditions de-rating` ✅
- Base follow-up: `verify bank and SMB customer mix` ❌
- Skill primary: `credit-spread risk-off derating` ✅
- Skill follow-up: `check customer exposure to regional banks` ❌

Judge notes: The primary answers are close enough to a financing/risk-duration de-rate. The follow-ups miss the key discriminator of spreads and duration-sensitive peers with company metrics intact, and instead drift into direct bank/customer exposure.

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
- Base follow-up: `check contract coverage and reset terms` ✅
- Skill primary: `minimal near-term margin impact` ✅
- Skill follow-up: `check volume protections and rollover pricing` ✅

Judge notes: Primary answers match the limited near-term impact from small cost share and contract delay. The follow-ups correctly focus on contract structure and rollover timing as the main arbitration before elevating the thesis.

### v14im_013 — Biotech Rally: Primary Driver Or Pure Squeeze?

- Source case: `v14cpi_008`
- Family: `primary_driver_vs_amplifier`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

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
- Base primary: `FDA panel win, squeeze amplified` ✅
- Base follow-up: `M&A rumor unconfirmed, secondary` ❌
- Skill primary: `FDA catalyst with short-squeeze amplification` ✅
- Skill follow-up: `keep M&A rumor explicitly unconfirmed` ❌

Judge notes: Both primaries match FDA/adcom as the main catalyst with squeeze as amplifier. Both follow-ups focus on the later unconfirmed M&A rumor instead of explicitly keeping the primary catalyst separate from squeeze amplification.

### v14im_014 — Which First Pressure Test Separates Financing Stress From Demand Softness?

- Source case: `v14cpi_013`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

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
- Base primary: `compare financed vs cash conversion` ✅
- Base follow-up: `watch approval rates and days-to-close` ❌
- Skill primary: `quote-to-close by financing dependence` ✅
- Skill follow-up: `check approval rates and close timing` ❌

Judge notes: Both primaries are acceptable financing-first probes because they segment by financing dependence. Both follow-ups watch financing-process metrics rather than the key downstream discriminator of orders and cancellations.

### v14im_015 — Fuel Shock Or Demand Weakness: Which Probe Comes First?

- Source case: `v14cpi_014`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `0/2`
- Skill field score: `1/2`

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
- Base primary: `fare pass-through test` ❌
- Base follow-up: `watch close-in bookings and yields` ❌
- Skill primary: `fuel-cost stress with bookings fixed` ✅
- Skill follow-up: `watch close-in yields and PRASM` ❌

Judge notes: The base answer shifts to a fare/demand probe and then monitors demand-side readouts, missing the fuel-cost stress framing. The skill primary correctly stresses fuel with demand held fixed, but its follow-up still watches revenue metrics instead of unit margin or EPS sensitivity.

### v14im_016 — EV Supplier Drop: Lithium Pass-Through Or Customer Inventory Reset?

- Source case: `v14cpi_015`
- Family: `pressure_test_design`
- Exact winner: `skill`
- Base exact: `incorrect`
- Skill exact: `correct`
- Base field score: `1/2`
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
- Base primary: `ASP-versus-volume bridge` ❌
- Base follow-up: `watch backlog conversion and OEM inventory days` ✅
- Skill primary: `inventory-reset stress with lithium fixed` ✅
- Skill follow-up: `watch backlog conversion and OEM order releases` ✅

Judge notes: The base primary uses an ASP/volume decomposition rather than stressing customer inventory and build schedules first. Both follow-ups include backlog-conversion-type readouts that directly arbitrate the inventory-reset story, and the skill primary correctly fixes lithium while stressing inventory reset.

### v14im_017 — Residential Solar Miss: Policy Step-Down Or Sales Execution?

- Source case: `v14cpi_016`
- Family: `pressure_test_design`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `0/2`
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
- Base primary: `conversion by response-time cohort` ❌
- Base follow-up: `close-rate after response-time normalizes` ❌
- Skill primary: `same-incentive follow-up-speed test` ❌
- Skill follow-up: `watch lead-to-booking conversion` ✅

Judge notes: Both primaries switch to a sales-execution lever instead of stressing incentive generosity. Base follow-up stays tied to response-time normalization rather than the incentive-linked lead-to-booking conversion; skill follow-up names the correct conversion readout.

### v14im_018 — Price Cut And Sales-Comp Rewrite In The Same Week

- Source case: `v14cpi_009`
- Family: `bundled_intervention_supportability`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
Leadership wants the effect of a price cut on unit sales, but the operating packet shows another major commercial intervention at the same time and in the same weak regions.

Primary question: Can you cleanly credit the unit-sales move to the price cut?
Follow-up question: What contamination would stop you from writing that note cleanly?

Evidence packet:
- Commercial rollout note (document_excerpt): The company reduced list price by 8% in the weakest four regions and simultaneously changed sales compensation to reward unit volume instead of gross profit dollars.
- Observed outcome summary (table): The treated regions saw unit growth accelerate after the rollout. Untreated regions kept the old price and old comp plan. No randomization or staggered timing was used.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `no, the price cut is bundled with the sales-comp rewrite in the same weak regions`
- Canonical follow-up: `targeted rollout and simultaneous commercial intervention contaminate attribution`
Evidence summary:
- the price cut and compensation rewrite happened together in the same weak regions
- the packet does not support a price-only causal claim because the commercial interventions were bundled
Common failure modes:
- pretending the price cut can be isolated despite same-window commercial changes
- ignoring that the intervention was targeted into the weakest regions
Canonical answer object:
```json
{
  "label": "C",
  "identified": false,
  "blocking_issue": "bundled_intervention_and_targeted_rollout"
}
```

Model replies:
- Base primary: `price cut not isolatable` ✅
- Base follow-up: `simultaneous comp-plan rewrite contamination` ✅
- Skill primary: `no, bundled price-and-comp treatment` ✅
- Skill follow-up: `simultaneous comp-plan contamination` ✅

Judge notes: Both primaries correctly reject clean price-cut attribution because treatment is bundled with comp changes. Both follow-ups capture the key simultaneous commercial-intervention contamination, even though they do not explicitly mention weak-region targeting.

### v14im_019 — Predictive Maintenance Rolled Out To The Worst Plants First

- Source case: `v14cpi_010`
- Family: `targeted_rollout_design_choice`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A maintenance model was adopted first where failures were already highest, and leadership wants a credible evaluation design.

Primary question: What evaluation read would you trust for the maintenance-model rollout?
Follow-up question: What threat are you explicitly defending against?

Evidence packet:
- Rollout summary (operational_log): The predictive-maintenance model was launched first at plants with the highest prior failure rates. Failure rates fell after deployment, but the untreated plants were lower-risk to begin with.
- Plant summary (table): Four treated plants adopted in month 1, four control plants remained on the old process. Treated plants started with materially worse pre-period failure levels.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `matched or staggered diff-in-diff event study`
- Canonical follow-up: `targeted rollout to high-failure plants and regression to the mean`
Evidence summary:
- the rollout started where failures were already worst, so a naive before-after read is not credible
- a staggered or matched design is needed to separate treatment from pre-existing plant risk
Common failure modes:
- using a simple before-after comparison on plants selected for severe prior failures
- forgetting regression to the mean when the worst plants are treated first
Canonical answer object:
```json
{
  "label": "B",
  "design": "matched_or_staggered_difference_in_differences_event_study",
  "main_threat": "targeted_rollout_and_regression_to_mean"
}
```

Model replies:
- Base primary: `pre-trend-checked difference-in-differences` ✅
- Base follow-up: `regression to the mean` ✅
- Skill primary: `difference-in-differences with pre-trends` ✅
- Skill follow-up: `regression to the mean` ✅

Judge notes: Both answers choose a credible DiD-style evaluation rather than a naive before-after read and identify regression to the mean as the main threat from worst-plants-first rollout.

### v14im_020 — Credit-Limit Increases For Prequalified Users

- Source case: `v14cpi_011`
- Family: `selection_bias_supportability`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A consumer-finance team increased credit limits only for users already scored as especially attractive, then asked for the treatment effect on purchase frequency.

Primary question: Can you trust the measured purchase-frequency lift from the credit-limit increase?
Follow-up question: What makes that read unsafe?

Evidence packet:
- Risk-team note (document_excerpt): Only prequalified users with high internal scores received the limit increase. The untreated pool contains more low-score and lower-spend customers.
- Outcome summary (table): Treated users increased purchase frequency after the offer. Current observables include age bucket, region, and merchant mix, but not latent spending appetite or the full internal scorecard.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `no, selection into prequalified users blocks clean attribution`
- Canonical follow-up: `latent purchase propensity was already higher before treatment`
Evidence summary:
- credit limits were raised only for users already screened as attractive
- the packet leaves a strong selection-on-propensity problem that a raw lift cannot remove
Common failure modes:
- treating prequalification as harmless rather than the core source of bias
- reading the observed lift as causal without addressing baseline user quality
Canonical answer object:
```json
{
  "label": "C",
  "identified": false,
  "blocking_issue": "selection_on_latent_purchase_propensity"
}
```

Model replies:
- Base primary: `no causal lift estimate` ✅
- Base follow-up: `selection on unobserved spending appetite` ✅
- Skill primary: `selection-biased, not causal` ✅
- Skill follow-up: `unobserved purchase-propensity confounding` ✅

Judge notes: Both reject a clean causal interpretation of the observed lift. The follow-ups correctly point to higher underlying purchase propensity among prequalified users as the source of bias.

### v14im_021 — Warehouse Expedite Policy And Temporary Staffing

- Source case: `v14cpi_012`
- Family: `simultaneous_operations_change`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
An operations packet shows late shipments falling after a new expedite policy, but staffing changed in the same window.

Primary question: Can you cleanly credit the late-shipment improvement to the expedite policy?
Follow-up question: What other moving part keeps the read dirty?

Evidence packet:
- Operations note (operational_log): A warehouse introduced a new expedite policy during peak season. The same week, temporary staffing was increased by 18% and overtime rules were relaxed.
- Late-shipment summary (table): Late shipments fell from 9.4% to 6.7% after the policy week. No site-level stagger or holdout group is available in the packet.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `no, temporary staffing changed in the same window`
- Canonical follow-up: `the simultaneous staffing change contaminates the effect`
Evidence summary:
- late shipments fell after the expedite policy, but staffing also changed in the same period
- the packet does not support isolating the expedite policy from the operational staffing shift
Common failure modes:
- equating timing with attribution when multiple warehouse levers moved together
- failing to name the simultaneous staffing change as the blocking issue
Canonical answer object:
```json
{
  "label": "C",
  "identified": false,
  "blocking_issue": "simultaneous_temporary_staffing_change"
}
```

Model replies:
- Base primary: `cannot isolate expedite policy` ✅
- Base follow-up: `temp staffing and overtime changes` ✅
- Skill primary: `no clean expedite attribution` ✅
- Skill follow-up: `temp staffing and overtime changes` ✅

Judge notes: Both correctly reject clean expedite attribution and identify the simultaneous temp-staffing shift as the contaminant; extra overtime detail does not change the core read.

### v14im_022 — Margin Expansion After A Pricing Change

- Source case: `v14d_009`
- Family: `finance_table_causal_interpretation`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A finance table and a short memo summarize unit volume, realized price, marketing spend, and gross margin before and after a pricing policy change.

Primary question: Was pricing alone enough to explain the margin expansion?
Follow-up question: What belongs in the bridge besides pricing?

Evidence packet:
- Before/after KPI snapshot (table): List price +2.0%; unit volume -1.0%; input cost per unit -4.0%; gross margin +3.0 percentage points; competitor prices flat.
- Management note (document_excerpt): A commodity hedge rolled in during the same quarter and materially reduced input costs. Management warns that the margin benefit should not be attributed to pricing alone.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `no, pricing and input-cost relief both mattered`
- Canonical follow-up: `include input-cost relief alongside realized price`
Evidence summary:
- the table shows pricing and input-cost relief moving in the same direction
- the packet supports a mixed explanation, not a pricing-only story
Common failure modes:
- giving all the credit to pricing just because it is the named intervention
- ignoring simultaneous input-cost relief that also improves margin
Canonical answer object:
```json
{
  "label": "B",
  "supportability": "price_not_sufficient_explanation",
  "rationale": "Pricing and input-cost relief moved at the same time. The packet supports a mixed explanation, not a pricing-only causal claim."
}
```

Model replies:
- Base primary: `input-cost hedge, not pricing alone` ✅
- Base follow-up: `include commodity-hedge cost relief` ✅
- Skill primary: `pricing alone not sufficient` ✅
- Skill follow-up: `hedge-driven input-cost reduction` ✅

Judge notes: Both capture that pricing was not sufficient on its own and that input-cost relief, phrased more specifically as hedge/commodity cost relief, belongs in the bridge.

### v14im_023 — Which Event Actually Drove The Shortage?

- Source case: `v14d_010`
- Family: `event_chain_attribution`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A short news packet describes weather disruptions, port congestion, and inventory shortages across several paragraphs.

Primary question: What actually broke the chain right before stores stocked out?
Follow-up question: What earlier story should stay secondary in the memo?

Evidence packet:
- Excerpt 1 (news_packet): A typhoon delayed inbound vessels over the weekend and pushed two ocean arrivals back by roughly three days.
- Excerpt 2 (news_packet): By Tuesday morning, the port said berth congestion had eased and most containers had been unloaded.
- Excerpt 3 (news_packet): On Tuesday night, a scanner outage at the retailer's regional distribution center left 40% of inbound pallets unprocessed. Stores ran out of a promoted SKU the next afternoon.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `distribution-center scanner outage`
- Canonical follow-up: `weather and port disruption were upstream context, not the final trigger`
Evidence summary:
- the packet says the immediate operational failure before stockouts was the scanner outage
- earlier weather and port issues matter as setup, but they are not the last-step driver
Common failure modes:
- choosing the biggest upstream headline instead of the direct downstream trigger
- retelling the chronology without identifying the immediate mechanism
Canonical answer object:
```json
{
  "label": "C",
  "direct_driver": "distribution_center_scanner_outage",
  "justification": "Upstream weather mattered earlier, but the packet states that the immediate failure before stores stocked out was the scanner outage."
}
```

Model replies:
- Base primary: `DC scanner outage bottleneck` ✅
- Base follow-up: `typhoon and port delays secondary` ✅
- Skill primary: `regional DC scanner outage` ✅
- Skill follow-up: `typhoon and port delays secondary` ✅

Judge notes: Both identify the DC scanner outage as the immediate downstream break and keep weather/port issues as upstream secondary context.

### v14im_024 — After Does Not Mean Because

- Source case: `v14d_011`
- Family: `causal_vs_temporal_disambiguation`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
Two semantically similar news summaries are given, but one implies only temporal succession while the other states an actual mechanism.

Primary question: What is the cleaner causal read on the move?
Follow-up question: What headline should not be over-credited?

Evidence packet:
- Excerpt 1 (news_packet): Before market open, the company announced a $2 billion buyback and raised full-year guidance.
- Excerpt 2 (news_packet): Midday, the CEO appeared on television and repeated the same points from the morning release without adding new information.
- Excerpt 3 (news_packet): The shares finished the day up 7.8%, with most of the move occurring in the first 20 minutes after the open.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `morning corporate actions were the driver, not the later interview`
- Canonical follow-up: `do not over-credit the later interview because it added no new information`
Evidence summary:
- the main price move happened before the interview and after the earlier corporate actions
- the later interview did not introduce a stronger mechanism than the earlier actions
Common failure modes:
- crediting the most recent headline despite the timing mismatch
- confusing temporal sequence with causal force
Canonical answer object:
```json
{
  "label": "B",
  "causal_read": "morning_corporate_actions_more_plausible_than_interview",
  "justification": "The major price move happened before the interview and the interview introduced no new information."
}
```

Model replies:
- Base primary: `buyback and guidance raise` ✅
- Base follow-up: `midday CEO TV recap` ✅
- Skill primary: `buyback and guidance raise` ✅
- Skill follow-up: `midday CEO TV appearance` ✅

Judge notes: Both correctly attribute the move to the earlier corporate actions and treat the later CEO interview/TV appearance as the headline that should not be over-credited.

### v14im_025 — If The Strike Had Not Happened

- Source case: `v14d_012`
- Family: `narrative_counterfactual`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A supply-chain story culminates in a missed delivery milestone. The case asks for a counterfactual read under removal of one key disruption.

Primary question: If the strike had not happened, where would deliveries most likely have landed?
Follow-up question: What would still have kept results below plan?

Evidence packet:
- Excerpt 1 (news_packet): A port strike cut throughput by roughly 25% for five days early in the month.
- Excerpt 2 (news_packet): Later in the month, heavy rain reduced rail departures by another 10%.
- Excerpt 3 (news_packet): Actual monthly exports ended 18% below plan.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `deliveries improve but still finish below plan`
- Canonical follow-up: `the later rail disruption would still hold exports back`
Evidence summary:
- removing the strike restores part of the throughput loss but not the later logistics shock
- the counterfactual improves the outcome without fully restoring plan
Common failure modes:
- assuming removal of one disruption fully repairs the chain despite later failures
- missing that the packet asks for a partial-improvement counterfactual
Canonical answer object:
```json
{
  "label": "C",
  "counterfactual_direction": "improve_but_remain_below_plan",
  "justification": "Removing the strike recovers part of the lost throughput, but the later rail disruption still leaves exports below plan."
}
```

Model replies:
- Base primary: `roughly 14% below plan` ✅
- Base follow-up: `rain-hit rail departures` ✅
- Skill primary: `about 14% below plan` ✅
- Skill follow-up: `heavy-rain rail disruption` ✅

Judge notes: Numeric below-plan endpoints are consistent with the partial-recovery counterfactual, and both follow-ups match the later rail disruption as the remaining drag.

### v14im_026 — What Happens If We Cut Paid Acquisition?

- Source case: `v14d_014`
- Family: `marketing_spend_intervention`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A growth team has CAC, retention, conversion, and revenue-per-user metrics. The case asks for the near-term causal effect of cutting paid acquisition.

Primary question: What is the near-term read if paid acquisition is cut now?
Follow-up question: Why should you not assume efficiency fully offsets it?

Evidence packet:
- Marketing memo (document_excerpt): Paid search contributes 62% of first qualified visits, organic contributes 28%, referral contributes 10%. Paid CAC has been rising but remains the largest controllable volume lever.
- Geo-test results (table): In prior geo tests, cutting one paid lead generated only 0.25 organic replacement leads on average within the same month.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `qualified lead volume falls with only partial efficiency offset`
- Canonical follow-up: `organic substitution is incomplete in the packet`
Evidence summary:
- the geo test and memo imply that paid leads do not fully reappear organically
- some efficiency gains are plausible, but they do not fully offset the near-term lead loss
Common failure modes:
- assuming a full efficiency offset with no evidence for complete substitution
- focusing on CAC optics while ignoring the lead-volume channel
Canonical answer object:
```json
{
  "label": "A",
  "base_case": "lead_volume_down_partial_efficiency_gain",
  "rationale": "The memo and geo test imply incomplete organic substitution. Cutting paid acquisition should reduce qualified leads before any efficiency benefit fully offsets the loss."
}
```

Model replies:
- Base primary: `near-term volume drop` ✅
- Base follow-up: `weak organic replacement` ✅
- Skill primary: `near-term acquisition volume drop` ✅
- Skill follow-up: `only 25% organic replacement` ✅

Judge notes: Both primaries capture the near-term volume decline, and both follow-ups correctly state that organic replacement is only partial rather than complete.

### v14im_027 — Did The Temperature Change Really Reduce Defects?

- Source case: `v14d_016`
- Family: `manufacturing_sensor_confounder`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `0/2`
- Skill field score: `0/2`

Scenario:
A manufacturing report shows defect rates before and after a temperature policy change, but maintenance timing also shifted.

Primary question: Can you credit the defect improvement to the temperature change?
Follow-up question: What would you need to control for before making that call?

Evidence packet:
- Process snapshot (operational_log): Defect rate fell from 4.8% to 3.9% after a temperature-policy increase on Line A. In the same week, Line A received a maintenance overhaul, while other lines did not.
- Rollout note (document_excerpt): The temperature change was applied only on the renovated line. Throughput also dipped during the same maintenance window.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `no clean causal claim because maintenance timing and line selection moved too`
- Canonical follow-up: `control for maintenance status, line id, and throughput`
Evidence summary:
- maintenance timing and treatment assignment changed alongside the temperature policy
- the packet does not support a clean estimate without plant and throughput controls
Common failure modes:
- treating the before-after defect change as causal despite simultaneous maintenance shifts
- failing to name the line-selection problem explicitly
Canonical answer object:
```json
{
  "identified": false,
  "needed_controls": [
    "maintenance_status",
    "line_id",
    "throughput"
  ],
  "risk_note": "The treatment is confounded by simultaneous maintenance and line selection. The observed packet does not support a clean causal estimate."
}
```

Model replies:
- Base primary: `maintenance confound, not temperature alone` ❌
- Base follow-up: `control maintenance timing and throughput` ❌
- Skill primary: `maintenance-confounded defect drop` ❌
- Skill follow-up: `control maintenance timing and throughput` ❌

Judge notes: Both primaries miss the explicit line-selection/treatment-assignment confound, and both follow-ups omit line ID even though maintenance and throughput are mentioned.

### v14im_028 — A Policy Rolled Out At Different Times

- Source case: `v14d_017`
- Family: `staggered_rollout_policy`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
A policy is rolled out across regions on different dates, and the case asks for the most credible identification strategy.

Primary question: What evaluation design is the cleanest read for the staggered rollout?
Follow-up question: What assumption or risk should stay explicit?

Evidence packet:
- Plant adoption timeline (operational_log): Six plants adopted a scheduling policy across four different months. Pre-rollout output and defect trends are visually similar across plants.
- Evaluation task (document_excerpt): Leadership wants a design that estimates the policy effect while accounting for staggered adoption.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `staggered diff-in-diff event study`
- Canonical follow-up: `parallel trends, plus anticipation or spillover risk`
Evidence summary:
- regions adopted on different dates, which makes an event-study style design the most credible default
- the identifying read still depends on absent-policy trend comparability and limited spillovers
Common failure modes:
- using a pooled before-after read that throws away the rollout timing information
- forgetting anticipation and spillover checks even with the right design family
Canonical answer object:
```json
{
  "design": "staggered_difference_in_differences_event_study",
  "key_assumption": "parallel_trends_absent_the_policy",
  "risk_note": "Check for anticipation effects and cross-plant spillovers."
}
```

Model replies:
- Base primary: `staggered difference-in-differences event study` ✅
- Base follow-up: `parallel trends and no anticipation` ✅
- Skill primary: `staggered DiD event study` ✅
- Skill follow-up: `parallel trends and no anticipation` ✅

Judge notes: Both answers correctly use a staggered DiD event-study design and name parallel trends plus anticipation risk, which satisfies the required caveat.

### v14im_029 — The Aggregate Says Yes, The Strata Say No

- Source case: `v14d_008`
- Family: `simpsons_paradox_causal_read`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

Scenario:
A table shows an overall performance lift but subgroup breakdowns move in the opposite direction due to a composition shift.

Primary question: Why does the aggregate look better if both customer segments got worse?
Follow-up question: What point should the note make explicitly?

Evidence packet:
- Segmented conversion table (table): Novice users: control 18/100 convert, treatment 15/100 convert. Expert users: control 70/100 convert, treatment 66/100 convert. Mixture: treatment traffic is disproportionately expert-heavy, so the aggregate treatment conversion rate appears higher than the aggregate control rate.
- Assignment note (document_excerpt): The treatment was rolled out more aggressively to expert users after a manual allocation decision.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `segment mix shift creates a Simpson's paradox`
- Canonical follow-up: `within both novice and expert strata the treatment underperformed`
Evidence summary:
- the treated group ended up with more high-converting experts, which distorts the aggregate
- within each segment the treatment actually underperformed, so the mix shift drives the top-line lift
Common failure modes:
- reporting the aggregate lift without opening the segment composition change
- missing that both within-stratum effects move against the headline aggregate
Canonical answer object:
```json
{
  "label": "B",
  "segment_conclusion": "simpsons_paradox_due_to_segment_mix",
  "rationale": "Within both novice and expert strata, treatment underperforms. The aggregate improvement is driven by the treated group containing more high-converting experts."
}
```

Model replies:
- Base primary: `expert-heavy composition shift` ✅
- Base follow-up: `state aggregate lift is mix-driven` ❌
- Skill primary: `composition shift from expert-heavy treatment` ✅
- Skill follow-up: `aggregate lift is mix-driven, not causal` ❌

Judge notes: Both primary answers capture the expert-heavy composition shift / Simpson's paradox. Both follow-ups miss the key explicit note that treatment underperformed within both novice and expert strata.

### v14im_030 — A/B Test With A Post-Treatment Metric

- Source case: `v14d_007`
- Family: `post_treatment_control_trap`
- Exact winner: `tie`
- Base exact: `correct`
- Skill exact: `correct`
- Base field score: `2/2`
- Skill field score: `2/2`

Scenario:
An experiment report includes treatment assignment, conversion, and an engagement metric that is measured after treatment.

Primary question: Should you control for three-day engagement before calling the experiment?
Follow-up question: Why is that the wrong adjustment?

Evidence packet:
- Experiment summary (table): Rows: control, treatment. Columns: assigned_users, conversions, three_day_engagement_score. The engagement score is measured only after assignment and after users see the experience.
- Metric definitions (document_excerpt): Conversion is the primary endpoint. Three-day engagement is computed from post-assignment behavior inside the product.

Naturalness rationale: Looks like a normal analyst, operator, or growth-team question about what is really driving the observed move and what would make the read credible.

Ground truth:
- Canonical primary: `no, three-day engagement is post-treatment`
- Canonical follow-up: `conditioning on a post-treatment metric biases the total effect`
Evidence summary:
- the engagement metric is measured after treatment assignment, so it sits on or after the treatment path
- controlling for it would contaminate the total-effect estimate rather than clean it up
Common failure modes:
- treating any predictive metric as a safe control without checking measurement timing
- confusing post-treatment adjustment with confounder adjustment
Canonical answer object:
```json
{
  "label": "B",
  "should_control": false,
  "rationale": "Three-day engagement is measured after treatment assignment and lies on or after the treatment path. Conditioning on it would bias total effect estimation."
}
```

Model replies:
- Base primary: `no, post-treatment mediator` ✅
- Base follow-up: `engagement is downstream of treatment` ✅
- Skill primary: `no, post-treatment bad control` ✅
- Skill follow-up: `conditions on a downstream mediator` ✅

Judge notes: All four answers identify three-day engagement as downstream/post-treatment; the follow-ups give the bad-control reason that conditioning on it would bias the total-effect estimate.


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
