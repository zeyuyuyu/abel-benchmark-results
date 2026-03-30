# v14 Track G Historical As-Of Cases

This markdown materializes the canonical Track G historical as-of pack.
Search is allowed, but it must not use sources later than each case's
`search_cutoff`.

- Source mirror: `v13/resolved_asof_questions.json`
- Case count: `15`

## v13ra_001 — Bank of Brazil decision in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `central_bank_decision`
- Search cutoff: `2026-01-27`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-27`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Bank of Brazil decision in January? (resolved around 2026-01-27 (GMT+8)). 
A.  the outcome be No change in the Selic rate after Bank of Brazil's January 2026 meeting?
B.  the Bank of Brazil raise the Selic rate after January 2026 meeting
C.  the Bank of Brazil lower the Selic rate after January 2026 meeting"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A}",
  "answer_tokens": [
    "A"
  ]
}
```

## v13ra_002 — At close of business on 23 January 2026, will the most recently announced Bank of Japan (BOJ) "uncollateralized overnight call [interest] rate" be lower, the same, or higher than it was at close of business on 19 December 2025?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `central_bank_decision`
- Search cutoff: `2026-01-23`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-01-24`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "At close of business on 23 January 2026, will the most recently announced Bank of Japan (BOJ) "uncollateralized overnight call [interest] rate" be lower, the same, or higher than it was at close of business on 19 December 2025? (resolved around 2026-01-24 (GMT+8)). 
A.  the outcome be Lower
B.  the outcome be Same
C.  the outcome be Higher"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{B}",
  "answer_tokens": [
    "B"
  ]
}
```

## v13ra_003 — Reserve Bank of Australia Decision in February

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `central_bank_decision`
- Search cutoff: `2026-02-03`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-03 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Reserve Bank of Australia Decision in February (resolved around 2026-02-03 (GMT+8)). 
A. the Reserve Bank of Australia decrease the target for the cash rate after the February Meeting
B. the Reserve Bank of Australia increase the target for the cash rate after the February Meeting
C. the Reserve Bank of Australia make no change to the target for the cash rate after the February Meeting"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{B}",
  "answer_tokens": [
    "B"
  ]
}
```

## v13ra_004 — At close of business on 5 February 2026, will the most recently announced European Central Bank (ECB) "Deposit facility" interest rate be lower, the same, or higher than it was at close of business on 18 December 2025?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `central_bank_decision`
- Search cutoff: `2026-02-05`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-02-06`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "At close of business on 5 February 2026, will the most recently announced European Central Bank (ECB) "Deposit facility" interest rate be lower, the same, or higher than it was at close of business on 18 December 2025? (resolved around 2026-02-06 (GMT+8)). 
A.  the outcome be Lower
B.  the outcome be Same
C.  the outcome be Higher"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{B}",
  "answer_tokens": [
    "B"
  ]
}
```

## v13ra_005 — Gold (GC) above ___ end of January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `commodity_thresholds`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Gold (GC) above ___ end of January? (resolved around 2026-02-01 (GMT+8)). 
A. Gold (GC) settle over $7,000 on the final trading day of January 2026
B. Gold (GC) settle over $6,500 on the final trading day of January 2026
C. Gold (GC) settle over $6,000 on the final trading day of January 2026
D. Gold (GC) settle over $5,500 on the final trading day of January 2026
E. Gold (GC) settle over $5,200 on the final trading day of January 2026
F. Gold (GC) settle over $5,000 on the final trading day of January 2026
G. Gold (GC) settle over $4,800 on the final trading day of January 2026
H. Gold (GC) settle over $4,600 on the final trading day of January 2026
I. Gold (GC) settle over $4,400 on the final trading day of January 2026
J. Gold (GC) settle over $4,200 on the final trading day of January 2026
K. Gold (GC) settle over $4,000 on the final trading day of January 2026
L. Gold (GC) settle over $3,600 on the final trading day of January 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{H, I, J, K, L}",
  "answer_tokens": [
    "H",
    "I",
    "J",
    "K",
    "L"
  ]
}
```

## v13ra_006 — What will Gold (GC) settle at in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `commodity_bucket`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will Gold (GC) settle at in January? (resolved around 2026-02-01 (GMT+8)). 
A. Gold (GC) settle at <$4,350 in January
B. Gold (GC) settle at $4,350-$4,475 in January
C. Gold (GC) settle at $4,475-$4,600 in January
D. Gold (GC) settle at $4,600-$4,725 in January
E. Gold (GC) settle at $4,725-$4,850 in January
F. Gold (GC) settle at $4,850-$4,975 in January
G. Gold (GC) settle at $4,975-$5,100 in January
H. Gold (GC) settle at >$5,100 in January"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{E}",
  "answer_tokens": [
    "E"
  ]
}
```

## v13ra_007 — What will Crude Oil (CL) hit__ by end of January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `commodity_hit_levels`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will Crude Oil (CL) hit__ by end of January? (resolved around 2026-02-01 (GMT+8)). 
A. Crude Oil (CL) hit (HIGH) $75 by end of January
B. Crude Oil (CL) hit (HIGH) $65 by end of January
C. Crude Oil (CL) hit (HIGH) $58 by end of January
D. Crude Oil (CL) hit (LOW) $47 by end of January
E. Crude Oil (CL) hit (LOW) $35 by end of January
F. Crude Oil (CL) hit (HIGH) $70 by end of January
G. Crude Oil (CL) hit (HIGH) $62 by end of January
H. Crude Oil (CL) hit (LOW) $52 by end of January
I. Crude Oil (CL) hit (LOW) $42 by end of January
J. Crude Oil (CL) hit (HIGH) $60 by end of January
K. Crude Oil (CL) hit (LOW) $50 by end of January
L. Crude Oil (CL) hit (LOW) $55 by end of January"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{B, C, G, J}",
  "answer_tokens": [
    "B",
    "C",
    "G",
    "J"
  ]
}
```

