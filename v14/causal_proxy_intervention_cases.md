# v14 Causal / Proxy / Intervention Focus Pack

This focused pack adds harder public-dev cases for the benchmark slices where we expect stronger separation on causal reasoning, proxy routing, bridge-noise rejection, intervention supportability, and pressure-test design.

- Case count: `16`
- Split: `public_dev`
- Files: `causal_proxy_intervention_cases.json`, `causal_proxy_intervention_ground_truth.json`

## v14cpi_001 — Homebuilder Miss: Funding Stress Or Demand Softness?

- Track: `finance_and_business_causal_reasoning`
- Task family: `proxy_family_selection`
- Prompt style: `analyst_memo`
- Truth type: `hybrid_structured_review`

**Scenario**

A morning note combines mortgage data, builder credit signals, order metrics, and website activity after a homebuilder stock selloff.

**Question**

Which proxy family should you prioritize to explain the move, and what evidence would most directly falsify that read?

**Materials**

- `document_excerpt` — **Morning note**

The stock fell 11% after management guided to lower near-term orders. Analysts noted no major land or permitting update. Channel checks described buyer hesitation around monthly payments rather than reduced tour activity.

- `table` — **Market and operating snapshot**

30-year mortgage rate: +55 bps over 6 weeks. Mortgage applications: -12%. Builder CDS: +38 bps. Website traffic: -1%. Model-home visits: flat. Cancellation rate: +1.2 points. Backlog burn: stable.

**Options**

- `A`: Financing conditions and mortgage affordability are the cleaner proxy family.
- `B`: End-demand collapse is the cleaner proxy family.
- `C`: Land-supply constraints are the cleaner proxy family.
- `D`: Accounting noise is the cleaner proxy family.

**Ground truth**

```json
{
  "label": "A",
  "primary_proxy_family": "financing_conditions_and_mortgage_affordability",
  "falsifier": "orders_keep_deteriorating_even_if_rate_and_credit_proxies_normalize"
}
```

**Evidence summary**

- Mortgage affordability worsened materially while traffic and visits stayed roughly intact.
- Credit and rate signals moved sharply, which fits hesitation around financing more than collapse in underlying shopper interest.

**Common failure modes**

- Treating a modest cancellation increase as proof of broad demand collapse.
- Ignoring the sharper movement in mortgage-rate and credit proxies.

## v14cpi_002 — Alt-Token Slump: Base-Asset Weakness Or Liquidity Drain?

- Track: `finance_and_business_causal_reasoning`
- Task family: `proxy_family_selection`
- Prompt style: `analyst_memo`
- Truth type: `hybrid_structured_review`

**Scenario**

A crypto market packet compares majors, alt-token liquidity, on-chain activity, and exchange conditions after a sharp decline in a gaming token basket.

**Question**

Which proxy family is the cleaner starting point for the selloff, and what would most directly falsify that interpretation?

**Materials**

- `document_excerpt` — **Crypto desk note**

BTC and ETH were nearly flat on the day, but gaming and lower-liquidity alt tokens sold off hard. No exploit, governance failure, or delisting notice was reported for the focal token.

- `table` — **Cross-market snapshot**

BTC return: +0.3%. ETH return: +0.1%. Alt-token order-book depth: -35%. Perp funding on small tokens: sharply negative. Exchange maintenance on one retail-heavy venue: 2 hours. Game DAU: flat. On-chain fees for the project: flat.

**Options**

- `A`: Base-asset adoption is the cleaner proxy family.
- `B`: Retail liquidity and alt-beta risk appetite are the cleaner proxy family.
- `C`: A project-specific protocol exploit is the cleaner proxy family.
- `D`: Institutional ETF flows are the cleaner proxy family.

**Ground truth**

```json
{
  "label": "B",
  "primary_proxy_family": "retail_liquidity_and_alt_beta",
  "falsifier": "project_specific_activity_breaks_while_broad_alt_liquidity_normalizes"
}
```

