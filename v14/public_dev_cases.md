# v14 Public Dev Cases

This markdown expands every public-dev case with its question and ground truth.

## v14d_001 — Campaign Lift With A Hidden Seasonal Driver

- Track: `formal_causality`
- Truth type: `oracle_graph`
- Prompt style: `naturalized_graph_question`
- Task family: `backdoor_adjustment`
- Evaluation regime: `unspecified`

Scenario:
```text
A business DAG is given for campaign exposure, site traffic, conversion, and seasonality. The case asks whether the effect of the campaign on conversion is identifiable and what should be adjusted for.
```

Question:
```text
Which adjustment set, if any, identifies the causal effect of campaign exposure on conversion?
```

Options:
- `A`: No adjustment is needed.
- `B`: Adjust for site_visits only.
- `C`: Adjust for seasonality only.
- `D`: Adjust for seasonality and site_visits.
- `E`: The total effect is not identifiable from observed variables.

Materials:
- `causal_graph` — Observed DAG
```text
Nodes: campaign_exposure, site_visits, conversion, seasonality. Edges: seasonality -> campaign_exposure; seasonality -> conversion; campaign_exposure -> site_visits; site_visits -> conversion; campaign_exposure -> conversion. All nodes are observed.
```
- `document_excerpt` — Measurement note
```text
Seasonality is measured before campaigns launch. Site visits are recorded after campaign exposure and before conversion.
```

Ground truth:
```json
{
  "label": "C",
  "identified": true,
  "adjustment_set": [
    "seasonality"
  ],
  "rationale": "Seasonality is the backdoor confounder. Site_visits lies on the causal pathway and should not be adjusted when estimating the total effect."
}
```

## v14d_002 — Would Outcome Y Have Changed Under Do(X)?

- Track: `formal_causality`
- Truth type: `oracle_graph`
- Prompt style: `naturalized_graph_question`
- Task family: `counterfactual_with_delexicalization`
- Evaluation regime: `unspecified`

Scenario:
```text
A delexicalized counterfactual case uses nonsense variable names so that the model cannot rely on prior semantic associations.
```

Question:
```text
Given the observed facts and the graph, would Y still have occurred if X had been set to 0?
```

Options:
- `A`: Yes, Y would still have occurred under do(X=0).
- `B`: No, Y would not have occurred under do(X=0).
- `C`: The counterfactual is not identifiable from the information given.

Materials:
- `causal_graph` — SCM graph
```text
Binary variables with edges X -> M -> Y and Z -> Y. No hidden confounding is assumed.
```
- `document_excerpt` — Structural equations and observations
```text
M := X. Y := M OR Z. Observed facts: X=1, Z=0, therefore M=1 and Y=1.
```

Ground truth:
```json
{
  "label": "B",
  "counterfactual_outcome": 0,
  "rationale": "Under do(X=0), M becomes 0. Because Z is observed to be 0, Y = 0 OR 0 = 0, so Y would not occur."
}
```

## v14d_003 — A Strong Association But No Direct Effect

- Track: `formal_causality`
- Truth type: `oracle_graph`
- Prompt style: `naturalized_graph_question`
- Task family: `correlation_vs_causation_discrimination`
- Evaluation regime: `unspecified`

Scenario:
```text
A short report describes a strong observational association between two business metrics, but the graph shows a shared upstream driver.
```

Question:
```text
Is the claim 'X causes Y' supported, unsupported, or contradicted by the structure?
```

Options:
- `A`: Supported: X has a causal effect on Y, but only indirectly.
- `B`: Unsupported: the graph shows association only, not causation.
- `C`: Contradicted: the graph rules out any causal effect from X to Y.

Materials:
- `causal_graph` — Observed structure
```text
Edges: Z -> X, Z -> Y, X -> M, M -> Y. There is no direct edge X -> Y.
```
- `table` — Association snapshot
```text
Observed data show P(Y=1 | X=1)=0.70 and P(Y=1 | X=0)=0.30.
```

Ground truth:
```json
{
  "label": "A",
  "effect_type": "indirect_causal_effect",
  "rationale": "X affects Y through the mediator M. The lack of a direct edge does not remove the indirect causal path."
}
```

## v14d_004 — Which Node Is Acting As The Mediator?

- Track: `graph_and_mechanism`
- Truth type: `oracle_graph`
- Prompt style: `graph_query`
- Task family: `mediator_vs_confounder_identification`
- Evaluation regime: `unspecified`

