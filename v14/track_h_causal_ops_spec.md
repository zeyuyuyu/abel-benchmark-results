# v14 Track H Causal Ops Spec

## Purpose

Track H measures whether an agent can operationally use a causal market network
for practical analyst tasks (selection, upstream attribution, role typing,
reachability checks).

## Design Principles

- Natural analyst question wording, not direct 'Abel function' wording.
- Programmatic ground truth from frozen CAP snapshot evidence.
- Questions and answers are separated (`questions.json` vs `ground_truth.json`).

## Composition

- Total cases: `24`
- Families:
  - `cross_asset_upside_selection`
  - `direct_parent_identification`
  - `markov_role_classification`
  - `directed_path_reachability`

## Files

- `track_h_causal_ops_questions.json`
- `track_h_causal_ops_ground_truth.json`
- `track_h_causal_ops_cases.md`
- `artifacts/track_h_causal_ops_snapshot.json`
