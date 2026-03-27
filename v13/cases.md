# v13 Live-Only Finance Cases

This is the human-readable casebook for the live-only main benchmark.

- Every case is expanded below.
- Because these are live cases, the markdown leaves ground truth blank unless the case has already been resolved later.
- The machine-readable resolution rules still live in `ground_truth.json`.

Today context: `March 26, 2026 (GMT+8, Asia/Shanghai)`

## v13_001 — S&P 500 Single-Day Gains and Losses (%) in Q1

- Source: `futurex_online`
- Category: `futurex_official`
- Pattern: `futurex_official`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
S&P 500 Single-Day Gains and Losses (%) in Q1
```

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

Ground truth: ``

## v13_002 — What will KOSPI (^KS11) hit in Q1 2026?

- Source: `futurex_online`
- Category: `threshold_ladder`
- Pattern: `futurex_official`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
What will KOSPI (^KS11) hit in Q1 2026?
```

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

Ground truth: ``

## v13_003 — Q1 S&P 500 Performance

- Source: `futurex_online`
- Category: `threshold_truth_set`
- Pattern: `futurex_official`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Q1 S&P 500 Performance
```

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

Ground truth: ``

## v13_004 — Will KOSPI (KS11) close above __ end of Q1?

- Source: `futurex_online`
- Category: `threshold_truth_set`
- Pattern: `futurex_official`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Will KOSPI (KS11) close above __ end of Q1?
```

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

Ground truth: ``

## v13_005 — What price will Bitcoin hit by March 2026? (add your prediction)

- Source: `futurex_online`
- Category: `threshold_ladder`
- Pattern: `futurex_official`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
What price will Bitcoin hit by March 2026? (add your prediction)
```

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

Ground truth: ``

## v13_006 — Banxico interest rate decision in March

- Source: `futurex_online`
- Category: `binary_event`
- Pattern: `futurex_official`
- End time: `2026-03-26`
- Answer format: `boxed_letters`

Question:
```text
Banxico interest rate decision in March
```

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

Ground truth: ``

## v13_007 — Robinhood launches prediction market through MIAXdx by March 31?

- Source: `futurex_online`
- Category: `binary_event`
- Pattern: `futurex_official`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Robinhood launches prediction market through MIAXdx by March 31?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Robinhood launches prediction market through MIAXdx by March 31? (resolved around 2026-03-31 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_008 — What will Gold futures (GC) close at on March 31, 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
What will Gold futures (GC) close at on March 31, 2026?
```

Options:
- `A`: Gold futures (GC) closes below $4,350
- `B`: Gold futures (GC) closes at least $4,350 but below $4,400
- `C`: Gold futures (GC) closes at least $4,400 but below $4,450
- `D`: Gold futures (GC) closes at least $4,450 but below $4,500
- `E`: Gold futures (GC) closes at least $4,500

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will Gold futures (GC) close at on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Gold futures (GC) closes below $4,350
B.  Gold futures (GC) closes at least $4,350 but below $4,400
C.  Gold futures (GC) closes at least $4,400 but below $4,450
D.  Gold futures (GC) closes at least $4,450 but below $4,500
E.  Gold futures (GC) closes at least $4,500"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_009 — Where will WTI crude oil futures (CL) settle on the final trading day of March 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Where will WTI crude oil futures (CL) settle on the final trading day of March 2026?
```

Options:
- `A`: WTI crude oil futures (CL) closes below $90
- `B`: WTI crude oil futures (CL) closes at least $90 but below $92
- `C`: WTI crude oil futures (CL) closes at least $92 but below $94
- `D`: WTI crude oil futures (CL) closes at least $94 but below $96
- `E`: WTI crude oil futures (CL) closes at least $96

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Where will WTI crude oil futures (CL) settle on the final trading day of March 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  WTI crude oil futures (CL) closes below $90
B.  WTI crude oil futures (CL) closes at least $90 but below $92
C.  WTI crude oil futures (CL) closes at least $92 but below $94
D.  WTI crude oil futures (CL) closes at least $94 but below $96
E.  WTI crude oil futures (CL) closes at least $96"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_010 — What price range will Bitcoin (BTC-USD) close in on March 31, 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
What price range will Bitcoin (BTC-USD) close in on March 31, 2026?
```

Options:
- `A`: Bitcoin (BTC-USD) closes below $64,000
- `B`: Bitcoin (BTC-USD) closes at least $64,000 but below $66,000
- `C`: Bitcoin (BTC-USD) closes at least $66,000 but below $68,000
- `D`: Bitcoin (BTC-USD) closes at least $68,000 but below $70,000
- `E`: Bitcoin (BTC-USD) closes at least $70,000

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What price range will Bitcoin (BTC-USD) close in on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Bitcoin (BTC-USD) closes below $64,000
B.  Bitcoin (BTC-USD) closes at least $64,000 but below $66,000
C.  Bitcoin (BTC-USD) closes at least $66,000 but below $68,000
D.  Bitcoin (BTC-USD) closes at least $68,000 but below $70,000
E.  Bitcoin (BTC-USD) closes at least $70,000"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_011 — Where will Ethereum (ETH-USD) finish on March 31, 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Where will Ethereum (ETH-USD) finish on March 31, 2026?
```

Options:
- `A`: Ethereum (ETH-USD) closes below $1,900
- `B`: Ethereum (ETH-USD) closes at least $1,900 but below $2,000
- `C`: Ethereum (ETH-USD) closes at least $2,000 but below $2,100
- `D`: Ethereum (ETH-USD) closes at least $2,100 but below $2,200
- `E`: Ethereum (ETH-USD) closes at least $2,200

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Where will Ethereum (ETH-USD) finish on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Ethereum (ETH-USD) closes below $1,900
B.  Ethereum (ETH-USD) closes at least $1,900 but below $2,000
C.  Ethereum (ETH-USD) closes at least $2,000 but below $2,100
D.  Ethereum (ETH-USD) closes at least $2,100 but below $2,200
E.  Ethereum (ETH-USD) closes at least $2,200"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_012 — What will NVIDIA (NVDA) close at by the end of March 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
What will NVIDIA (NVDA) close at by the end of March 2026?
```

Options:
- `A`: NVIDIA (NVDA) closes below $160
- `B`: NVIDIA (NVDA) closes at least $160 but below $165
- `C`: NVIDIA (NVDA) closes at least $165 but below $170
- `D`: NVIDIA (NVDA) closes at least $170 but below $175
- `E`: NVIDIA (NVDA) closes at least $175

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will NVIDIA (NVDA) close at by the end of March 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  NVIDIA (NVDA) closes below $160
B.  NVIDIA (NVDA) closes at least $160 but below $165
C.  NVIDIA (NVDA) closes at least $165 but below $170
D.  NVIDIA (NVDA) closes at least $170 but below $175
E.  NVIDIA (NVDA) closes at least $175"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_013 — Which range best describes the AMD (AMD) close on March 31, 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which range best describes the AMD (AMD) close on March 31, 2026?
```

Options:
- `A`: AMD (AMD) closes below $195
- `B`: AMD (AMD) closes at least $195 but below $200
- `C`: AMD (AMD) closes at least $200 but below $205
- `D`: AMD (AMD) closes at least $205 but below $210
- `E`: AMD (AMD) closes at least $210

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which range best describes the AMD (AMD) close on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  AMD (AMD) closes below $195
B.  AMD (AMD) closes at least $195 but below $200
C.  AMD (AMD) closes at least $200 but below $205
D.  AMD (AMD) closes at least $205 but below $210
E.  AMD (AMD) closes at least $210"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_014 — What is the most likely closing range for Broadcom (AVGO) on March 31, 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
What is the most likely closing range for Broadcom (AVGO) on March 31, 2026?
```

Options:
- `A`: Broadcom (AVGO) closes below $300
- `B`: Broadcom (AVGO) closes at least $300 but below $305
- `C`: Broadcom (AVGO) closes at least $305 but below $310
- `D`: Broadcom (AVGO) closes at least $310 but below $315
- `E`: Broadcom (AVGO) closes at least $315

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What is the most likely closing range for Broadcom (AVGO) on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Broadcom (AVGO) closes below $300
B.  Broadcom (AVGO) closes at least $300 but below $305
C.  Broadcom (AVGO) closes at least $305 but below $310
D.  Broadcom (AVGO) closes at least $310 but below $315
E.  Broadcom (AVGO) closes at least $315"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_015 — Where does Taiwan Semiconductor (TSM) end up at the March 31, 2026 close?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Where does Taiwan Semiconductor (TSM) end up at the March 31, 2026 close?
```

Options:
- `A`: Taiwan Semiconductor (TSM) closes below $315
- `B`: Taiwan Semiconductor (TSM) closes at least $315 but below $320
- `C`: Taiwan Semiconductor (TSM) closes at least $320 but below $325
- `D`: Taiwan Semiconductor (TSM) closes at least $325 but below $330
- `E`: Taiwan Semiconductor (TSM) closes at least $330

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Where does Taiwan Semiconductor (TSM) end up at the March 31, 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  Taiwan Semiconductor (TSM) closes below $315
B.  Taiwan Semiconductor (TSM) closes at least $315 but below $320
C.  Taiwan Semiconductor (TSM) closes at least $320 but below $325
D.  Taiwan Semiconductor (TSM) closes at least $325 but below $330
E.  Taiwan Semiconductor (TSM) closes at least $330"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_016 — What will the closing price of Tesla (TSLA) be on the final trading day of March 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
What will the closing price of Tesla (TSLA) be on the final trading day of March 2026?
```