Scenario:
```text
The case presents a graph and a natural-language description of a mechanism linking price, demand, and margin.
```

Question:
```text
Which node is the mediator between price change and margin change?
```

Materials:
- `causal_graph` — Mechanism graph
```text
Edges: price_change -> unit_volume, unit_volume -> freight_cost, unit_volume -> gross_margin, freight_cost -> gross_margin, cost_inflation -> freight_cost, cost_inflation -> gross_margin.
```
- `document_excerpt` — Narrative description
```text
Management says the price change first altered unit volume, which then affected both shipping intensity and margin realization.
```

Ground truth:
```json
{
  "mediator_node": "unit_volume",
  "mechanism_path": [
    "price_change",
    "unit_volume",
    "gross_margin"
  ]
}
```

## v14d_005 — Can This Effect Be Reached Through Any Directed Path?

- Track: `graph_and_mechanism`
- Truth type: `oracle_graph`
- Prompt style: `graph_query`
- Task family: `path_supportability`
- Evaluation regime: `unspecified`

Scenario:
```text
A graph and a short product-growth story are both provided. The model must decide whether a claimed effect is structurally reachable.
```

Question:
```text
Is there a directed causal path from the intervention node to the stated outcome node?
```

Materials:
- `causal_graph` — Service graph
```text
Edges: supplier_delay -> stockout -> fulfillment_delay -> customer_complaints -> churn. Also marketing_spend -> new_customers and price_discount -> new_customers. No arrows lead from marketing_spend or price_discount into churn through the service chain.
```

Ground truth:
```json
{
  "reachable": true,
  "example_path": [
    "supplier_delay",
    "stockout",
    "fulfillment_delay",
    "customer_complaints",
    "churn"
  ],
  "rationale": "A fully directed service-failure path exists from supplier_delay to churn."
}
```

## v14d_006 — Same Graph, Different Encoding

- Track: `graph_and_mechanism`
- Truth type: `oracle_graph`
- Prompt style: `graph_query`
- Task family: `encoding_invariance`
- Evaluation regime: `unspecified`

Scenario:
```text
The same causal graph is shown in two encodings: adjacency-list style and narrative description. The model should reach the same conclusion.
```

Question:
```text
Do the two graph encodings imply the same answer to the causal query?
```

Options:
- `A`: promo_discount
- `B`: macro_demand
- `C`: inventory_constraint
- `D`: visits

Materials:
- `causal_graph` — Encoding A: adjacency list
```text
macro_demand -> ad_spend; macro_demand -> sales; ad_spend -> visits; visits -> sales; promo_discount -> visits; inventory_constraint -> sales.
```
- `narrative` — Encoding B: paragraph
```text
When macro demand strengthens, the company spends more on ads and would have sold more even without those extra ads. Ads increase visits, and visits help sales. Promotions also lift visits, while inventory constraints can cap sales.
```
- `document_excerpt` — Question focus
```text
Identify the node that is the confounder for the relationship between ad_spend and sales across both encodings.
```

Ground truth:
```json
{
  "label": "B",
  "confounder": "macro_demand",
  "rationale": "Macro demand causes both ad_spend and sales. The answer should stay the same under either encoding."
}
```

## v14d_007 — A/B Test With A Post-Treatment Metric

- Track: `data_grounded_causal_reasoning`
- Truth type: `programmatic_from_data`
- Prompt style: `table_qa`
- Task family: `post_treatment_control_trap`
- Evaluation regime: `unspecified`

Scenario:
```text
An experiment report includes treatment assignment, conversion, and an engagement metric that is measured after treatment.
```

Question:
```text
Should the engagement metric be controlled for when estimating the treatment effect on conversion?
```

Options:
- `A`: Yes. Control for engagement because it predicts conversion.
- `B`: No. Engagement is post-treatment and should not be controlled for.
- `C`: Yes, but only to improve precision without affecting identification.
- `D`: The treatment effect is unidentifiable no matter what is done.

Materials:
- `table` — Experiment summary
```text
Rows: control, treatment. Columns: assigned_users, conversions, three_day_engagement_score. The engagement score is measured only after assignment and after users see the experience.
```
- `document_excerpt` — Metric definitions
```text
Conversion is the primary endpoint. Three-day engagement is computed from post-assignment behavior inside the product.
```

