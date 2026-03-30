# v14 Public Dev Case Results

This markdown expands every evaluated case with the question, ground truth,
and the `codex only` vs `codex + skill` outputs.

- Timestamp: `2026-03-30T10:07:24.699666+08:00`
- Model: `gpt-5.4`
- Reasoning effort: `low`
- Case count: `25`

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
  "rationale": "The backdoor path campaign_exposure <- seasonality -> conversion must be blocked. Seasonality is pre-treatment and observed, so adjusting for it identifies the total effect. Site_visits is post-treatment and a mediator, so adjusting for it would block part of the total causal effect."
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
  "rationale": "Seasonality is a pre-treatment common cause of campaign_exposure and conversion, so adjusting for it blocks the backdoor path campaign_exposure <- seasonality -> conversion. Site_visits is post-treatment and lies on the causal pathway, so it should not be adjusted for when identifying the total effect."
}
```
- Exact-primary correct: `yes`
- Weighted score: `100.00%`
Field results:
- `label`: `match`
- `identified`: `match`
- `adjustment_set`: `match`
- `rationale`: `match`

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
  "counterfactual_outcome": "Y=0 under do(X=0)",
  "rationale": "From the structural equations, setting X=0 forces M=0 because M := X. With the observed Z=0 unchanged for the same unit, Y := M OR Z becomes 0 OR 0 = 0. So Y would not have occurred."
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
  "counterfactual_outcome": "Y=0",
  "rationale": "Under do(X=0), M becomes 0 because M:=X. With Z fixed at its observed value 0, Y:=M OR Z becomes 0 OR 0 = 0. So Y would not have occurred."
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
  "rationale": "The graph includes a directed path X -> M -> Y, so X has a causal effect on Y through M. The structure rules out a direct edge X -> Y, but it does not rule out causation; it supports an indirect effect."
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
  "rationale": "The structure contains a directed path X -> M -> Y, so X can causally affect Y indirectly even though there is no direct edge X -> Y. Z also creates association between X and Y, but the graph does not rule out causation; it supports an indirect effect."
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
  "rationale": "No directed path from marketing_spend or price_discount to churn; those nodes only lead to new_customers, while churn is only downstream of supplier_delay -> stockout -> fulfillment_delay -> customer_complaints."
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
  "example_path": null,
  "rationale": "No directed path leads from marketing_spend or price_discount to churn; both only point to new_customers, while churn is downstream of supplier_delay -> stockout -> fulfillment_delay -> customer_complaints."
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
  "rationale": "macro_demand is a common cause of both ad_spend and sales in both encodings."
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
  "rationale": "Both encodings show macro_demand causing both ad_spend and sales, so it is the confounder in each representation."
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
  "should_control": false,
  "rationale": "No. The engagement score is measured only after assignment and from post-assignment behavior after users see the experience, so it is a post-treatment variable and should not be controlled for when estimating the treatment effect on conversion."
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
  "rationale": "The engagement metric is measured only after assignment and after users see the experience, so it is post-treatment and should not be controlled for when estimating the treatment effect on conversion."
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
  "segment_conclusion": "worse_within_both_segments",
  "rationale": "Treatment underperforms within both strata: novices convert at 15/100 vs 18/100 for control, and experts at 66/100 vs 70/100 for control. The aggregate treatment rate looks higher only because treatment traffic is disproportionately expert-heavy after a manual allocation decision."
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
  "segment_conclusion": "worse_in_both_segments",
  "rationale": "Within both strata, treatment converts worse than control (novice 15/100 vs 18/100; expert 66/100 vs 70/100). The aggregate lift is explained by treatment being disproportionately expert-heavy after a manual allocation decision."
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
  "supportability": "not_solely_pricing",
  "rationale": "The gross-margin increase is not supportable as a pricing-only effect because input cost per unit also fell materially (-4.0%), and the memo states that a commodity hedge reduced input costs in the same quarter and that the margin benefit should not be attributed to pricing alone."
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
  "supportability": "not_pricing_alone",
  "rationale": "Gross margin rose, but input cost per unit also fell 4.0%, and management states a commodity hedge materially reduced input costs and that the margin benefit should not be attributed to pricing alone."
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
  "justification": "The shortage followed immediately after the Tuesday-night scanner outage left 40% of inbound pallets unprocessed. Port congestion had already eased, and the typhoon was a more upstream delay."
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
  "direct_driver": "scanner_outage_at_regional_distribution_center",
  "justification": "By Tuesday morning the port congestion had eased and most containers were unloaded. The immediate disruption before stores ran out was the Tuesday-night scanner outage that left 40% of inbound pallets unprocessed."
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
  "causal_read": "buyback_and_raised_guidance_causal; CEO_interview_temporal_only",
  "justification": "Most of the stock move happened in the first 20 minutes after the open, aligning with the pre-open buyback and guidance news. The midday interview added no new information, so it supports timing, not causation."
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
  "causal_read": "Causal: pre-open buyback_and_raised_guidance; Temporal_only: midday_CEO_interview",
  "justification": "Most of the stock move happened in the first 20 minutes after the open, aligning with the pre-open announcement. The CEO interview came later and repeated the same points without new information."
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
  "justification": "Removing the strike would improve exports versus the realized result, but the later heavy rain would still reduce rail departures, so exports would likely remain below plan rather than fully recover."
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
  "justification": "Without the strike, exports would have been higher than realized, but the later heavy rain would still have reduced rail departures. So the result is best read as still below plan, but improved versus the actual outcome."
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
  "primary_driver": "unfavorable_hardware_mix_shift",
  "supporting_variables": {
    "relationship": "higher_hardware_mix_and_lower_hardware_margin_reduced_blended_margin",
    "evidence": [
      "Hardware mix 46%->58%",
      "Services mix 54%->42%",
      "Hardware gross margin 24%->18%",
      "Services gross margin 72%->70%",
      "Expedited freight cost as % of revenue 0.4%->2.2% (secondary pressure)"
    ]
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
  "primary_driver": "lower-margin hardware mix shift",
  "supporting_variables": {
    "relationship": "hardware_mix_up + services_mix_down -> blended_margin_down",
    "evidence": "Hardware mix rose from 46% to 58% while services mix fell from 54% to 42%; hardware gross margin was far below services and also fell from 24% to 18% versus services at 72% to 70%. Expedited freight rose from 0.4% to 2.2% of revenue, but that looks secondary to the mix shift."
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
  "rationale": "Paid search supplies 62% of first qualified visits, and prior geo tests showed only 0.25 same-month organic replacement for each paid lead cut. A 20% paid reduction therefore most likely hits qualified leads first, while CAC may improve only partially."
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
  "base_case": "qualified_leads_down_first; CAC_improves_partially",
  "rationale": "Paid search drives 62% of first qualified visits and prior geo tests showed only 0.25 same-month organic replacement for each paid lead cut. A 20% paid reduction therefore most likely hits qualified lead volume first, with only partial CAC benefit because organic does not fully replace the lost paid traffic."
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
  "primary_driver": "weaker_channel_sell_through_and_inventory_buildup",
  "supporting_variables": {
    "relationship": "sell_through_down_and_inventory_days_up_best_explain_most_of_the_revenue_miss",
    "evidence": [
      "Revenue miss versus plan: -6%",
      "Constant-currency impact: -1 point",
      "Legal reserve impact on operating margin: -0.4 points",
      "Channel inventory days: +12 days",
      "End-market sell-through: -9%"
    ],
    "falsifier": "channel_inventory_days_flat_or_down_and_end_market_sell_through_not_materially_weaker"
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
  "primary_driver": "weaker channel sell-through causing inventory build and a revenue miss",
  "supporting_variables": {
    "relationship": "sell_through_down + inventory_days_up -> revenue_miss",
    "evidence": "End-market sell-through fell 9% and channel inventory days rose by 12 days, which fits the 6% revenue miss. The other cited factors are much smaller: constant-currency was only a 1-point headwind and the legal reserve was only a 0.4-point operating-margin impact.",
    "falsifier": "Evidence that sell-through was not actually weak, or that inventory days rose for a non-demand reason, or that FX/legal effects were large enough to explain most of the miss by themselves."
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
    "maintenance_timing",
    "maintenance_status",
    "throughput"
  ],
  "risk_note": "The temperature change occurred only on the renovated line during the same maintenance window, so the observed defect drop is confounded with maintenance and throughput changes and the temperature effect is not separately identifiable."
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
  "identified": "no",
  "needed_controls": [
    "maintenance",
    "throughput",
    "line_time"
  ],
  "risk_note": "Temperature changed only on the renovated line during the maintenance window, so the defect drop is confounded with maintenance and throughput changes."
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
  "design": "staggered_did_event_study",
  "key_assumption": "parallel_trends",
  "risk_note": "The main threat is endogenous adoption timing or other plant-specific shocks that violate parallel trends; with staggered rollout, a naive TWFE implementation can also be biased if effects differ across cohorts or time."
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
  "design": "staggered_did_event_study",
  "key_assumption": "parallel_trends",
  "risk_note": "The main threat is endogenous adoption timing: if plants rolled out the policy when plant-specific shocks or trends were changing, the estimate is biased."
}
```
- Exact-primary correct: `no`
- Weighted score: `35.00%`
Field results:
- `design`: `mismatch`
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
  "estimate": 2.4,
  "assumptions": [
    "no_unmeasured_confounding_given_plant_size_shift_baseline_quality_score_and_operator_tenure",
    "positivity_or_overlap",
    "consistency_and_no_interference",
    "correct_weighting_or_adjustment_specification"
  ],
  "confidence": "moderate"
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `estimate`: `match`
- `assumptions`: `mismatch`
- `confidence`: `mismatch`

