# v14 Causal / Proxy / Intervention Focus Pack

## Why This Pack Exists

The main `v14 public-dev` pack is intentionally broad. It covers seven tracks
and gives the benchmark a credible industrial shape, but it is not yet focused
on the slices where a graph-heavy causal skill should have the clearest
advantage.

This focused pack is meant to tighten that gap.

It adds harder cases that force the evaluator to:

- choose the right proxy family instead of repeating the loudest narrative
- reject bridge noise when a move looks causally tempting but is not on the
  cleanest transmission path
- separate supportable interventions from bundled or selected treatments
- choose the first pressure test that would most efficiently change the verdict

## What Is Different From Generic Finance QA

These cases are not simple lookup questions, not generic macro commentary, and
not pure event summarization.

They are designed to require one or more of the following:

- proxy routing
- transmission-path judgment
- intervention-boundary recognition
- falsifier selection
- pressure-test design

That makes them a better match for:

- `causal-abel`
- graph-based market reasoning
- decision-oriented causal reads

## Coverage

- `16` cases total
- `4` proxy-family selection cases
- `4` bridge-noise / transmission-strength cases
- `4` intervention-boundary / identification cases
- `4` pressure-test design cases

## Track Mix

- `finance_and_business_causal_reasoning`
- `graph_and_mechanism`
- `natural_event_causality`
- `industrial_intervention_and_estimation`
- `agentic_live_analysis`

## Benchmark Inspirations Used Most Heavily

- `XFinBench`, `FinBen`, `BizBench`, `Finance Agent`
  - work-like finance surface
  - multi-variable market interpretation
  - evidence packets that sound like analyst work

- `CausalGraph2LLM`, `CausalBench`, `CausalFlip`
  - path supportability
  - bridge-noise rejection
  - minimal-but-decisive causal differences

- `InterveneBench`, `CausalReasoningBenchmark`, `causalAssembly`, `RealCause`
  - supportability vs estimation separation
  - targeted-rollout and bundled-intervention traps
  - operational design quality

## Intended Use

This pack should be treated as:

- a focused public-dev pack
- a sharper stress slice for `codex only` vs `codex + skill`
- a complement to the broader `v14 public-dev` pack rather than a replacement

## File Layout

- `causal_proxy_intervention_cases.json`
- `causal_proxy_intervention_ground_truth.json`
- `causal_proxy_intervention_cases.md`
- `build_causal_proxy_intervention_pack.py`