Options:
- `A`: Tesla (TSLA) closes below $350
- `B`: Tesla (TSLA) closes at least $350 but below $360
- `C`: Tesla (TSLA) closes at least $360 but below $370
- `D`: Tesla (TSLA) closes at least $370 but below $380
- `E`: Tesla (TSLA) closes at least $380

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will the closing price of Tesla (TSLA) be on the final trading day of March 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Tesla (TSLA) closes below $350
B.  Tesla (TSLA) closes at least $350 but below $360
C.  Tesla (TSLA) closes at least $360 but below $370
D.  Tesla (TSLA) closes at least $370 but below $380
E.  Tesla (TSLA) closes at least $380"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_017 — Where will Apple (AAPL) close at month-end on March 31, 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Where will Apple (AAPL) close at month-end on March 31, 2026?
```

Options:
- `A`: Apple (AAPL) closes below $245
- `B`: Apple (AAPL) closes at least $245 but below $250
- `C`: Apple (AAPL) closes at least $250 but below $255
- `D`: Apple (AAPL) closes at least $255 but below $260
- `E`: Apple (AAPL) closes at least $260

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Where will Apple (AAPL) close at month-end on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Apple (AAPL) closes below $245
B.  Apple (AAPL) closes at least $245 but below $250
C.  Apple (AAPL) closes at least $250 but below $255
D.  Apple (AAPL) closes at least $255 but below $260
E.  Apple (AAPL) closes at least $260"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_018 — Which closing bucket fits Microsoft (MSFT) on March 31, 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which closing bucket fits Microsoft (MSFT) on March 31, 2026?
```

Options:
- `A`: Microsoft (MSFT) closes below $355
- `B`: Microsoft (MSFT) closes at least $355 but below $360
- `C`: Microsoft (MSFT) closes at least $360 but below $365
- `D`: Microsoft (MSFT) closes at least $365 but below $370
- `E`: Microsoft (MSFT) closes at least $370

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which closing bucket fits Microsoft (MSFT) on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Microsoft (MSFT) closes below $355
B.  Microsoft (MSFT) closes at least $355 but below $360
C.  Microsoft (MSFT) closes at least $360 but below $365
D.  Microsoft (MSFT) closes at least $365 but below $370
E.  Microsoft (MSFT) closes at least $370"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_019 — What closing range does Amazon (AMZN) land in on March 31, 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
What closing range does Amazon (AMZN) land in on March 31, 2026?
```

Options:
- `A`: Amazon (AMZN) closes below $200
- `B`: Amazon (AMZN) closes at least $200 but below $205
- `C`: Amazon (AMZN) closes at least $205 but below $210
- `D`: Amazon (AMZN) closes at least $210 but below $215
- `E`: Amazon (AMZN) closes at least $215

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What closing range does Amazon (AMZN) land in on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Amazon (AMZN) closes below $200
B.  Amazon (AMZN) closes at least $200 but below $205
C.  Amazon (AMZN) closes at least $205 but below $210
D.  Amazon (AMZN) closes at least $210 but below $215
E.  Amazon (AMZN) closes at least $215"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_020 — Where will Meta (META) finish at the March 2026 close?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Where will Meta (META) finish at the March 2026 close?
```

Options:
- `A`: Meta (META) closes below $530
- `B`: Meta (META) closes at least $530 but below $540
- `C`: Meta (META) closes at least $540 but below $550
- `D`: Meta (META) closes at least $550 but below $560
- `E`: Meta (META) closes at least $560

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Where will Meta (META) finish at the March 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  Meta (META) closes below $530
B.  Meta (META) closes at least $530 but below $540
C.  Meta (META) closes at least $540 but below $550
D.  Meta (META) closes at least $550 but below $560
E.  Meta (META) closes at least $560"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_021 — What will Invesco QQQ Trust (QQQ) close at on the last trading day of March 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
What will Invesco QQQ Trust (QQQ) close at on the last trading day of March 2026?
```

Options:
- `A`: Invesco QQQ Trust (QQQ) closes below $565
- `B`: Invesco QQQ Trust (QQQ) closes at least $565 but below $570
- `C`: Invesco QQQ Trust (QQQ) closes at least $570 but below $575
- `D`: Invesco QQQ Trust (QQQ) closes at least $575 but below $580
- `E`: Invesco QQQ Trust (QQQ) closes at least $580

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will Invesco QQQ Trust (QQQ) close at on the last trading day of March 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Invesco QQQ Trust (QQQ) closes below $565
B.  Invesco QQQ Trust (QQQ) closes at least $565 but below $570
C.  Invesco QQQ Trust (QQQ) closes at least $570 but below $575
D.  Invesco QQQ Trust (QQQ) closes at least $575 but below $580
E.  Invesco QQQ Trust (QQQ) closes at least $580"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_022 — Which bucket contains the SPDR S&P 500 ETF (SPY) close on March 31, 2026?

- Source: `custom_live`
- Category: `month_end_bucket`
- Pattern: `interval bin`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which bucket contains the SPDR S&P 500 ETF (SPY) close on March 31, 2026?
```

Options:
- `A`: SPDR S&P 500 ETF (SPY) closes below $635
- `B`: SPDR S&P 500 ETF (SPY) closes at least $635 but below $640
- `C`: SPDR S&P 500 ETF (SPY) closes at least $640 but below $645
- `D`: SPDR S&P 500 ETF (SPY) closes at least $645 but below $650
- `E`: SPDR S&P 500 ETF (SPY) closes at least $650

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which bucket contains the SPDR S&P 500 ETF (SPY) close on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  SPDR S&P 500 ETF (SPY) closes below $635
B.  SPDR S&P 500 ETF (SPY) closes at least $635 but below $640
C.  SPDR S&P 500 ETF (SPY) closes at least $640 but below $645
D.  SPDR S&P 500 ETF (SPY) closes at least $645 but below $650
E.  SPDR S&P 500 ETF (SPY) closes at least $650"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_023 — Which of these statements about the Bitcoin (BTC-USD) close on March 31, 2026 will be true?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these statements about the Bitcoin (BTC-USD) close on March 31, 2026 will be true?
```

Options:
- `A`: Bitcoin (BTC-USD) closes above $64,000 at the March 2026 close
- `B`: Bitcoin (BTC-USD) closes above $66,000 at the March 2026 close
- `C`: Bitcoin (BTC-USD) closes above $68,000 at the March 2026 close
- `D`: Bitcoin (BTC-USD) closes above $70,000 at the March 2026 close
- `E`: Bitcoin (BTC-USD) closes above $72,000 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these statements about the Bitcoin (BTC-USD) close on March 31, 2026 will be true? (resolved around 2026-03-31 (GMT+8)). 
A.  Bitcoin (BTC-USD) closes above $64,000 at the March 2026 close
B.  Bitcoin (BTC-USD) closes above $66,000 at the March 2026 close
C.  Bitcoin (BTC-USD) closes above $68,000 at the March 2026 close
D.  Bitcoin (BTC-USD) closes above $70,000 at the March 2026 close
E.  Bitcoin (BTC-USD) closes above $72,000 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_024 — Which of these Ethereum (ETH-USD) close-above statements still hold at the end of March 2026?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these Ethereum (ETH-USD) close-above statements still hold at the end of March 2026?
```

Options:
- `A`: Ethereum (ETH-USD) closes above $1,900 at the March 2026 close
- `B`: Ethereum (ETH-USD) closes above $2,000 at the March 2026 close
- `C`: Ethereum (ETH-USD) closes above $2,100 at the March 2026 close
- `D`: Ethereum (ETH-USD) closes above $2,200 at the March 2026 close
- `E`: Ethereum (ETH-USD) closes above $2,300 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these Ethereum (ETH-USD) close-above statements still hold at the end of March 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Ethereum (ETH-USD) closes above $1,900 at the March 2026 close
B.  Ethereum (ETH-USD) closes above $2,000 at the March 2026 close
C.  Ethereum (ETH-USD) closes above $2,100 at the March 2026 close
D.  Ethereum (ETH-USD) closes above $2,200 at the March 2026 close
E.  Ethereum (ETH-USD) closes above $2,300 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_025 — Which of these claims about NVIDIA (NVDA) on the March 31, 2026 close will be true?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these claims about NVIDIA (NVDA) on the March 31, 2026 close will be true?
```

Options:
- `A`: NVIDIA (NVDA) closes above $160 at the March 2026 close
- `B`: NVIDIA (NVDA) closes above $165 at the March 2026 close
- `C`: NVIDIA (NVDA) closes above $170 at the March 2026 close
- `D`: NVIDIA (NVDA) closes above $175 at the March 2026 close
- `E`: NVIDIA (NVDA) closes above $180 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these claims about NVIDIA (NVDA) on the March 31, 2026 close will be true? (resolved around 2026-03-31 (GMT+8)). 
A.  NVIDIA (NVDA) closes above $160 at the March 2026 close
B.  NVIDIA (NVDA) closes above $165 at the March 2026 close
C.  NVIDIA (NVDA) closes above $170 at the March 2026 close
D.  NVIDIA (NVDA) closes above $175 at the March 2026 close
E.  NVIDIA (NVDA) closes above $180 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_026 — Which of these higher-close outcomes for AMD (AMD) will be true on March 31, 2026?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these higher-close outcomes for AMD (AMD) will be true on March 31, 2026?
```