Ground truth:
```json
{
  "label": "B",
  "should_control": false,
  "rationale": "Three-day engagement is measured after treatment assignment and lies on or after the treatment path. Conditioning on it would bias total effect estimation."
}
```

## v14d_008 — The Aggregate Says Yes, The Strata Say No

- Track: `data_grounded_causal_reasoning`
- Truth type: `programmatic_from_data`
- Prompt style: `table_qa`
- Task family: `simpsons_paradox_causal_read`
- Evaluation regime: `unspecified`

Scenario:
```text
A table shows an overall performance lift but subgroup breakdowns move in the opposite direction due to a composition shift.
```

Question:
```text
Is the aggregate increase sufficient evidence of a positive causal effect?
```

Options:
- `A`: Treatment helps both overall and within each segment.
- `B`: Treatment looks better in aggregate but performs worse within both segments because the traffic mix changed.
- `C`: Treatment is worse overall but better within both segments.
- `D`: No conclusion can be drawn from the table.

Materials:
- `table` — Segmented conversion table
```text
Novice users: control 18/100 convert, treatment 15/100 convert. Expert users: control 70/100 convert, treatment 66/100 convert. Mixture: treatment traffic is disproportionately expert-heavy, so the aggregate treatment conversion rate appears higher than the aggregate control rate.
```
- `document_excerpt` — Assignment note
```text
The treatment was rolled out more aggressively to expert users after a manual allocation decision.
```

Ground truth:
```json
{
  "label": "B",
  "segment_conclusion": "simpsons_paradox_due_to_segment_mix",
  "rationale": "Within both novice and expert strata, treatment underperforms. The aggregate improvement is driven by the treated group containing more high-converting experts."
}
```

## v14d_009 — Margin Expansion After A Pricing Change

- Track: `data_grounded_causal_reasoning`
- Truth type: `hybrid_structured_review`
- Prompt style: `mixed_modal_finance_qa`
- Task family: `finance_table_causal_interpretation`
- Evaluation regime: `unspecified`

Scenario:
```text
A finance table and a short memo summarize unit volume, realized price, marketing spend, and gross margin before and after a pricing policy change.
```

Question:
```text
Which variable most plausibly mediates the effect of the pricing change on gross margin?
```

Options:
- `A`: The pricing change clearly caused the full margin expansion.
- `B`: The margin expansion cannot be attributed solely to pricing because input costs also moved materially.
- `C`: The company must have cut price because volume fell.
- `D`: No causal statement of any kind is possible here.

Materials:
- `table` — Before/after KPI snapshot
```text
List price +2.0%; unit volume -1.0%; input cost per unit -4.0%; gross margin +3.0 percentage points; competitor prices flat.
```
- `document_excerpt` — Management note
```text
A commodity hedge rolled in during the same quarter and materially reduced input costs. Management warns that the margin benefit should not be attributed to pricing alone.
```

Ground truth:
```json
{
  "label": "B",
  "supportability": "price_not_sufficient_explanation",
  "rationale": "Pricing and input-cost relief moved at the same time. The packet supports a mixed explanation, not a pricing-only causal claim."
}
```

## v14d_010 — Which Event Actually Drove The Shortage?

- Track: `natural_event_causality`
- Truth type: `expert_labeled`
- Prompt style: `news_narrative`
- Task family: `event_chain_attribution`
- Evaluation regime: `unspecified`

Scenario:
```text
A short news packet describes weather disruptions, port congestion, and inventory shortages across several paragraphs.
```

Question:
```text
Which event is the most likely direct driver of the final shortage event?
```

Options:
- `A`: The typhoon was the most direct driver of the shortage.
- `B`: Port congestion was the most direct driver of the shortage.
- `C`: The distribution-center scanner outage was the most direct driver of the shortage.
- `D`: Seasonal demand was the most direct driver of the shortage.

Materials:
- `news_packet` — Excerpt 1
```text
A typhoon delayed inbound vessels over the weekend and pushed two ocean arrivals back by roughly three days.
```
- `news_packet` — Excerpt 2
```text
By Tuesday morning, the port said berth congestion had eased and most containers had been unloaded.
```
- `news_packet` — Excerpt 3
```text
On Tuesday night, a scanner outage at the retailer's regional distribution center left 40% of inbound pallets unprocessed. Stores ran out of a promoted SKU the next afternoon.
```