## v13ra_008 — What will Crude Oil (CL) settle at in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `commodity_bucket`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will Crude Oil (CL) settle at in January? (resolved around 2026-02-01 (GMT+8)). 
A. Crude Oil (CL) settle at <$45 in January
B. Crude Oil (CL) settle at $45-$50 in January
C. Crude Oil (CL) settle at $60-$65 in January
D. Crude Oil (CL) settle at $70-$75 in January
E. Crude Oil (CL) settle at $50-$55 in January
F. Crude Oil (CL) settle at $65-$70 in January
G. Crude Oil (CL) settle at $55-$60 in January
H. Crude Oil (CL) settle at >$75 in January"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{F}",
  "answer_tokens": [
    "F"
  ]
}
```

## v13ra_009 — Tesla hits $400 or $500 first before end of January 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `first_hit`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Tesla hits $400 or $500 first before end of January 2026? (resolved around 2026-02-01 (GMT+8)). 
A. the outcome be Tesla hits or trades below $400.00 first
B. the outcome be Tesla hits or trades above $500.00 first
C. the outcome be Tesla hits neither $400 nor $500 before market close on Jan 30"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A}",
  "answer_tokens": [
    "A"
  ]
}
```

## v13ra_010 — Nvidia hits 170, 200 or neither first by end of January 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `first_hit`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Nvidia hits 170, 200 or neither first by end of January 2026? (resolved around 2026-02-01 (GMT+8)). 
A. the outcome be Hits or goes below $170.00 first
B. the outcome be Hits or goes above $200.00 first
C. the outcome be Hits neither before end of trading January 30"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A}",
  "answer_tokens": [
    "A"
  ]
}
```

## v13ra_011 — Will Bitcoin close above USD $100,000 on 31 January 2026 (UTC)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `crypto_binary`
- Search cutoff: `2026-01-31`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-02-02 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Bitcoin close above USD $100,000 on 31 January 2026 (UTC)? (resolved around 2026-02-02 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Yes} or \boxed{No}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{No}",
  "answer_tokens": [
    "No"
  ]
}
```

## v13ra_012 — Bitcoin below $82K in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `crypto_binary`
- Search cutoff: `2026-02-02`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-02 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Bitcoin below $82K in January? (resolved around 2026-02-02 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Yes} or \boxed{No}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Yes}",
  "answer_tokens": [
    "Yes"
  ]
}
```

## v13ra_013 — Between 10 October 2025 and 6 March 2026, what will be the lowest closing price of soybeans?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `agriculture_bucket`
- Search cutoff: `2026-03-06`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-03-07`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Between 10 October 2025 and 6 March 2026, what will be the lowest closing price of soybeans? (resolved around 2026-03-07 (GMT+8)). 
A.  the outcome be Less than $8.00/bushel
B.  the outcome be At least $8.00/bushel, but less than $8.50/bushel
C.  the outcome be At least $8.50/bushel, but less than $9.00/bushel
D.  the outcome be At least $9.00/bushel, but less than $9.50/bushel
E.  the outcome be $9.50/bushel or more"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{E}",
  "answer_tokens": [
    "E"
  ]
}
```

## v13ra_014 — Will global platinum availability fall below 2 million ounces by March 4, 2026, due to South African mine supply issues?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `supply_shock_binary`
- Search cutoff: `2026-03-04`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-03-05`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will global platinum availability fall below 2 million ounces by March 4, 2026, due to South African mine supply issues? (resolved around 2026-03-05 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{No}",
  "answer_tokens": [
    "No"
  ]
}
```

## v13ra_015 — Will NVIDIA stock be higher on March 16, 2026 than on March 09, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Category: `single_stock_direction`
- Search cutoff: `2026-03-16`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-03-17`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will NVIDIA stock be higher on March 16, 2026 than on March 09, 2026? (resolved around 2026-03-17 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Usage policy:
```json
{
  "search_allowed": true,
  "as_of_cutoff_enforced": true,
  "rule": "Do not use or rely on sources published after search_cutoff."
}
```

Ground truth:
```json
{
  "answer_box": "\\boxed{No}",
  "answer_tokens": [
    "No"
  ]
}
```

