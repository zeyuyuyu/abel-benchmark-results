# v8 CAP CausalBench v1

Date run: March 25, 2026

Model: `gpt-5.4`

Reasoning effort: `low`

Setup: identical Codex runs against the live public Abel CAP server, with the only intentional variable being whether the installed `causal-abel` skill was present in `CODEX_HOME`. Ground truth is probed live from CAP before scoring, so this suite behaves like a capability-aligned regression benchmark instead of a static handwritten quiz.

This benchmark is designed to match the skill surface more closely than FutureX. It focuses on CAP contract discovery, public node normalization, structural graph reads, path/connectivity checks, intervention boundary handling, and Abel-specific extension semantics.

## Headline Result

| Run | Score | Accuracy | Total Time |
|-----|-------|----------|------------|
| Base | `31/31` | `100%` | `970.70s` |
| Skill | `31/31` | `100%` | `1017.36s` |

Key observations:

- Both runs achieved perfect accuracy on all 31 scored fields.
- The skill-enabled run was slower by `46.66s` overall.
- This makes `v8` a strong live contract/regression suite for Abel CAP, but not yet a discriminative skill-advantage benchmark.
- The right next layer is a more natural intent-level suite with proxy routing, ambiguous task framing, and workflow-choice pressure.

## Category Scores

| Category | Base | Skill |
|----------|------|-------|
| Capability contract | `4/4` | `4/4` |
| Extension semantics | `7/7` | `7/7` |
| Intervention boundaries | `8/8` | `8/8` |
| Node normalization | `1/1` | `1/1` |
| Reachability and validation | `5/5` | `5/5` |
| Structural reads | `6/6` | `6/6` |

## Case Taxonomy

| Task | Category | Checks | Expected Output Snapshot |
|------|----------|--------|--------------------------|
| `capability_core_verbs` | `capability_contract` | `verbs` | `{"verbs": ["graph.markov_blanket", "graph.neighbors", "graph.paths", "intervene.do", "meta.capabilities", "meta.methods", "observe.predict"]}` |
| `capability_extension_verbs` | `capability_contract` | `verbs` | `{"verbs": ["extensions.abel.counterfactual_preview", "extensions.abel.intervene_time_lag", "extensions.abel.markov_blanket", "extensions.abel.observe_predict_resolved_time", "extensions.abel.validate_connectivity"]}` |
| `methods_graph_paths_required_arguments` | `capability_contract` | `required_arguments` | `{"required_arguments": ["source_node_id", "target_node_id"]}` |
| `methods_counterfactual_preview_required_arguments` | `capability_contract` | `required_arguments` | `{"required_arguments": ["intervene_new_value", "intervene_node", "intervene_time", "observe_node", "observe_time"]}` |
| `normalize_nvda` | `node_normalization` | `normalized_node_id` | `{"normalized_node_id": "NVDA_close"}` |
| `neighbors_parents_nvda` | `structural_reads` | `neighbors` | `{"neighbors": ["AGNCO_close", "MBPUSD_close", "PEAKUSD_close"]}` |
| `traverse_parents_nvda` | `structural_reads` | `nodes` | `{"nodes": []}` |
| `abel_markov_blanket_nvda` | `structural_reads` | `drivers, blanket_size` | `{"blanket_size": 20, "drivers": ["AGNCO_close", "MBPUSD_close", "PEAKUSD_close"]}` |
| `observe_nvda_drivers` | `structural_reads` | `target_node, drivers` | `{"drivers": ["AGNCO_close", "MBPUSD_close", "PEAKUSD_close"], "target_node": "NVDA_close"}` |
| `path_nvda_amd` | `reachability_and_validation` | `connected, path_count` | `{"connected": true, "path_count": 1}` |
| `validate_connectivity` | `reachability_and_validation` | `passed, connected_pairs, invalid_variable_count` | `{"connected_pairs": [], "invalid_variable_count": 2, "passed": false}` |
| `intervene_nvda_amd` | `intervention_boundaries` | `path_exists, effect_returned, intervention_skipped, error_code` | `{"effect_returned": false, "error_code": "invalid_intervention", "intervention_skipped": false, "path_exists": true}` |
| `intervene_soxx_amd` | `intervention_boundaries` | `path_exists, effect_returned, intervention_skipped, skip_reason` | `{"effect_returned": false, "intervention_skipped": true, "path_exists": false, "skip_reason": "no_directed_path_found"}` |
| `counterfactual_preview_nvda_amd` | `extension_semantics` | `reachable, effect_support, path_count, preview_only` | `{"effect_support": "no_structural_path", "path_count": 0, "preview_only": true, "reachable": false}` |
| `intervene_time_lag_nvda_amd` | `extension_semantics` | `ok, status_code, error_code` | `{"error_code": "invalid_intervention", "ok": false, "status_code": 400}` |

## Timing Notes

Largest skill speedups:

- `capability_extension_verbs`: skill faster by `56.91s`
- `capability_core_verbs`: skill faster by `33.93s`
- `intervene_soxx_amd`: skill faster by `19.56s`
- `intervene_time_lag_nvda_amd`: skill faster by `15.99s`
- `observe_nvda_drivers`: skill faster by `12.51s`

Largest skill slowdowns:

- `methods_counterfactual_preview_required_arguments`: skill slower by `48.50s`
- `traverse_parents_nvda`: skill slower by `43.62s`
- `normalize_nvda`: skill slower by `28.30s`
- `validate_connectivity`: skill slower by `22.32s`
- `neighbors_parents_nvda`: skill slower by `21.79s`

## Interpretation

- `v8` is best treated as a capability-aligned regression and contract suite. It checks that Codex can inspect the live CAP surface correctly and preserve tricky semantics such as `invalid_intervention`, `no_directed_path_found`, preview-only counterfactuals, and extension-specific method signatures.
- It is less useful as a headline A/B benchmark because the prompts are intentionally explicit. A strong base model can often inspect the same live surface and match the skill-assisted run exactly.
- For a more decision-relevant comparison, the next suite should shift from direct verb questions to natural task intents where the skill meaningfully changes routing and workflow choice.

## Reproducibility

- Harness: [`test_script.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v8/test_script.py)
- Benchmark spec: [`benchmark_spec.md`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v8/benchmark_spec.md)
- Compact summary: [`results.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v8/results.json)
- Full raw summary: [`artifacts/summary.full.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v8/artifacts/summary.full.json)
