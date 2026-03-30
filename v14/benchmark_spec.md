# v14 Industrial Causal Benchmark

## Goal

`v14` is the first benchmark in this repo that is explicitly designed as an
**industrial causal benchmark**, not only a finance benchmark and not only an
Abel-aligned benchmark.

It is meant to evaluate whether a model or agent can:

1. reason correctly about causal structure
2. distinguish correlation, intervention, and counterfactuals
3. work from graphs, data tables, narratives, and domain documents
4. perform analyst-style multi-step reasoning in realistic business settings
5. use retrieval and tools without leaking into shortcut-heavy behavior

This version combines ideas from:

- causal benchmarks: `CLADDER`, `QRData`, `QRText`, `CRAB`, `CounterBench`,
  `CORR2CAUSE`, `CausalGraph2LLM`, `CausalBench`, `InterveneBench`,
  `CausalReasoningBenchmark`, `CausalFlip`, `ExpliCa`
- finance and business benchmarks: `XFinBench`, `BizBench`, `FinQA`, `FinBen`
- industrial data benchmarks: `causalAssembly`, `CSuite`, `RealCause`,
  `CIPCaD-Bench`

## Design Principles

1. No single benchmark is sufficient.
2. Public leaderboard tasks and private industrial evaluation tasks must be
   separated.
3. Open-book, model-only, and tool-agent evaluation must be scored separately.
4. Final answers are not enough; identification quality and supportability must
   also be scored.
5. Synthetic, semi-synthetic, and real-world task sources must coexist.

## Source Benchmark Integration

### Causality Core

- `CLADDER`
  - Use for: Pearl ladder coverage, graph-derived questions, oracle-labeled
    causal truth.
  - Borrow: association / intervention / counterfactual templates.

- `QRData`
  - Use for: data-grounded statistical and causal questions.
  - Borrow: same question family with explicit data table grounding.

- `QRText`
  - Use for: text-only control split for the same reasoning families.
  - Borrow: comparison between data-grounded and text-grounded reasoning.

- `CRAB`
  - Use for: natural event-graph questions grounded in stories and news.
  - Borrow: natural causal narratives instead of purely formal graph prompts.

- `CounterBench`
  - Use for: hard counterfactual stress tests.
  - Borrow: rung-3-only slices and delexicalized robustness checks.

- `CORR2CAUSE`
  - Use for: correlation-versus-causation discrimination.
  - Borrow: anti-shortcut pairs and causal-direction traps.

### Graph / Mechanism Layer

- `CausalGraph2LLM`
  - Use for: graph-level and node-level causal queries.
  - Borrow: parent / child / confounder / mediator / path / intervention task
    families and encoding-sensitivity checks.

- `CausalBench`
  - Use for: same causal relation asked through text, math, and code views.
  - Borrow: multi-view reformulation of the same underlying causal problem.

- `CausalFlip` and `ExpliCa`
  - Use for: anti-semantic-shortcut and causal-vs-temporal robustness.
  - Borrow: paired cases whose wording is similar but whose correct answers
    flip under small causal changes.

### Real-World Design Layer

- `InterveneBench`
  - Use for: study-design and intervention reasoning without explicit graphs.
  - Borrow: realistic end-to-end causal reasoning from natural descriptions.

- `CausalReasoningBenchmark`
  - Use for: identification and estimation as separate skills.
  - Borrow: structured output scoring, where method quality and estimate
    quality are not collapsed into a single number.

### Finance / Business Layer

- `FinQA`
  - Use for: table and document calculation under domain context.
  - Borrow: computation-heavy analyst tasks.

- `BizBench`
  - Use for: business and finance quantitative reasoning.
  - Borrow: domain-context understanding and business-style quantitative tasks.

- `FinBen`
  - Use for: broad finance capability coverage.
  - Borrow: wide-domain finance slices and diverse task surface.

- `XFinBench`
  - Use for: difficult finance reasoning with temporal, scenario, and
    multimodal flavor.
  - Borrow: harder domain-expert questions and realistic analyst surface form.

- `Finance Agent`
  - Use for: evaluation mode, not only source data.
  - Borrow: event-analysis and agentic workflow setting with freshness
    requirements.

### Industrial Data Layer

- `causalAssembly`, `CSuite`, `RealCause`, `CIPCaD-Bench`
  - Use for: semi-synthetic or industrial-style data with known or recoverable
    causal structure.
  - Borrow: process realism, treatment-effect realism, heterogeneity, and
    recoverable hidden truth.

## Core Tracks

`v14` should contain the following tracks.

### Track A: Formal Causality

- Primary sources: `CLADDER`, `CounterBench`, `CORR2CAUSE`
- Inputs: short graph-derived natural-language questions
- Skills:
  - association
  - intervention
  - counterfactual
  - correlation-vs-causation

### Track B: Graph And Mechanism

- Primary sources: `CausalGraph2LLM`
- Inputs: explicit graph or graph-derived narrative
- Skills:
  - parent / child / ancestor / descendant
  - confounder / mediator / collider
  - path existence and mechanism tracing
  - intervention supportability

### Track C: Data-Grounded Causal Reasoning

- Primary sources: `QRData`, `QRText`, `FinQA`
- Inputs: data tables, plots, summaries, or text-only variants
- Skills:
  - statistical grounding
  - causal interpretation from data
  - estimation-aware calculation
  - data-vs-text gap analysis

### Track D: Natural Event Causality