Ground truth:
```json
{
  "label": "C",
  "direct_driver": "distribution_center_scanner_outage",
  "justification": "Upstream weather mattered earlier, but the packet states that the immediate failure before stores stocked out was the scanner outage."
}
```

## v14d_011 — After Does Not Mean Because

- Track: `natural_event_causality`
- Truth type: `expert_labeled`
- Prompt style: `news_narrative`
- Task family: `causal_vs_temporal_disambiguation`
- Evaluation regime: `unspecified`

Scenario:
```text
Two semantically similar news summaries are given, but one implies only temporal succession while the other states an actual mechanism.
```

Question:
```text
Which summary supports a causal reading and which supports only a temporal reading?
```

Options:
- `A`: Yes. The CEO interview was the direct cause of the stock move.
- `B`: Unsupported. The buyback and raised guidance are the better-supported drivers, while the interview mostly repeated old information.
- `C`: No. Interviews can never cause stock moves.
- `D`: The move was random and cannot be analyzed causally.

Materials:
- `news_packet` — Excerpt 1
```text
Before market open, the company announced a $2 billion buyback and raised full-year guidance.
```
- `news_packet` — Excerpt 2
```text
Midday, the CEO appeared on television and repeated the same points from the morning release without adding new information.
```
- `news_packet` — Excerpt 3
```text
The shares finished the day up 7.8%, with most of the move occurring in the first 20 minutes after the open.
```

Ground truth:
```json
{
  "label": "B",
  "causal_read": "morning_corporate_actions_more_plausible_than_interview",
  "justification": "The major price move happened before the interview and the interview introduced no new information."
}
```

## v14d_012 — If The Strike Had Not Happened

- Track: `natural_event_causality`
- Truth type: `expert_labeled`
- Prompt style: `news_narrative`
- Task family: `narrative_counterfactual`
- Evaluation regime: `unspecified`

Scenario:
```text
A supply-chain story culminates in a missed delivery milestone. The case asks for a counterfactual read under removal of one key disruption.
```

Question:
```text
Would the missed delivery still have occurred if the strike had not happened, assuming the other events remained unchanged?
```

Options:
- `A`: Exports would have finished above plan.
- `B`: Exports would have been roughly on plan.
- `C`: Exports would still have been below plan, but materially better than realized.
- `D`: Exports would have been worse than realized.

Materials:
- `news_packet` — Excerpt 1
```text
A port strike cut throughput by roughly 25% for five days early in the month.
```
- `news_packet` — Excerpt 2
```text
Later in the month, heavy rain reduced rail departures by another 10%.
```
- `news_packet` — Excerpt 3
```text
Actual monthly exports ended 18% below plan.
```

Ground truth:
```json
{
  "label": "C",
  "counterfactual_direction": "improve_but_remain_below_plan",
  "justification": "Removing the strike recovers part of the lost throughput, but the later rail disruption still leaves exports below plan."
}
```

## v14d_013 — Why Did Margin Miss Despite Revenue Growth?

- Track: `finance_and_business_causal_reasoning`
- Truth type: `hybrid_structured_review`
- Prompt style: `analyst_memo`
- Task family: `earnings_driver_analysis`
- Evaluation regime: `unspecified`

Scenario:
```text
An analyst memo, earnings excerpt, and compact KPI table are given for a company that grew revenue but missed margin expectations.
```

Question:
```text
What is the most plausible primary driver of the margin miss, and which variable relationship best supports that explanation?
```

Materials:
- `document_excerpt` — Earnings excerpt
```text
Revenue grew 12% year over year, but operating margin missed consensus. Management highlighted a larger-than-expected mix shift into lower-margin hardware and elevated expedited freight costs.
```
- `table` — KPI table
```text
Hardware mix: 46% -> 58%. Services mix: 54% -> 42%. Hardware gross margin: 24% -> 18%. Services gross margin: 72% -> 70%. Expedited freight cost as % of revenue: 0.4% -> 2.2%.
```

Ground truth:
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

## v14d_014 — What Happens If We Cut Paid Acquisition?

- Track: `finance_and_business_causal_reasoning`
- Truth type: `hybrid_structured_review`
- Prompt style: `analyst_memo`
- Task family: `marketing_spend_intervention`
- Evaluation regime: `unspecified`

Scenario:
```text
A growth team has CAC, retention, conversion, and revenue-per-user metrics. The case asks for the near-term causal effect of cutting paid acquisition.
```