**Evidence summary**

- Majors were stable while lower-liquidity books and alt funding deteriorated sharply.
- Project-specific usage stayed flat, which argues against a token-specific adoption collapse.

**Common failure modes**

- Projecting a broad BTC/ETH narrative onto a move that is concentrated in low-liquidity alt exposure.
- Assuming a hack or exploit without any evidence packet support.

## v14cpi_003 — Airline Selloff: Fuel Shock Or Demand Crack?

- Track: `finance_and_business_causal_reasoning`
- Task family: `proxy_family_selection`
- Prompt style: `analyst_memo`
- Truth type: `hybrid_structured_review`

**Scenario**

An airline equity drawdown arrives alongside a commodity move, while booking and traffic indicators are updated in the same note.

**Question**

Which proxy family should be treated as the primary causal read, and what would most clearly falsify it?

**Materials**

- `document_excerpt` — **Airline sector note**

The stock fell after a sharp move in energy markets. Management did not cut capacity or demand commentary, and no labor disruption was disclosed.

- `table` — **Operating and market snapshot**

Jet fuel crack spread: +18%. Front-month crude: +11%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue guidance: flat. Wage agreement updates: none. FX basket: flat.

**Options**

- `A`: Fuel and input-cost pressure are the primary proxy family.
- `B`: End-demand weakness is the primary proxy family.
- `C`: Labor disruption is the primary proxy family.
- `D`: FX translation is the primary proxy family.

**Ground truth**

```json
{
  "label": "A",
  "primary_proxy_family": "fuel_and_input_cost_pressure",
  "falsifier": "forward_bookings_or_unit_revenue_break_while_fuel_pressure_eases"
}
```

**Evidence summary**

- The sharpest moving variables are fuel-linked while bookings and unit-revenue guidance are stable.
- There is no evidence packet support for labor or FX being the dominant marginal driver.

**Common failure modes**

- Assuming all airline weakness is demand-driven without checking booking and unit-revenue evidence.
- Overweighting crude headlines without relating them to the actual airline cost channel.

## v14cpi_004 — Small-Cap Software De-Rate: Duration Pressure Or Product Trouble?

- Track: `finance_and_business_causal_reasoning`
- Task family: `proxy_family_selection`
- Prompt style: `analyst_memo`
- Truth type: `hybrid_structured_review`

**Scenario**

A software stock sells off with a broader factor move while company-specific operating metrics are also reported.

**Question**

Which proxy family is the cleaner explanation for the move, and what would most directly falsify that read?

**Materials**

- `document_excerpt` — **Software note**

The company reiterated annual ARR guidance and disclosed no outage, product recall, or major customer loss. The stock fell alongside a broader selloff in long-duration software names.

- `table` — **Factor and operating snapshot**

High-yield OAS: +75 bps. 10Y real yield: +19 bps. Small-cap software basket: -11%. ARR guidance: unchanged. Net revenue retention: 112% -> 111%. Churn: flat. Major incident count: 0.

**Options**

- `A`: Financing conditions and discount-rate duration are the cleaner proxy family.
- `B`: Product trouble is the cleaner proxy family.
- `C`: Channel inventory correction is the cleaner proxy family.
- `D`: Accounting restatement risk is the cleaner proxy family.

**Ground truth**

```json
{
  "label": "A",
  "primary_proxy_family": "financing_conditions_and_duration_pressure",
  "falsifier": "renewal_or_churn_metrics_break_even_if_credit_and_rate_proxies_stabilize"
}
```

**Evidence summary**

- Macro duration and credit-sensitive software factors moved sharply while company operating metrics were largely intact.
- The packet does not contain company-specific failure evidence strong enough to outrank the factor move.

**Common failure modes**

- Inventing product trouble from price action alone.
- Ignoring the explicit sector-factor de-rating in the evidence packet.

## v14cpi_005 — Soybean Rally And Snack-Maker Weakness

