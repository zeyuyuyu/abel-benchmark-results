# v13 Resolved As-Of Partial Results

Open-book run with time-bounded search (`search_cutoff`) over the first 6 cases.

- Base: `4/6`
- Skill: `4/6`

| Case ID | Category | Cutoff | Ground truth | Base | Skill |
|---|---|---|---|---|---|
| `v13ra_001` | `central_bank_decision` | `2026-01-27` | `\boxed{A}` | `\boxed{A}` ✅ | `\boxed{A}` ✅ |
| `v13ra_002` | `central_bank_decision` | `2026-01-23` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ |
| `v13ra_003` | `central_bank_decision` | `2026-02-03` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{C}` ❌ |
| `v13ra_004` | `central_bank_decision` | `2026-02-05` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ |
| `v13ra_005` | `commodity_thresholds` | `2026-02-01` | `\boxed{H, I, J, K, L}` | `\boxed{F, G, H, I, J, K, L}` ❌ | `\boxed{H, I, J, K, L}` ✅ |
| `v13ra_006` | `commodity_bucket` | `2026-02-01` | `\boxed{E}` | `\boxed{A}` ❌ | `\boxed{F}` ❌ |

## v13ra_001 — Bank of Brazil decision in January?

- Category: `central_bank_decision`
- Search cutoff: `2026-01-27`
- Ground truth: `\boxed{A}`
- `codex only`: `\boxed{A}` ✅
- `codex + skill`: `\boxed{A}` ✅

## v13ra_002 — At close of business on 23 January 2026, will the most recently announced Bank of Japan (BOJ) "uncollateralized overnight call [interest] rate" be lower, the same, or higher than it was at close of business on 19 December 2025?

- Category: `central_bank_decision`
- Search cutoff: `2026-01-23`
- Ground truth: `\boxed{B}`
- `codex only`: `\boxed{B}` ✅
- `codex + skill`: `\boxed{B}` ✅

## v13ra_003 — Reserve Bank of Australia Decision in February

- Category: `central_bank_decision`
- Search cutoff: `2026-02-03`
- Ground truth: `\boxed{B}`
- `codex only`: `\boxed{B}` ✅
- `codex + skill`: `\boxed{C}` ❌

## v13ra_004 — At close of business on 5 February 2026, will the most recently announced European Central Bank (ECB) "Deposit facility" interest rate be lower, the same, or higher than it was at close of business on 18 December 2025?

- Category: `central_bank_decision`
- Search cutoff: `2026-02-05`
- Ground truth: `\boxed{B}`
- `codex only`: `\boxed{B}` ✅
- `codex + skill`: `\boxed{B}` ✅

## v13ra_005 — Gold (GC) above ___ end of January?

- Category: `commodity_thresholds`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{H, I, J, K, L}`
- `codex only`: `\boxed{F, G, H, I, J, K, L}` ❌
- `codex + skill`: `\boxed{H, I, J, K, L}` ✅

## v13ra_006 — What will Gold (GC) settle at in January?

- Category: `commodity_bucket`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{E}`
- `codex only`: `\boxed{A}` ❌
- `codex + skill`: `\boxed{F}` ❌