Question:
```text
Which KPI is most likely to change first if paid acquisition is reduced by 20 percent, and why?
```

Options:
- `A`: Qualified leads would likely drop materially, while CAC improves only partially because organic replacement is limited.
- `B`: Qualified leads would stay roughly flat because organic demand will fully replace paid traffic.
- `C`: Revenue would rise immediately because paid traffic is always low quality.
- `D`: There is no basis for any directional judgment.

Materials:
- `document_excerpt` — Marketing memo
```text
Paid search contributes 62% of first qualified visits, organic contributes 28%, referral contributes 10%. Paid CAC has been rising but remains the largest controllable volume lever.
```
- `table` — Geo-test results
```text
In prior geo tests, cutting one paid lead generated only 0.25 organic replacement leads on average within the same month.
```

Ground truth:
```json
{
  "label": "A",
  "base_case": "lead_volume_down_partial_efficiency_gain",
  "rationale": "The memo and geo test imply incomplete organic substitution. Cutting paid acquisition should reduce qualified leads before any efficiency benefit fully offsets the loss."
}
```

## v14d_015 — Three Plausible Stories, One Dominant Driver

- Track: `finance_and_business_causal_reasoning`
- Truth type: `hybrid_structured_review`
- Prompt style: `analyst_memo`
- Task family: `multi_factor_finance_synthesis`
- Evaluation regime: `unspecified`

Scenario:
```text
A cross-asset memo includes rates, FX, commodity costs, and company guidance. Several causal stories look plausible.
```

Question:
```text
Which causal story best explains the observed move, and what key evidence would falsify it?
```

Materials:
- `document_excerpt` — Analyst note
```text
Management cited three factors for the quarter: a one-point constant-currency headwind, a 40 bps legal reserve, and weaker channel sell-through that pushed inventory days higher.
```
- `table` — Operating summary
```text
Revenue miss versus plan: -6%. Constant-currency impact: -1 point. Legal reserve impact on operating margin: -0.4 points. Channel inventory days: +12 days. End-market sell-through: -9%.
```

Ground truth:
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

## v14d_016 — Did The Temperature Change Really Reduce Defects?

- Track: `industrial_intervention_and_estimation`
- Truth type: `semi_synthetic_ground_truth`
- Prompt style: `operational_report`
- Task family: `manufacturing_sensor_confounder`
- Evaluation regime: `unspecified`

Scenario:
```text
A manufacturing report shows defect rates before and after a temperature policy change, but maintenance timing also shifted.
```

Question:
```text
Is the causal effect of the temperature change on defect rate identifiable from the observed variables?
```

Materials:
- `operational_log` — Process snapshot
```text
Defect rate fell from 4.8% to 3.9% after a temperature-policy increase on Line A. In the same week, Line A received a maintenance overhaul, while other lines did not.
```
- `document_excerpt` — Rollout note
```text
The temperature change was applied only on the renovated line. Throughput also dipped during the same maintenance window.
```

Ground truth:
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

## v14d_017 — A Policy Rolled Out At Different Times

- Track: `industrial_intervention_and_estimation`
- Truth type: `expert_labeled`
- Prompt style: `study_design_prompt`
- Task family: `staggered_rollout_policy`
- Evaluation regime: `unspecified`

Scenario:
```text
A policy is rolled out across regions on different dates, and the case asks for the most credible identification strategy.
```

Question:
```text
Which identification strategy is most defensible for estimating the policy effect, and what is the main threat to validity?
```

Materials:
- `operational_log` — Plant adoption timeline
```text
Six plants adopted a scheduling policy across four different months. Pre-rollout output and defect trends are visually similar across plants.
```
- `document_excerpt` — Evaluation task
```text
Leadership wants a design that estimates the policy effect while accounting for staggered adoption.
```

Ground truth:
```json
{
  "design": "staggered_difference_in_differences_event_study",
  "key_assumption": "parallel_trends_absent_the_policy",
  "risk_note": "Check for anticipation effects and cross-plant spillovers."
}
```

## v14d_018 — Estimate The Effect And State The Assumptions

- Track: `industrial_intervention_and_estimation`
- Truth type: `semi_synthetic_ground_truth`
- Prompt style: `study_design_prompt`
- Task family: `treatment_effect_estimation`
- Evaluation regime: `unspecified`

Scenario:
```text
A semi-synthetic healthcare-like dataset is summarized, with clear treatment, covariates, and outcome definitions.
```

