# v7 FutureX-Online Live-Only A/B

Date run: March 24, 2026

Last rescored: 2026-03-24

Model: `gpt-5.4`

Reasoning effort: `low`

Setup: identical Codex CLI runs over unresolved current-week `FutureX-Online` finance tasks, with the only intentional variable being whether the installed `causal-abel` skill was present in `CODEX_HOME`.

This version intentionally excludes `FutureX-Past`, so there is no historical-answer leakage from already-resolved questions.

## Live Run Summary

| Run | Questions | Valid box answers | Total Time | Notes |
|-----|-----------|-------------------|------------|-------|
| Base | 7 | 6/7 | 722.09s | Returned an invalid BTC answer: `\boxed{}` |
| Skill | 7 | 7/7 | 1217.83s | Confirmed `causal-abel` usage from session log |

Key observations:

- The two runs produced different predictions on `3/7` live questions.
- The skill-enabled run was slower by `495.74s`.
- The skill-enabled run avoided the base run's malformed BTC output.
- The skill-enabled run switched Banxico from `hold` to `cut`.

## Scoring Status

| Metric | Base | Skill |
|--------|------|-------|
| Resolved questions | 0/7 | 0/7 |
| Correct | pending | pending |
| Accuracy on resolved subset | pending | pending |

Pending tasks:

- `S&P 500 Single-Day Gains and Losses (%) in Q1` (`69a2e39e5692ef005cdbf2d9`), end time `2026-03-31`
- `What will KOSPI (^KS11) hit in Q1 2026?` (`69a2e39e5692ef005cdbf2e9`), end time `2026-03-31`
- `Q1 S&P 500 Performance` (`69a2e39e5692ef005cdbf2d8`), end time `2026-03-31`
- `Will KOSPI (KS11) close above __ end of Q1?` (`69a2e39e5692ef005cdbf2e8`), end time `2026-03-31`
- `What price will Bitcoin hit by March 2026? (add your prediction)` (`69a4319df2cb3b006875e9d0`), end time `2026-03-31`
- `Banxico interest rate decision in March` (`699c4887d1d3cf005c1e48ad`), end time `2026-03-26`
- `Robinhood launches prediction market through MIAXdx by March 31?` (`69a2e39e5692ef005cdbf27c`), end time `2026-03-31`

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

| Task | Base | Skill | Ground Truth | Status |
|------|------|-------|--------------|--------|
| `S&P 500 Single-Day Gains and Losses (%) in Q1` | `\boxed{F, I, J}` | `\boxed{F, I, J}` | `pending` | pending |
| `What will KOSPI (^KS11) hit in Q1 2026?` | `\boxed{B, C, D, E, F, G, H, J, K, L, M, N, O}` | `\boxed{B, C, D, E, F, J, K, L, M}` | `pending` | pending |
| `Q1 S&P 500 Performance` | `\boxed{A}` | `\boxed{A}` | `pending` | pending |
| `Will KOSPI (KS11) close above __ end of Q1?` | `\boxed{A, C, F, G, H}` | `\boxed{A, C, F, G, H}` | `pending` | pending |
| `What price will Bitcoin hit by March 2026? (add your prediction)` | `\boxed{}` | `\boxed{A}` | `pending` | pending |
| `Banxico interest rate decision in March` | `\boxed{B}` | `\boxed{A}` | `pending` | pending |
| `Robinhood launches prediction market through MIAXdx by March 31?` | `\boxed{No}` | `\boxed{No}` | `pending` | pending |

## Reproducibility

- Harness: [`test_script.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/test_script.py)
- Rescorer: [`rescore_live.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/rescore_live.py)
- Refresh command: `python3 /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/rescore_live.py`
- Compact summary: [`results.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/results.json)
- Full raw summary: [`artifacts/summary.full.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/artifacts/summary.full.json)