- Track: `finance_and_business_causal_reasoning`
- Task family: `bridge_noise_rejection`
- Prompt style: `analyst_memo`
- Truth type: `hybrid_structured_review`

**Scenario**

A consumer staples note lists several moving commodities, but only some sit on the company’s true cost path.

**Question**

Which candidate driver is most likely bridge noise rather than the core transmission channel?

**Materials**

- `document_excerpt` — **Staples note**

The stock traded lower after a basket of agricultural commodities moved higher. Management commentary emphasizes freight, packaging resin, palm oil, and cocoa as the main variable costs.

- `table` — **Cost exposure snapshot**

Soybeans: +9%. Palm oil: +4%. Cocoa: +6%. Packaging resin: +7%. Freight surcharge impact: +110 bps to COGS. Soy exposure in the focal brand mix: not material.

**Options**

- `A`: The soybean rally is most likely bridge noise rather than the core driver.
- `B`: Freight surcharges are most likely bridge noise rather than the core driver.
- `C`: Packaging-resin inflation is most likely bridge noise rather than the core driver.
- `D`: Palm-oil and cocoa costs are most likely bridge noise rather than the core driver.

**Ground truth**

```json
{
  "label": "A",
  "bridge_noise": "soybean_rally",
  "rationale_tag": "company_cost_structure_does_not_run_through_soybeans"
}
```

**Evidence summary**

- The note explicitly says soy is not a material input for the focal brand mix.
- Freight, resin, palm oil, and cocoa all sit more directly on the company cost path.

**Common failure modes**

- Equating any agricultural headline with causal relevance to a food stock.
- Picking the most visible market move instead of the cleanest company-specific transmission channel.

## v14cpi_006 — Regional Bank Stress And A Small-Cap SaaS Selloff

- Track: `graph_and_mechanism`
- Task family: `transmission_supportability`
- Prompt style: `analyst_memo`
- Truth type: `hybrid_structured_review`

**Scenario**

A software stock trades off during regional-bank stress even though the company has no direct deposit or lending disclosure in the packet.

**Question**

Which transmission path is the most supportable causal explanation?

**Materials**

- `document_excerpt` — **Market note**

The company stated that cash is spread across money-center banks and disclosed no unusual financing event. The stock still sold off with other long-duration software names when regional banks weakened.

- `table` — **Factor snapshot**

Regional bank ETF: -14%. Small-cap software basket: -9%. HY OAS: +48 bps. Company net cash: positive. Revenue guidance: unchanged.

**Options**

- `A`: No plausible path exists from regional-bank stress to the software stock.
- `B`: Direct deposit-loss exposure is the most supportable path.
- `C`: A valuation-duration and refinancing channel is the most supportable path.
- `D`: A hardware inventory channel is the most supportable path.

**Ground truth**

```json
{
  "label": "C",
  "mechanism": "valuation_duration_and_refinancing_channel",
  "supportability": "supported_but_indirect"
}
```

**Evidence summary**

- The packet rules out direct deposit exposure, but a broader risk and financing channel remains plausible.
- High-yield spreads widened and duration-sensitive software names sold off together.

**Common failure modes**

- Assuming no path simply because the company lacks direct bank exposure.
- Inventing a balance-sheet crisis despite the explicit net-cash note.

## v14cpi_007 — Rare-Earth Spike Into EV Gross Margin

- Track: `graph_and_mechanism`
- Task family: `transmission_strength_judgment`
- Prompt style: `mixed_modal_finance_qa`
- Truth type: `hybrid_structured_review`

**Scenario**

A commodity shock looks intuitively relevant, but the evidence packet includes cost-share and contracting details that constrain near-term transmission.

**Question**

How strong is the near-term transmission from rare-earth prices to the EV maker’s gross margin?

**Materials**

- `document_excerpt` — **Supply-chain note**

Rare-earth spot prices jumped after export restrictions. The automaker’s procurement note says the focal materials are covered by fixed contracts for the next two quarters.

