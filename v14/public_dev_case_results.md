# v14 Public Dev Case Results

This markdown expands every evaluated case with the question, ground truth,
and the `codex only` vs `codex + skill` outputs.

- Timestamp: `2026-03-27T18:02:07.742470+08:00`
- Model: `gpt-5.4`
- Reasoning effort: `low`
- Case count: `21`

## v14d_001 — Campaign Lift With A Hidden Seasonal Driver

- Track: `formal_causality`
- Truth type: `oracle_graph`
- Task family: `backdoor_adjustment`

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

`codex only`:
```json
{
  "label": "C",
  "identified": true,
  "adjustment_set": [
    "seasonality"
  ],
  "rationale": "Seasonality is a common cause of campaign_exposure and conversion, so it opens a backdoor path that must be blocked. Site_visits is downstream of campaign_exposure and lies on the causal pathway to conversion, so adjusting for it would block part of the total effect."
}
```
- Exact-primary correct: `yes`
- Weighted score: `85.00%`
Field results:
- `label`: `match`
- `identified`: `match`
- `adjustment_set`: `match`
- `rationale`: `mismatch`

`codex + skill`:
```json
{
  "label": "C",
  "identified": true,
  "adjustment_set": [
    "seasonality"
  ],
  "rationale": "Seasonality is a pre-treatment common cause of campaign_exposure and conversion, so adjusting for it blocks the backdoor path. site_visits is post-exposure and lies on the causal pathway, so adjusting for it would block part of the total effect."
}
```
- Exact-primary correct: `yes`
- Weighted score: `85.00%`
Field results:
- `label`: `match`
- `identified`: `match`
- `adjustment_set`: `match`
- `rationale`: `mismatch`

## v14d_002 — Would Outcome Y Have Changed Under Do(X)?

- Track: `formal_causality`
- Truth type: `oracle_graph`
- Task family: `counterfactual_with_delexicalization`

Question:
```text
Given the observed facts and the graph, would Y still have occurred if X had been set to 0?
```

Options:
- `A`: Yes, Y would still have occurred under do(X=0).
- `B`: No, Y would not have occurred under do(X=0).
- `C`: The counterfactual is not identifiable from the information given.

Ground truth:
```json
{
  "label": "B",
  "counterfactual_outcome": 0,
  "rationale": "Under do(X=0), M becomes 0. Because Z is observed to be 0, Y = 0 OR 0 = 0, so Y would not occur."
}
```

`codex only`:
```json
{
  "label": "B",
  "counterfactual_outcome": 0,
  "rationale": "For the observed unit, Z=0. Under do(X=0), the structural equations give M:=X=0, and then Y:=M OR Z = 0 OR 0 = 0. So Y would not have occurred."
}
```
- Exact-primary correct: `yes`
- Weighted score: `80.00%`
Field results:
- `label`: `match`
- `counterfactual_outcome`: `match`
- `rationale`: `mismatch`

`codex + skill`:
```json
{
  "label": "B",
  "counterfactual_outcome": 0,
  "rationale": "Under do(X=0), M becomes 0 because M:=X. With the same observed Z=0, Y:=M OR Z becomes 0 OR 0 = 0, so Y would not occur."
}
```
- Exact-primary correct: `yes`
- Weighted score: `100.00%`
Field results:
- `label`: `match`
- `counterfactual_outcome`: `match`
- `rationale`: `match`

## v14d_003 — A Strong Association But No Direct Effect

- Track: `formal_causality`
- Truth type: `oracle_graph`
- Task family: `correlation_vs_causation_discrimination`

Question:
```text
Is the claim 'X causes Y' supported, unsupported, or contradicted by the structure?
```

Options:
- `A`: Supported: X has a causal effect on Y, but only indirectly.
- `B`: Unsupported: the graph shows association only, not causation.
- `C`: Contradicted: the graph rules out any causal effect from X to Y.

Ground truth:
```json
{
  "label": "A",
  "effect_type": "indirect_causal_effect",
  "rationale": "X affects Y through the mediator M. The lack of a direct edge does not remove the indirect causal path."
}
```

