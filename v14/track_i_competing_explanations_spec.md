# v14 Track I Competing Explanations Spec

## Purpose

Track I measures whether a model or agent can choose between multiple plausible
business or market explanations using causal reasoning, rather than simply
retrieving facts or repeating the loudest narrative.

The target user experience is ordinary analyst work:

- "Which explanation best fits this miss?"
- "What would falsify management's story?"
- "If this thesis is right, what else should follow?"
- "Which claimed driver is really just a downstream consequence?"

This is intentionally different from Track H. Track H asks whether an agent can
operate a causal network. Track I asks whether the agent can reason well in a
natural analyst workflow where the user never mentions graphs, paths, parents,
or tools.

## Anti-Contrivance Rule

A Track I case fails the authoring bar if it obviously looks like it was built
to reward one specific skill or tool.

Practical test:

- if the case can be rewritten as "which causal-network function should I call?"
  then it does not belong here
- if the answer options mirror internal tool primitives more than realistic
  analyst disagreements, reject the case
- if a strong non-Abel model with good reasoning would have no coherent way to
  compete, reject the case

Track I should reward causal capability, not product familiarity.

## What This Track Measures

- primary-explanation selection
- falsifier selection
- implication selection
- cause-vs-consequence separation
- supportability-aware explanation ranking

## Why This Track Should Show Real Skill Advantage

If `codex + skill` is actually useful, it should help most on cases where:

- multiple stories are plausible on the surface
- temporal coincidence is not enough
- one explanation is upstream while another is just a symptom
- the right falsifier depends on mechanism, not keyword matching

That advantage should emerge naturally. The benchmark should never need to ask
for an explicit graph operation to make the gap visible.

## Benchmark Inspirations

- `BizBench`: analyst-style business reasoning
- `XFinBench`: hard temporal and scenario-heavy finance questions
- `QRData` / `QRText`: evidence-aware disambiguation with and without tables
- `InterveneBench`: supportability and realistic intervention framing
- `Finance Agent`: evidence packets and workflow realism

## Recommended Composition

- Total cases: `24` to `36`
- Public dev: `8` to `12`
- Hidden eval: refreshed quarterly or per release

Recommended subfamilies:

- `primary_explanation_selection`
- `falsifier_selection`
- `implication_selection`
- `cause_vs_consequence_tagging`
- `management_claim_stress_test`

## Case Surface

Each case should look like a realistic work artifact, not a benchmark puzzle.

Good input materials:

- earnings or management commentary excerpt
- KPI table or compact operating metrics
- event timeline
- peer or supplier/customer reaction sheet
- short alternative analyst notes
- policy or operational update memo

Bad input materials:

- explicit graph adjacency lists
- node-relation vocabulary in the user prompt
- answer choices that are just renamed tool actions

## Output Shape

Public-dev cases should stay objectively scoreable. The recommended format is:

1. one short explanation choice
2. one falsifier choice
3. one implication choice
4. optional confidence or abstention flag

Example contract:

```json
{
  "primary_explanation": "B",
  "best_falsifier": "C",
  "best_implication": "A",
  "confidence": "medium"
}
```

Hidden cases can add a short memo field, but anchored fields should remain so
scoring does not collapse into pure prose review.

## Truth Generation

Preferred truth types:

- `hybrid_structured_review`
- `expert_panel_review`
- `programmatic_from_data` where the mechanism is recoverable from the packet
- `semi_synthetic_ground_truth` for industrial workflow variants

Every case should record:

- why the winning explanation is upstream rather than symptomatic
- why the falsifier actually separates the top explanations
- which distractor is the shortcut trap

## Shortcut Traps

Each case should contain at least one of:

- a consequence metric presented as if it were a driver
- a peer move that is correlated but not mechanism-defining
- a management explanation that is incomplete but rhetorically persuasive
- a timeline that supports multiple stories unless the model uses structure
- a KPI that confirms every hypothesis and therefore is not a real falsifier

## Scoring

Primary metrics:

- field-level accuracy
- valid-output rate
- abstention quality where ambiguity is real

Secondary metrics:

- memo supportability
- calibration
- shortcut-failure tags

Track-level reporting should keep "picked the right explanation" separate from
"wrote a persuasive note."

## Boundary With Other Tracks

- `Track G`: live retrieval, freshness, and search discipline
- `Track H`: explicit operational use of a causal network
- `Track I`: realistic explanation selection under competing narratives

If a case's main difficulty is "find the latest evidence," it is not Track I.
If its main difficulty is "operate the graph correctly," it is not Track I.
If its main difficulty is "which explanation is causally more defensible?", it
belongs here.
