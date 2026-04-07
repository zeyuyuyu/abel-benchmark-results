# v13 FutureX-Online Official Live A/B

Run timestamp: `20260324-144021`
Today context: `March 24, 2026 (UTC+8, Asia/Shanghai)`
Case count: `7`
Resolved cases: `5`
Pending cases: `2`

Only resolved cases count toward accuracy. Pending cases remain unanswered by design until the external source settles them.

| Run | Correct on resolved subset | Accuracy on resolved subset | Duration (s) |
|-----|----------------------------|-----------------------------|--------------|
| `base` | `3/5` | `0.6` | `722.09` |
| `skill` | `2/5` | `0.4` | `1217.83` |

## Per-Case Status

| Case ID | Source ID | Ground Truth | Base | Skill | Status |
|---------|-----------|--------------|------|-------|--------|
| `v13_001` | `69a2e39e5692ef005cdbf2d9` | `\boxed{B, C, D, E, F}` | `\boxed{F, I, J}` | `\boxed{F, I, J}` | both incorrect |
| `v13_002` | `69a2e39e5692ef005cdbf2e9` | `pending` | `\boxed{B, C, D, E, F, G, H, J, K, L, M, N, O}` | `\boxed{B, C, D, E, F, J, K, L, M}` | pending |
| `v13_003` | `69a2e39e5692ef005cdbf2d8` | `\boxed{A}` | `\boxed{A}` | `\boxed{A}` | both correct |
| `v13_004` | `69a2e39e5692ef005cdbf2e8` | `\boxed{C, F, G}` | `\boxed{A, C, F, G, H}` | `\boxed{A, C, F, G, H}` | both incorrect |
| `v13_005` | `69a4319df2cb3b006875e9d0` | `pending` | `\boxed{}` | `\boxed{A}` | pending |
| `v13_006` | `699c4887d1d3cf005c1e48ad` | `\boxed{B}` | `\boxed{B}` | `\boxed{A}` | base only |
| `v13_007` | `69a2e39e5692ef005cdbf27c` | `\boxed{No}` | `\boxed{No}` | `\boxed{No}` | both correct |

## Full Cases

### v13_001 — S&P 500 Single-Day Gains and Losses (%) in Q1

- FutureX source id: `69a2e39e5692ef005cdbf2d9`
- End time: `2026-03-31`
- Difficulty level: `2`
- Ground truth: `\boxed{B, C, D, E, F}`
- Base: `\boxed{F, I, J}` (incorrect)
- Skill: `\boxed{F, I, J}` (incorrect)

Prompt:

```text
You are an agent that can predict future events. The event to be predicted: "S&P 500 Single-Day Gains and Losses (%) in Q1 (resolved around 2026-03-31 (GMT+8)). 
A.  the S&P 500 Index gain at least 5% on any day in Q1
B.  the S&P 500 Index lose at least 5% on any day in Q1
C.  the S&P 500 Index gain at least 3% on any day in Q1
D.  the S&P 500 Index lose at least 3% on any day in Q1
E.  the S&P 500 Index gain at least 4% on any day in Q1
F.  the S&P 500 Index lose at least 2% on any day in Q1
G.  the S&P 500 Index lose at least 4% on any day in Q1
H.  the S&P 500 Index gain at least 2% on any day in Q1
I.  the S&P 500 Index gain at least 1% on any day in Q1
J.  the S&P 500 Index lose at least 1% on any day in Q1"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

### v13_002 — What will KOSPI (^KS11) hit in Q1 2026?

- FutureX source id: `69a2e39e5692ef005cdbf2e9`
- End time: `2026-03-31`
- Difficulty level: `2`
- Ground truth: `pending`
- Base: `\boxed{B, C, D, E, F, G, H, J, K, L, M, N, O}` (pending)
- Skill: `\boxed{B, C, D, E, F, J, K, L, M}` (pending)

Prompt:

```text
You are an agent that can predict future events. The event to be predicted: "What will KOSPI (^KS11) hit in Q1 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  KOSPI Composite Index (^KS11) hit 7000 (HIGH) in Q1 2026
B.  KOSPI Composite Index (^KS11) hit 6000 (HIGH) in Q1 2026
C.  KOSPI Composite Index (^KS11) hit 5500 (HIGH) in Q1 2026
D.  KOSPI Composite Index (^KS11) hit 5300 (HIGH) in Q1 2026
E.  KOSPI Composite Index (^KS11) hit 5100 (HIGH) in Q1 2026
F.  KOSPI Composite Index (^KS11) hit 4900 (LOW) in Q1 2026
G.  KOSPI Composite Index (^KS11) hit 4700 (LOW) in Q1 2026
H.  KOSPI Composite Index (^KS11) hit 4500 (LOW) in Q1 2026
I.  KOSPI Composite Index (^KS11) hit 6500 (HIGH) in Q1 2026
J.  KOSPI Composite Index (^KS11) hit 5750 (HIGH) in Q1 2026
K.  KOSPI Composite Index (^KS11) hit 5400 (HIGH) in Q1 2026
L.  KOSPI Composite Index (^KS11) hit 5200 (HIGH) in Q1 2026
M.  KOSPI Composite Index (^KS11) hit 5000 (HIGH) in Q1 2026
N.  KOSPI Composite Index (^KS11) hit 4800 (LOW) in Q1 2026
O.  KOSPI Composite Index (^KS11) hit 4600 (LOW) in Q1 2026"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