`codex only`:
```json
{
  "label": "A",
  "effect_type": "indirect",
  "rationale": "The graph contains a causal path X -> M -> Y, so X does causally affect Y. The structure rules out only a direct X -> Y edge, not causation altogether."
}
```
- Exact-primary correct: `yes`
- Weighted score: `80.00%`
Field results:
- `label`: `match`
- `effect_type`: `match`
- `rationale`: `mismatch`

`codex + skill`:
```json
{
  "label": "A",
  "effect_type": "indirect",
  "rationale": "The graph contains a causal path X -> M -> Y, so X does affect Y indirectly. Z is a shared upstream cause of X and Y, which can create association, but it does not remove the indirect causal effect."
}
```
- Exact-primary correct: `yes`
- Weighted score: `80.00%`
Field results:
- `label`: `match`
- `effect_type`: `match`
- `rationale`: `mismatch`

## v14d_004 — Which Node Is Acting As The Mediator?

- Track: `graph_and_mechanism`
- Truth type: `oracle_graph`
- Task family: `mediator_vs_confounder_identification`

Question:
```text
Which node is the mediator between price change and margin change?
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

`codex only`:
```json
{
  "mediator_node": "unit_volume",
  "mechanism_path": "price_change -> unit_volume -> gross_margin"
}
```
- Exact-primary correct: `no`
- Weighted score: `60.00%`
Field results:
- `mediator_node`: `match`
- `mechanism_path`: `mismatch`

`codex + skill`:
```json
{
  "mediator_node": "unit_volume",
  "mechanism_path": "price_change -> unit_volume -> gross_margin"
}
```
- Exact-primary correct: `no`
- Weighted score: `60.00%`
Field results:
- `mediator_node`: `match`
- `mechanism_path`: `mismatch`

## v14d_005 — Can This Effect Be Reached Through Any Directed Path?

- Track: `graph_and_mechanism`
- Truth type: `oracle_graph`
- Task family: `path_supportability`

Question:
```text
Is there a directed causal path from the intervention node to the stated outcome node?
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

`codex only`:
```json
{
  "reachable": false,
  "example_path": "none",
  "rationale": "No directed path from marketing_spend or price_discount to churn is shown; those nodes only point to new_customers, while churn is only downstream of supplier_delay -> stockout -> fulfillment_delay -> customer_complaints."
}
```
- Exact-primary correct: `no`
- Weighted score: `0.00%`
Field results:
- `reachable`: `mismatch`
- `example_path`: `mismatch`
- `rationale`: `mismatch`

`codex + skill`:
```json
{
  "reachable": false,
  "example_path": "none",
  "rationale": "There is no directed path from the growth-side nodes shown (marketing_spend or price_discount) to churn; churn is only downstream of the service chain starting at supplier_delay."
}
```
- Exact-primary correct: `no`
- Weighted score: `0.00%`
Field results:
- `reachable`: `mismatch`
- `example_path`: `mismatch`
- `rationale`: `mismatch`

## v14d_006 — Same Graph, Different Encoding

- Track: `graph_and_mechanism`
- Truth type: `oracle_graph`
- Task family: `encoding_invariance`

Question:
```text
Do the two graph encodings imply the same answer to the causal query?
```

Options:
- `A`: promo_discount
- `B`: macro_demand
- `C`: inventory_constraint
- `D`: visits

Ground truth:
```json
{
  "label": "B",
  "confounder": "macro_demand",
  "rationale": "Macro demand causes both ad_spend and sales. The answer should stay the same under either encoding."
}
```

`codex only`:
```json
{
  "label": "B",
  "confounder": "macro_demand",
  "rationale": "macro_demand causes both ad_spend and sales in both encodings, so it is the confounder."
}
```
- Exact-primary correct: `yes`
- Weighted score: `80.00%`
Field results:
- `label`: `match`
- `confounder`: `match`
- `rationale`: `mismatch`

`codex + skill`:
```json
{
  "label": "B",
  "confounder": "macro_demand",
  "rationale": "Both encodings show macro_demand causes ad_spend and also independently affects sales, so it is the common cause confounding the ad_spend-sales relationship."
}
```
- Exact-primary correct: `yes`
- Weighted score: `80.00%`
Field results:
- `label`: `match`
- `confounder`: `match`
- `rationale`: `mismatch`

## v14d_007 — A/B Test With A Post-Treatment Metric