`codex + skill`:
```json
{
  "estimate": {
    "ate_points": 2.4
  },
  "assumptions": [
    "conditional_exchangeability_given_covariates",
    "positivity_overlap",
    "consistency_no_interference",
    "adequate_weighting_balance"
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
  "primary_driver": "Canal disruption forced rerouting, leading carriers to add emergency surcharges and pushing freight rates sharply higher.",
  "uncertainty": "The key unknown is duration: if passage normalizes quickly, the surcharge/rate shock could fade. Retail pass-through is also not yet visible.",
  "evidence_used": [
    "Carriers announced emergency surcharges after rerouting on Asia-Europe lanes.",
    "Freight rate indices jumped sharply in the same two-day window.",
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
  "primary_driver": "The most likely driver is the canal-disruption rerouting shock: carriers imposed emergency surcharges on affected Asia-Europe lanes, and that appears to have driven the sharp freight-rate move.",
  "uncertainty": "Do not overstate persistence. Analysts explicitly said the shock could fade if passage normalizes quickly, and retailers had not yet repriced goods, so downstream pass-through is not established.",
  "evidence_used": [
    "Snippet 1: emergency surcharges followed canal-disruption rerouting on Asia-Europe lanes",
    "Snippet 2: freight rate indices jumped in the same two-day window while retailers had not yet repriced goods",
    "Snippet 3: analysts said duration of the rerouting shock was unclear and could fade quickly"
  ]
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `primary_driver`: `match`
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
  "primary_driver": "Most likely a funding-cost/deposit-pressure read: the policy official flagged intense deposit competition for smaller lenders, and the bank's filing already showed high interest-bearing deposits and rising funding costs.",
  "next_verification": "Check for any primary-source filing or company statement on the rumored capital raise, and for updated deposit/funding-cost data that would confirm or weaken the pressure thesis.",
  "uncertainty": "The capital-raise rumor is unconfirmed, and the severity of future deposit/funding pressure is still unclear from the provided materials."
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
  "primary_driver": "Best-supported explanation: the selloff was a funding-pressure repricing. The policy comment said deposit competition is intense for smaller lenders, and this bank's own filing showed high interest-bearing deposits plus rising funding costs, making it look exposed.",
  "next_verification": "Check for any primary-source filing or company statement on the capital-raise rumor, and for fresh disclosure on deposit mix and funding costs. A confirmed capital raise, or clear evidence that funding pressure is easing or worsening, would change the view.",
  "uncertainty": "The capital-raise rumor is unconfirmed, and the provided materials do not prove an idiosyncratic capital problem beyond exposure to broader smaller-lender deposit competition."
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
  "primary_driver": "The most plausible driver is the favorable FDA advisory-panel vote.",
  "uncertainty": "Two alternatives remain open enough to keep in view: elevated short interest may have amplified the rally, and the acquisition rumor is still unconfirmed and should not be treated as established.",
  "evidence_used": [
    "The stock rallied after an FDA advisory panel voted in favor of the therapy.",
    "Social media circulated an acquisition rumor, but no credible outlet confirmed it.",
    "Short interest was elevated heading into the vote, which could have amplified the move."
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
  "primary_driver": "The most causally plausible driver is the positive FDA advisory-panel vote on the therapy.",
  "uncertainty": "Keep two alternatives open: elevated short interest may have amplified the size of the rally, and the acquisition rumor remains live only as an unverified possibility, not a confirmed driver.",
  "evidence_used": [
    "Snippet 1: the stock rallied after the FDA advisory panel voted in favor",
    "Snippet 2: acquisition rumor circulated on social media but had no credible confirmation",
    "Snippet 3: short interest was elevated heading into the vote and may have amplified the move"
  ]
}
```
- Exact-primary correct: `no`
- Weighted score: `0.00%`
Field results:
- `primary_driver`: `mismatch`
- `uncertainty`: `mismatch`
- `evidence_used`: `mismatch`

