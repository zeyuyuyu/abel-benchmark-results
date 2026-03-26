# v14 Authoring Playbook

## Purpose

This playbook turns benchmark inspirations into concrete case-authoring rules.

The goal is not to clone any one benchmark. The goal is to absorb the best
parts of multiple strong benchmarks and use them to build an industrial causal
benchmark that is:

- causally rigorous
- domain-realistic
- resistant to shortcutting
- usable in model-only, open-book, and tool-agent settings

## What To Borrow, Benchmark By Benchmark

### `CLADDER`

Borrow:

- full ladder-of-causation coverage
- graph-backed answer keys
- natural language wrapped around formal structure

Authoring rule:

- every public pack should include association, intervention, and
  counterfactual cases
- graph-derived cases should read like realistic tasks, not theorem exercises

### `QRData` and `QRText`

Borrow:

- paired data-present and data-absent versions
- explicit separation between reasoning from evidence and reasoning from prose

Authoring rule:

- at least some cases must come in pairs where the question family is the same
  but the available evidence differs
- scoring should track the `data -> text` performance gap

### `CRAB`

Borrow:

- event-rich narratives
- causal reasoning in realistic stories and news packets

Authoring rule:

- every narrative track case needs at least three events and at least one
  plausible-but-wrong narrative shortcut

### `CounterBench`

Borrow:

- explicit rung-3 stress tests
- counterfactuals that cannot be solved by surface plausibility alone

Authoring rule:

- counterfactuals should expose whether the model truly follows the SCM or only
  echoes the observed world

### `CORR2CAUSE`

Borrow:

- correlation-vs-causation traps
- direct attacks on shortcut pattern matching

Authoring rule:

- every track needs at least one “looks causal but is not” slice

### `CausalGraph2LLM`

Borrow:

- graph-level and node-level queries
- encoding sensitivity

Authoring rule:

- reuse the same graph under at least two surfaces:
  - adjacency-list / explicit graph
  - natural-language mechanism description

### `CausalBench`

Borrow:

- multi-view restatements of the same underlying causal relation

Authoring rule:

- important cases should have at least one reformulation variant so we can test
  whether answers survive surface changes

### `CausalFlip` and `ExpliCa`

Borrow:

- near-minimal answer-flip perturbations
- causal-vs-temporal disambiguation

Authoring rule:

- write adversarial sibling cases where one changed edge, timing cue, or
  intervention assumption flips the correct answer

### `InterveneBench` and `CausalReasoningBenchmark`

Borrow:

- realistic identification tasks
- explicit separation of identification vs estimation

Authoring rule:

- do not collapse “picked the right design” and “got the right number” into one
  scalar
- study-design cases must score supportability and assumptions separately

### `BizBench`

Borrow:

- work-like business reasoning
- context-heavy quantitative prompts

Authoring rule:

- finance and business cases should sound like analyst or operator work, not
  standardized exam questions

### `FinQA`

Borrow:

- tables plus text
- multi-step calculation burden

Authoring rule:

- some finance cases must require calculation and not be solvable from prose
  alone

### `FinBen`

Borrow:

- breadth across finance subdomains

Authoring rule:

- finance coverage should be sliced explicitly: earnings, pricing, marketing,
  macro, credit, and event interpretation

### `XFinBench`

Borrow:

- expert-level difficulty
- temporal and scenario-heavy questions

Authoring rule:

- the hard slice should require multiple linked variables, time awareness, and
  domain judgment

### `causalAssembly`, `CSuite`, `RealCause`, `CIPCaD-Bench`

Borrow:

- semi-synthetic realism
- known or recoverable ground truth
- operational flavor

Authoring rule:

- industrial tracks should prefer logs, sensor summaries, rollout timelines,
  and process metrics over toy tabular snapshots

### `Finance Agent`

Borrow:

- freshness-sensitive event analysis
- multi-source evidence synthesis

Authoring rule:

- live or agentic cases should use frozen evidence packets for public dev, and
  third-party resolution for hidden live evaluation

## Cross-Benchmark Rules

### 1. Truth Should Match Case Type

- `oracle_graph` for formal graph cases
- `programmatic_from_data` for table-heavy cases
- `expert_labeled` or `hybrid_structured_review` for narrative and memo cases
- `semi_synthetic_ground_truth` for industrial intervention cases
- `hidden_live_resolution` only for real live evaluation

### 2. Every Track Needs A Shortcut Trap

Examples:

- confounder vs mediator
- post-treatment variable vs valid control
- temporal ordering vs direct causation
- revenue growth vs margin driver
- policy rollout vs concurrent maintenance shift

### 3. Surface Form Should Vary

Allowed surfaces should include:

- graph query
- naturalized graph question
- table QA
- news narrative
- analyst memo
- operational report
- study-design prompt
- agent brief

No one surface should dominate the benchmark.

### 4. Public Dev Should Teach, Hidden Eval Should Surprise

Public dev should:

- expose the schema
- show representative reasoning patterns
- provide interpretable answers and rubrics

Hidden eval should:

- refresh narratives and data values
- preserve task families but change evidence packets
- include adversarial siblings and paired variants not shown publicly

### 5. Live Tasks Must Not Be Self-Graded

Never let the same tool both define truth and receive credit for matching it.

For live tasks:

- freeze predictions first
- resolve later with third-party outcomes or externally verified events

## Authoring Checklist

Before a case is accepted, check:

1. Is the task clearly causal, not just factual or temporal?
2. Is there a valid ground-truth path?
3. Is there at least one plausible wrong answer?
4. Does the case reward real evidence use rather than benchmark gaming?
5. Does the output schema separate the parts we actually care about?
6. If the case is domain-heavy, does it still test causality rather than trivia?
7. If the case is live or agentic, is the evidence packet frozen and auditable?

## What Not To Copy

- single-number leaderboard design with no slice visibility
- answer keys that leak through benchmark phrasing
- self-scored tool benchmarks
- too many toy DAGs with no narrative or operational meaning
- finance questions that reduce to raw quote lookup
- narrative questions with no structurally justified answer

## Immediate Use In `v14`

This playbook should be used to:

- instantiate the first `public_dev` cases
- define hidden refresh rules
- create paired adversarial and data/text variants
- keep industrial realism without sacrificing causal correctness