- Track: `data_grounded_causal_reasoning`
- Truth type: `programmatic_from_data`
- Task family: `post_treatment_control_trap`

Question:
```text
Should the engagement metric be controlled for when estimating the treatment effect on conversion?
```

Options:
- `A`: Yes. Control for engagement because it predicts conversion.
- `B`: No. Engagement is post-treatment and should not be controlled for.
- `C`: Yes, but only to improve precision without affecting identification.
- `D`: The treatment effect is unidentifiable no matter what is done.

Ground truth:
```json
{
  "label": "B",
  "should_control": false,
  "rationale": "Three-day engagement is measured after treatment assignment and lies on or after the treatment path. Conditioning on it would bias total effect estimation."
}
```

`codex only`:
```json
{
  "label": "B",
  "should_control": "no",
  "rationale": "The three-day engagement score is measured only after assignment and after users see the experience, and it is computed from post-assignment behavior. It is therefore post-treatment and should not be controlled for when estimating the treatment effect on conversion."
}
```
- Exact-primary correct: `yes`
- Weighted score: `80.00%`
Field results:
- `label`: `match`
- `should_control`: `match`
- `rationale`: `mismatch`

`codex + skill`:
```json
{
  "label": "B",
  "should_control": false,
  "rationale": "Three-day engagement is measured after assignment and after exposure, so it is post-treatment. Controlling for it would condition on a post-treatment variable rather than estimate the total treatment effect on conversion."
}
```
- Exact-primary correct: `yes`
- Weighted score: `80.00%`
Field results:
- `label`: `match`
- `should_control`: `match`
- `rationale`: `mismatch`

## v14d_008 — The Aggregate Says Yes, The Strata Say No

- Track: `data_grounded_causal_reasoning`
- Truth type: `programmatic_from_data`
- Task family: `simpsons_paradox_causal_read`

Question:
```text
Is the aggregate increase sufficient evidence of a positive causal effect?
```

Options:
- `A`: Treatment helps both overall and within each segment.
- `B`: Treatment looks better in aggregate but performs worse within both segments because the traffic mix changed.
- `C`: Treatment is worse overall but better within both segments.
- `D`: No conclusion can be drawn from the table.

Ground truth:
```json
{
  "label": "B",
  "segment_conclusion": "simpsons_paradox_due_to_segment_mix",
  "rationale": "Within both novice and expert strata, treatment underperforms. The aggregate improvement is driven by the treated group containing more high-converting experts."
}
```

