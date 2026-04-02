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

## Case Overview

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

## Full Cases

### v14i_001 — Three Plausible Stories, One Dominant Driver

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
Follow-up question: What is the most important next verification or uncertainty to keep live?

Evidence packet:
- Analyst note (document_excerpt): Management cited three factors for the quarter: a one-point constant-currency headwind, a 40 bps legal reserve, and weaker channel sell-through that pushed inventory days higher.
- Operating summary (table): Revenue miss versus plan: -6%. Constant-currency impact: -1 point. Legal reserve impact on operating margin: -0.4 points. Channel inventory days: +12 days. End-market sell-through: -9%.

Naturalness rationale: Looks like a normal analyst disagreement about explanations and what to verify next, rather than a graph or skill operation.

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
- Base primary: `weak sell-through driving inventory build` ✅
- Base follow-up: `sell-through and inventory days` ✅
- Skill primary: `channel destocking` ✅
- Skill follow-up: `watch sell-through and inventory days` ✅

Judge notes: Base matches weak sell-through plus inventory correction; skill's channel destocking is acceptable shorthand for the same dominant story. Both follow-ups name the key discriminators: sell-through and inventory-days normalization.

### v14i_003 — Build The Event Memo, Not Just The Answer

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

Naturalness rationale: Looks like a normal analyst disagreement about explanations and what to verify next, rather than a graph or skill operation.

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
- Base primary: `deposit competition squeezing funding costs` ✅
- Base follow-up: `primary-source capital raise confirmation` ❌
- Skill primary: `deposit-cost pressure` ✅
- Skill follow-up: `check for capital-raise filings` ❌

Judge notes: Both primaries capture funding-cost/deposit-beta pressure. Both follow-ups miss the needed verification of uninsured-deposit mix or wholesale-funding dependence and instead focus on capital-raise confirmation/filings.

### v14i_004 — One Event, Multiple Conflicting Narratives

- Source case: `v14d_021`
- Family: `cross_source_event_integration`
- Exact winner: `tie`
- Base exact: `incorrect`
- Skill exact: `incorrect`
- Base field score: `1/2`
- Skill field score: `1/2`

Scenario:
A live case includes conflicting media explanations, partial company commentary, and market reaction across related assets.

Primary question: What is the most causally plausible primary driver of the rally?
Follow-up question: What uncertainty or alternative is still live enough to monitor?

Evidence packet:
- Snippet 1 (retrieval_bundle): A biotech stock rallied after an FDA advisory panel voted in favor of its therapy.
- Snippet 2 (retrieval_bundle): Social media accounts also circulated an acquisition rumor, but no credible outlet confirmed it.
- Snippet 3 (retrieval_bundle): Short interest was elevated heading into the vote, which may have amplified the magnitude of the move.

Naturalness rationale: Looks like a normal analyst disagreement about explanations and what to verify next, rather than a graph or skill operation.

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
- Base primary: `favorable FDA panel vote` ✅
- Base follow-up: `watch for credible M&A confirmation` ❌
- Skill primary: `positive FDA panel vote` ✅
- Skill follow-up: `watch credible M&A confirmation` ❌

Judge notes: Both primaries correctly identify the FDA panel vote as the main driver. Both follow-ups chase M&A rumor rather than the live canonical uncertainty of short-squeeze amplification via timing and short-interest checks.

### v14i_005 — Homebuilder Miss: Funding Stress Or Demand Softness?

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
Follow-up question: What would make you revisit that view first?

Evidence packet:
- Morning note (document_excerpt): The stock fell 11% after management guided to lower near-term orders. Analysts noted no major land or permitting update. Channel checks described buyer hesitation around monthly payments rather than reduced tour activity.
- Market and operating snapshot (table): 30-year mortgage rate: +55 bps over 6 weeks. Mortgage applications: -12%. Builder CDS: +38 bps. Website traffic: -1%. Model-home visits: flat. Cancellation rate: +1.2 points. Backlog burn: stable.

Naturalness rationale: Looks like a normal analyst disagreement about explanations and what to verify next, rather than a graph or skill operation.

Ground truth:
- Canonical primary: `financing conditions and mortgage affordability`
- Canonical follow-up: `if orders stay weak after financing proxies normalize, demand softness gains weight`
Evidence summary:
- Mortgage affordability worsened materially while traffic and visits stayed roughly intact.
- Credit and rate signals moved sharply, which fits hesitation around financing more than collapse in underlying shopper interest.
Common failure modes:
- Treating a modest cancellation increase as proof of broad demand collapse.
- Ignoring the sharper movement in mortgage-rate and credit proxies.
Canonical answer object:
```json
{
  "label": "A",
  "primary_proxy_family": "financing_conditions_and_mortgage_affordability",
  "falsifier": "orders_keep_deteriorating_even_if_rate_and_credit_proxies_normalize"
}
```

Model replies:
- Base primary: `affordability-driven order softness` ✅
- Base follow-up: `watch CDS and land/permitting changes` ❌
- Skill primary: `affordability-driven demand softness` ✅
- Skill follow-up: `watch builder CDS and debt access` ❌

Judge notes: Both primaries are close enough because they anchor the move to affordability/financing stress rather than a broad collapse in shopper interest. Neither follow-up gives the discriminating test of whether orders stay weak after financing proxies normalize.

### v14i_006 — Regional Bank Stress And A Small-Cap SaaS Selloff

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

Naturalness rationale: Looks like a normal analyst disagreement about explanations and what to verify next, rather than a graph or skill operation.

