# v14 Case Schema

## Purpose

This schema defines the unified case format for the `v14` industrial causal
benchmark.

It is designed so that cases from:

- graph-derived causal benchmarks
- data-grounded statistical / causal benchmarks
- narrative event-causality benchmarks
- finance and business reasoning benchmarks
- industrial intervention / estimation benchmarks
- agentic live-analysis settings

can all be represented in one shared structure.

## Top-Level Object

Each benchmark case should be a single JSON object.

### Required Fields

- `id`
- `split`
- `track`
- `source_family`
- `task_family`
- `generation_pipeline`
- `prompt_style`
- `title`
- `scenario`
- `question`
- `inputs_needed`
- `truth_type`
- `mode_compatibility`
- `skills_required`
- `slice_tags`
- `expected_output_schema`
- `scoring_focus`
- `authoring_status`

### Optional Fields

- `difficulty`
- `industrial_relevance`
- `benchmark_inspirations`
- `notes`
- `ground_truth_plan`
- `private_eval_constraints`
- `refresh_policy`
- `paired_case_group`
- `instantiated_inputs`
- `response_contract`
- `ground_truth_ref`

## Field Definitions

### `id`

- Type: `string`
- Format: `v14d_###` for public dev seeds

Example:

```json
"id": "v14d_001"
```

### `split`

- Type: `string`
- Allowed values:
  - `public_dev`
  - `public_test`
  - `private_hidden`
  - `rolling_live`

### `track`

- Type: `string`
- Allowed values:
  - `formal_causality`
  - `graph_and_mechanism`
  - `data_grounded_causal_reasoning`
  - `natural_event_causality`
  - `finance_and_business_causal_reasoning`
  - `industrial_intervention_and_estimation`
  - `agentic_live_analysis`

### `source_family`

- Type: `array[string]`
- Purpose: identifies the benchmark families the case borrows from

Examples:

```json
["CLADDER", "CounterBench"]
```

```json
["BizBench", "FinQA", "FinBen"]
```

### `task_family`

- Type: `string`
- Purpose: the narrow skill family inside the track

Examples:

- `backdoor_adjustment`
- `counterfactual`
- `mediator_identification`
- `data_vs_text_gap`
- `event_chain_attribution`
- `earnings_driver_analysis`
- `policy_rollout_identification`
- `agentic_event_synthesis`

### `generation_pipeline`

- Type: `string`
- Allowed values:
  - `structure_plus_data_to_nl`
  - `domain_knowledge_plus_news_to_structural_task`
  - `simple_qa_to_complex_analysis`

### `prompt_style`

- Type: `string`
- Allowed values:
  - `naturalized_graph_question`
  - `graph_query`
  - `table_qa`
  - `mixed_modal_finance_qa`
  - `news_narrative`
  - `analyst_memo`
  - `study_design_prompt`
  - `operational_report`
  - `agent_brief`

### `title`

- Type: `string`
- Short user-facing case label

### `scenario`

- Type: `string`
- A concise description of the problem context, inputs, and decision setting

### `question`

- Type: `string`
- The main question the evaluated model or agent must answer

### `inputs_needed`

- Type: `array[object]`
- Each entry describes the artifacts required to instantiate the case

Each input object should include:

- `type`
- `description`
- `required`

Recommended `type` values:

- `causal_graph`
- `table`
- `chart`
- `document_excerpt`
- `narrative`
- `news_packet`
- `operational_log`
- `retrieval_bundle`
- `evaluation_metadata`

### `instantiated_inputs`

- Type: `array[object]`
- Purpose: the concrete public-dev materials attached to an instantiated case

Each input object will usually include:

- `type`
- `title`
- `content`

This field is optional because hidden sets may store materials in a separate
artifact system.

### `truth_type`

- Type: `string`
- Allowed values:
  - `oracle_graph`
  - `programmatic_from_data`
  - `expert_labeled`
  - `semi_synthetic_ground_truth`
  - `hidden_live_resolution`
  - `hybrid_structured_review`

### `mode_compatibility`

