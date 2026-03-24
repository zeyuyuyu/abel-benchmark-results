# v5 Live Abel CAP A/B

Date run: March 24, 2026

Model: `gpt-5.4`

Reasoning effort: `low`

Setup: identical Codex CLI runs against `https://cap.abel.ai`, with the only variable being whether the installed `causal-abel` skill was present in `CODEX_HOME`.

## Summary

| Run | Score | Accuracy | Total Time |
|-----|-------|----------|------------|
| Base | 13/14 | 92.86% | 734.96s |
| Skill | 14/14 | 100.00% | 375.50s |

Net effect:

- Accuracy improved by `+1/14` absolute task-fields.
- Runtime dropped by `359.46s` overall.
- The only base miss was on the intervention skip reason for `intervene_soxx_amd`.

## Task Breakdown

| Task | Base | Skill | Base Time | Skill Time | Notes |
|------|------|-------|-----------|------------|-------|
| `methods_graph_paths` | 1/1 | 1/1 | 52.80s | 57.23s | Both recovered required args correctly |
| `nvda_parent_neighbors` | 1/1 | 1/1 | 130.44s | 63.53s | Skill was much faster on direct graph lookup |
| `path_nvda_amd` | 2/2 | 2/2 | 72.82s | 52.44s | Both found the directed path |
| `validate_connectivity` | 2/2 | 2/2 | 72.14s | 60.82s | Both matched the Abel extension output |
| `intervene_nvda_amd` | 4/4 | 4/4 | 170.31s | 74.20s | Both captured the “path exists but no propagated effect” edge case |
| `intervene_soxx_amd` | 3/4 | 4/4 | 236.45s | 67.28s | Base used `no_structural_path`; skill matched Abel’s `no_directed_path_found` |

## Most Informative Failure

`intervene_soxx_amd` is the clearest behavioral difference:

- Ground truth skip reason: `no_directed_path_found`
- Base output: `no_structural_path`
- Skill output: `no_directed_path_found`

That suggests the installed skill helped Codex preserve Abel’s exact intervention-gating semantics instead of paraphrasing them.

## Reproducibility

- Harness: [`test_script.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v5/test_script.py)
- Compact summary: [`results.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v5/results.json)
- Full raw run outputs: [`raw/summary.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v5/raw/summary.json)