- `table` — **Cost-structure snapshot**

Rare-earth component share of COGS: 1.2%. Fixed-price coverage horizon: 2 quarters. Battery metals and logistics remain the larger variable exposures.

**Options**

- `A`: It is a strong and immediate primary driver of gross margin.
- `B`: It is a moderate near-term driver, but not the dominant one.
- `C`: It is a weak, bridge-heavy near-term channel rather than a clean primary driver.
- `D`: No judgment of any kind is possible from the packet.

**Ground truth**

```json
{
  "label": "C",
  "transmission_strength": "weak_near_term",
  "blocking_factor": "fixed_contracts_and_low_cost_share"
}
```

**Evidence summary**

- The cost share is small and the contract coverage delays pass-through.
- The packet explicitly points to larger variable exposures elsewhere in the cost stack.

**Common failure modes**

- Overweighting the most dramatic commodity headline without checking cost share and contract timing.
- Calling the move impossible to assess despite clear packet constraints.

## v14cpi_008 — Biotech Rally: Primary Driver Or Pure Squeeze?

- Track: `natural_event_causality`
- Task family: `primary_driver_vs_amplifier`
- Prompt style: `news_narrative`
- Truth type: `expert_labeled`

**Scenario**

A market-news packet contains a regulatory catalyst, a later rumor, and evidence that short interest may have amplified the move.

**Question**

Which explanation best fits the move without overstating the evidence?

**Materials**

- `news_packet` — **Event timeline**

09:00: FDA advisory panel votes favorably on the therapy. 09:05: stock opens sharply higher. 12:10: an unconfirmed social-media rumor mentions a possible acquisition. Short interest entering the day was 24% of float.

- `table` — **Intraday move summary**

Open-to-10am move: +21%. Noon-to-close incremental move: +6%. Borrow fee: elevated. Company filings: no acquisition filing or comment.

**Options**

- `A`: The unconfirmed acquisition rumor is the primary driver.
- `B`: Short-squeeze dynamics are the primary driver, with no stronger causal event in the packet.
- `C`: The FDA advisory-panel vote is the primary driver, while squeeze dynamics likely amplified the move.
- `D`: No supportable causal read is possible from the packet.

**Ground truth**

```json
{
  "label": "C",
  "primary_driver": "fda_advisory_panel_vote",
  "amplifier": "short_squeeze_dynamics"
}
```

**Evidence summary**

- Most of the move occurred immediately after the regulatory event and before the rumor appeared.
- Short interest can explain amplification without replacing the primary catalyst.

**Common failure modes**

- Treating the later rumor as primary despite the timing mismatch.
- Collapsing primary driver and amplifier into the same answer.

## v14cpi_009 — Price Cut And Sales-Comp Rewrite In The Same Week

- Track: `industrial_intervention_and_estimation`
- Task family: `bundled_intervention_supportability`
- Prompt style: `study_design_prompt`
- Truth type: `expert_labeled`

**Scenario**

Leadership wants the effect of a price cut on unit sales, but the operating packet shows another major commercial intervention at the same time and in the same weak regions.

**Question**

Is the causal effect of the price cut on units identified from the observed packet?

**Materials**

- `document_excerpt` — **Commercial rollout note**

The company reduced list price by 8% in the weakest four regions and simultaneously changed sales compensation to reward unit volume instead of gross profit dollars.

- `table` — **Observed outcome summary**

The treated regions saw unit growth accelerate after the rollout. Untreated regions kept the old price and old comp plan. No randomization or staggered timing was used.

**Options**

- `A`: Yes. A simple before/after comparison identifies the price effect.
- `B`: Yes. Region controls are enough to identify the price effect.
- `C`: No. The packet bundles two interventions on selected weak regions.
- `D`: Yes. A treated-vs-untreated snapshot identifies the price effect.

**Ground truth**