Options:
- `A`: AMD (AMD) closes above $195 at the March 2026 close
- `B`: AMD (AMD) closes above $200 at the March 2026 close
- `C`: AMD (AMD) closes above $205 at the March 2026 close
- `D`: AMD (AMD) closes above $210 at the March 2026 close
- `E`: AMD (AMD) closes above $215 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these higher-close outcomes for AMD (AMD) will be true on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  AMD (AMD) closes above $195 at the March 2026 close
B.  AMD (AMD) closes above $200 at the March 2026 close
C.  AMD (AMD) closes above $205 at the March 2026 close
D.  AMD (AMD) closes above $210 at the March 2026 close
E.  AMD (AMD) closes above $215 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_027 — Which of these Tesla (TSLA) closing thresholds are still met at the March 2026 close?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these Tesla (TSLA) closing thresholds are still met at the March 2026 close?
```

Options:
- `A`: Tesla (TSLA) closes above $350 at the March 2026 close
- `B`: Tesla (TSLA) closes above $360 at the March 2026 close
- `C`: Tesla (TSLA) closes above $370 at the March 2026 close
- `D`: Tesla (TSLA) closes above $380 at the March 2026 close
- `E`: Tesla (TSLA) closes above $390 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these Tesla (TSLA) closing thresholds are still met at the March 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  Tesla (TSLA) closes above $350 at the March 2026 close
B.  Tesla (TSLA) closes above $360 at the March 2026 close
C.  Tesla (TSLA) closes above $370 at the March 2026 close
D.  Tesla (TSLA) closes above $380 at the March 2026 close
E.  Tesla (TSLA) closes above $390 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_028 — Which of these statements about Apple (AAPL) finishing above a level on March 31, 2026 will be true?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these statements about Apple (AAPL) finishing above a level on March 31, 2026 will be true?
```

Options:
- `A`: Apple (AAPL) closes above $245 at the March 2026 close
- `B`: Apple (AAPL) closes above $250 at the March 2026 close
- `C`: Apple (AAPL) closes above $255 at the March 2026 close
- `D`: Apple (AAPL) closes above $260 at the March 2026 close
- `E`: Apple (AAPL) closes above $265 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these statements about Apple (AAPL) finishing above a level on March 31, 2026 will be true? (resolved around 2026-03-31 (GMT+8)). 
A.  Apple (AAPL) closes above $245 at the March 2026 close
B.  Apple (AAPL) closes above $250 at the March 2026 close
C.  Apple (AAPL) closes above $255 at the March 2026 close
D.  Apple (AAPL) closes above $260 at the March 2026 close
E.  Apple (AAPL) closes above $265 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_029 — Which of these Microsoft (MSFT) close-above levels remain true at month-end?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these Microsoft (MSFT) close-above levels remain true at month-end?
```

Options:
- `A`: Microsoft (MSFT) closes above $355 at the March 2026 close
- `B`: Microsoft (MSFT) closes above $360 at the March 2026 close
- `C`: Microsoft (MSFT) closes above $365 at the March 2026 close
- `D`: Microsoft (MSFT) closes above $370 at the March 2026 close
- `E`: Microsoft (MSFT) closes above $375 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these Microsoft (MSFT) close-above levels remain true at month-end? (resolved around 2026-03-31 (GMT+8)). 
A.  Microsoft (MSFT) closes above $355 at the March 2026 close
B.  Microsoft (MSFT) closes above $360 at the March 2026 close
C.  Microsoft (MSFT) closes above $365 at the March 2026 close
D.  Microsoft (MSFT) closes above $370 at the March 2026 close
E.  Microsoft (MSFT) closes above $375 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_030 — Which of these outcomes for the Amazon (AMZN) close on March 31, 2026 will be true?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these outcomes for the Amazon (AMZN) close on March 31, 2026 will be true?
```

Options:
- `A`: Amazon (AMZN) closes above $200 at the March 2026 close
- `B`: Amazon (AMZN) closes above $205 at the March 2026 close
- `C`: Amazon (AMZN) closes above $210 at the March 2026 close
- `D`: Amazon (AMZN) closes above $215 at the March 2026 close
- `E`: Amazon (AMZN) closes above $220 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these outcomes for the Amazon (AMZN) close on March 31, 2026 will be true? (resolved around 2026-03-31 (GMT+8)). 
A.  Amazon (AMZN) closes above $200 at the March 2026 close
B.  Amazon (AMZN) closes above $205 at the March 2026 close
C.  Amazon (AMZN) closes above $210 at the March 2026 close
D.  Amazon (AMZN) closes above $215 at the March 2026 close
E.  Amazon (AMZN) closes above $220 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_031 — Which of these stronger month-end close statements about Meta (META) will be true?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these stronger month-end close statements about Meta (META) will be true?
```

Options:
- `A`: Meta (META) closes above $530 at the March 2026 close
- `B`: Meta (META) closes above $540 at the March 2026 close
- `C`: Meta (META) closes above $550 at the March 2026 close
- `D`: Meta (META) closes above $560 at the March 2026 close
- `E`: Meta (META) closes above $570 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these stronger month-end close statements about Meta (META) will be true? (resolved around 2026-03-31 (GMT+8)). 
A.  Meta (META) closes above $530 at the March 2026 close
B.  Meta (META) closes above $540 at the March 2026 close
C.  Meta (META) closes above $550 at the March 2026 close
D.  Meta (META) closes above $560 at the March 2026 close
E.  Meta (META) closes above $570 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_032 — Which of these Invesco QQQ Trust (QQQ) statements survive the March 31, 2026 close?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these Invesco QQQ Trust (QQQ) statements survive the March 31, 2026 close?
```

Options:
- `A`: Invesco QQQ Trust (QQQ) closes above $565 at the March 2026 close
- `B`: Invesco QQQ Trust (QQQ) closes above $570 at the March 2026 close
- `C`: Invesco QQQ Trust (QQQ) closes above $575 at the March 2026 close
- `D`: Invesco QQQ Trust (QQQ) closes above $580 at the March 2026 close
- `E`: Invesco QQQ Trust (QQQ) closes above $585 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these Invesco QQQ Trust (QQQ) statements survive the March 31, 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  Invesco QQQ Trust (QQQ) closes above $565 at the March 2026 close
B.  Invesco QQQ Trust (QQQ) closes above $570 at the March 2026 close
C.  Invesco QQQ Trust (QQQ) closes above $575 at the March 2026 close
D.  Invesco QQQ Trust (QQQ) closes above $580 at the March 2026 close
E.  Invesco QQQ Trust (QQQ) closes above $585 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_033 — Which of these close-above outcomes for iShares Semiconductor ETF (SOXX) will still be true on March 31, 2026?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these close-above outcomes for iShares Semiconductor ETF (SOXX) will still be true on March 31, 2026?
```

Options:
- `A`: iShares Semiconductor ETF (SOXX) closes above $320 at the March 2026 close
- `B`: iShares Semiconductor ETF (SOXX) closes above $325 at the March 2026 close
- `C`: iShares Semiconductor ETF (SOXX) closes above $330 at the March 2026 close
- `D`: iShares Semiconductor ETF (SOXX) closes above $335 at the March 2026 close
- `E`: iShares Semiconductor ETF (SOXX) closes above $340 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these close-above outcomes for iShares Semiconductor ETF (SOXX) will still be true on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  iShares Semiconductor ETF (SOXX) closes above $320 at the March 2026 close
B.  iShares Semiconductor ETF (SOXX) closes above $325 at the March 2026 close
C.  iShares Semiconductor ETF (SOXX) closes above $330 at the March 2026 close
D.  iShares Semiconductor ETF (SOXX) closes above $335 at the March 2026 close
E.  iShares Semiconductor ETF (SOXX) closes above $340 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_034 — Which of these statements about SPDR Gold Shares (GLD) at the March 2026 close end up being true?

- Source: `custom_live`
- Category: `month_end_thresholds`
- Pattern: `statement-truth set`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these statements about SPDR Gold Shares (GLD) at the March 2026 close end up being true?
```

