# v14 Track G FutureX-Style Subset

Run timestamp: `2026-03-30T10:28:19.604647+08:00`
Case count: `4`
Prediction differences: `4`

| Run | Exact-primary | Weighted average | Duration (s) |
|-----|---------------|------------------|--------------|
| `base` | `0/4` | `0.4750` | `30.47` |
| `skill` | `0/4` | `0.5750` | `37.72` |

## Per-Case Status

| Case ID | Canonical Label | Base Exact | Skill Exact | Base Weighted | Skill Weighted |
|---------|-----------------|------------|-------------|---------------|----------------|
| `v14d_022` | `A` | `0` | `0` | `0.45` | `0.65` |
| `v14d_023` | `B` | `0` | `0` | `0.45` | `0.65` |
| `v14d_024` | `B` | `0` | `0` | `0.50` | `0.50` |
| `v14d_025` | `B` | `0` | `0` | `0.50` | `0.50` |

## Full Cases

### v14d_022 — Banxico Decision Contract-Style Exemplar

- Track: `agentic_live_analysis`
- Evaluation regime: `live_forward_resolution`
- Task family: `futurex_style_live_prediction`

Scenario: A public-dev exemplar of a FutureX-style policy prediction question. The evidence packet is frozen, but because this split includes an explicit answer key for development, it should be treated as frozen-evidence public-dev rather than true live forward resolution.

Question: As of the frozen packet, which policy outcome is the best prediction for Banxico's next meeting?

Inputs:
- Freeze packet: Core inflation remains above target, but recent monthly prints have eased. Growth indicators softened and overnight-index swaps price a modest easing probability for the next meeting rather than a large move.
- Market pricing snapshot: Consensus commentary leans toward a 25 bps cut. FX is stable and there is no emergency-liquidity signal in local rates.

Options:
- `A`: Cut the policy rate by 25 bps.
- `B`: Hold the policy rate unchanged.
- `C`: Raise the policy rate.

Ground truth canonical answer:

```json
{
  "label": "A",
  "primary_basis": "disinflation_plus_softer_growth_and_market_pricing_for_a_modest_cut",
  "confidence": "medium"
}
```

Evidence summary:
- This is a frozen-evidence public-dev exemplar that imitates a live-forward policy contract.
- The key lesson is that prediction should be based on freeze-time packet evidence, not hindsight.

Common failure modes:
- using later commentary rather than the frozen packet
- overstating confidence when the packet only supports a modest base case

Base prediction: `{"label": "A", "primary_basis": "easing_signals_plus_consensus", "confidence": 0.72}`
Base field results: `{"label": true, "primary_basis": false, "confidence": false}`
Base exact-primary: `0` | weighted `0.45`

Skill prediction: `{"label": "A", "primary_basis": "Consensus and OIS both lean to modest easing; softer growth, easing inflation prints, and stable FX fit a 25 bps cut over hold or hike.", "confidence": "medium"}`
Skill field results: `{"label": true, "primary_basis": false, "confidence": true}`
Skill exact-primary: `0` | weighted `0.65`

### v14d_023 — Month-End Commodity Threshold Exemplar

- Track: `agentic_live_analysis`
- Evaluation regime: `live_forward_resolution`
- Task family: `futurex_style_live_prediction`

Scenario: A public-dev exemplar of a FutureX-style commodity threshold question. It imitates a month-end live contract, but because this split exposes the answer key for development, it belongs to frozen-evidence public-dev rather than true live forward resolution.

Question: Given the freeze packet, which threshold set is the best prediction for gold by month-end?

Inputs:
- Freeze packet: Gold has been supported by lower real yields and steady central-bank buying. The dollar softened modestly, while positioning looks constructive but not euphoric.
- Threshold card: The relevant forecast question is which threshold bucket is the best month-end prediction, not the exact settlement number.

Options:
- `A`: The highest threshold set is the best prediction.
- `B`: The middle threshold set is the best prediction.
- `C`: The lowest threshold set is the best prediction.

Ground truth canonical answer:

```json
{
  "label": "B",
  "primary_basis": "supportive_macro_and_flow_backdrop_but_not_strong_enough_for_the_most_extreme_threshold_set",
  "confidence": "medium"
}
```

Evidence summary:
- This is a frozen-evidence public-dev exemplar that imitates a live-forward commodity threshold contract.
- The case teaches bucketed prediction under freeze-time evidence rather than point forecasting.

Common failure modes:
- jumping to the most bullish bucket just because the asset has momentum
- answering with an exact price instead of the contract-style bucket

Base prediction: `{"label": "B", "primary_basis": "supportive_gold_drivers_but_not_euphoric", "confidence": 0.62}`
Base field results: `{"label": true, "primary_basis": false, "confidence": false}`
Base exact-primary: `0` | weighted `0.45`