```json
{
  "label": "C",
  "identified": false,
  "blocking_issue": "bundled_intervention_and_targeted_rollout"
}
```

**Evidence summary**

- Price and comp changed together on the same weak regions, so the packet does not isolate price alone.
- There is no randomization or staggered variation to separate the two levers cleanly.

**Common failure modes**

- Treating any untreated region as a valid control despite targeted rollout.
- Ignoring the incentive-plan rewrite because the price cut feels more salient.

## v14cpi_010 — Predictive Maintenance Rolled Out To The Worst Plants First

- Track: `industrial_intervention_and_estimation`
- Task family: `targeted_rollout_design_choice`
- Prompt style: `study_design_prompt`
- Truth type: `expert_labeled`

**Scenario**

A maintenance model was adopted first where failures were already highest, and leadership wants a credible evaluation design.

**Question**

Which design is most defensible for estimating the model’s effect, and what is the main threat to validity?

**Materials**

- `operational_log` — **Rollout summary**

The predictive-maintenance model was launched first at plants with the highest prior failure rates. Failure rates fell after deployment, but the untreated plants were lower-risk to begin with.

- `table` — **Plant summary**

Four treated plants adopted in month 1, four control plants remained on the old process. Treated plants started with materially worse pre-period failure levels.

**Options**

- `A`: A simple before/after comparison is the most defensible design.
- `B`: A matched or staggered difference-in-differences event study with pretrend checks is the most defensible design.
- `C`: A post-only treated-vs-control cross-section is the most defensible design.
- `D`: Instrumenting treatment with plant size is the most defensible design.

**Ground truth**

```json
{
  "label": "B",
  "design": "matched_or_staggered_difference_in_differences_event_study",
  "main_threat": "targeted_rollout_and_regression_to_mean"
}
```

**Evidence summary**

- The rollout is non-random and correlated with pre-period failure levels.
- A DID/event-study framing is the cleanest public-dev answer because it explicitly tests pretrends and uses staggered structure when available.

**Common failure modes**

- Choosing before/after because failures visibly fell.
- Ignoring regression to the mean in a targeted rollout.

## v14cpi_011 — Credit-Limit Increases For Prequalified Users

- Track: `industrial_intervention_and_estimation`
- Task family: `selection_bias_supportability`
- Prompt style: `study_design_prompt`
- Truth type: `expert_labeled`

**Scenario**

A consumer-finance team increased credit limits only for users already scored as especially attractive, then asked for the treatment effect on purchase frequency.

**Question**

Can the treated-vs-untreated mean difference identify the effect on purchase frequency?

**Materials**

- `document_excerpt` — **Risk-team note**

Only prequalified users with high internal scores received the limit increase. The untreated pool contains more low-score and lower-spend customers.

- `table` — **Outcome summary**

Treated users increased purchase frequency after the offer. Current observables include age bucket, region, and merchant mix, but not latent spending appetite or the full internal scorecard.

**Options**

- `A`: Yes. The treated-vs-untreated mean difference identifies the treatment effect.
- `B`: Yes. The current covariates are enough to remove the bias.
- `C`: No. Selection on latent spending propensity still blocks identification.
- `D`: Yes. Stable merchant mix is sufficient to identify the effect.

**Ground truth**

```json
{
  "label": "C",
  "identified": false,
  "blocking_issue": "selection_on_latent_purchase_propensity"
}
```

**Evidence summary**

- Treatment assignment depends on an internal score that the analyst does not fully observe.
- The untreated pool differs on the same latent propensity that likely affects future purchases.

**Common failure modes**

- Assuming any observed covariates guarantee ignorability.
- Treating stable merchant mix as a substitute for assignment information.

## v14cpi_012 — Warehouse Expedite Policy And Temporary Staffing

- Track: `industrial_intervention_and_estimation`
- Task family: `simultaneous_operations_change`
- Prompt style: `study_design_prompt`
- Truth type: `expert_labeled`

**Scenario**