Options:
- `A`: SPDR Gold Shares (GLD) closes above $390 at the March 2026 close
- `B`: SPDR Gold Shares (GLD) closes above $395 at the March 2026 close
- `C`: SPDR Gold Shares (GLD) closes above $400 at the March 2026 close
- `D`: SPDR Gold Shares (GLD) closes above $405 at the March 2026 close
- `E`: SPDR Gold Shares (GLD) closes above $410 at the March 2026 close

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these statements about SPDR Gold Shares (GLD) at the March 2026 close end up being true? (resolved around 2026-03-31 (GMT+8)). 
A.  SPDR Gold Shares (GLD) closes above $390 at the March 2026 close
B.  SPDR Gold Shares (GLD) closes above $395 at the March 2026 close
C.  SPDR Gold Shares (GLD) closes above $400 at the March 2026 close
D.  SPDR Gold Shares (GLD) closes above $405 at the March 2026 close
E.  SPDR Gold Shares (GLD) closes above $410 at the March 2026 close"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_035 — Which of these WTI crude oil futures (CL) levels will trade before market close on March 31, 2026?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these WTI crude oil futures (CL) levels will trade before market close on March 31, 2026?
```

Options:
- `A`: WTI crude oil futures (CL) hits $96 on the high side before March 31, 2026
- `B`: WTI crude oil futures (CL) hits $98 on the high side before March 31, 2026
- `C`: WTI crude oil futures (CL) hits $100 on the high side before March 31, 2026
- `D`: WTI crude oil futures (CL) hits $90 on the low side before March 31, 2026
- `E`: WTI crude oil futures (CL) hits $88 on the low side before March 31, 2026
- `F`: WTI crude oil futures (CL) hits $86 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these WTI crude oil futures (CL) levels will trade before market close on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  WTI crude oil futures (CL) hits $96 on the high side before March 31, 2026
B.  WTI crude oil futures (CL) hits $98 on the high side before March 31, 2026
C.  WTI crude oil futures (CL) hits $100 on the high side before March 31, 2026
D.  WTI crude oil futures (CL) hits $90 on the low side before March 31, 2026
E.  WTI crude oil futures (CL) hits $88 on the low side before March 31, 2026
F.  WTI crude oil futures (CL) hits $86 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_036 — Which of these price levels will Gold futures (GC) hit before March 31, 2026?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these price levels will Gold futures (GC) hit before March 31, 2026?
```

Options:
- `A`: Gold futures (GC) hits $4,500 on the high side before March 31, 2026
- `B`: Gold futures (GC) hits $4,550 on the high side before March 31, 2026
- `C`: Gold futures (GC) hits $4,600 on the high side before March 31, 2026
- `D`: Gold futures (GC) hits $4,350 on the low side before March 31, 2026
- `E`: Gold futures (GC) hits $4,300 on the low side before March 31, 2026
- `F`: Gold futures (GC) hits $4,250 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these price levels will Gold futures (GC) hit before March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Gold futures (GC) hits $4,500 on the high side before March 31, 2026
B.  Gold futures (GC) hits $4,550 on the high side before March 31, 2026
C.  Gold futures (GC) hits $4,600 on the high side before March 31, 2026
D.  Gold futures (GC) hits $4,350 on the low side before March 31, 2026
E.  Gold futures (GC) hits $4,300 on the low side before March 31, 2026
F.  Gold futures (GC) hits $4,250 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_037 — Before trading ends on March 31, 2026, which of these levels will Bitcoin (BTC-USD) trade at?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Before trading ends on March 31, 2026, which of these levels will Bitcoin (BTC-USD) trade at?
```

Options:
- `A`: Bitcoin (BTC-USD) hits $72,000 on the high side before March 31, 2026
- `B`: Bitcoin (BTC-USD) hits $74,000 on the high side before March 31, 2026
- `C`: Bitcoin (BTC-USD) hits $76,000 on the high side before March 31, 2026
- `D`: Bitcoin (BTC-USD) hits $66,000 on the low side before March 31, 2026
- `E`: Bitcoin (BTC-USD) hits $64,000 on the low side before March 31, 2026
- `F`: Bitcoin (BTC-USD) hits $62,000 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Before trading ends on March 31, 2026, which of these levels will Bitcoin (BTC-USD) trade at? (resolved around 2026-03-31 (GMT+8)). 
A.  Bitcoin (BTC-USD) hits $72,000 on the high side before March 31, 2026
B.  Bitcoin (BTC-USD) hits $74,000 on the high side before March 31, 2026
C.  Bitcoin (BTC-USD) hits $76,000 on the high side before March 31, 2026
D.  Bitcoin (BTC-USD) hits $66,000 on the low side before March 31, 2026
E.  Bitcoin (BTC-USD) hits $64,000 on the low side before March 31, 2026
F.  Bitcoin (BTC-USD) hits $62,000 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_038 — Which of these Ethereum (ETH-USD) levels get touched before the March 2026 close?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these Ethereum (ETH-USD) levels get touched before the March 2026 close?
```

Options:
- `A`: Ethereum (ETH-USD) hits $2,200 on the high side before March 31, 2026
- `B`: Ethereum (ETH-USD) hits $2,300 on the high side before March 31, 2026
- `C`: Ethereum (ETH-USD) hits $2,400 on the high side before March 31, 2026
- `D`: Ethereum (ETH-USD) hits $1,900 on the low side before March 31, 2026
- `E`: Ethereum (ETH-USD) hits $1,800 on the low side before March 31, 2026
- `F`: Ethereum (ETH-USD) hits $1,700 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these Ethereum (ETH-USD) levels get touched before the March 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  Ethereum (ETH-USD) hits $2,200 on the high side before March 31, 2026
B.  Ethereum (ETH-USD) hits $2,300 on the high side before March 31, 2026
C.  Ethereum (ETH-USD) hits $2,400 on the high side before March 31, 2026
D.  Ethereum (ETH-USD) hits $1,900 on the low side before March 31, 2026
E.  Ethereum (ETH-USD) hits $1,800 on the low side before March 31, 2026
F.  Ethereum (ETH-USD) hits $1,700 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_039 — Which of these price marks will NVIDIA (NVDA) reach before March 31, 2026?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these price marks will NVIDIA (NVDA) reach before March 31, 2026?
```

Options:
- `A`: NVIDIA (NVDA) hits $180 on the high side before March 31, 2026
- `B`: NVIDIA (NVDA) hits $185 on the high side before March 31, 2026
- `C`: NVIDIA (NVDA) hits $190 on the high side before March 31, 2026
- `D`: NVIDIA (NVDA) hits $165 on the low side before March 31, 2026
- `E`: NVIDIA (NVDA) hits $160 on the low side before March 31, 2026
- `F`: NVIDIA (NVDA) hits $155 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these price marks will NVIDIA (NVDA) reach before March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  NVIDIA (NVDA) hits $180 on the high side before March 31, 2026
B.  NVIDIA (NVDA) hits $185 on the high side before March 31, 2026
C.  NVIDIA (NVDA) hits $190 on the high side before March 31, 2026
D.  NVIDIA (NVDA) hits $165 on the low side before March 31, 2026
E.  NVIDIA (NVDA) hits $160 on the low side before March 31, 2026
F.  NVIDIA (NVDA) hits $155 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_040 — Which of these AMD (AMD) levels trade at any point before market close on March 31, 2026?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these AMD (AMD) levels trade at any point before market close on March 31, 2026?
```

Options:
- `A`: AMD (AMD) hits $210 on the high side before March 31, 2026
- `B`: AMD (AMD) hits $215 on the high side before March 31, 2026
- `C`: AMD (AMD) hits $220 on the high side before March 31, 2026
- `D`: AMD (AMD) hits $195 on the low side before March 31, 2026
- `E`: AMD (AMD) hits $190 on the low side before March 31, 2026
- `F`: AMD (AMD) hits $185 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these AMD (AMD) levels trade at any point before market close on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  AMD (AMD) hits $210 on the high side before March 31, 2026
B.  AMD (AMD) hits $215 on the high side before March 31, 2026
C.  AMD (AMD) hits $220 on the high side before March 31, 2026
D.  AMD (AMD) hits $195 on the low side before March 31, 2026
E.  AMD (AMD) hits $190 on the low side before March 31, 2026
F.  AMD (AMD) hits $185 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_041 — Which of these levels does Tesla (TSLA) print before the end of March 2026?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these levels does Tesla (TSLA) print before the end of March 2026?
```

Options:
- `A`: Tesla (TSLA) hits $390 on the high side before March 31, 2026
- `B`: Tesla (TSLA) hits $400 on the high side before March 31, 2026
- `C`: Tesla (TSLA) hits $410 on the high side before March 31, 2026
- `D`: Tesla (TSLA) hits $360 on the low side before March 31, 2026
- `E`: Tesla (TSLA) hits $350 on the low side before March 31, 2026
- `F`: Tesla (TSLA) hits $340 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these levels does Tesla (TSLA) print before the end of March 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Tesla (TSLA) hits $390 on the high side before March 31, 2026
B.  Tesla (TSLA) hits $400 on the high side before March 31, 2026
C.  Tesla (TSLA) hits $410 on the high side before March 31, 2026
D.  Tesla (TSLA) hits $360 on the low side before March 31, 2026
E.  Tesla (TSLA) hits $350 on the low side before March 31, 2026
F.  Tesla (TSLA) hits $340 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_042 — Which of these Invesco QQQ Trust (QQQ) prices are traded before March 31, 2026?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these Invesco QQQ Trust (QQQ) prices are traded before March 31, 2026?
```

