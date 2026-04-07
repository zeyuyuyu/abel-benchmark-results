# v13 Live-Only Finance A/B

Run timestamp: `20260325-221728`

Last rescored: `2026-04-07T09:56:40+08:00`

This benchmark is live-only by design, so unresolved tasks remain pending until third-party sources can settle them.

| Run | Cases | Valid boxed outputs | Correct on resolved subset | Accuracy on resolved subset | Duration (s) |
|-----|-------|---------------------|----------------------------|-----------------------------|--------------|
| `base` | `17` | `0/17` | `0/15` | `0.0` | `742.18` |
| `skill` | `17` | `0/17` | `0/15` | `0.0` | `742.17` |

- Prediction differences: `0`
- Resolved cases: `15/17`
- Pending cases: `2`

## Per-Case Status

| Case ID | Source | Ground Truth | Base | Skill | Status |
|---------|--------|--------------|------|-------|--------|
| `v13_001` | `futurex_online` | `\boxed{B, C, D, E, F}` | `None` | `None` | both incorrect |
| `v13_002` | `futurex_online` | `pending` | `None` | `None` | pending |
| `v13_003` | `futurex_online` | `\boxed{A}` | `None` | `None` | both incorrect |
| `v13_004` | `futurex_online` | `\boxed{C, F, G}` | `None` | `None` | both incorrect |
| `v13_005` | `futurex_online` | `pending` | `None` | `None` | pending |
| `v13_006` | `futurex_online` | `\boxed{B}` | `None` | `None` | both incorrect |
| `v13_007` | `futurex_online` | `\boxed{No}` | `None` | `None` | both incorrect |
| `v13_008` | `custom_live` | `\boxed{E}` | `None` | `None` | both incorrect |
| `v13_009` | `custom_live` | `\boxed{E}` | `None` | `None` | both incorrect |
| `v13_010` | `custom_live` | `\boxed{D}` | `None` | `None` | both incorrect |
| `v13_011` | `custom_live` | `\boxed{D}` | `None` | `None` | both incorrect |
| `v13_012` | `custom_live` | `\boxed{E}` | `None` | `None` | both incorrect |
| `v13_013` | `custom_live` | `\boxed{E}` | `None` | `None` | both incorrect |
| `v13_014` | `custom_live` | `\boxed{D}` | `None` | `None` | both incorrect |
| `v13_015` | `custom_live` | `\boxed{E}` | `None` | `None` | both incorrect |
| `v13_016` | `custom_live` | `\boxed{E}` | `None` | `None` | both incorrect |
| `v13_017` | `custom_live` | `\boxed{D}` | `None` | `None` | both incorrect |