An operations packet shows late shipments falling after a new expedite policy, but staffing changed in the same window.

**Question**

Is the expedite-policy effect identified from the observed packet, and what is the most important confound?

**Materials**

- `operational_log` — **Operations note**

A warehouse introduced a new expedite policy during peak season. The same week, temporary staffing was increased by 18% and overtime rules were relaxed.

- `table` — **Late-shipment summary**

Late shipments fell from 9.4% to 6.7% after the policy week. No site-level stagger or holdout group is available in the packet.

**Options**

- `A`: Yes. Staffing is too small to matter here.
- `B`: Yes. Controlling for shift is enough to identify the policy effect.
- `C`: No. The simultaneous temporary-staffing change is the key confound.
- `D`: No. The outcome metric itself is unusable.

**Ground truth**

```json
{
  "label": "C",
  "identified": false,
  "blocking_issue": "simultaneous_temporary_staffing_change"
}
```

**Evidence summary**

- The packet changes operational capacity and expedite rules together in the same window.
- Without staggered adoption or a holdout, attribution to expedite policy alone is not supportable.

**Common failure modes**

- Treating the bigger named intervention as the only causal lever.
- Assuming a good outcome metric implies clean identification.

## v14cpi_013 — Which First Pressure Test Separates Financing Stress From Demand Softness?

- Track: `agentic_live_analysis`
- Task family: `pressure_test_design`
- Prompt style: `agent_brief`
- Truth type: `hybrid_structured_review`

**Scenario**

A distributor note leaves two live stories on the table, and the task is to pick the first stress lever that would most efficiently separate them.

**Question**

Which first pressure test would best separate financing stress from demand softness?

**Materials**

- `document_excerpt` — **Agent brief**

Rate-sensitive customer verticals have slowed, but service attach and installed-base usage remain stable. Credit spreads widened and management said quote activity was healthy but close timing stretched.

- `table` — **Commercial snapshot**

New orders: -4%. Cancellations: +2 points. Service attach: flat. Installed-base usage: flat. HY OAS: +62 bps. Accounts receivable days: +4 days.

**Options**

- `A`: Stress commodity input costs and inspect gross margin.
- `B`: Stress financing conditions and inspect orders plus cancellations.
- `C`: Stress FX and inspect backlog conversion.
- `D`: Stress labor availability and inspect headcount growth.

**Ground truth**

```json
{
  "label": "B",
  "stress_target": "financing_conditions",
  "readout": "order_intake_and_cancellations"
}
```

**Evidence summary**

- The open causal split is financing friction versus true demand softness.
- Orders and cancellations are the closest downstream variables for distinguishing the two stories after stressing financing conditions.

**Common failure modes**

- Choosing a lever unrelated to the live uncertainty.
- Looking at margin before testing the order-flow channel that actually separates the stories.

## v14cpi_014 — Fuel Shock Or Demand Weakness: Which Probe Comes First?

- Track: `agentic_live_analysis`
- Task family: `pressure_test_design`
- Prompt style: `agent_brief`
- Truth type: `hybrid_structured_review`

**Scenario**

An airline packet leaves cost shock and demand weakness as competing stories, and the task is to choose the first clean pressure test.

**Question**

Which first pressure test most cleanly distinguishes fuel shock from demand weakness?

**Materials**

- `document_excerpt` — **Agent brief**

The stock sold off with energy markets. Forward bookings and capacity plans held steady. Analysts want the first probe that would most quickly separate cost pressure from true demand deterioration.

- `table` — **Sector snapshot**

Jet fuel crack: +18%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue: flat. FX: flat.

**Options**

- `A`: Stress jet-fuel costs and inspect unit margin or EPS sensitivity.
- `B`: Stress load factor and inspect fuel hedges.
- `C`: Stress FX and inspect baggage-fee revenue.
- `D`: Stress wage inflation and inspect loyalty signups.

**Ground truth**