Options:
- `A`: Invesco QQQ Trust (QQQ) hits $580 on the high side before March 31, 2026
- `B`: Invesco QQQ Trust (QQQ) hits $585 on the high side before March 31, 2026
- `C`: Invesco QQQ Trust (QQQ) hits $590 on the high side before March 31, 2026
- `D`: Invesco QQQ Trust (QQQ) hits $565 on the low side before March 31, 2026
- `E`: Invesco QQQ Trust (QQQ) hits $560 on the low side before March 31, 2026
- `F`: Invesco QQQ Trust (QQQ) hits $555 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these Invesco QQQ Trust (QQQ) prices are traded before March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Invesco QQQ Trust (QQQ) hits $580 on the high side before March 31, 2026
B.  Invesco QQQ Trust (QQQ) hits $585 on the high side before March 31, 2026
C.  Invesco QQQ Trust (QQQ) hits $590 on the high side before March 31, 2026
D.  Invesco QQQ Trust (QQQ) hits $565 on the low side before March 31, 2026
E.  Invesco QQQ Trust (QQQ) hits $560 on the low side before March 31, 2026
F.  Invesco QQQ Trust (QQQ) hits $555 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_043 — Which of these levels will SPDR S&P 500 ETF (SPY) see before the month closes on March 31, 2026?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these levels will SPDR S&P 500 ETF (SPY) see before the month closes on March 31, 2026?
```

Options:
- `A`: SPDR S&P 500 ETF (SPY) hits $655 on the high side before March 31, 2026
- `B`: SPDR S&P 500 ETF (SPY) hits $660 on the high side before March 31, 2026
- `C`: SPDR S&P 500 ETF (SPY) hits $665 on the high side before March 31, 2026
- `D`: SPDR S&P 500 ETF (SPY) hits $640 on the low side before March 31, 2026
- `E`: SPDR S&P 500 ETF (SPY) hits $635 on the low side before March 31, 2026
- `F`: SPDR S&P 500 ETF (SPY) hits $630 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these levels will SPDR S&P 500 ETF (SPY) see before the month closes on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  SPDR S&P 500 ETF (SPY) hits $655 on the high side before March 31, 2026
B.  SPDR S&P 500 ETF (SPY) hits $660 on the high side before March 31, 2026
C.  SPDR S&P 500 ETF (SPY) hits $665 on the high side before March 31, 2026
D.  SPDR S&P 500 ETF (SPY) hits $640 on the low side before March 31, 2026
E.  SPDR S&P 500 ETF (SPY) hits $635 on the low side before March 31, 2026
F.  SPDR S&P 500 ETF (SPY) hits $630 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_044 — Which of these iShares Semiconductor ETF (SOXX) levels are reached before the final March close?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these iShares Semiconductor ETF (SOXX) levels are reached before the final March close?
```

Options:
- `A`: iShares Semiconductor ETF (SOXX) hits $335 on the high side before March 31, 2026
- `B`: iShares Semiconductor ETF (SOXX) hits $340 on the high side before March 31, 2026
- `C`: iShares Semiconductor ETF (SOXX) hits $345 on the high side before March 31, 2026
- `D`: iShares Semiconductor ETF (SOXX) hits $320 on the low side before March 31, 2026
- `E`: iShares Semiconductor ETF (SOXX) hits $315 on the low side before March 31, 2026
- `F`: iShares Semiconductor ETF (SOXX) hits $310 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these iShares Semiconductor ETF (SOXX) levels are reached before the final March close? (resolved around 2026-03-31 (GMT+8)). 
A.  iShares Semiconductor ETF (SOXX) hits $335 on the high side before March 31, 2026
B.  iShares Semiconductor ETF (SOXX) hits $340 on the high side before March 31, 2026
C.  iShares Semiconductor ETF (SOXX) hits $345 on the high side before March 31, 2026
D.  iShares Semiconductor ETF (SOXX) hits $320 on the low side before March 31, 2026
E.  iShares Semiconductor ETF (SOXX) hits $315 on the low side before March 31, 2026
F.  iShares Semiconductor ETF (SOXX) hits $310 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_045 — Which of these prices does Coinbase (COIN) trade before March 31, 2026?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these prices does Coinbase (COIN) trade before March 31, 2026?
```

Options:
- `A`: Coinbase (COIN) hits $180 on the high side before March 31, 2026
- `B`: Coinbase (COIN) hits $185 on the high side before March 31, 2026
- `C`: Coinbase (COIN) hits $190 on the high side before March 31, 2026
- `D`: Coinbase (COIN) hits $165 on the low side before March 31, 2026
- `E`: Coinbase (COIN) hits $160 on the low side before March 31, 2026
- `F`: Coinbase (COIN) hits $155 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these prices does Coinbase (COIN) trade before March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Coinbase (COIN) hits $180 on the high side before March 31, 2026
B.  Coinbase (COIN) hits $185 on the high side before March 31, 2026
C.  Coinbase (COIN) hits $190 on the high side before March 31, 2026
D.  Coinbase (COIN) hits $165 on the low side before March 31, 2026
E.  Coinbase (COIN) hits $160 on the low side before March 31, 2026
F.  Coinbase (COIN) hits $155 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_046 — Which of these Strategy (MSTR) levels come into play before March 31, 2026?

- Source: `custom_live`
- Category: `hit_levels`
- Pattern: `threshold ladder`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these Strategy (MSTR) levels come into play before March 31, 2026?
```

Options:
- `A`: Strategy (MSTR) hits $160 on the high side before March 31, 2026
- `B`: Strategy (MSTR) hits $180 on the high side before March 31, 2026
- `C`: Strategy (MSTR) hits $200 on the high side before March 31, 2026
- `D`: Strategy (MSTR) hits $100 on the low side before March 31, 2026
- `E`: Strategy (MSTR) hits $80 on the low side before March 31, 2026
- `F`: Strategy (MSTR) hits $60 on the low side before March 31, 2026

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these Strategy (MSTR) levels come into play before March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  Strategy (MSTR) hits $160 on the high side before March 31, 2026
B.  Strategy (MSTR) hits $180 on the high side before March 31, 2026
C.  Strategy (MSTR) hits $200 on the high side before March 31, 2026
D.  Strategy (MSTR) hits $100 on the low side before March 31, 2026
E.  Strategy (MSTR) hits $80 on the low side before March 31, 2026
F.  Strategy (MSTR) hits $60 on the low side before March 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_047 — Will NVIDIA (NVDA) close above $180 on March 31, 2026?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will NVIDIA (NVDA) close above $180 on March 31, 2026?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will NVIDIA (NVDA) close above $180 on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_048 — Will AMD (AMD) finish above $215 at the March 31, 2026 close?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will AMD (AMD) finish above $215 at the March 31, 2026 close?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will AMD (AMD) finish above $215 at the March 31, 2026 close? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_049 — Will Broadcom (AVGO) end March 2026 with a close above $320?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Broadcom (AVGO) end March 2026 with a close above $320?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Broadcom (AVGO) end March 2026 with a close above $320? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_050 — Will Taiwan Semiconductor (TSM) close through $340 on the final trading day of March 2026?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Taiwan Semiconductor (TSM) close through $340 on the final trading day of March 2026?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Taiwan Semiconductor (TSM) close through $340 on the final trading day of March 2026? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_051 — Will the March 31, 2026 close for Tesla (TSLA) be above $400?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will the March 31, 2026 close for Tesla (TSLA) be above $400?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will the March 31, 2026 close for Tesla (TSLA) be above $400? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_052 — Will Apple (AAPL) finish the month above $260 on March 31, 2026?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Apple (AAPL) finish the month above $260 on March 31, 2026?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Apple (AAPL) finish the month above $260 on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_053 — Will Microsoft (MSFT) close higher than $375 on March 31, 2026?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Microsoft (MSFT) close higher than $375 on March 31, 2026?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Microsoft (MSFT) close higher than $375 on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_054 — Will Amazon (AMZN) end the March 2026 close above $215?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Amazon (AMZN) end the March 2026 close above $215?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Amazon (AMZN) end the March 2026 close above $215? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_055 — Will Meta (META) settle above $570 on the final trading day of March 2026?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Meta (META) settle above $570 on the final trading day of March 2026?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Meta (META) settle above $570 on the final trading day of March 2026? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_056 — Will Invesco QQQ Trust (QQQ) close above $590 by month-end on March 31, 2026?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Invesco QQQ Trust (QQQ) close above $590 by month-end on March 31, 2026?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Invesco QQQ Trust (QQQ) close above $590 by month-end on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_057 — Will SPDR S&P 500 ETF (SPY) end March 2026 above $655 at the close?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will SPDR S&P 500 ETF (SPY) end March 2026 above $655 at the close?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will SPDR S&P 500 ETF (SPY) end March 2026 above $655 at the close? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_058 — Will the final March close for iShares Russell 2000 ETF (IWM) clear $255?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will the final March close for iShares Russell 2000 ETF (IWM) clear $255?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will the final March close for iShares Russell 2000 ETF (IWM) clear $255? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_059 — Will Bitcoin (BTC-USD) close above $72,000 on the last trading day of March 2026?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Bitcoin (BTC-USD) close above $72,000 on the last trading day of March 2026?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Bitcoin (BTC-USD) close above $72,000 on the last trading day of March 2026? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_060 — Will Ethereum (ETH-USD) finish above $2,200 by the March 31, 2026 close?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Ethereum (ETH-USD) finish above $2,200 by the March 31, 2026 close?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Ethereum (ETH-USD) finish above $2,200 by the March 31, 2026 close? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_061 — Will Coinbase (COIN) close north of $185 on March 31, 2026?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Coinbase (COIN) close north of $185 on March 31, 2026?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Coinbase (COIN) close north of $185 on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_062 — Will Strategy (MSTR) end March above $160 at the closing bell?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Strategy (MSTR) end March above $160 at the closing bell?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Strategy (MSTR) end March above $160 at the closing bell? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_063 — Will Energy Select Sector SPDR Fund (XLE) close below $58 on March 31, 2026?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Energy Select Sector SPDR Fund (XLE) close below $58 on March 31, 2026?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Energy Select Sector SPDR Fund (XLE) close below $58 on March 31, 2026? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_064 — Will Financial Select Sector SPDR Fund (XLF) finish March 2026 with a close below $48?

