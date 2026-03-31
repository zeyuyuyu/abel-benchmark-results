# v14 Track G Past-As-Of（Finance 15）Valid-Only Summary

Comparison rule:

- Keep only cases where **both** `codex only` and `codex + skill` produced valid boxed outputs.
- Exclude empty predictions and format-invalid outputs.

Filtered set:

- Total original cases: `15`
- Valid-both cases used for scoring: `13`
- Excluded cases: `v13ra_006`, `v13ra_007`

Scores on valid-both cases:

| Run | Correct | Accuracy |
|---|---:|---:|
| codex only | 9/13 | 69.23% |
| codex + skill | 9/13 | 69.23% |

Notes:

- Under this valid-only fairness rule, the two runs are tied.
- Raw 15-case score difference came from timeout/format issues, not from a clear quality gap on valid outputs.
