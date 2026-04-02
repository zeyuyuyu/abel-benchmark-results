# v13 Live-Only Finance A/B

Run timestamp: `20260326-111553`

Last rescored: `2026-04-02T15:08:24+08:00`

This benchmark is live-only by design, so unresolved tasks remain pending until third-party sources can settle them.

| Run | Cases | Valid boxed outputs | Correct on resolved subset | Accuracy on resolved subset | Duration (s) |
|-----|-------|---------------------|----------------------------|-----------------------------|--------------|
| `base` | `14` | `14/14` | `7/14` | `0.5` | `3456.04` |
| `skill` | `14` | `14/14` | `7/14` | `0.5` | `5093.61` |

- Prediction differences: `6`
- Resolved cases: `14/14`
- Pending cases: `0`

## Per-Case Status

| Case ID | Source | Ground Truth | Base | Skill | Status |
|---------|--------|--------------|------|-------|--------|
| `v13_008` | `custom_live` | `\boxed{E}` | `\boxed{C}` | `\boxed{E}` | skill only |
| `v13_012` | `custom_live` | `\boxed{E}` | `\boxed{D}` | `\boxed{C}` | both incorrect |
| `v13_023` | `custom_live` | `\boxed{A, B, C}` | `\boxed{A, B, C}` | `\boxed{A, B, C}` | both correct |
| `v13_027` | `custom_live` | `\boxed{A, B, C, D}` | `\boxed{A, B}` | `\boxed{A, B}` | both incorrect |
| `v13_035` | `custom_live` | `\boxed{A, B, C}` | `\boxed{A, B, D, E}` | `\boxed{A, B, C, D, E}` | both incorrect |
| `v13_039` | `custom_live` | `\boxed{D}` | `\boxed{A}` | `\boxed{A}` | both incorrect |
| `v13_047` | `custom_live` | `\boxed{No}` | `\boxed{No}` | `\boxed{No}` | both correct |
| `v13_059` | `custom_live` | `\boxed{No}` | `\boxed{No}` | `\boxed{No}` | both correct |
| `v13_068` | `custom_live` | `\boxed{B}` | `\boxed{B}` | `\boxed{B}` | both correct |
| `v13_071` | `custom_live` | `\boxed{C}` | `\boxed{C}` | `\boxed{C}` | both correct |
| `v13_074` | `custom_live` | `\boxed{A, B, C, D}` | `\boxed{A, B, C, D}` | `\boxed{A, B, D}` | base only |
| `v13_077` | `custom_live` | `\boxed{B}` | `\boxed{A, D}` | `\boxed{B}` | skill only |
| `v13_083` | `custom_live` | `\boxed{B}` | `\boxed{A}` | `\boxed{A}` | both incorrect |
| `v13_087` | `custom_live` | `\boxed{B}` | `\boxed{B}` | `\boxed{A}` | base only |