- Primary sources: `CRAB`, `ExpliCa`, `CausalFlip`
- Inputs: news, stories, multi-event narratives
- Skills:
  - event causality
  - temporal-vs-causal disambiguation
  - natural-language robustness

### Track E: Finance And Business Causal Reasoning

- Primary sources: `XFinBench`, `BizBench`, `FinBen`, `FinQA`
- Inputs: filings, tables, analyst prompts, event narratives
- Skills:
  - financial knowledge QA
  - context understanding
  - calculation
  - event analysis
  - variable relationship reasoning

### Track F: Industrial Intervention And Estimation

- Primary sources: `InterveneBench`, `CausalReasoningBenchmark`,
  `causalAssembly`, `CSuite`, `RealCause`, `CIPCaD-Bench`
- Inputs: study descriptions, operational datasets, semi-synthetic logs
- Skills:
  - identification
  - estimation
  - supportability
  - transportability / realism slices where available

### Track G: Agentic Live Analysis

- Primary sources: `Finance Agent` style tasks plus private company-internal
  tasks
- Inputs: unresolved or freshness-sensitive questions
- Skills:
  - retrieval
  - tool usage
  - event-grounded synthesis
  - abstention under insufficient evidence

Recommended Track G subfamilies:

- `task_family = agentic_event_synthesis`
  - for frozen-evidence public-dev cases that test evidence gathering and
    synthesis without live outcome resolution
- `task_family = futurex_style_live_prediction`
  - for contract-style prediction tasks with explicit freeze times and later
    third-party scoring
  - this family should be split again by `evaluation_regime`
    - `live_forward_resolution`
    - `historical_asof_search_cutoff`
  - strict rule:
    - `live_forward_resolution` is only for genuinely unresolved future cases
    - public-dev exemplars with visible answers must use
      `frozen_evidence_public_dev`

## Task Generation Pipelines

The benchmark should use three generation pipelines.

### Pipeline 1: Structure + Data -> Natural Language

- Start from causal graphs, SCMs, or structured datasets.
- Generate natural-language questions.
- Best for: `CLADDER`, `CounterBench`, `QRData`, graph tracks.

### Pipeline 2: Domain Knowledge + News -> Structural Task

- Start from domain knowledge, reports, tables, or narratives.
- Build structural knowledge base and then derive tasks.
- Best for: `CRAB`, finance tracks, industrial intervention tracks.

### Pipeline 3: Simple QA -> Complex Analysis

- Start from short domain questions.
- Expand into analyst-style multi-step tasks.
- Best for: `BizBench`, `XFinBench`, `FinBen`, agentic tracks.

## Evaluation Modes

Every track should support the same three run modes.

1. `model_only`
2. `open_book`
3. `tool_agent`

Scores from these three modes must remain separate.

## Scoring

### Core Metrics

- final-answer accuracy
- field-level structured accuracy
- identification accuracy
- estimation accuracy
- abstention quality
- calibration
- latency
- cost
- tool-use correctness

### Slice Metrics

- fact knowledge
- causal relationship
- counterfactual
- calculation
- variable relationship
- temporal-vs-causal confusion
- domain knowledge
- supportability / unsupported-detection

## Public / Private Split

### Public Dev

- synthetic and semi-synthetic cases
- representative but contamination-tolerant
- used for prompt and system iteration

### Public Test

- harder cases and adversarial slices
- still fully reproducible

### Private Hidden Test

- industrial datasets
- confidential or delayed-answer tasks
- refreshed periodically

### Rolling Live Set

- unresolved questions with later third-party resolution
- scored after freeze time, not at prediction time

For `FutureX`-style tasks, this live split should not be the only setup. The
benchmark should also support a historically resolved, time-bounded open-book
variant where search is allowed but strictly capped by a case-level cutoff.

## v14 Alpha Build Recommendation

The first serious build should target:

- `240` public dev cases
- `120` public stress cases
- `200` hidden private cases

Suggested public allocation:

- `40` Track A
- `30` Track B
- `40` Track C
- `40` Track D
- `50` Track E
- `40` Track F
- `optional live holdout` tracked separately

## What v14 Must Avoid

- tool-facing questions that directly mention internal APIs or node ids
- purely searchable historical questions as the only source of truth
- collapsing open-book and closed-book results into one score
- scoring only the final numeric answer while ignoring identification quality
- over-indexing on finance while calling the benchmark general-purpose

## Immediate Next Deliverables

Completed:

1. `source_benchmark_matrix.md`
2. `case_schema.md`
3. `public_dev_seed_set.json`
4. `benchmark_lessons.md`
5. `track_taxonomy.md`
6. `hidden_eval_spec.md`
7. `authoring_playbook.md`
8. `build_public_dev_pack.py`
9. `public_dev_cases.json`
10. `public_dev_ground_truth.json`
11. `public_dev_cases.md`
12. `build_track_g_true_live_pack.py`
13. `track_g_true_live_questions.json`
14. `track_g_true_live_ground_truth.json`
15. `track_g_true_live_cases.md`
16. `track_g_true_live_spec.md`
17. `build_track_g_past_asof_pack.py`
18. `track_g_past_asof_questions.json`
19. `track_g_past_asof_ground_truth.json`
20. `track_g_past_asof_cases.md`
21. `track_g_past_asof_spec.md`

Next:

1. instantiate paired `data_present` / `data_absent` sibling cases
2. create hidden-set refresh templates by track
3. define a mode-separated runner contract for `model_only`, `open_book`, and
   `tool_agent`

Related:

1. `benchmark_lessons.md`
