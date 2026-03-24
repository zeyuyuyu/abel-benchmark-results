# v6 FutureX Financial-Subset A/B

Date run: March 24, 2026

Model: `gpt-5.4`

Reasoning effort: `low`

Setup: identical Codex CLI runs over official FutureX data, with the only variable being whether the installed `causal-abel` skill was present in `CODEX_HOME`.

This version contains two experiments:

- A scored `FutureX-Past` financial subset with 10 resolved questions
- A live `FutureX-Online` financial subset with 7 unresolved questions from the current week

## FutureX-Past Summary

| Run | Correct | Accuracy | Total Time |
|-----|---------|----------|------------|
| Base | 7/10 | 70.0% | 380.93s |
| Skill | 8/10 | 80.0% | 593.65s |

Observed tradeoff:

- The skill improved accuracy by `+1` question.
- The skill was slower by `212.72s`.

## FutureX-Past Per-Question Notes

Questions where the runs differed:

- `What will Gold (GC) settle at in January?`
  Base: `\boxed{D}`
  Skill: `\boxed{E}`
  Ground truth: `['E']`

Questions both runs missed:

- `Tesla hits $400 or $500 first before end of January 2026?`
  Base: `\boxed{C}`
  Skill: `\boxed{C}`
  Ground truth: `['A']`
- `Nvidia hits 170, 200 or neither first by end of January 2026?`
  Base: `\boxed{C}`
  Skill: `\boxed{C}`
  Ground truth: `['A']`

## FutureX-Online Summary

These predictions were generated on March 24, 2026, using the then-current weekly `FutureX-Online` financial subset. They are not yet scoreable until the underlying events resolve.

| Run | Questions | Total Time | Predictions |
|-----|-----------|------------|-------------|
| Base | 7 | 804.59s | 7/7 returned |
| Skill | 7 | 602.86s | 7/7 returned |

The two runs produced identical predictions, but the skill-enabled run finished faster.

## FutureX-Online Predictions

| Task | Base | Skill |
|------|------|-------|
| `S&P 500 Single-Day Gains and Losses (%) in Q1` | `\boxed{F, I, J}` | `\boxed{F, I, J}` |
| `What will KOSPI (^KS11) hit in Q1 2026?` | `\boxed{B, C, D, E, F, G, H, J, K, L, M, N, O}` | `\boxed{B, C, D, E, F, G, H, J, K, L, M, N, O}` |
| `Q1 S&P 500 Performance` | `\boxed{A}` | `\boxed{A}` |
| `Will KOSPI (KS11) close above __ end of Q1?` | `\boxed{A, C, F, G, H}` | `\boxed{A, C, F, G, H}` |
| `What price will Bitcoin hit by March 2026?` | `\boxed{A}` | `\boxed{A}` |
| `Banxico interest rate decision in March` | `\boxed{A}` | `\boxed{A}` |
| `Robinhood launches prediction market through MIAXdx by March 31?` | `\boxed{No}` | `\boxed{No}` |

## Reproducibility

- Harness: [`test_script.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v6/test_script.py)
- Compact summary: [`results.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v6/results.json)
- Full artifacts: [`artifacts/summary.full.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v6/artifacts/summary.full.json)
