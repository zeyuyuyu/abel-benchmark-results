# v14 Hidden Evaluation Spec

## Goal

The hidden evaluation split is where `v14` becomes an industrial benchmark
rather than only a public academic benchmark.

It should preserve the reproducibility benefits of public dev, while protecting
against:

- benchmark contamination
- prompt overfitting
- answer-key memorization
- tool-flow gaming

## Hidden Split Structure

### `private_hidden_static`

- confidential or non-public cases
- stable enough for recurring internal evaluation
- not released publicly

### `private_hidden_refreshing`

- periodically refreshed case pool
- same schema, different concrete instantiations
- designed to break overfitting

### `rolling_live`

- unresolved questions scored only after external resolution
- useful for event analysis, analyst workflows, and freshness-sensitive tasks

## Recommended Composition

For the first industrial hidden set:

- `60` formal / graph / data cases
- `60` finance / business cases
- `40` industrial intervention / estimation cases
- `40` agentic live-analysis cases

Target total: `200` hidden cases

## What Must Be Hidden

### Hidden Graph Instantiations

- new node names
- new graph topologies
- new delexicalized variable sets

### Hidden Data Instantiations

- unseen tables
- semi-synthetic effect sizes
- new confounding patterns

### Hidden Narrative Instantiations

- unseen event chains
- adversarially paired causal-vs-temporal paraphrases

### Hidden Business Cases

- new filings, KPIs, operating memos, or mock internal reports
- unseen finance combinations and causal stories

### Hidden Agentic Cases

- freshness-sensitive tasks
- new retrieval bundles
- delayed-resolution questions

## Hidden Evaluation Modes

All hidden cases should still be scored separately by mode:

1. `model_only`
2. `open_book`
3. `tool_agent`

Do not publish a single blended score as the main headline.

## Hidden Scoring Policy

### Track A / B

- primary: final-answer accuracy
- secondary: field-level structural accuracy

### Track C / E

- primary: field-level accuracy
- secondary: calculation and supportability

### Track F

- primary: identification accuracy
- secondary: estimation accuracy
- tertiary: calibration and abstention quality

### Track G

- primary: field-level outcome quality
- secondary: tool-use correctness
- tertiary: latency and evidence efficiency

## Anti-Gaming Rules

### Rule 1: No Answer-Key Side Channels

- hidden cases must not expose answer identifiers in filenames or prompt text

### Rule 2: Distinct Evidence Packets

- retrieval bundles and live evidence should be rotated or regenerated

### Rule 3: Paired Adversarial Cases

- include answer-flipping pairs inspired by `CausalFlip` and `ExpliCa`

### Rule 4: Data/Text Duals

- maintain some `QRData` / `QRText`-style matched pairs so the benchmark can
  detect whether systems are genuinely using data

### Rule 5: Hidden Estimation Checks

- for semi-synthetic cases, keep the estimand and effect-generation metadata
  private

## Resolution Paths

Every hidden case must declare a resolution path, even if the path is not
publicly revealed.

Allowed resolution paths:

- `oracle_graph_engine`
- `programmatic_dataset_scoring`
- `semi_synthetic_generator_truth`
- `expert_panel_review`
- `third_party_live_resolution`

## Human Review Requirements

Human review is required for:

- study-design quality
- supportability under ambiguity
- analyst-style multi-factor explanation quality
- live-event synthesis where multiple explanations remain plausible

Human review is optional for:

- graph-derived formal cases
- fully programmatic table-calculation cases

## Benchmark Hygiene

### Public / Hidden Separation

- Public dev should teach the format.
- Hidden eval should test generalization.

### Refresh Cadence

- static hidden cases: quarterly review
- refreshing hidden cases: monthly or per release
- live cases: scored after each resolution window

### Audit Logging

For hidden runs, log:

- model version
- tool permissions
- retrieval count
- latency
- cost
- failure mode tags

## First Hidden Build

The first hidden build should prioritize:

1. identification-vs-estimation separation
2. anti-shortcut robustness
3. realistic finance/business analysis
4. industrial operational realism
5. agentic freshness-sensitive work
