# v14 Track G Past-As-Of Results

Full `historical_asof_search_cutoff` run over the 15-case Track G pack.

- Base: `10/15 = 66.67%`
- Skill: `9/15 = 60.00%`
- Base valid outputs: `14/15`
- Skill valid outputs: `13/15`
- Base duration: `1344.25s`
- Skill duration: `1625.23s`

| Case ID | Category | Cutoff | Ground truth | Base | Skill | Notes |
|---|---|---|---|---|---|---|
| `v13ra_001` | `central_bank_decision` | `2026-01-27` | `\boxed{A}` | `\boxed{A}` ✅ | `\boxed{A}` ✅ | completed |
| `v13ra_002` | `central_bank_decision` | `2026-01-23` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ | completed |
| `v13ra_005` | `commodity_thresholds` | `2026-02-01` | `\boxed{H, I, J, K, L}` | `\boxed{H}` ❌ | `\boxed{F}` ❌ | completed |
| `v13ra_008` | `commodity_bucket` | `2026-02-01` | `\boxed{F}` | `\boxed{F}` ✅ | `\boxed{F}` ✅ | completed |
| `v13ra_007` | `commodity_hit_levels` | `2026-02-01` | `\boxed{B, C, G, J}` | `\boxed{BCGJ}` ❌ | `None` | base_invalid_or_missing, skill_invalid_or_missing |
| `v13ra_006` | `commodity_bucket` | `2026-02-01` | `\boxed{E}` | `\boxed{E}` ✅ | `None` | skill_invalid_or_missing |
| `v13ra_009` | `first_hit` | `2026-02-01` | `\boxed{A}` | `\boxed{C}` ❌ | `\boxed{C}` ❌ | completed |
| `v13ra_003` | `central_bank_decision` | `2026-02-03` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ | completed |
| `v13ra_010` | `first_hit` | `2026-02-01` | `\boxed{A}` | `\boxed{C}` ❌ | `\boxed{C}` ❌ | completed |
| `v13ra_011` | `crypto_binary` | `2026-01-31` | `\boxed{No}` | `\boxed{No}` ✅ | `\boxed{No}` ✅ | completed |
| `v13ra_012` | `crypto_binary` | `2026-02-02` | `\boxed{Yes}` | `\boxed{Yes}` ✅ | `\boxed{Yes}` ✅ | completed |
| `v13ra_004` | `central_bank_decision` | `2026-02-05` | `\boxed{B}` | `\boxed{B}` ✅ | `\boxed{B}` ✅ | completed |
| `v13ra_013` | `agriculture_bucket` | `2026-03-06` | `\boxed{E}` | `\boxed{E}` ✅ | `\boxed{E}` ✅ | completed |
| `v13ra_014` | `supply_shock_binary` | `2026-03-04` | `\boxed{No}` | `\boxed{No}` ✅ | `\boxed{No}` ✅ | completed |
| `v13ra_015` | `single_stock_direction` | `2026-03-16` | `\boxed{No}` | `\boxed{Yes}` ❌ | `\boxed{Yes}` ❌ | completed |

## Per-Category

- `agriculture_bucket`: base `1/1`, skill `1/1`
- `central_bank_decision`: base `4/4`, skill `4/4`
- `commodity_bucket`: base `2/2`, skill `1/2`
- `commodity_hit_levels`: base `0/1`, skill `0/1`
- `commodity_thresholds`: base `0/1`, skill `0/1`
- `crypto_binary`: base `2/2`, skill `2/2`
- `first_hit`: base `0/2`, skill `0/2`
- `single_stock_direction`: base `0/1`, skill `0/1`
- `supply_shock_binary`: base `1/1`, skill `1/1`

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

## v13ra_005 — Gold (GC) above ___ end of January?

- Category: `commodity_thresholds`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{H, I, J, K, L}`
- `codex only`: `\boxed{H}` ❌
- `codex + skill`: `\boxed{F}` ❌

## v13ra_008 — What will Crude Oil (CL) settle at in January?

- Category: `commodity_bucket`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{F}`
- `codex only`: `\boxed{F}` ✅
- `codex + skill`: `\boxed{F}` ✅

## v13ra_007 — What will Crude Oil (CL) hit__ by end of January?

- Category: `commodity_hit_levels`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{B, C, G, J}`
- `codex only`: `\boxed{BCGJ}` ❌
- `codex + skill`: `None`

## v13ra_006 — What will Gold (GC) settle at in January?

- Category: `commodity_bucket`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{E}`
- `codex only`: `\boxed{E}` ✅
- `codex + skill`: `None`

## v13ra_009 — Tesla hits $400 or $500 first before end of January 2026?

- Category: `first_hit`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{A}`
- `codex only`: `\boxed{C}` ❌
- `codex + skill`: `\boxed{C}` ❌

## v13ra_003 — Reserve Bank of Australia Decision in February

- Category: `central_bank_decision`
- Search cutoff: `2026-02-03`
- Ground truth: `\boxed{B}`
- `codex only`: `\boxed{B}` ✅
- `codex + skill`: `\boxed{B}` ✅

## v13ra_010 — Nvidia hits 170, 200 or neither first by end of January 2026?

- Category: `first_hit`
- Search cutoff: `2026-02-01`
- Ground truth: `\boxed{A}`
- `codex only`: `\boxed{C}` ❌
- `codex + skill`: `\boxed{C}` ❌

## v13ra_011 — Will Bitcoin close above USD $100,000 on 31 January 2026 (UTC)?

- Category: `crypto_binary`
- Search cutoff: `2026-01-31`
- Ground truth: `\boxed{No}`
- `codex only`: `\boxed{No}` ✅
- `codex + skill`: `\boxed{No}` ✅

## v13ra_012 — Bitcoin below $82K in January?

- Category: `crypto_binary`
- Search cutoff: `2026-02-02`
- Ground truth: `\boxed{Yes}`
- `codex only`: `\boxed{Yes}` ✅
- `codex + skill`: `\boxed{Yes}` ✅

## v13ra_004 — At close of business on 5 February 2026, will the most recently announced European Central Bank (ECB) "Deposit facility" interest rate be lower, the same, or higher than it was at close of business on 18 December 2025?

- Category: `central_bank_decision`
- Search cutoff: `2026-02-05`
- Ground truth: `\boxed{B}`
- `codex only`: `\boxed{B}` ✅
- `codex + skill`: `\boxed{B}` ✅

## v13ra_013 — Between 10 October 2025 and 6 March 2026, what will be the lowest closing price of soybeans?

- Category: `agriculture_bucket`
- Search cutoff: `2026-03-06`
- Ground truth: `\boxed{E}`
- `codex only`: `\boxed{E}` ✅
- `codex + skill`: `\boxed{E}` ✅

## v13ra_014 — Will global platinum availability fall below 2 million ounces by March 4, 2026, due to South African mine supply issues?

- Category: `supply_shock_binary`
- Search cutoff: `2026-03-04`
- Ground truth: `\boxed{No}`
- `codex only`: `\boxed{No}` ✅
- `codex + skill`: `\boxed{No}` ✅

## v13ra_015 — Will NVIDIA stock be higher on March 16, 2026 than on March 09, 2026?

- Category: `single_stock_direction`
- Search cutoff: `2026-03-16`
- Ground truth: `\boxed{No}`
- `codex only`: `\boxed{Yes}` ❌
- `codex + skill`: `\boxed{Yes}` ❌