```json
{
  "label": "A",
  "stress_target": "jet_fuel_costs",
  "readout": "unit_margin_or_eps_sensitivity"
}
```

**Evidence summary**

- The packet already shows stable demand-side evidence and a large energy move.
- Margin and EPS sensitivity are the most direct downstream readouts of a fuel-cost stress.

**Common failure modes**

- Choosing a demand-side probe despite the packet already showing stable booking evidence.
- Picking a variable that is not downstream of the suspected cost channel.

## v14cpi_015 — EV Supplier Drop: Lithium Pass-Through Or Customer Inventory Reset?

- Track: `agentic_live_analysis`
- Task family: `pressure_test_design`
- Prompt style: `agent_brief`
- Truth type: `hybrid_structured_review`

**Scenario**

A supplier stock weakens while both upstream commodity and downstream customer signals are moving, and the analyst must pick the first separating probe.

**Question**

Which first pressure test best distinguishes lithium pass-through from customer inventory reset?

**Materials**

- `document_excerpt` — **Agent brief**

Lithium prices softened, but customer inventory days also rose across two major OEMs. The supplier guides to softer near-term shipments without changing long-run content assumptions.

- `table` — **Supplier snapshot**

Lithium spot: -14%. Customer inventory days: +11 days. OEM production schedules: trimmed for next quarter. Supplier gross-margin guide: only modestly lower. Backlog conversion: slowing.

**Options**

- `A`: Stress lithium prices and inspect next-quarter gross margin.
- `B`: Stress customer inventory and build schedules, then inspect shipments and backlog conversion.
- `C`: Stress FX and inspect operating expenses.
- `D`: Stress energy prices and inspect depreciation.

**Ground truth**

```json
{
  "label": "B",
  "stress_target": "customer_inventory_reset",
  "readout": "shipments_and_backlog_conversion"
}
```

**Evidence summary**

- Customer inventory and build schedules are the variables most directly tied to the supplier’s shipment softness in the packet.
- Lithium softness alone does not explain a slower backlog conversion nearly as cleanly.

**Common failure modes**

- Defaulting to the flashier commodity move instead of the more direct downstream transmission path.
- Reading margin before checking the shipment path that actually distinguishes the stories.

## v14cpi_016 — Residential Solar Miss: Policy Step-Down Or Sales Execution?

- Track: `agentic_live_analysis`
- Task family: `pressure_test_design`
- Prompt style: `agent_brief`
- Truth type: `hybrid_structured_review`

**Scenario**

The packet leaves policy and execution stories both live, and the evaluation asks for the cleanest first probe to challenge the leading thesis.

**Question**

Which pressure test most directly challenges the thesis that policy incentive step-down is the main driver?

**Materials**

- `document_excerpt` — **Agent brief**

Order volume weakened after a state incentive step-down, but channel checks also mention elevated rep turnover and slower lead follow-up times.

- `table` — **Sales funnel snapshot**

Lead volume: -3%. Lead-to-booking conversion: -16%. Incentive value: -22%. Sales-rep turnover: +8 points. Follow-up time: slower by 1.4 days.

**Options**

- `A`: Stress incentive-policy generosity and inspect lead-to-booking conversion.
- `B`: Stress panel input costs and inspect gross margin.
- `C`: Stress installer hiring and inspect warehouse rent.
- `D`: Stress bitcoin and inspect lead generation.

**Ground truth**

```json
{
  "label": "A",
  "stress_target": "incentive_policy_generosity",
  "readout": "lead_to_booking_conversion"
}
```

**Evidence summary**

- The leading thesis is specifically about incentive generosity, so the cleanest challenge is to stress that lever and inspect the conversion step most directly tied to purchase economics.
- Lead volume moved far less than conversion, which makes the conversion readout more decision-relevant than top-of-funnel traffic.

**Common failure modes**

- Choosing a lever that is unrelated to the stated uncertainty.
- Looking at margin instead of the funnel step most exposed to incentive economics.
