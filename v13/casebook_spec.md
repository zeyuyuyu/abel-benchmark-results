# v13 Casebook Spec

## Goal

v13 is the first benchmark in this repo that is intentionally designed to avoid collapsing into historical search.

- It is live-only.
- It does not use Abel itself as ground truth.
- It keeps the benchmark question surface general and finance-facing.
- It compares unrestricted `codex` vs unrestricted `codex + causal-abel`, with normal search allowed for both.

## Composition

- Official current-week `FutureX-Online` finance tasks: `7`
- Custom `FutureX`-style live market tasks resolved by public price data: `93`
- Each custom live question is authored in a separate LLM-written seed file, not generated from a repeated prompt template at build time.
- Total cases: `100`

## Ground Truth Policy

- Official `FutureX-Online` cases resolve by matching the same `id` after it lands in `FutureX-Past`.
- Custom live cases resolve through `yfinance` daily data using explicit rules stored in `ground_truth.json`.
- No answer is written into `questions.json`.
- `cases.md` intentionally omits the answer key.

## Why This Is Better Than FutureX-Past For The Main Benchmark

- `FutureX-Past` is valuable as historical reference, but it can degrade into after-the-fact search.
- `v13` forces the model to make live forward predictions and wait for later resolution.
- This means any eventual accuracy gap between base and skill is much more meaningful.

## Artifacts

- `artifacts/futurex_online_rows.json`: raw official source rows used in the benchmark.
- `artifacts/reference_snapshot.json`: the build-time market reference snapshot for custom live tasks.
- `llm_custom_case_seeds.json`: individually written custom live question surfaces used by the builder.
- `artifacts/manifest.json`: artifact index.

## Reproducibility

- Build package: `python3 /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v13/build_live_casebook.py`
- Run live A/B: `python3 /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v13/test_script.py`
- Backfill scores later: `python3 /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v13/rescore_live.py`