Ground truth:
- Canonical primary: `valuation-duration and refinancing channel`
- Canonical follow-up: `watch spreads and duration-sensitive peers while company metrics stay intact`
Evidence summary:
- The packet rules out direct deposit exposure, but a broader risk and financing channel remains plausible.
- High-yield spreads widened and duration-sensitive software names sold off together.
Common failure modes:
- Assuming no path simply because the company lacks direct bank exposure.
- Inventing a balance-sheet crisis despite the explicit net-cash note.
Canonical answer object:
```json
{
  "label": "C",
  "mechanism": "valuation_duration_and_refinancing_channel",
  "supportability": "supported_but_indirect"
}
```

Model replies:
- Base primary: `credit-tightening duration derating` ✅
- Base follow-up: `watch HY OAS and SaaS peer correlation` ✅
- Skill primary: `credit-spread multiple compression` ✅
- Skill follow-up: `watch HY OAS and SaaS peers` ✅

Judge notes: Both capture the bank-stress transmission as a broad credit/duration de-rating rather than direct exposure; the follow-ups correctly point to HY spreads and duration-sensitive SaaS peer behavior as the key arbiters.

### v14i_007 — Airline Selloff: Fuel Shock Or Demand Crack?

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

Naturalness rationale: Looks like a normal analyst disagreement about explanations and what to verify next, rather than a graph or skill operation.

Ground truth:
- Canonical primary: `fuel and input-cost pressure`
- Canonical follow-up: `if bookings or unit revenue break while fuel pressure eases`
Evidence summary:
- The sharpest moving variables are fuel-linked while bookings and unit-revenue guidance are stable.
- There is no evidence packet support for labor or FX being the dominant marginal driver.
Common failure modes:
- Assuming all airline weakness is demand-driven without checking booking and unit-revenue evidence.
- Overweighting crude headlines without relating them to the actual airline cost channel.
Canonical answer object:
```json
{
  "label": "A",
  "primary_proxy_family": "fuel_and_input_cost_pressure",
  "falsifier": "forward_bookings_or_unit_revenue_break_while_fuel_pressure_eases"
}
```

Model replies:
- Base primary: `jet fuel cost shock` ✅
- Base follow-up: `watch bookings and unit revenue guidance` ✅
- Skill primary: `fuel-cost squeeze` ✅
- Skill follow-up: `watch bookings and unit revenue` ✅

Judge notes: Both correctly read the selloff through fuel/input-cost pressure, and both follow-ups use bookings/unit revenue as the concrete evidence that would flip the read toward demand.

### v14i_008 — Small-Cap Software De-Rate: Duration Pressure Or Product Trouble?

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

Naturalness rationale: Looks like a normal analyst disagreement about explanations and what to verify next, rather than a graph or skill operation.

Ground truth:
- Canonical primary: `duration pressure and financing conditions`
- Canonical follow-up: `if renewal or churn metrics break while rates and credit stabilize`
Evidence summary:
- Macro duration and credit-sensitive software factors moved sharply while company operating metrics were largely intact.
- The packet does not contain company-specific failure evidence strong enough to outrank the factor move.
Common failure modes:
- Inventing product trouble from price action alone.
- Ignoring the explicit sector-factor de-rating in the evidence packet.
Canonical answer object:
```json
{
  "label": "A",
  "primary_proxy_family": "financing_conditions_and_duration_pressure",
  "falsifier": "renewal_or_churn_metrics_break_even_if_credit_and_rate_proxies_stabilize"
}
```

Model replies:
- Base primary: `duration pressure, not product trouble` ✅
- Base follow-up: `watch NRR/churn and customer losses` ✅
- Skill primary: `duration pressure over product trouble` ✅
- Skill follow-up: `guidance cut or churn spike` ✅

Judge notes: Both identify the cleaner explanation as macro duration/factor pressure rather than product trouble; the follow-ups appropriately focus on churn/retention-type deterioration as the idiosyncratic breaker.

### v14i_009 — Rare-Earth Spike Into EV Gross Margin

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

Naturalness rationale: Looks like a normal analyst disagreement about explanations and what to verify next, rather than a graph or skill operation.

Ground truth:
- Canonical primary: `weak near-term pass-through because contracts and cost share limit it`
- Canonical follow-up: `verify contract coverage or cost share before promoting the shock`
Evidence summary:
- The cost share is small and the contract coverage delays pass-through.
- The packet explicitly points to larger variable exposures elsewhere in the cost stack.
Common failure modes:
- Overweighting the most dramatic commodity headline without checking cost share and contract timing.
- Calling the move impossible to assess despite clear packet constraints.
Canonical answer object:
```json
{
  "label": "C",
  "transmission_strength": "weak_near_term",
  "blocking_factor": "fixed_contracts_and_low_cost_share"
}
```

Model replies:
- Base primary: `limited near-term margin impact` ✅
- Base follow-up: `verify contract roll-off and availability` ✅
- Skill primary: `minimal near-term margin hit` ✅
- Skill follow-up: `contract rollover and supply availability` ✅

Judge notes: Both preserve the core point that the rare-earth shock should have limited near-term margin impact; the follow-ups correctly focus on contract timing/coverage, with extra supply checks not negating the main discriminator.


## Per-Family

- `analyst_workflow_agent`: base exact `0/1`, skill exact `0/1`
- `cross_source_event_integration`: base exact `0/1`, skill exact `0/1`
- `multi_factor_finance_synthesis`: base exact `1/1`, skill exact `1/1`
- `proxy_family_selection`: base exact `2/3`, skill exact `2/3`
- `transmission_strength_judgment`: base exact `1/1`, skill exact `1/1`
- `transmission_supportability`: base exact `1/1`, skill exact `1/1`