Question:
```text
Estimate the average treatment effect and list the critical assumptions needed for that estimate to be credible.
```

Materials:
- `table` — Weighted cohort summary
```text
Adjusted treated mean outcome: 81.2. Adjusted control mean outcome: 78.8. Estimated average treatment effect after weighting: +2.4 points.
```
- `document_excerpt` — Balance note
```text
Covariates available for adjustment include plant size, shift, baseline quality score, and operator tenure. Overlap diagnostics are acceptable.
```

Ground truth:
```json
{
  "estimate": 2.4,
  "assumptions": [
    "no_unmeasured_confounding_given_adjusted_covariates",
    "positivity_or_overlap",
    "stable_outcome_definition_and_no_interference"
  ],
  "confidence": "medium"
}
```

## v14d_019 — Fresh Event, Fast Causal Read

- Track: `agentic_live_analysis`
- Truth type: `hybrid_structured_review`
- Prompt style: `agent_brief`
- Task family: `fresh_event_synthesis`
- Evaluation regime: `frozen_evidence_public_dev`

Scenario:
```text
An unresolved event analysis task asks for a short causal read using current information, with evidence freshness explicitly relevant.
```

Question:
```text
What is the most likely causal driver of the move, and what is still uncertain enough that you should not overstate it?
```

Materials:
- `retrieval_bundle` — Snippet 1
```text
Ocean carriers announced emergency surcharges after a canal disruption forced rerouting on several Asia-Europe lanes.
```
- `retrieval_bundle` — Snippet 2
```text
Freight rate indices jumped sharply over the same two-day window, while retailers said they had not yet repriced goods.
```
- `retrieval_bundle` — Snippet 3
```text
Analysts cautioned that the duration of the rerouting shock remained unclear and could fade if passage normalizes quickly.
```

Ground truth:
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

## v14d_020 — Build The Event Memo, Not Just The Answer

- Track: `agentic_live_analysis`
- Truth type: `hybrid_structured_review`
- Prompt style: `agent_brief`
- Task family: `analyst_workflow_agent`
- Evaluation regime: `frozen_evidence_public_dev`

Scenario:
```text
The agent receives a short business question but must collect current evidence, decide whether it is enough, and produce an analyst-style memo.
```

Question:
```text
What is your best-supported causal explanation, what evidence did you rely on, and what would make you change your view?
```

Materials:
- `retrieval_bundle` — Snippet 1
```text
A regional bank's shares fell after a policy official commented that deposit competition remains intense for smaller lenders.
```
- `retrieval_bundle` — Snippet 2
```text
The bank's last quarterly filing showed a relatively high share of interest-bearing deposits and rising funding costs.
```
- `retrieval_bundle` — Snippet 3
```text
A rumor about a capital raise circulated online, but no primary-source filing or company statement confirmed it.
```

Ground truth:
```json
{
  "primary_driver": "funding_cost_and_deposit_beta_concern",
  "next_verification": "verify_insured_vs_uninsured_deposit_mix_and_wholesale_funding_dependence",
  "uncertainty": "the_unconfirmed_capital_raise_rumor_should_not_be_treated_as_established_fact"
}
```

## v14d_021 — One Event, Multiple Conflicting Narratives

- Track: `agentic_live_analysis`
- Truth type: `hybrid_structured_review`
- Prompt style: `agent_brief`
- Task family: `cross_source_event_integration`
- Evaluation regime: `frozen_evidence_public_dev`

Scenario:
```text
A live case includes conflicting media explanations, partial company commentary, and market reaction across related assets.
```

Question:
```text
Which explanation is most causally plausible right now, and which alternatives remain live enough that you should keep them open?
```

Materials:
- `retrieval_bundle` — Snippet 1
```text
A biotech stock rallied after an FDA advisory panel voted in favor of its therapy.
```
- `retrieval_bundle` — Snippet 2
```text
Social media accounts also circulated an acquisition rumor, but no credible outlet confirmed it.
```
- `retrieval_bundle` — Snippet 3
```text
Short interest was elevated heading into the vote, which may have amplified the magnitude of the move.
```

Ground truth:
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

## v14d_022 — Banxico Decision Contract-Style Exemplar