`codex only`:
```json
{
  "label": "B",
  "segment_conclusion": "worse in both segments; aggregate uplift is mix-driven",
  "rationale": "Within novices, treatment converts 15/100 versus 18/100 for control. Within experts, treatment converts 66/100 versus 70/100 for control. The aggregate treatment rate only looks higher because treatment traffic was shifted toward expert users after a manual allocation decision."
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `segment_conclusion`: `mismatch`
- `rationale`: `mismatch`

`codex + skill`:
```json
{
  "label": "B",
  "segment_conclusion": "aggregate_not_sufficient",
  "rationale": "Within both segments, treatment converts worse than control: novices 15/100 vs 18/100 and experts 66/100 vs 70/100. The higher aggregate treatment rate is explained by the expert-heavy treatment mix after manual allocation."
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `segment_conclusion`: `mismatch`
- `rationale`: `mismatch`

## v14d_009 — Margin Expansion After A Pricing Change

- Track: `data_grounded_causal_reasoning`
- Truth type: `hybrid_structured_review`
- Task family: `finance_table_causal_interpretation`

Question:
```text
Which variable most plausibly mediates the effect of the pricing change on gross margin?
```

Options:
- `A`: The pricing change clearly caused the full margin expansion.
- `B`: The margin expansion cannot be attributed solely to pricing because input costs also moved materially.
- `C`: The company must have cut price because volume fell.
- `D`: No causal statement of any kind is possible here.

Ground truth:
```json
{
  "label": "B",
  "supportability": "price_not_sufficient_explanation",
  "rationale": "Pricing and input-cost relief moved at the same time. The packet supports a mixed explanation, not a pricing-only causal claim."
}
```

`codex only`:
```json
{
  "label": "B",
  "supportability": "not_pricing_alone",
  "rationale": "List price increased by 2.0%, but input cost per unit fell by 4.0%, and management states that a commodity hedge materially reduced input costs and that the margin benefit should not be attributed to pricing alone. So the margin expansion is not supportably attributable solely to pricing."
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `supportability`: `mismatch`
- `rationale`: `mismatch`

`codex + skill`:
```json
{
  "label": "B",
  "supportability": "pricing_alone_unsupported",
  "rationale": "Gross margin rose while input cost per unit fell 4.0%, and the memo says a commodity hedge materially reduced input costs in the same quarter. That means the margin expansion cannot be attributed solely to pricing."
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `supportability`: `mismatch`
- `rationale`: `mismatch`

## v14d_010 — Which Event Actually Drove The Shortage?

- Track: `natural_event_causality`
- Truth type: `expert_labeled`
- Task family: `event_chain_attribution`

Question:
```text
Which event is the most likely direct driver of the final shortage event?
```

Options:
- `A`: The typhoon was the most direct driver of the shortage.
- `B`: Port congestion was the most direct driver of the shortage.
- `C`: The distribution-center scanner outage was the most direct driver of the shortage.
- `D`: Seasonal demand was the most direct driver of the shortage.

Ground truth:
```json
{
  "label": "C",
  "direct_driver": "distribution_center_scanner_outage",
  "justification": "Upstream weather mattered earlier, but the packet states that the immediate failure before stores stocked out was the scanner outage."
}
```

`codex only`:
```json
{
  "label": "C",
  "direct_driver": "distribution_center_scanner_outage",
  "justification": "The shortage follows most directly from the Tuesday-night scanner outage that left 40% of inbound pallets unprocessed. The earlier typhoon and port congestion had largely cleared by then."
}
```
- Exact-primary correct: `yes`
- Weighted score: `80.00%`
Field results:
- `label`: `match`
- `direct_driver`: `match`
- `justification`: `mismatch`

`codex + skill`:
```json
{
  "label": "C",
  "direct_driver": "distribution_center_scanner_outage",
  "justification": "The shortage came right after the Tuesday-night scanner outage left 40% of inbound pallets unprocessed. The typhoon was earlier and the port congestion had already eased with most containers unloaded."
}
```
- Exact-primary correct: `yes`
- Weighted score: `80.00%`
Field results:
- `label`: `match`
- `direct_driver`: `match`
- `justification`: `mismatch`

## v14d_011 — After Does Not Mean Because

- Track: `natural_event_causality`
- Truth type: `expert_labeled`
- Task family: `causal_vs_temporal_disambiguation`

Question:
```text
Which summary supports a causal reading and which supports only a temporal reading?
```

Options:
- `A`: Yes. The CEO interview was the direct cause of the stock move.
- `B`: Unsupported. The buyback and raised guidance are the better-supported drivers, while the interview mostly repeated old information.
- `C`: No. Interviews can never cause stock moves.
- `D`: The move was random and cannot be analyzed causally.

Ground truth:
```json
{
  "label": "B",
  "causal_read": "morning_corporate_actions_more_plausible_than_interview",
  "justification": "The major price move happened before the interview and the interview introduced no new information."
}
```

`codex only`:
```json
{
  "label": "B",
  "causal_read": "buyback_and_raised_guidance_causal; ceo_interview_temporal_only",
  "justification": "The buyback and raised guidance were announced before the open, and most of the stock move happened in the first 20 minutes after the open. The midday interview added no new information, so it is at most temporally adjacent, not the best-supported cause."
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `causal_read`: `mismatch`
- `justification`: `mismatch`

`codex + skill`:
```json
{
  "label": "B",
  "causal_read": "buyback_and_guidance_causal;_ceo_interview_temporal_only",
  "justification": "The new buyback and raised guidance were announced before the open, and most of the stock move happened in the first 20 minutes after the open. The midday TV interview added no new information, so it supports only temporal succession, not a separate causal claim."
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `causal_read`: `mismatch`
- `justification`: `mismatch`

## v14d_012 — If The Strike Had Not Happened

- Track: `natural_event_causality`
- Truth type: `expert_labeled`
- Task family: `narrative_counterfactual`

Question:
```text
Would the missed delivery still have occurred if the strike had not happened, assuming the other events remained unchanged?
```

Options:
- `A`: Exports would have finished above plan.
- `B`: Exports would have been roughly on plan.
- `C`: Exports would still have been below plan, but materially better than realized.
- `D`: Exports would have been worse than realized.

Ground truth:
```json
{
  "label": "C",
  "counterfactual_direction": "improve_but_remain_below_plan",
  "justification": "Removing the strike recovers part of the lost throughput, but the later rail disruption still leaves exports below plan."
}
```

`codex only`:
```json
{
  "label": "C",
  "counterfactual_direction": "still_below_plan_but_materially_better",
  "justification": "Without the strike, one clear source of lost throughput disappears, so exports should improve versus the realized 18% miss. But the later heavy rain still reduced rail departures, so exports would likely remain below plan."
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `counterfactual_direction`: `mismatch`
- `justification`: `mismatch`

`codex + skill`:
```json
{
  "label": "C",
  "counterfactual_direction": "still_below_plan_but_materially_better",
  "justification": "Removing the strike would improve exports, but the later heavy-rain disruption would still cut rail departures. Since monthly exports still faced that separate shock, the result would likely remain below plan, though better than the realized 18% miss."
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `counterfactual_direction`: `mismatch`
- `justification`: `mismatch`

## v14d_013 — Why Did Margin Miss Despite Revenue Growth?

- Track: `finance_and_business_causal_reasoning`
- Truth type: `hybrid_structured_review`
- Task family: `earnings_driver_analysis`

Question:
```text
What is the most plausible primary driver of the margin miss, and which variable relationship best supports that explanation?
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

`codex only`:
```json
{
  "primary_driver": "mix_shift_to_lower_margin_hardware",
  "supporting_variables": {
    "relationship": "hardware_mix_up + services_mix_down, with hardware_gross_margin far below services_gross_margin, drives blended_margin_down",
    "evidence": "hardware mix 46%->58%; services mix 54%->42%; hardware GM 24%->18% vs services GM 72%->70%; freight 0.4%->2.2% is a secondary drag"
  },
  "confidence": "high"
}
```
- Exact-primary correct: `no`
- Weighted score: `65.00%`
Field results:
- `primary_driver`: `match`
- `supporting_variables`: `mismatch`
- `confidence`: `match`

`codex + skill`:
```json
{
  "primary_driver": "mix_shift_to_lower_margin_hardware",
  "supporting_variables": {
    "relationship": "hardware_mix_up + services_mix_down with hardware_gm << services_gm -> blended_margin_down",
    "evidence": {
      "hardware_mix": "46%->58%",
      "services_mix": "54%->42%",
      "hardware_gm": "24%->18%",
      "services_gm": "72%->70%",
      "freight_pct_rev": "0.4%->2.2% secondary"
    }
  },
  "confidence": "high"
}
```
- Exact-primary correct: `no`
- Weighted score: `65.00%`
Field results:
- `primary_driver`: `match`
- `supporting_variables`: `mismatch`
- `confidence`: `match`

## v14d_014 — What Happens If We Cut Paid Acquisition?

- Track: `finance_and_business_causal_reasoning`
- Truth type: `hybrid_structured_review`
- Task family: `marketing_spend_intervention`

Question:
```text
Which KPI is most likely to change first if paid acquisition is reduced by 20 percent, and why?
```

Options:
- `A`: Qualified leads would likely drop materially, while CAC improves only partially because organic replacement is limited.
- `B`: Qualified leads would stay roughly flat because organic demand will fully replace paid traffic.
- `C`: Revenue would rise immediately because paid traffic is always low quality.
- `D`: There is no basis for any directional judgment.

Ground truth:
```json
{
  "label": "A",
  "base_case": "lead_volume_down_partial_efficiency_gain",
  "rationale": "The memo and geo test imply incomplete organic substitution. Cutting paid acquisition should reduce qualified leads before any efficiency benefit fully offsets the loss."
}
```

`codex only`:
```json
{
  "label": "A",
  "base_case": "qualified_leads_drop_first",
  "rationale": "Paid search drives 62% of first qualified visits, and prior geo tests showed only 0.25 same-month organic replacement for each paid lead cut, so volume falls quickly while CAC only partially improves."
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `base_case`: `mismatch`
- `rationale`: `mismatch`

`codex + skill`:
```json
{
  "label": "A",
  "base_case": "qualified_leads_drop_first; CAC_improves_only_partially",
  "rationale": "Paid search drives 62% of first qualified visits, and prior geo tests showed only 0.25 same-month organic replacement for each paid lead cut, so a 20% paid reduction most likely reduces near-term qualified leads first, with only partial CAC improvement."
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `base_case`: `mismatch`
- `rationale`: `mismatch`

## v14d_015 — Three Plausible Stories, One Dominant Driver

- Track: `finance_and_business_causal_reasoning`
- Truth type: `hybrid_structured_review`
- Task family: `multi_factor_finance_synthesis`

Question:
```text
Which causal story best explains the observed move, and what key evidence would falsify it?
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

`codex only`:
```json
{
  "primary_driver": "weaker_channel_sell_through_causing_inventory_build",
  "supporting_variables": {
    "support": "end-market sell-through fell 9% and channel inventory days rose 12 days, which fits the 6% revenue miss better than FX (-1 point) or the legal reserve (-0.4 margin points)",
    "falsifier": "stable_or_improving_sell-through and no_inventory_day_build"
  },
  "confidence": "high"
}
```
- Exact-primary correct: `no`
- Weighted score: `20.00%`
Field results:
- `primary_driver`: `mismatch`
- `supporting_variables`: `mismatch`
- `confidence`: `match`

`codex + skill`:
```json
{
  "primary_driver": "weaker_channel_sell_through_causing_inventory_build",
  "supporting_variables": {
    "relationship": "sell_through_down + inventory_days_up -> revenue_miss",
    "evidence": {
      "revenue_miss_vs_plan": "-6%",
      "end_market_sell_through": "-9%",
      "channel_inventory_days": "+12 days",
      "constant_currency": "-1 point",
      "legal_reserve": "-0.4 point margin"
    },
    "falsifier": "channel_inventory_days_not_up_and_sell_through_not_down"
  },
  "confidence": "high"
}
```
- Exact-primary correct: `no`
- Weighted score: `20.00%`
Field results:
- `primary_driver`: `mismatch`
- `supporting_variables`: `mismatch`
- `confidence`: `match`

## v14d_016 — Did The Temperature Change Really Reduce Defects?

- Track: `industrial_intervention_and_estimation`
- Truth type: `semi_synthetic_ground_truth`
- Task family: `manufacturing_sensor_confounder`

Question:
```text
Is the causal effect of the temperature change on defect rate identifiable from the observed variables?
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

`codex only`:
```json
{
  "identified": "no",
  "needed_controls": [
    "maintenance overhaul/renovation timing",
    "concurrent throughput or downtime changes",
    "independent variation in temperature separate from renovation"
  ],
  "risk_note": "The temperature change happened only on the renovated line during the maintenance window, so maintenance and related operating changes are confounded with the observed defect-rate drop."
}
```
- Exact-primary correct: `no`
- Weighted score: `50.00%`
Field results:
- `identified`: `match`
- `needed_controls`: `mismatch`
- `risk_note`: `mismatch`

`codex + skill`:
```json
{
  "identified": false,
  "needed_controls": [
    "maintenance_overhaul",
    "maintenance_timing",
    "throughput"
  ],
  "risk_note": "The temperature change was applied only on the renovated line and in the same maintenance window, with throughput also changing, so the temperature effect is confounded with maintenance/renovation and is not separately identifiable from these observed data."
}
```
- Exact-primary correct: `no`
- Weighted score: `50.00%`
Field results:
- `identified`: `match`
- `needed_controls`: `mismatch`
- `risk_note`: `mismatch`

## v14d_017 — A Policy Rolled Out At Different Times

- Track: `industrial_intervention_and_estimation`
- Truth type: `expert_labeled`
- Task family: `staggered_rollout_policy`

Question:
```text
Which identification strategy is most defensible for estimating the policy effect, and what is the main threat to validity?
```

Ground truth:
```json
{
  "design": "staggered_difference_in_differences_event_study",
  "key_assumption": "parallel_trends_absent_the_policy",
  "risk_note": "Check for anticipation effects and cross-plant spillovers."
}
```

`codex only`:
```json
{
  "design": "staggered_diff_in_diff",
  "key_assumption": "Absent the policy, plants would have continued on parallel outcome trends, with no anticipatory effects before adoption.",
  "risk_note": "The main threat is endogenous rollout timing or other plant-specific shocks that coincide with adoption and violate parallel trends."
}
```
- Exact-primary correct: `no`
- Weighted score: `35.00%`
Field results:
- `design`: `mismatch`
- `key_assumption`: `match`
- `risk_note`: `mismatch`

`codex + skill`:
```json
{
  "design": "staggered_difference_in_differences_event_study",
  "key_assumption": "parallel_trends",
  "risk_note": "The main threat is endogenous adoption timing or other plant-specific shocks around rollout; if adoption responds to those shocks, not-yet-treated plants are not a valid counterfactual."
}
```
- Exact-primary correct: `yes`
- Weighted score: `80.00%`
Field results:
- `design`: `match`
- `key_assumption`: `match`
- `risk_note`: `mismatch`

## v14d_018 — Estimate The Effect And State The Assumptions

- Track: `industrial_intervention_and_estimation`
- Truth type: `semi_synthetic_ground_truth`
- Task family: `treatment_effect_estimation`

Question:
```text
Estimate the average treatment effect and list the critical assumptions needed for that estimate to be credible.
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

`codex only`:
```json
{
  "estimate": {
    "ate": 2.4,
    "unit": "points"
  },
  "assumptions": [
    "no unmeasured confounding after adjusting for plant size, shift, baseline quality score, and operator tenure",
    "positivity/overlap",
    "consistency/SUTVA",
    "correct weighting/specification"
  ],
  "confidence": "moderate"
}
```
- Exact-primary correct: `no`
- Weighted score: `0.00%`
Field results:
- `estimate`: `mismatch`
- `assumptions`: `mismatch`
- `confidence`: `mismatch`

`codex + skill`:
```json
{
  "estimate": {
    "ate": 2.4,
    "unit": "points"
  },
  "assumptions": [
    "no_unmeasured_confounding_given_observed_covariates",
    "positivity_overlap",
    "consistency_stable_treatment",
    "correct_weighting_adjustment"
  ],
  "confidence": "moderate"
}
```
- Exact-primary correct: `no`
- Weighted score: `0.00%`
Field results:
- `estimate`: `mismatch`
- `assumptions`: `mismatch`
- `confidence`: `mismatch`

## v14d_019 — Fresh Event, Fast Causal Read

- Track: `agentic_live_analysis`
- Truth type: `hybrid_structured_review`
- Task family: `fresh_event_synthesis`

Question:
```text
What is the most likely causal driver of the move, and what is still uncertain enough that you should not overstate it?
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

`codex only`:
```json
{
  "primary_driver": "Canal disruption forced Asia-Europe rerouting, carriers added emergency surcharges, and that shipping shock most likely drove the freight-rate jump.",
  "uncertainty": "The key unknown is duration: if canal passage normalizes quickly, surcharges and rates could fade. Retailers had not yet repriced goods, so downstream pass-through should not be overstated.",
  "evidence_used": [
    "Emergency surcharges were announced after rerouting on Asia-Europe lanes.",
    "Freight rate indices jumped over the same two-day window.",
    "Retailers said they had not yet repriced goods.",
    "Analysts said the rerouting shock could fade if passage normalizes quickly."
  ]
}
```
- Exact-primary correct: `no`
- Weighted score: `0.00%`
Field results:
- `primary_driver`: `mismatch`
- `uncertainty`: `mismatch`
- `evidence_used`: `mismatch`

`codex + skill`:
```json
{
  "primary_driver": "Canal disruption forcing rerouting on Asia-Europe lanes, which led carriers to impose emergency surcharges and drove the freight-rate jump.",
  "uncertainty": "The duration of the rerouting shock is still unclear. If passage normalizes quickly, the surcharge/rate spike could fade, and retailers had not yet repriced goods so downstream pass-through is not established.",
  "evidence_used": [
    "Ocean carriers announced emergency surcharges after a canal disruption forced rerouting on several Asia-Europe lanes.",
    "Freight rate indices jumped sharply over the same two-day window.",
    "Retailers said they had not yet repriced goods.",
    "Analysts cautioned that the duration of the rerouting shock remained unclear and could fade if passage normalizes quickly."
  ]
}
```
- Exact-primary correct: `no`
- Weighted score: `0.00%`
Field results:
- `primary_driver`: `mismatch`
- `uncertainty`: `mismatch`
- `evidence_used`: `mismatch`

## v14d_020 — Build The Event Memo, Not Just The Answer

- Track: `agentic_live_analysis`
- Truth type: `hybrid_structured_review`
- Task family: `analyst_workflow_agent`

Question:
```text
What is your best-supported causal explanation, what evidence did you rely on, and what would make you change your view?
```

Ground truth:
```json
{
  "primary_driver": "funding_cost_and_deposit_beta_concern",
  "next_verification": "verify_insured_vs_uninsured_deposit_mix_and_wholesale_funding_dependence",
  "uncertainty": "the_unconfirmed_capital_raise_rumor_should_not_be_treated_as_established_fact"
}
```

`codex only`:
```json
{
  "primary_driver": "The best-supported driver is concern about deposit competition and funding-cost pressure for smaller lenders, made more acute here by the bank's high share of interest-bearing deposits and rising funding costs.",
  "next_verification": "Check for primary-source filings or company statements on any capital raise, and for updated deposit mix/funding-cost data to see whether pressure is worsening or stabilizing.",
  "uncertainty": "The capital-raise rumor is unconfirmed and should not be treated as causal without a filing or company statement."
}
```
- Exact-primary correct: `no`
- Weighted score: `0.00%`
Field results:
- `primary_driver`: `mismatch`
- `next_verification`: `mismatch`
- `uncertainty`: `mismatch`

`codex + skill`:
```json
{
  "primary_driver": "Most likely, the selloff was driven by concern that intense deposit competition will pressure this regional bank's funding costs, especially because its last quarterly filing already showed a high share of interest-bearing deposits and rising funding costs.",
  "next_verification": "Primary-source confirmation or denial of the capital-raise rumor is the key next check. I would also update the view if new company disclosures showed materially better or worse deposit mix and funding-cost trends than the last filing.",
  "uncertainty": "The capital-raise rumor remains unconfirmed and could change the causal read if validated, but with no filing or company statement it should stay a secondary possibility rather than the base case."
}
```
- Exact-primary correct: `no`
- Weighted score: `0.00%`
Field results:
- `primary_driver`: `mismatch`
- `next_verification`: `mismatch`
- `uncertainty`: `mismatch`

## v14d_021 — One Event, Multiple Conflicting Narratives

- Track: `agentic_live_analysis`
- Truth type: `hybrid_structured_review`
- Task family: `cross_source_event_integration`

Question:
```text
Which explanation is most causally plausible right now, and which alternatives remain live enough that you should keep them open?
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

`codex only`:
```json
{
  "primary_driver": "The most causally plausible driver is the favorable FDA advisory-panel vote, which directly improved the therapy's perceived outlook.",
  "uncertainty": "The size of the rally may have been amplified by elevated short interest, and the acquisition rumor remains unconfirmed enough that it should stay only as a low-confidence alternative.",
  "evidence_used": [
    "The stock rallied after the FDA advisory panel voted in favor of the therapy.",
    "Short interest was elevated heading into the vote, which could amplify the move.",
    "Acquisition chatter was only on social media and had no credible confirmation."
  ]
}
```
- Exact-primary correct: `no`
- Weighted score: `0.00%`
Field results:
- `primary_driver`: `mismatch`
- `uncertainty`: `mismatch`
- `evidence_used`: `mismatch`

`codex + skill`:
```json
{
  "primary_driver": "The favorable FDA advisory-panel vote is the most causally plausible primary driver of the rally.",
  "uncertainty": "High short interest may have amplified the size of the move through short covering, and the acquisition rumor remains a low-confidence alternative because it lacks credible confirmation.",
  "evidence_used": [
    "The biotech stock rallied after an FDA advisory panel voted in favor of its therapy.",
    "Social media accounts circulated an acquisition rumor, but no credible outlet confirmed it.",
    "Short interest was elevated heading into the vote, which may have amplified the magnitude of the move."
  ]
}
```
- Exact-primary correct: `no`
- Weighted score: `0.00%`
Field results:
- `primary_driver`: `mismatch`
- `uncertainty`: `mismatch`
- `evidence_used`: `mismatch`
