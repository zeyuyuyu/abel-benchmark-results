# v8 Benchmark Spec

## Goal

`v8` is a CAP-adapted causal benchmark for the `causal-abel` skill. It is meant to evaluate the abilities the skill actually exposes on the live Abel CAP surface, rather than generic future prediction.

This version is intentionally centered on:

- capability discovery
- node normalization
- structural graph reads
- path and connectivity checks
- intervention boundary handling
- Abel extension semantics

## Non-Goals

`v8` is not meant to replace `FutureX-Online`.

It does not primarily measure:

- open-ended world prediction
- broad web-research skill
- general financial forecasting
- long-horizon decision quality

Instead, it measures whether the model can correctly inspect and use the live CAP interface that the `causal-abel` skill is built around.

## Design Principles

1. Ground truth should come from the live CAP server, not handwritten labels.
2. Cases should mirror the skill's real workflow from [`SKILL.md`](/Users/zeyu/.codex/skills/causal-abel/SKILL.md), [`probe-usage.md`](/Users/zeyu/.codex/skills/causal-abel/references/probe-usage.md), and [`question-routing.md`](/Users/zeyu/.codex/skills/causal-abel/references/question-routing.md).
3. Scoring should happen on structured fields, not subjective prose.
4. The suite should include boundary and failure semantics, not only happy-path reads.
5. Prompts should be explicit enough to make the benchmark reproducible and debuggable.

## Taxonomy

### 1. Capability Contract

Checks that the model can inspect the live server and recover the published method surface:

- core verbs from `meta.capabilities`
- Abel extension verbs
- required arguments for `graph.paths`
- required arguments for `extensions.abel.counterfactual_preview`

### 2. Node Normalization

Checks the public node-id naming rule:

- bare ticker `NVDA` should normalize to `NVDA_close`

### 3. Structural Reads

Checks direct graph reading behavior:

- immediate parent neighbors of `NVDA_close`
- `traverse.parents` output for `NVDA_close`
- Abel Markov blanket drivers and blanket size
- `observe.predict` echoed target node plus surfaced drivers

### 4. Reachability and Validation

Checks directed-path and connectivity semantics:

- `graph.paths` for `NVDA_close -> AMD_close`
- `extensions.abel.validate_connectivity` on `NVDA_close` and `SOXX_close`

### 5. Intervention Boundaries

Checks when intervention calls should return an effect versus a structured failure or skip:

- `intervene.do(NVDA_close=0.05 -> AMD_close)`
- `intervene.do(SOXX_close=0.05 -> AMD_close)`

### 6. Extension Semantics

Checks Abel-specific semantics that are easy to describe incorrectly:

- `extensions.abel.counterfactual_preview`
- `extensions.abel.intervene_time_lag`

## Scoring

Each task is scored by exact match on one or more structured fields.

Examples:

- `verbs`
- `required_arguments`
- `neighbors`
- `path_exists`
- `skip_reason`
- `effect_support`
- `error_code`

This makes the benchmark auditable and robust to wording variation.

## Why This Benchmark Is Useful

`v8` is strong as a live contract and regression suite because it verifies:

- the current public CAP surface
- current method signatures
- current node normalization behavior
- current graph answers
- current extension error and skip semantics

That makes it useful for:

- regression testing after skill updates
- prompt changes
- CAP server version changes
- checking whether the model preserves Abel-specific semantics

## Known Limitation

`v8` is not highly discriminative for `llm only` vs `llm + skill` when prompts are explicit and the base model is strong enough to inspect the same live surface directly.

That is why `v8` should be treated as a capability-aligned contract benchmark, not the final headline benchmark for skill advantage.

## Recommended Next Layer

The next suite should keep `v8` as the regression core and add a more natural intent-level layer:

- ambiguous user questions that require method selection
- proxy-routed finance and macro questions
- cases where the model must choose between direct graph, extension verbs, and observational reads
- refusal versus skip versus error-boundary distinctions
- cases where direct future prediction is a bad abstraction but causal routing is useful

That next layer is where we should expect clearer separation between `llm only` and `llm + skill`.
