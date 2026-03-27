# v13 Resolved As-Of Partial Results

Open-book run with time-bounded search (`search_cutoff`) over the first 9 completed cases.

- Base: `6/9 = 66.67%`
- Skill: `5/9 = 55.56%`

| Case ID | Category | Cutoff | Ground truth | Base | Skill | Notes |
|---|---|---|---|---|---|---|
| `v13ra_001` | `central_bank_decision` | `2026-01-27` | `\boxed{A}` | `\boxed{A}` ✅ | `\boxed{A}` ✅ | resolved_asof_test_script.py --batch-size 1 |
| `v13ra_002` | `central_bank_decision` | `2026-01-23` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ | resolved_asof_test_script.py --batch-size 1 |
| `v13ra_003` | `central_bank_decision` | `2026-02-03` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{C}` ❌ | resolved_asof_test_script.py --batch-size 1 |
| `v13ra_004` | `central_bank_decision` | `2026-02-05` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ | resolved_asof_test_script.py --batch-size 1 |
| `v13ra_005` | `commodity_thresholds` | `2026-02-01` | `\boxed{H, I, J, K, L}` | `\boxed{F, G, H, I, J, K, L}` ❌ | `\boxed{H, I, J, K, L}` ✅ | resolved_asof_test_script.py --batch-size 1 |
| `v13ra_006` | `commodity_bucket` | `2026-02-01` | `\boxed{E}` | `\boxed{A}` ❌ | `\boxed{F}` ❌ | resolved_asof_test_script.py --batch-size 1 |
| `v13ra_007` | `commodity_hit_levels` | `2026-02-01` | `\boxed{B, C, G, J}` | `\boxed{B, C, G, J}` ✅ | `\boxed{B, C, G, J}` ✅ | resolved_asof light prompt |
| `v13ra_008` | `commodity_bucket` | `2026-02-01` | `\boxed{F}` | `\boxed{F}` ✅ | `None` timeout | resolved_asof light prompt |
| `v13ra_009` | `first_hit` | `2026-02-01` | `\boxed{A}` | `\boxed{C}` ❌ | `\boxed{C}` ❌ | resolved_asof light prompt |

## v13ra_001 — Bank of Brazil decision in January?

- Category: `central_bank_decision`
- Search cutoff: `2026-01-27`
- Ground truth: `\boxed{A}`
- `codex only`: `\boxed{A}` ✅
- `codex + skill`: `\boxed{A}` ✅
- Runner: `resolved_asof_test_script.py --batch-size 1`

## v13ra_002 — At close of business on 23 January 2026, will the most recently announced Bank of Japan (BOJ) "uncollateralized overnight call [interest] rate" be lower, the same, or higher than it was at close of business on 19 December 2025?

- Category: `central_bank_decision`
- Search cutoff: `2026-01-23`
- Ground truth: `\boxed{B}`
- `codex only`: `\boxed{B}` ✅
- `codex + skill`: `\boxed{B}` ✅
- Runner: `resolved_asof_test_script.py --batch-size 1`

## v13ra_003 — Reserve Bank of Australia Decision in February

- Category: `central_bank_decision`
- Search cutoff: `2026-02-03`
- Ground truth: `\boxed{B}`
- `codex only`: `\boxed{B}` ✅
- `codex + skill`: `\boxed{C}` ❌
- Runner: `resolved_asof_test_script.py --batch-size 1`

## v13ra_004 — At close of business on 5 February 2026, will the most recently announced European Central Bank (ECB) "Deposit facility" interest rate be lower, the same, or higher than it was at close of business on 18 December 2025?

- Category: `central_bank_decision`
- Search cutoff: `2026-02-05`
- Ground truth: `\boxed{B}`
- `codex only`: `\boxed{B}` ✅
- `codex + skill`: `\boxed{B}` ✅
- Runner: `resolved_asof_test_script.py --batch-size 1`

## v13ra_005 — Gold (GC) above ___ end of January?

- Category: `commodity_thresholds`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{H, I, J, K, L}`
- `codex only`: `\boxed{F, G, H, I, J, K, L}` ❌
- `codex + skill`: `\boxed{H, I, J, K, L}` ✅
- Runner: `resolved_asof_test_script.py --batch-size 1`

## v13ra_006 — What will Gold (GC) settle at in January?

- Category: `commodity_bucket`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{E}`
- `codex only`: `\boxed{A}` ❌
- `codex + skill`: `\boxed{F}` ❌
- Runner: `resolved_asof_test_script.py --batch-size 1`

## v13ra_007 — What will Crude Oil (CL) hit__ by end of January?

- Category: `commodity_hit_levels`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{B, C, G, J}`
- `codex only`: `\boxed{B, C, G, J}` ✅
- `codex + skill`: `\boxed{B, C, G, J}` ✅
- Runner: `resolved_asof light prompt`

## v13ra_008 — What will Crude Oil (CL) settle at in January?

- Category: `commodity_bucket`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{F}`
- `codex only`: `\boxed{F}` ✅
- `codex + skill`: `None` timeout
- Runner: `resolved_asof light prompt`

## v13ra_009 — Tesla hits $400 or $500 first before end of January 2026?

- Category: `first_hit`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{A}`
- `codex only`: `\boxed{C}` ❌
- `codex + skill`: `\boxed{C}` ❌
- Runner: `resolved_asof light prompt`