Skill prediction: `{"label": "B", "primary_basis": "Gold has supportive drivers, but the setup is constructive rather than euphoric, which fits a middle threshold bucket better than the highest or lowest.", "confidence": "medium"}`
Skill field results: `{"label": true, "primary_basis": false, "confidence": true}`
Skill exact-primary: `0` | weighted `0.65`

### v14d_024 — As-Of Bitcoin Close Threshold Exemplar

- Track: `agentic_live_analysis`
- Evaluation regime: `historical_asof_search_cutoff`
- Task family: `futurex_style_live_prediction`

Scenario: A public-dev exemplar of a FutureX-Past case run under an as-of search policy. Search is allowed, but only with sources dated on or before the case cutoff.

Question: Using only information available by the cutoff date, should the prediction be Yes or No?

Inputs:
- As-of packet: Case cutoff: 2026-01-31 UTC. BTC traded below 100k into the final session, with no confirmed late-session catalyst in the packet suggesting a decisive break above the threshold.
- Usage rule: Search is allowed only with sources dated on or before the case cutoff. Later month-end recaps are invalid for this case.

Options:
- `A`: Yes
- `B`: No

Ground truth canonical answer:

```json
{
  "label": "B",
  "cutoff_rule": "do_not_use_sources_after_2026_01_31",
  "primary_basis": "the_as_of_packet_does_not_support_a_clean_break_above_100k_by_the_cutoff"
}
```

Evidence summary:
- Adapted from the v13 historical as-of slice.
- The core lesson is not the BTC view itself, but respecting the search cutoff.

Common failure modes:
- using post-cutoff summaries
- omitting the as-of rule entirely and answering like unrestricted historical QA

Base prediction: `{"label": "B", "cutoff_rule": "Only evidence available on or before 2026-01-31 UTC is valid.", "primary_basis": "As-of packet says BTC was below 100k into the final session and shows no confirmed late-session catalyst for a break above the threshold."}`
Base field results: `{"label": true, "cutoff_rule": false, "primary_basis": false}`
Base exact-primary: `0` | weighted `0.50`

Skill prediction: `{"label": "B", "cutoff_rule": "Use only information dated on or before 2026-01-31 UTC; later month-end recaps are invalid.", "primary_basis": "The packet says BTC was still below 100k into the final session and provides no confirmed late-session catalyst for a decisive move above the threshold."}`
Skill field results: `{"label": true, "cutoff_rule": false, "primary_basis": false}`
Skill exact-primary: `0` | weighted `0.50`

### v14d_025 — As-Of Supply Shock Binary Exemplar

- Track: `agentic_live_analysis`
- Evaluation regime: `historical_asof_search_cutoff`
- Task family: `futurex_style_live_prediction`

Scenario: A public-dev exemplar of a FutureX-Past supply-shock question evaluated with a strict case-level search cutoff.

Question: Using only information available by the cutoff date, should the prediction be Yes or No?

Inputs:
- As-of packet: Case cutoff: 2026-03-04. South African supply disruption concerns were real, but the packet does not support global platinum availability falling below the stated threshold by the deadline.
- Usage rule: Search is allowed only with sources dated on or before the case cutoff. Any later settlement or retrospective article is invalid evidence.

Options:
- `A`: Yes
- `B`: No

Ground truth canonical answer:

```json
{
  "label": "B",
  "cutoff_rule": "do_not_use_sources_after_2026_03_04",
  "primary_basis": "the_as_of_supply_packet_supports_stress_but_not_a_sub_threshold_global_availability_outcome"
}
```

Evidence summary:
- Adapted from the v13 historical as-of slice.
- This exemplar teaches time-bounded search discipline on supply-shock questions.

Common failure modes:
- treating supply stress as proof of crossing the threshold
- using later coverage instead of the case-bounded evidence window

Base prediction: `{"label": "B", "cutoff_rule": "Only evidence available on or before 2026-03-04 is valid.", "primary_basis": "As-of packet says supply disruption concerns existed, but does not support global platinum availability falling below the stated threshold by the deadline."}`
Base field results: `{"label": true, "cutoff_rule": false, "primary_basis": false}`
Base exact-primary: `0` | weighted `0.50`

Skill prediction: `{"label": "B", "cutoff_rule": "Use only information dated on or before 2026-03-04; later settlements or retrospective articles are invalid.", "primary_basis": "The packet says supply disruption concerns existed, but it does not support global platinum availability falling below the stated threshold by the deadline."}`
Skill field results: `{"label": true, "cutoff_rule": false, "primary_basis": false}`
Skill exact-primary: `0` | weighted `0.50`

