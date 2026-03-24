# v7 FutureX-Online Live-Only A/B

Date run: March 24, 2026

Model: `gpt-5.4`

Reasoning effort: `low`

Setup: identical Codex CLI runs over unresolved current-week `FutureX-Online` finance tasks, with the only intentional variable being whether the installed `causal-abel` skill was present in `CODEX_HOME`.

This version intentionally excludes `FutureX-Past`, so there is no historical-answer leakage from already-resolved questions.

## Summary

| Run | Questions | Valid box answers | Total Time | Notes |
|-----|-----------|-------------------|------------|-------|
| Base | 7 | 6/7 | 722.09s | Returned an invalid BTC answer: `\boxed{}` |
| Skill | 7 | 7/7 | 1217.83s | Confirmed `causal-abel` usage from session log |

Key observations:

- The two runs produced different predictions on `3/7` live questions.
- The skill-enabled run was slower by `495.74s`.
- The skill-enabled run avoided the base run's malformed BTC output.
- The skill-enabled run switched Banxico from `hold` to `cut`.

## Evidence That The Skill Was Actually Used

The skill-side session log shows direct Abel CAP probing, including:

- `python3 scripts/cap_probe.py capabilities`
- `python3 scripts/cap_probe.py normalize-node BTC`
- `python3 scripts/cap_probe.py observe BTC`
- `python3 scripts/cap_probe.py observe SPY`
- `python3 scripts/cap_probe.py paths SPY BTC --max-paths 3`
- `python3 scripts/cap_probe.py traverse-parents COIN --top-k 8`
- `python3 scripts/cap_probe.py traverse-parents MSTR --top-k 8`
- `python3 scripts/cap_probe.py traverse-parents EWY --top-k 8`

See [`artifacts/skill_session_excerpt.txt`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/artifacts/skill_session_excerpt.txt).

## Per-Task Predictions

| Task | Base | Skill |
|------|------|-------|
| `S&P 500 Single-Day Gains and Losses (%) in Q1` | `\boxed{F, I, J}` | `\boxed{F, I, J}` |
| `What will KOSPI (^KS11) hit in Q1 2026?` | `\boxed{B, C, D, E, F, G, H, J, K, L, M, N, O}` | `\boxed{B, C, D, E, F, J, K, L, M}` |
| `Q1 S&P 500 Performance` | `\boxed{A}` | `\boxed{A}` |
| `Will KOSPI (KS11) close above __ end of Q1?` | `\boxed{A, C, F, G, H}` | `\boxed{A, C, F, G, H}` |
| `What price will Bitcoin hit by March 2026?` | `\boxed{}` | `\boxed{A}` |
| `Banxico interest rate decision in March` | `\boxed{B}` | `\boxed{A}` |
| `Robinhood launches prediction market through MIAXdx by March 31?` | `\boxed{No}` | `\boxed{No}` |

## Interpretation

Because these are live unresolved questions, this benchmark does not yet provide accuracy scores.

What it does show already:

- `LLM only` leaned more heavily on generic web retrieval and produced one malformed final answer.
- `LLM + skill` took longer, but it clearly routed part of the reasoning through Abel CAP and returned a fully valid 7/7 prediction set.
- The largest semantic divergence was on `KOSPI (^KS11) hit in Q1 2026`, where the skill-enabled run removed several lower-probability downside thresholds that the base run still selected.

## Reproducibility

- Harness: [`test_script.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/test_script.py)
- Compact summary: [`results.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/results.json)
- Full raw summary: [`artifacts/summary.full.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/artifacts/summary.full.json)