- Source: `custom_live`
- Category: `binary_price_event`
- Pattern: `binary`
- End time: `2026-03-31`
- Answer format: `boxed_yes_no`

Question:
```text
Will Financial Select Sector SPDR Fund (XLF) finish March 2026 with a close below $48?
```

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Financial Select Sector SPDR Fund (XLF) finish March 2026 with a close below $48? (resolved around 2026-03-31 (GMT+8)). " IMPORTANT: Your final answer MUST end with this exact format: \boxed{Yes} or \boxed{No} Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_065 — Which of these semiconductor names posts the best return from the March 26, 2026 close through the March 31, 2026 close?

- Source: `custom_live`
- Category: `winner_market`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these semiconductor names posts the best return from the March 26, 2026 close through the March 31, 2026 close?
```

Options:
- `A`: NVIDIA (NVDA)
- `B`: AMD (AMD)
- `C`: Broadcom (AVGO)
- `D`: Taiwan Semiconductor (TSM)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these semiconductor names posts the best return from the March 26, 2026 close through the March 31, 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  NVIDIA (NVDA)
B.  AMD (AMD)
C.  Broadcom (AVGO)
D.  Taiwan Semiconductor (TSM)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_066 — From the March 26, 2026 close to the March 31, 2026 close, which of these megacap tech names performs best?

- Source: `custom_live`
- Category: `winner_market`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
From the March 26, 2026 close to the March 31, 2026 close, which of these megacap tech names performs best?
```

Options:
- `A`: Apple (AAPL)
- `B`: Microsoft (MSFT)
- `C`: Amazon (AMZN)
- `D`: Meta (META)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "From the March 26, 2026 close to the March 31, 2026 close, which of these megacap tech names performs best? (resolved around 2026-03-31 (GMT+8)). 
A.  Apple (AAPL)
B.  Microsoft (MSFT)
C.  Amazon (AMZN)
D.  Meta (META)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_067 — Which name in this market beta ETFs group has the strongest return from March 26, 2026 through March 31, 2026?

- Source: `custom_live`
- Category: `winner_market`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which name in this market beta ETFs group has the strongest return from March 26, 2026 through March 31, 2026?
```

Options:
- `A`: SPDR S&P 500 ETF (SPY)
- `B`: Invesco QQQ Trust (QQQ)
- `C`: iShares Russell 2000 ETF (IWM)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which name in this market beta ETFs group has the strongest return from March 26, 2026 through March 31, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  SPDR S&P 500 ETF (SPY)
B.  Invesco QQQ Trust (QQQ)
C.  iShares Russell 2000 ETF (IWM)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_068 — Across these crypto assets and proxies, which delivers the best performance from the March 27, 2026 close to the March 31, 2026 close?

- Source: `custom_live`
- Category: `winner_market`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Across these crypto assets and proxies, which delivers the best performance from the March 27, 2026 close to the March 31, 2026 close?
```

Options:
- `A`: Bitcoin (BTC-USD)
- `B`: Ethereum (ETH-USD)
- `C`: Coinbase (COIN)
- `D`: Strategy (MSTR)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Across these crypto assets and proxies, which delivers the best performance from the March 27, 2026 close to the March 31, 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  Bitcoin (BTC-USD)
B.  Ethereum (ETH-USD)
C.  Coinbase (COIN)
D.  Strategy (MSTR)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_069 — Which of these energy names gains the most between the March 27, 2026 close and the March 31, 2026 close?

- Source: `custom_live`
- Category: `winner_market`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these energy names gains the most between the March 27, 2026 close and the March 31, 2026 close?
```

Options:
- `A`: WTI crude oil futures (CL)
- `B`: Energy Select Sector SPDR Fund (XLE)
- `C`: Exxon Mobil (XOM)
- `D`: Chevron (CVX)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these energy names gains the most between the March 27, 2026 close and the March 31, 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  WTI crude oil futures (CL)
B.  Energy Select Sector SPDR Fund (XLE)
C.  Exxon Mobil (XOM)
D.  Chevron (CVX)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_070 — From March 26, 2026 through the close on March 31, 2026, which of these financial names leads on return?

- Source: `custom_live`
- Category: `winner_market`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
From March 26, 2026 through the close on March 31, 2026, which of these financial names leads on return?
```

Options:
- `A`: Financial Select Sector SPDR Fund (XLF)
- `B`: JPMorgan Chase (JPM)
- `C`: Goldman Sachs (GS)
- `D`: Bank of America (BAC)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "From March 26, 2026 through the close on March 31, 2026, which of these financial names leads on return? (resolved around 2026-03-31 (GMT+8)). 
A.  Financial Select Sector SPDR Fund (XLF)
B.  JPMorgan Chase (JPM)
C.  Goldman Sachs (GS)
D.  Bank of America (BAC)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_071 — Which of these precious-metals names finishes with the best return from the March 27, 2026 close through month-end?

- Source: `custom_live`
- Category: `winner_market`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these precious-metals names finishes with the best return from the March 27, 2026 close through month-end?
```

Options:
- `A`: Gold futures (GC)
- `B`: SPDR Gold Shares (GLD)
- `C`: iShares Silver Trust (SLV)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these precious-metals names finishes with the best return from the March 27, 2026 close through month-end? (resolved around 2026-03-31 (GMT+8)). 
A.  Gold futures (GC)
B.  SPDR Gold Shares (GLD)
C.  iShares Silver Trust (SLV)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_072 — Over the stretch from the March 26, 2026 close to the March 31, 2026 close, which of these AI platform names outperforms?

- Source: `custom_live`
- Category: `winner_market`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Over the stretch from the March 26, 2026 close to the March 31, 2026 close, which of these AI platform names outperforms?
```

Options:
- `A`: NVIDIA (NVDA)
- `B`: Microsoft (MSFT)
- `C`: Meta (META)
- `D`: Amazon (AMZN)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Over the stretch from the March 26, 2026 close to the March 31, 2026 close, which of these AI platform names outperforms? (resolved around 2026-03-31 (GMT+8)). 
A.  NVIDIA (NVDA)
B.  Microsoft (MSFT)
C.  Meta (META)
D.  Amazon (AMZN)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_073 — Which of these high-beta growth names posts the top return between the March 26, 2026 close and the March 2026 close?

- Source: `custom_live`
- Category: `winner_market`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these high-beta growth names posts the top return between the March 26, 2026 close and the March 2026 close?
```

Options:
- `A`: Tesla (TSLA)
- `B`: Coinbase (COIN)
- `C`: Strategy (MSTR)
- `D`: iShares Semiconductor ETF (SOXX)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these high-beta growth names posts the top return between the March 26, 2026 close and the March 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  Tesla (TSLA)
B.  Coinbase (COIN)
C.  Strategy (MSTR)
D.  iShares Semiconductor ETF (SOXX)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_074 — Which of these semiconductor names close March 31, 2026 above their March 26, 2026 close?

- Source: `custom_live`
- Category: `up_membership`
- Pattern: `roster membership`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these semiconductor names close March 31, 2026 above their March 26, 2026 close?
```

