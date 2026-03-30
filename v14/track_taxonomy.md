# v14 Track Taxonomy

## Purpose

This document turns the `v14` benchmark architecture into an operational track
taxonomy.

Each track below defines:

- what it measures
- what benchmark families it inherits from
- what should count as success
- what common benchmark-design mistakes it must avoid

## Track A: Formal Causality

### Measures

- association vs intervention vs counterfactual
- causal direction
- valid adjustment
- correlation-vs-causation discrimination

### Benchmark Inspirations

- `CLADDER`
- `CounterBench`
- `CORR2CAUSE`

### Why This Track Exists

Many systems can sound causally fluent without actually respecting causal
identification rules. This track is the hard floor.

### What Good Looks Like

- correct causal-level classification
- correct identification or rejection
- consistent reasoning under delexicalization
- robustness to shortcut-breaking perturbations

### Common Failure Modes

- treating strong association as causal support
- confusing observation with intervention
- using lexical priors instead of structure

## Track B: Graph And Mechanism

### Measures

- graph traversal
- mechanism tracing
- confounder / mediator / collider recognition
- path supportability

### Benchmark Inspirations

- `CausalGraph2LLM`
- `CausalBench`

### Why This Track Exists

Industrial causal systems often rely on explicit structure somewhere in the
stack, whether as a graph, SCM, workflow DAG, or analyst mental model.

### What Good Looks Like

- correct node-role identification
- stable performance across graph encodings
- ability to say “no path” when structure does not support the claim

### Common Failure Modes

- over-reading broad correlation paths as mechanism
- encoding sensitivity
- graph-local errors that collapse global reasoning

## Track C: Data-Grounded Causal Reasoning

### Measures

- causal interpretation with data present
- statistical grounding
- calculation
- data-vs-text consistency

### Benchmark Inspirations

- `QRData`
- `QRText`
- `FinQA`

### Why This Track Exists

Real industrial causal work is almost never pure text. It usually includes a
table, metric report, experiment result, or operational summary.

### What Good Looks Like

- correct reading of the data
- explicit recognition of post-treatment traps and aggregation traps
- better decisions when data is available than when it is hidden

### Common Failure Modes

- ignoring the numbers
- cherry-picking one row instead of reading the full table
- confusing subgroup composition with causal effect

## Track D: Natural Event Causality

### Measures

- event-chain causality
- causal-vs-temporal disambiguation
- robust narrative reasoning

### Benchmark Inspirations

- `CRAB`
- `CausalFlip`
- `ExpliCa`
- `ACCESS`

### Why This Track Exists

Industrial users rarely ask in graph language. They ask through stories, event
timelines, and qualitative explanations.

### What Good Looks Like

- correct attribution in multi-event narratives
- resistance to surface-form shortcuts
- ability to keep alternatives alive when the narrative is underspecified

### Common Failure Modes

- “after therefore because”
- keyword matching without mechanism
- overconfidence in narrative interpretation

## Track E: Finance And Business Causal Reasoning

### Measures

- domain-context understanding
- variable-relationship reasoning
- event analysis
- financially grounded causal interpretation

### Benchmark Inspirations

- `BizBench`
- `FinQA`
- `FinBen`
- `XFinBench`

### Why This Track Exists

Finance and business are one of the highest-value industrial causal application
areas, but most existing causal benchmarks are too synthetic or too domain-light
to capture this.

### What Good Looks Like

- correct analyst-style reasoning over filings, KPIs, and event context
- strong temporal and scenario reasoning
- correct separation of domain facts from causal claims

### Common Failure Modes

- using finance jargon without causal substance
- hallucinating market mechanisms
- missing multi-factor interactions

## Track F: Industrial Intervention And Estimation

### Measures

- identification quality
- estimation quality
- supportability under real constraints
- operational realism

### Benchmark Inspirations

- `InterveneBench`
- `CausalReasoningBenchmark`
- `causalAssembly`
- `CSuite`
- `RealCause`
- `CIPCaD-Bench`

### Why This Track Exists

Industry needs more than “which variable causes which.” It needs valid designs,
defensible assumptions, and estimation that survives contact with real data.

### What Good Looks Like

- clear identification strategy
- explicit assumptions
- estimates that track known semi-synthetic truth
- honest rejection when assumptions are not defensible

### Common Failure Modes

- jumping straight to estimation without identifying the estimand
- pretending unsupported designs are valid
- giving precise numbers with unjustified certainty

## Track G: Agentic Live Analysis

### Measures

- retrieval
- tool-use quality
- event-grounded synthesis
- abstention and uncertainty handling

### Benchmark Inspirations

- `Finance Agent`
- freshness-sensitive slices from finance benchmarks
- `FutureX`

### Why This Track Exists

Modern industrial use is often agentic. The benchmark must evaluate not only
what answer the model gives, but how it gathers evidence and whether it knows
when evidence is insufficient.

### What Good Looks Like

- efficient retrieval
- correct use of current evidence
- no hidden answer-key leakage
- explicit uncertainty with disciplined scope

### Track G Subfamilies

- `agentic_event_synthesis`
  - frozen-evidence or packet-based agent tasks
  - public-dev friendly
  - usually `evaluation_regime = frozen_evidence_public_dev`

- `futurex_style_live_prediction`
  - contract-style prediction questions with explicit freeze time, format
    contract, and later scoring
  - should be split into two evaluation regimes:
    - `live_forward_resolution`
    - `historical_asof_search_cutoff`
  - strict rule:
    - `live_forward_resolution` is only for genuinely unresolved future cases
    - public-dev examples that already expose answers belong under
      `frozen_evidence_public_dev`, even if they imitate FutureX-style live
      contracts

### Why FutureX-Style Tasks Belong Here

`FutureX` is not a top-level causal track by itself. It is an evaluation surface
inside Track G.

The reason is structural:

- the top-level `v14` tracks are organized by capability type
- `FutureX` is a benchmark family and task surface, not a standalone causal
  capability category
- what `FutureX` contributes is high-quality contract-style agent evaluation,
  especially for time-bounded search and frozen prediction workflows

### Common Failure Modes

- over-retrieval
- wrong tool choice
- recency neglect
- unsupported confidence
- using future information in historical as-of settings

## Cross-Track Tagging

Every instantiated case should also carry slice tags from these shared groups:

### Causal Level

- `association`
- `intervention`
- `counterfactual`

### Structural Role

- `confounder`
- `mediator`
- `collider`
- `path_existence`

### Reasoning Surface

- `graph`
- `table`
- `narrative`
- `document`
- `agentic`

### Evaluation Risk

- `shortcut_risk`
- `freshness_sensitive`
- `supportability`
- `calculation`
- `temporal_vs_causal`

## Public Alpha Recommendation

For a credible `v14 alpha`, public dev should cover all seven tracks. Avoid
launching with only finance or only synthetic graph questions.