- Type: `array[string]`
- Allowed values:
  - `model_only`
  - `open_book`
  - `tool_agent`

### `paired_case_group`

- Type: `string`
- Purpose: groups sibling cases that share a skill family but vary in evidence
  surface, wording, or adversarial perturbation

### `response_contract`

- Type: `object`
- Purpose: defines the answer shape actually expected by the evaluator

Typical contents:

- `format`
- `required_fields`
- optional answer-label constraints

### `skills_required`

- Type: `array[string]`
- Purpose: what capabilities are actually being tested

Examples:

- `causal_formula`
- `graph_reasoning`
- `counterfactual_reasoning`
- `statistical_grounding`
- `calculation`
- `domain_knowledge`
- `retrieval`
- `tool_use`
- `abstention`

### `slice_tags`

- Type: `array[string]`
- Purpose: fine-grained evaluation slices

Common tags:

- `association`
- `intervention`
- `counterfactual`
- `confounder`
- `collider`
- `mediator`
- `correlation_vs_causation`
- `temporal_vs_causal`
- `finance`
- `business`
- `industrial_process`
- `identification`
- `estimation`
- `event_analysis`
- `freshness_sensitive`

### `expected_output_schema`

- Type: `object`
- Required subfields:
  - `format`
  - `required_fields`
  - `abstention_allowed`

Recommended `format` values:

- `multiple_choice`
- `yes_no`
- `structured_json`
- `short_text_plus_json`
- `estimate_with_interval`

### `scoring_focus`

- Type: `array[string]`
- Purpose: what gets graded for this case

Common values:

- `final_answer_accuracy`
- `field_level_accuracy`
- `identification_accuracy`
- `estimation_accuracy`
- `calculation_accuracy`
- `abstention_quality`
- `calibration`
- `tool_use_correctness`

### `authoring_status`

- Type: `string`
- Allowed values:
  - `seed`
  - `draft`
  - `instantiated`
  - `validated`

## Example

```json
{
  "id": "v14d_001",
  "split": "public_dev",
  "track": "formal_causality",
  "source_family": ["CLADDER", "CounterBench"],
  "task_family": "backdoor_adjustment",
  "generation_pipeline": "structure_plus_data_to_nl",
  "prompt_style": "naturalized_graph_question",
  "title": "Marketing Lift And A Backdoor Trap",
  "scenario": "A small DAG and a short business story are given. The model must decide whether a causal claim about campaign lift is identifiable and which variables should be adjusted for.",
  "question": "Which variable set, if any, identifies the causal effect of the campaign on conversion?",
  "inputs_needed": [
    {
      "type": "causal_graph",
      "description": "Observed DAG with campaign, conversion, seasonality, and site traffic",
      "required": true
    }
  ],
  "truth_type": "oracle_graph",
  "mode_compatibility": ["model_only", "open_book", "tool_agent"],
  "skills_required": ["causal_formula", "graph_reasoning"],
  "slice_tags": ["intervention", "confounder", "identification"],
  "expected_output_schema": {
    "format": "structured_json",
    "required_fields": ["identified", "adjustment_set", "rationale"],
    "abstention_allowed": true
  },
  "scoring_focus": ["field_level_accuracy", "identification_accuracy"],
  "authoring_status": "seed"
}
```

## Validation Rules

1. `track` must match the `task_family`.
2. `truth_type` must be compatible with the source family.
3. `mode_compatibility` must not be empty.
4. `expected_output_schema.required_fields` must be non-empty for all
   structured tasks.
5. `scoring_focus` must contain at least one primary metric.
6. `agentic_live_analysis` cases should usually include `open_book` or
   `tool_agent`.
7. `rolling_live` cases must define a resolution path in `ground_truth_plan`
   once instantiated.
8. Instantiated `public_dev` cases should usually include `instantiated_inputs`
   and `response_contract`.

## Public Dev Guidance

Public dev cases should be:

- diverse enough for iteration
- reproducible
- contamination-tolerant
- rich in slice tags
- balanced across tracks

They should not depend on confidential company data.