Options:
- `A`: NVIDIA (NVDA)
- `B`: AMD (AMD)
- `C`: Broadcom (AVGO)
- `D`: Taiwan Semiconductor (TSM)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these semiconductor names close March 31, 2026 above their March 26, 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  NVIDIA (NVDA)
B.  AMD (AMD)
C.  Broadcom (AVGO)
D.  Taiwan Semiconductor (TSM)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_075 — Which of these megacap tech names finish the March 31, 2026 close above their March 26, 2026 level?

- Source: `custom_live`
- Category: `up_membership`
- Pattern: `roster membership`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these megacap tech names finish the March 31, 2026 close above their March 26, 2026 level?
```

Options:
- `A`: Apple (AAPL)
- `B`: Microsoft (MSFT)
- `C`: Amazon (AMZN)
- `D`: Meta (META)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these megacap tech names finish the March 31, 2026 close above their March 26, 2026 level? (resolved around 2026-03-31 (GMT+8)). 
A.  Apple (AAPL)
B.  Microsoft (MSFT)
C.  Amazon (AMZN)
D.  Meta (META)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_076 — By the close on March 31, 2026, which of these market beta ETFs are above their March 26, 2026 close?

- Source: `custom_live`
- Category: `up_membership`
- Pattern: `roster membership`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
By the close on March 31, 2026, which of these market beta ETFs are above their March 26, 2026 close?
```

Options:
- `A`: SPDR S&P 500 ETF (SPY)
- `B`: Invesco QQQ Trust (QQQ)
- `C`: iShares Russell 2000 ETF (IWM)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "By the close on March 31, 2026, which of these market beta ETFs are above their March 26, 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  SPDR S&P 500 ETF (SPY)
B.  Invesco QQQ Trust (QQQ)
C.  iShares Russell 2000 ETF (IWM)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_077 — Which of these crypto assets and proxies end March 2026 above their March 27, 2026 close?

- Source: `custom_live`
- Category: `up_membership`
- Pattern: `roster membership`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these crypto assets and proxies end March 2026 above their March 27, 2026 close?
```

Options:
- `A`: Bitcoin (BTC-USD)
- `B`: Ethereum (ETH-USD)
- `C`: Coinbase (COIN)
- `D`: Strategy (MSTR)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these crypto assets and proxies end March 2026 above their March 27, 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  Bitcoin (BTC-USD)
B.  Ethereum (ETH-USD)
C.  Coinbase (COIN)
D.  Strategy (MSTR)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_078 — Which names in this energy names group close higher on March 31, 2026 than they did on March 27, 2026?

- Source: `custom_live`
- Category: `up_membership`
- Pattern: `roster membership`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which names in this energy names group close higher on March 31, 2026 than they did on March 27, 2026?
```

Options:
- `A`: WTI crude oil futures (CL)
- `B`: Energy Select Sector SPDR Fund (XLE)
- `C`: Exxon Mobil (XOM)
- `D`: Chevron (CVX)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which names in this energy names group close higher on March 31, 2026 than they did on March 27, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  WTI crude oil futures (CL)
B.  Energy Select Sector SPDR Fund (XLE)
C.  Exxon Mobil (XOM)
D.  Chevron (CVX)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_079 — Which of these financial names finish above their March 26, 2026 close by month-end?

- Source: `custom_live`
- Category: `up_membership`
- Pattern: `roster membership`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these financial names finish above their March 26, 2026 close by month-end?
```

Options:
- `A`: Financial Select Sector SPDR Fund (XLF)
- `B`: JPMorgan Chase (JPM)
- `C`: Goldman Sachs (GS)
- `D`: Bank of America (BAC)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these financial names finish above their March 26, 2026 close by month-end? (resolved around 2026-03-31 (GMT+8)). 
A.  Financial Select Sector SPDR Fund (XLF)
B.  JPMorgan Chase (JPM)
C.  Goldman Sachs (GS)
D.  Bank of America (BAC)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_080 — At the March 31, 2026 close, which of these precious-metals names are still above their March 27, 2026 close?

- Source: `custom_live`
- Category: `up_membership`
- Pattern: `roster membership`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
At the March 31, 2026 close, which of these precious-metals names are still above their March 27, 2026 close?
```

Options:
- `A`: Gold futures (GC)
- `B`: SPDR Gold Shares (GLD)
- `C`: iShares Silver Trust (SLV)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "At the March 31, 2026 close, which of these precious-metals names are still above their March 27, 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  Gold futures (GC)
B.  SPDR Gold Shares (GLD)
C.  iShares Silver Trust (SLV)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_081 — Which of these AI platform names close March 2026 above where they closed on March 26, 2026?

- Source: `custom_live`
- Category: `up_membership`
- Pattern: `roster membership`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these AI platform names close March 2026 above where they closed on March 26, 2026?
```

Options:
- `A`: NVIDIA (NVDA)
- `B`: Microsoft (MSFT)
- `C`: Meta (META)
- `D`: Amazon (AMZN)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these AI platform names close March 2026 above where they closed on March 26, 2026? (resolved around 2026-03-31 (GMT+8)). 
A.  NVIDIA (NVDA)
B.  Microsoft (MSFT)
C.  Meta (META)
D.  Amazon (AMZN)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_082 — Which of these high-beta growth names end the month above their March 26, 2026 close?

- Source: `custom_live`
- Category: `up_membership`
- Pattern: `roster membership`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which of these high-beta growth names end the month above their March 26, 2026 close?
```

Options:
- `A`: Tesla (TSLA)
- `B`: Coinbase (COIN)
- `C`: Strategy (MSTR)
- `D`: iShares Semiconductor ETF (SOXX)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which of these high-beta growth names end the month above their March 26, 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  Tesla (TSLA)
B.  Coinbase (COIN)
C.  Strategy (MSTR)
D.  iShares Semiconductor ETF (SOXX)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_083 — Which performs better from the March 27, 2026 close through the March 31, 2026 close: Bitcoin (BTC-USD) or Ethereum (ETH-USD)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which performs better from the March 27, 2026 close through the March 31, 2026 close: Bitcoin (BTC-USD) or Ethereum (ETH-USD)?
```

Options:
- `A`: Bitcoin (BTC-USD)
- `B`: Ethereum (ETH-USD)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which performs better from the March 27, 2026 close through the March 31, 2026 close: Bitcoin (BTC-USD) or Ethereum (ETH-USD)? (resolved around 2026-03-31 (GMT+8)). 
A.  Bitcoin (BTC-USD)
B.  Ethereum (ETH-USD)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_084 — From the March 26, 2026 close to the March 31, 2026 close, which has the stronger return: NVIDIA (NVDA) or AMD (AMD)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
From the March 26, 2026 close to the March 31, 2026 close, which has the stronger return: NVIDIA (NVDA) or AMD (AMD)?
```

Options:
- `A`: NVIDIA (NVDA)
- `B`: AMD (AMD)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "From the March 26, 2026 close to the March 31, 2026 close, which has the stronger return: NVIDIA (NVDA) or AMD (AMD)? (resolved around 2026-03-31 (GMT+8)). 
A.  NVIDIA (NVDA)
B.  AMD (AMD)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_085 — Which outperforms between March 26, 2026 and the close on March 31, 2026: Apple (AAPL) or Microsoft (MSFT)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which outperforms between March 26, 2026 and the close on March 31, 2026: Apple (AAPL) or Microsoft (MSFT)?
```

Options:
- `A`: Apple (AAPL)
- `B`: Microsoft (MSFT)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which outperforms between March 26, 2026 and the close on March 31, 2026: Apple (AAPL) or Microsoft (MSFT)? (resolved around 2026-03-31 (GMT+8)). 
A.  Apple (AAPL)
B.  Microsoft (MSFT)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_086 — Which posts the better return from the March 26, 2026 close through month-end: Amazon (AMZN) or Meta (META)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which posts the better return from the March 26, 2026 close through month-end: Amazon (AMZN) or Meta (META)?
```

Options:
- `A`: Amazon (AMZN)
- `B`: Meta (META)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which posts the better return from the March 26, 2026 close through month-end: Amazon (AMZN) or Meta (META)? (resolved around 2026-03-31 (GMT+8)). 
A.  Amazon (AMZN)
B.  Meta (META)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_087 — Between SPDR S&P 500 ETF (SPY) and Invesco QQQ Trust (QQQ), which does better from the March 26, 2026 close to the March 31, 2026 close?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Between SPDR S&P 500 ETF (SPY) and Invesco QQQ Trust (QQQ), which does better from the March 26, 2026 close to the March 31, 2026 close?
```

Options:
- `A`: SPDR S&P 500 ETF (SPY)
- `B`: Invesco QQQ Trust (QQQ)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Between SPDR S&P 500 ETF (SPY) and Invesco QQQ Trust (QQQ), which does better from the March 26, 2026 close to the March 31, 2026 close? (resolved around 2026-03-31 (GMT+8)). 
A.  SPDR S&P 500 ETF (SPY)
B.  Invesco QQQ Trust (QQQ)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_088 — Which has the higher return over the stretch from March 26, 2026 to March 31, 2026: Energy Select Sector SPDR Fund (XLE) or Financial Select Sector SPDR Fund (XLF)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which has the higher return over the stretch from March 26, 2026 to March 31, 2026: Energy Select Sector SPDR Fund (XLE) or Financial Select Sector SPDR Fund (XLF)?
```