## v14d_022 — Banxico Decision Contract-Style Exemplar

- Track: `agentic_live_analysis`
- Truth type: `hidden_live_resolution`
- Task family: `futurex_style_live_prediction`

Question:
```text
As of the frozen packet, which policy outcome is the best prediction for Banxico's next meeting?
```

Options:
- `A`: Cut the policy rate by 25 bps.
- `B`: Hold the policy rate unchanged.
- `C`: Raise the policy rate.

Ground truth:
```json
{
  "label": "A",
  "primary_basis": "disinflation_plus_softer_growth_and_market_pricing_for_a_modest_cut",
  "confidence": "medium"
}
```

`codex only`:
```json
{
  "label": "A",
  "primary_basis": "Consensus and OIS both point to a modest 25 bps easing, with softer growth and easing inflation but no stress signal for a larger move.",
  "confidence": 0.71
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `primary_basis`: `mismatch`
- `confidence`: `mismatch`

`codex + skill`:
```json
{
  "label": "A",
  "primary_basis": "Consensus commentary and OIS both lean to modest easing, while stable FX and no local-rates stress fit a standard 25 bps cut rather than a hold or hike.",
  "confidence": 0.69
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `primary_basis`: `mismatch`
- `confidence`: `mismatch`

## v14d_023 — Month-End Commodity Threshold Exemplar

- Track: `agentic_live_analysis`
- Truth type: `hidden_live_resolution`
- Task family: `futurex_style_live_prediction`

Question:
```text
Given the freeze packet, which threshold set is the best prediction for gold by month-end?
```

Options:
- `A`: The highest threshold set is the best prediction.
- `B`: The middle threshold set is the best prediction.
- `C`: The lowest threshold set is the best prediction.

Ground truth:
```json
{
  "label": "B",
  "primary_basis": "supportive_macro_and_flow_backdrop_but_not_strong_enough_for_the_most_extreme_threshold_set",
  "confidence": "medium"
}
```

`codex only`:
```json
{
  "label": "B",
  "primary_basis": "The setup is supportive for gold, but 'constructive not euphoric' positioning argues for a moderate outcome rather than the highest bucket.",
  "confidence": 0.6
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `primary_basis`: `mismatch`
- `confidence`: `mismatch`

`codex + skill`:
```json
{
  "label": "B",
  "primary_basis": "The packet is supportive for gold, but the setup looks moderate rather than extreme: lower real yields, steady central-bank buying, a modestly softer dollar, and constructive but not euphoric positioning.",
  "confidence": 0.58
}
```
- Exact-primary correct: `no`
- Weighted score: `45.00%`
Field results:
- `label`: `match`
- `primary_basis`: `mismatch`
- `confidence`: `mismatch`

## v14d_024 — As-Of Bitcoin Close Threshold Exemplar

- Track: `agentic_live_analysis`
- Truth type: `expert_labeled`
- Task family: `futurex_style_live_prediction`

Question:
```text
Using only information available by the cutoff date, should the prediction be Yes or No?
```

Options:
- `A`: Yes
- `B`: No

Ground truth:
```json
{
  "label": "B",
  "cutoff_rule": "do_not_use_sources_after_2026_01_31",
  "primary_basis": "the_as_of_packet_does_not_support_a_clean_break_above_100k_by_the_cutoff"
}
```

`codex only`:
```json
{
  "label": "B",
  "cutoff_rule": "use_only_pre_2026-01-31_utc_sources",
  "primary_basis": "By the cutoff packet, BTC was still below 100k into the final session and no confirmed late-session catalyst suggested a decisive break above the threshold."
}
```
- Exact-primary correct: `no`
- Weighted score: `50.00%`
Field results:
- `label`: `match`
- `cutoff_rule`: `mismatch`
- `primary_basis`: `mismatch`

`codex + skill`:
```json
{
  "label": "B",
  "cutoff_rule": "Use only information available on or before 2026-01-31 UTC; later month-end recaps are invalid.",
  "primary_basis": "The packet shows BTC below 100k into the final session and no confirmed late-session catalyst suggesting a decisive break above the threshold."
}
```
- Exact-primary correct: `no`
- Weighted score: `50.00%`
Field results:
- `label`: `match`
- `cutoff_rule`: `mismatch`
- `primary_basis`: `mismatch`

## v14d_025 — As-Of Supply Shock Binary Exemplar

- Track: `agentic_live_analysis`
- Truth type: `expert_labeled`
- Task family: `futurex_style_live_prediction`

Question:
```text
Using only information available by the cutoff date, should the prediction be Yes or No?
```

Options:
- `A`: Yes
- `B`: No

Ground truth:
```json
{
  "label": "B",
  "cutoff_rule": "do_not_use_sources_after_2026_03_04",
  "primary_basis": "the_as_of_supply_packet_supports_stress_but_not_a_sub_threshold_global_availability_outcome"
}
```

`codex only`:
```json
{
  "label": "B",
  "cutoff_rule": "only materials available on or before 2026-03-04",
  "primary_basis": "As-of packet says supply disruption concerns were real, but it does not support global platinum availability falling below the stated threshold by the deadline."
}
```
- Exact-primary correct: `no`
- Weighted score: `50.00%`
Field results:
- `label`: `match`
- `cutoff_rule`: `mismatch`
- `primary_basis`: `mismatch`

`codex + skill`:
```json
{
  "label": "B",
  "cutoff_rule": "Use only sources dated on or before 2026-03-04; later settlement or retrospective evidence is invalid.",
  "primary_basis": "The as-of packet says South African supply disruption concerns were real, but it does not support global platinum availability falling below the stated threshold by the deadline."
}
```
- Exact-primary correct: `no`
- Weighted score: `50.00%`
Field results:
- `label`: `match`
- `cutoff_rule`: `mismatch`
- `primary_basis`: `mismatch`