### v13_003 — Q1 S&P 500 Performance

- FutureX source id: `69a2e39e5692ef005cdbf2d8`
- End time: `2026-03-31`
- Difficulty level: `2`
- Ground truth: `\boxed{A}`
- Base: `\boxed{A}` (correct)
- Skill: `\boxed{A}` (correct)

Prompt:

```text
You are an agent that can predict future events. The event to be predicted: "Q1 S&P 500 Performance (resolved around 2026-03-31 (GMT+8)). 
A.  the percentage change in the S&P 500 in Q1 2026 be less than 0%
B.  the percentage change in the S&P 500 in Q1 2026 be between 3% and 4%
C.  the percentage change in the S&P 500 in Q1 2026 be between 8% and 10%
D.  the percentage change in the S&P 500 in Q1 2026 be at least 10%
E.  the percentage change in the S&P 500 in Q1 2026 be between 0% and 2%
F.  the percentage change in the S&P 500 in Q1 2026 be between 2% and 3%
G.  the percentage change in the S&P 500 in Q1 2026 be between 5% and 6%
H.  the percentage change in the S&P 500 in Q1 2026 be between 4% and 5%
I.  the percentage change in the S&P 500 in Q1 2026 be between 6% and 8%"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

### v13_004 — Will KOSPI (KS11) close above __ end of Q1?

- FutureX source id: `69a2e39e5692ef005cdbf2e8`
- End time: `2026-03-31`
- Difficulty level: `2`
- Ground truth: `\boxed{C, F, G}`
- Base: `\boxed{A, C, F, G, H}` (incorrect)
- Skill: `\boxed{A, C, F, G, H}` (incorrect)

Prompt:

```text
You are an agent that can predict future events. The event to be predicted: "Will KOSPI (KS11) close above __ end of Q1? (resolved around 2026-03-31 (GMT+8)). 
A.  the KOSPI Composite Index (^KS11) close above 5250 on the final trading day of Q1 2026
B.  the KOSPI Composite Index (^KS11) close above 6000 on the final trading day of Q1 2026
C.  the KOSPI Composite Index (^KS11) close above 4750 on the final trading day of Q1 2026
D.  the KOSPI Composite Index (^KS11) close above 5750 on the final trading day of Q1 2026
E.  the KOSPI Composite Index (^KS11) close above 7000 on the final trading day of Q1 2026
F.  the KOSPI Composite Index (^KS11) close above 5000 on the final trading day of Q1 2026
G.  the KOSPI Composite Index (^KS11) close above 4500 on the final trading day of Q1 2026
H.  the KOSPI Composite Index (^KS11) close above 5500 on the final trading day of Q1 2026
I.  the KOSPI Composite Index (^KS11) close above 6500 on the final trading day of Q1 2026"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

### v13_005 — What price will Bitcoin hit by March 2026? (add your prediction)

- FutureX source id: `69a4319df2cb3b006875e9d0`
- End time: `2026-03-31`
- Difficulty level: `2`
- Ground truth: `pending`
- Base: `\boxed{}` (pending)
- Skill: `\boxed{A}` (pending)

Prompt:

```text
You are an agent that can predict future events. The event to be predicted: "What price will Bitcoin hit by March 2026? (add your prediction) (resolved around 2026-03-31 (GMT+8)). 
A.  the outcome be $75,001 - $80,000
B.  the outcome be $80,001 - $85,000
C.  the outcome be $85,001 - $90,000
D.  the outcome be $90,001 - $95,000
E.  the outcome be $95,001 - $100,000
F.  the outcome be $100,001 - $105,000
G.  the outcome be $105,001 - $110,000
H.  the outcome be $110,001 - $115,000"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

### v13_006 — Banxico interest rate decision in March

- FutureX source id: `699c4887d1d3cf005c1e48ad`
- End time: `2026-03-26`
- Difficulty level: `1`
- Ground truth: `\boxed{B}`
- Base: `\boxed{B}` (correct)
- Skill: `\boxed{A}` (incorrect)

Prompt:

```text
You are an agent that can predict future events. The event to be predicted: "Banxico interest rate decision in March (resolved around 2026-03-26 (GMT+8)). 
A.  the outcome be Lower the rate
B.  the outcome be Maintain the same rate
C.  the outcome be Increase the rate"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

### v13_007 — Robinhood launches prediction market through MIAXdx by March 31?

- FutureX source id: `69a2e39e5692ef005cdbf27c`
- End time: `2026-03-31`
- Difficulty level: `1`
- Ground truth: `\boxed{No}`
- Base: `\boxed{No}` (correct)
- Skill: `\boxed{No}` (correct)

Prompt:

```text
You are an agent that can predict future events. The event to be predicted: "Robinhood launches prediction market through MIAXdx by March 31? (resolved around 2026-03-31 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

