# v14 Benchmark Lessons

## Why This File Exists

This document records the practical design lessons that `v14` should borrow
from existing causal, finance, and industrial benchmarks.

It is intentionally opinionated. The point is not to summarize papers, but to
translate their strongest ideas into benchmark-building rules.

## Lessons From Causal Benchmarks

### `CLADDER`

What it gets right:

- full ladder-of-causation coverage
- oracle-backed truth
- natural-language wrappers around formal causal structure

What to borrow:

- every serious causal benchmark needs explicit rung coverage
- graph-derived cases are useful, but only as one layer

### `QRData` and `QRText`

What they get right:

- same reasoning family can be asked with and without data
- exposes whether a model is truly using evidence

What to borrow:

- maintain paired `data-present` and `data-absent` variants
- score the gap, not only the absolute accuracy

### `CRAB`

What it gets right:

- natural event narratives
- causal structure in realistic stories instead of toy graphs

What to borrow:

- public benchmarks must include narrative event causality, not just formulas

### `CounterBench`

What it gets right:

- hard counterfactual emphasis
- minimal reliance on surface semantics

What to borrow:

- counterfactual reasoning needs dedicated slices, not only a few mixed-in
  items

### `CORR2CAUSE`

What it gets right:

- directly attacks the common “correlation sounds causal” error

What to borrow:

- anti-shortcut cases should be deliberate, not accidental

### `CausalGraph2LLM`

What it gets right:

- graph-level and node-level tasks
- encoding-sensitivity analysis

What to borrow:

- track whether performance changes when the same structure is re-encoded

### `CausalFlip` and `ExpliCa`

What they get right:

- adversarial answer-flip cases
- causal-vs-temporal robustness

What to borrow:

- benchmark pairs should sometimes differ in only one causal feature
- robustness is a first-class capability, not an appendix metric

### `InterveneBench` and `CausalReasoningBenchmark`

What they get right:

- realistic tasks
- identification and estimation treated as distinct skills

What to borrow:

- industrial causal evaluation must not collapse method quality into one final
  numeric answer

## Lessons From Finance And Business Benchmarks

### `BizBench`

What it gets right:

- analyst-style quantitative reasoning
- business and finance context rather than pure abstract math

What to borrow:

- causal benchmark cases in business should sound like work, not classroom
  quizzes

### `FinQA`

What it gets right:

- tables plus text
- real calculation burden

What to borrow:

- numeric reasoning should be required in at least part of the benchmark

### `FinBen`

What it gets right:

- wide coverage across finance tasks

What to borrow:

- breadth matters, but should be organized into explicit slices

### `XFinBench`

What it gets right:

- expert-level difficulty
- temporal reasoning
- scenario planning
- numerical modelling

What to borrow:

- “hard mode” in industry means multi-step, time-aware, domain-heavy problems

## Lessons From Industrial Data Benchmarks

### `causalAssembly`, `CSuite`, `RealCause`, `CIPCaD-Bench`

What they get right:

- semi-synthetic realism
- known or recoverable truth
- operational-process flavor

What to borrow:

- hidden industrial sets should use realistic data generation, not only toy SCMs
- programmatic truth should be preserved where possible

## Concrete Rules For v14

1. Every track needs at least one anti-shortcut slice.
2. At least one track must separate identification from estimation.
3. At least one track must include data/text matched pairs.
4. Public dev should be reproducible; hidden test should be refreshable.
5. Finance/business tasks should be analyst-like, not generic multiple choice
   trivia.
6. Narrative event causality must be included.
7. Agentic evaluation must be mode-separated from model-only evaluation.
8. Live tasks should be third-party resolved, not self-scored by the same tool
   being evaluated.