- Track: `agentic_live_analysis`
- Truth type: `hidden_live_resolution`
- Prompt style: `agent_brief`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`

Scenario:
```text
A public-dev exemplar of a FutureX-style policy prediction question. The evidence packet is frozen at prediction time and the answer is evaluated only after the decision occurs.
```

Question:
```text
As of the frozen packet, which policy outcome is the best prediction for Banxico's next meeting?
```

Options:
- `A`: Cut the policy rate by 25 bps.
- `B`: Hold the policy rate unchanged.
- `C`: Raise the policy rate.

Materials:
- `retrieval_bundle` — Freeze packet
```text
Core inflation remains above target, but recent monthly prints have eased. Growth indicators softened and overnight-index swaps price a modest easing probability for the next meeting rather than a large move.
```
- `retrieval_bundle` — Market pricing snapshot
```text
Consensus commentary leans toward a 25 bps cut. FX is stable and there is no emergency-liquidity signal in local rates.
```

Ground truth:
```json
{
  "label": "A",
  "primary_basis": "disinflation_plus_softer_growth_and_market_pricing_for_a_modest_cut",
  "confidence": "medium"
}
```

## v14d_023 — Month-End Commodity Threshold Exemplar

- Track: `agentic_live_analysis`
- Truth type: `hidden_live_resolution`
- Prompt style: `agent_brief`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `live_forward_resolution`

Scenario:
```text
A public-dev exemplar of a FutureX-style commodity threshold question, scored only after the month-end close.
```

Question:
```text
Given the freeze packet, which threshold set is the best prediction for gold by month-end?
```

Options:
- `A`: The highest threshold set is the best prediction.
- `B`: The middle threshold set is the best prediction.
- `C`: The lowest threshold set is the best prediction.

Materials:
- `retrieval_bundle` — Freeze packet
```text
Gold has been supported by lower real yields and steady central-bank buying. The dollar softened modestly, while positioning looks constructive but not euphoric.
```
- `retrieval_bundle` — Threshold card
```text
The relevant forecast question is which threshold bucket is the best month-end prediction, not the exact settlement number.
```

Ground truth:
```json
{
  "label": "B",
  "primary_basis": "supportive_macro_and_flow_backdrop_but_not_strong_enough_for_the_most_extreme_threshold_set",
  "confidence": "medium"
}
```

## v14d_024 — As-Of Bitcoin Close Threshold Exemplar

- Track: `agentic_live_analysis`
- Truth type: `expert_labeled`
- Prompt style: `agent_brief`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`

Scenario:
```text
A public-dev exemplar of a FutureX-Past case run under an as-of search policy. Search is allowed, but only with sources dated on or before the case cutoff.
```

Question:
```text
Using only information available by the cutoff date, should the prediction be Yes or No?
```

Options:
- `A`: Yes
- `B`: No

Materials:
- `retrieval_bundle` — As-of packet
```text
Case cutoff: 2026-01-31 UTC. BTC traded below 100k into the final session, with no confirmed late-session catalyst in the packet suggesting a decisive break above the threshold.
```
- `retrieval_bundle` — Usage rule
```text
Search is allowed only with sources dated on or before the case cutoff. Later month-end recaps are invalid for this case.
```

Ground truth:
```json
{
  "label": "B",
  "cutoff_rule": "do_not_use_sources_after_2026_01_31",
  "primary_basis": "the_as_of_packet_does_not_support_a_clean_break_above_100k_by_the_cutoff"
}
```

## v14d_025 — As-Of Supply Shock Binary Exemplar

- Track: `agentic_live_analysis`
- Truth type: `expert_labeled`
- Prompt style: `agent_brief`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`

Scenario:
```text
A public-dev exemplar of a FutureX-Past supply-shock question evaluated with a strict case-level search cutoff.
```

Question:
```text
Using only information available by the cutoff date, should the prediction be Yes or No?
```

Options:
- `A`: Yes
- `B`: No

Materials:
- `retrieval_bundle` — As-of packet
```text
Case cutoff: 2026-03-04. South African supply disruption concerns were real, but the packet does not support global platinum availability falling below the stated threshold by the deadline.
```
- `retrieval_bundle` — Usage rule
```text
Search is allowed only with sources dated on or before the case cutoff. Any later settlement or retrospective article is invalid evidence.
```

Ground truth:
```json
{
  "label": "B",
  "cutoff_rule": "do_not_use_sources_after_2026_03_04",
  "primary_basis": "the_as_of_supply_packet_supports_stress_but_not_a_sub_threshold_global_availability_outcome"
}
```