Options:
- `A`: Energy Select Sector SPDR Fund (XLE)
- `B`: Financial Select Sector SPDR Fund (XLF)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which has the higher return over the stretch from March 26, 2026 to March 31, 2026: Energy Select Sector SPDR Fund (XLE) or Financial Select Sector SPDR Fund (XLF)? (resolved around 2026-03-31 (GMT+8)). 
A.  Energy Select Sector SPDR Fund (XLE)
B.  Financial Select Sector SPDR Fund (XLF)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_089 — From the March 27, 2026 close through the final March close, which performs better: Gold futures (GC) or WTI crude oil futures (CL)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
From the March 27, 2026 close through the final March close, which performs better: Gold futures (GC) or WTI crude oil futures (CL)?
```

Options:
- `A`: Gold futures (GC)
- `B`: WTI crude oil futures (CL)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "From the March 27, 2026 close through the final March close, which performs better: Gold futures (GC) or WTI crude oil futures (CL)? (resolved around 2026-03-31 (GMT+8)). 
A.  Gold futures (GC)
B.  WTI crude oil futures (CL)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_090 — Which wins on return between the March 26, 2026 close and the March 31, 2026 close: Coinbase (COIN) or Strategy (MSTR)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which wins on return between the March 26, 2026 close and the March 31, 2026 close: Coinbase (COIN) or Strategy (MSTR)?
```

Options:
- `A`: Coinbase (COIN)
- `B`: Strategy (MSTR)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which wins on return between the March 26, 2026 close and the March 31, 2026 close: Coinbase (COIN) or Strategy (MSTR)? (resolved around 2026-03-31 (GMT+8)). 
A.  Coinbase (COIN)
B.  Strategy (MSTR)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_091 — Which finishes stronger from the March 26, 2026 close through March 31, 2026: SPDR Gold Shares (GLD) or iShares Silver Trust (SLV)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which finishes stronger from the March 26, 2026 close through March 31, 2026: SPDR Gold Shares (GLD) or iShares Silver Trust (SLV)?
```

Options:
- `A`: SPDR Gold Shares (GLD)
- `B`: iShares Silver Trust (SLV)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which finishes stronger from the March 26, 2026 close through March 31, 2026: SPDR Gold Shares (GLD) or iShares Silver Trust (SLV)? (resolved around 2026-03-31 (GMT+8)). 
A.  SPDR Gold Shares (GLD)
B.  iShares Silver Trust (SLV)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_092 — Which has the better move from March 26, 2026 to the March 2026 close: iShares Semiconductor ETF (SOXX) or Invesco QQQ Trust (QQQ)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which has the better move from March 26, 2026 to the March 2026 close: iShares Semiconductor ETF (SOXX) or Invesco QQQ Trust (QQQ)?
```

Options:
- `A`: iShares Semiconductor ETF (SOXX)
- `B`: Invesco QQQ Trust (QQQ)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which has the better move from March 26, 2026 to the March 2026 close: iShares Semiconductor ETF (SOXX) or Invesco QQQ Trust (QQQ)? (resolved around 2026-03-31 (GMT+8)). 
A.  iShares Semiconductor ETF (SOXX)
B.  Invesco QQQ Trust (QQQ)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_093 — Between the March 26, 2026 close and the March 31, 2026 close, which outperforms: Tesla (TSLA) or NVIDIA (NVDA)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Between the March 26, 2026 close and the March 31, 2026 close, which outperforms: Tesla (TSLA) or NVIDIA (NVDA)?
```

Options:
- `A`: Tesla (TSLA)
- `B`: NVIDIA (NVDA)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Between the March 26, 2026 close and the March 31, 2026 close, which outperforms: Tesla (TSLA) or NVIDIA (NVDA)? (resolved around 2026-03-31 (GMT+8)). 
A.  Tesla (TSLA)
B.  NVIDIA (NVDA)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_094 — Which posts the stronger return into month-end: JPMorgan Chase (JPM) or Goldman Sachs (GS)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which posts the stronger return into month-end: JPMorgan Chase (JPM) or Goldman Sachs (GS)?
```

Options:
- `A`: JPMorgan Chase (JPM)
- `B`: Goldman Sachs (GS)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which posts the stronger return into month-end: JPMorgan Chase (JPM) or Goldman Sachs (GS)? (resolved around 2026-03-31 (GMT+8)). 
A.  JPMorgan Chase (JPM)
B.  Goldman Sachs (GS)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_095 — Which ends the period from March 26, 2026 through March 31, 2026 with the better return: Exxon Mobil (XOM) or Chevron (CVX)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which ends the period from March 26, 2026 through March 31, 2026 with the better return: Exxon Mobil (XOM) or Chevron (CVX)?
```

Options:
- `A`: Exxon Mobil (XOM)
- `B`: Chevron (CVX)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which ends the period from March 26, 2026 through March 31, 2026 with the better return: Exxon Mobil (XOM) or Chevron (CVX)? (resolved around 2026-03-31 (GMT+8)). 
A.  Exxon Mobil (XOM)
B.  Chevron (CVX)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_096 — Which does better from the March 26, 2026 close to the close on March 31, 2026: Apple (AAPL) or Amazon (AMZN)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which does better from the March 26, 2026 close to the close on March 31, 2026: Apple (AAPL) or Amazon (AMZN)?
```

Options:
- `A`: Apple (AAPL)
- `B`: Amazon (AMZN)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which does better from the March 26, 2026 close to the close on March 31, 2026: Apple (AAPL) or Amazon (AMZN)? (resolved around 2026-03-31 (GMT+8)). 
A.  Apple (AAPL)
B.  Amazon (AMZN)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_097 — From March 26, 2026 through the March 2026 close, which leads on return: Meta (META) or Alphabet (GOOGL)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
From March 26, 2026 through the March 2026 close, which leads on return: Meta (META) or Alphabet (GOOGL)?
```

Options:
- `A`: Meta (META)
- `B`: Alphabet (GOOGL)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "From March 26, 2026 through the March 2026 close, which leads on return: Meta (META) or Alphabet (GOOGL)? (resolved around 2026-03-31 (GMT+8)). 
A.  Meta (META)
B.  Alphabet (GOOGL)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_098 — Which has the edge from the March 26, 2026 close through the March 31, 2026 close: Broadcom (AVGO) or Taiwan Semiconductor (TSM)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which has the edge from the March 26, 2026 close through the March 31, 2026 close: Broadcom (AVGO) or Taiwan Semiconductor (TSM)?
```

Options:
- `A`: Broadcom (AVGO)
- `B`: Taiwan Semiconductor (TSM)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which has the edge from the March 26, 2026 close through the March 31, 2026 close: Broadcom (AVGO) or Taiwan Semiconductor (TSM)? (resolved around 2026-03-31 (GMT+8)). 
A.  Broadcom (AVGO)
B.  Taiwan Semiconductor (TSM)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_099 — Which outperforms over the run from March 26, 2026 to March 31, 2026: iShares Russell 2000 ETF (IWM) or SPDR S&P 500 ETF (SPY)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which outperforms over the run from March 26, 2026 to March 31, 2026: iShares Russell 2000 ETF (IWM) or SPDR S&P 500 ETF (SPY)?
```

Options:
- `A`: iShares Russell 2000 ETF (IWM)
- `B`: SPDR S&P 500 ETF (SPY)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which outperforms over the run from March 26, 2026 to March 31, 2026: iShares Russell 2000 ETF (IWM) or SPDR S&P 500 ETF (SPY)? (resolved around 2026-03-31 (GMT+8)). 
A.  iShares Russell 2000 ETF (IWM)
B.  SPDR S&P 500 ETF (SPY)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

## v13_100 — Which closes out the period with the better return, Bitcoin (BTC-USD) or Coinbase (COIN)?

- Source: `custom_live`
- Category: `head_to_head`
- Pattern: `winner market`
- End time: `2026-03-31`
- Answer format: `boxed_letters`

Question:
```text
Which closes out the period with the better return, Bitcoin (BTC-USD) or Coinbase (COIN)?
```

Options:
- `A`: Bitcoin (BTC-USD)
- `B`: Coinbase (COIN)

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which closes out the period with the better return, Bitcoin (BTC-USD) or Coinbase (COIN)? (resolved around 2026-03-31 (GMT+8)). 
A.  Bitcoin (BTC-USD)
B.  Coinbase (COIN)"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options.

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth: ``

