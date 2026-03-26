# v14 Source Benchmark Matrix

| Benchmark | Family | What To Borrow | Role In v14 |
|---|---|---|---|
| `CLADDER` | Causality core | Pearl ladder, graph-to-language generation, oracle truth | `Track A` backbone |
| `QRData` | Data-grounded causality | Table/data-grounded causal and statistical QA | `Track C` backbone |
| `QRText` | Data-grounded causality | Text-only control for the same reasoning families | `Track C` control split |
| `CRAB` | Natural event causality | News/story event graph tasks | `Track D` backbone |
| `CounterBench` | Counterfactual stress | Hard rung-3 counterfactuals | `Track A` stress slice |
| `CORR2CAUSE` | Anti-shortcut causality | Correlation-vs-causation contrast | `Track A` robustness slice |
| `CausalGraph2LLM` | Graph reasoning | Parent/child/confounder/mediator/path/intervention | `Track B` backbone |
| `CausalBench` | Multi-view reasoning | Same causal task across text/math/code | `Track B/C` bridge |
| `CausalFlip` | Robustness | Answer-flipping paired cases | `Track D` robustness |
| `ExpliCa` | Robustness | Causal-vs-temporal and linguistic perturbations | `Track D` robustness |
| `InterveneBench` | Real-world design | Natural intervention and study-design reasoning | `Track F` backbone |
| `CausalReasoningBenchmark` | Identification/estimation | Separate scoring for method and estimate | `Track F` backbone |
| `FinQA` | Finance reasoning | Table/document calculation | `Track C/E` bridge |
| `BizBench` | Business reasoning | Quantitative reasoning in business contexts | `Track E` backbone |
| `FinBen` | Finance breadth | Broad finance task coverage | `Track E` coverage layer |
| `XFinBench` | Hard finance reasoning | Expert-level, temporal, scenario-style finance QA | `Track E` hard slice |
| `Finance Agent` | Agentic finance analysis | Event analysis and freshness-sensitive workflow | `Track G` mode layer |
| `causalAssembly` | Industrial data | Process realism and recoverable industrial causal structure | `Track F` industrial slice |
| `CSuite` | Industrial / semi-synthetic | Intervention-aware benchmark environments | `Track F` industrial slice |
| `RealCause` | Semi-synthetic effect estimation | Realistic treatment-effect realism with known truth | `Track F` industrial slice |
| `CIPCaD-Bench` | Industrial causal discovery | Process-style industrial discovery tasks | `Track F` industrial slice |

## Inclusion Rule

`v14` should not copy any single benchmark wholesale.

Instead:

- copy `task families`
- copy `truth-generation method`
- copy `scoring granularity`
- preserve `mode separation`
- rebuild all tasks into a unified schema

## Unified Schema Targets

Every case in `v14` should declare:

- `track`
- `source_family`
- `question_surface`
- `truth_type`
- `mode_compatibility`
- `skills_required`
- `slice_tags`
- `scoring_fields`
