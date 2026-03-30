# v14 Track G Historical As-Of Cases

This markdown materializes the full FutureX-Past pack under the Track G
`historical_asof_search_cutoff` regime.

- Source dataset: `futurex-ai/Futurex-Past`
- Case count: `244`
- Legacy finance-tagged cases: `15`
- Search is allowed, but evidence must not use sources after each case's `search_cutoff`.

## v14ga_0001 — Right approach to @bens puzzle (#2) / Collaboration space

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694bdd0b43684c005d3473f1`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Right approach to @bens puzzle (#2) / Collaboration space (resolved around 2026-01-18 (GMT+8)). 
A. the outcome be Order in which hints are revealed matters
B. the outcome be Hints should be broken into chunks of size 5 words
C. the outcome be Binary
D. the outcome be The second letter of the first step is K
E. the outcome be Optical (as in round 1)
F. the outcome be Wait for more hints (at least 150). Will not be an answer if less than 150 hints
G. the outcome be The third letter of the first step is L
H. the outcome be A step of the puzzle involves looking for specific letters present or not present in each word
I. the outcome be The fourth letter of the first step is I
J. the outcome be The first letter of the first step's result is S
K. the outcome be Some other symbols or signs than letters
L. the outcome be Ignore letter case
M. the outcome be The final answer has a Wikipedia page
N. the outcome be Each word provides exactly one data point toward the first step of the puzzle"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D, E, F, G, H, I, J, K, L, M, N}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N"
  ]
}
```

## v14ga_0002 — How many characters in the solution to @bens puzzle (round 2)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694bdd0b43684c005d3473f6`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "How many characters in the solution to @bens puzzle (round 2) (resolved around 2026-01-18 (GMT+8)). 
A. the outcome be 4 - 6
B. the outcome be 7 - 9
C. the outcome be 10 - 12
D. the outcome be 13 - 15
E. the outcome be 16 - 18
F. the outcome be 19 - 20"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0003 — Which candidates will make it to the second round of the Portuguese Presidential elections on 18 Jan 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694a8b8fbd65d70068ad7db4`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which candidates will make it to the second round of the Portuguese Presidential elections on 18 Jan 2026? (resolved around 2026-01-18 (GMT+8)). 
A. the outcome be Other
B. the outcome be António José Seguro vs. André Ventura
C. the outcome be Marques Mendes vs. André Ventura
D. the outcome be Marques Mendes vs. António José Seguro
E. the outcome be Gouveia e Melo vs. André Ventura
F. the outcome be Gouveia e Melo vs. Marques Mendes
G. the outcome be Gouveia e Melo vs. António José Seguro
H. the outcome be No second round"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0004 — Who will qualify for the second round of the Portugal Presidential Election?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69493cb11e67de005c795b7e`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will qualify for the second round of the Portugal Presidential Election? (resolved around 2026-01-18 (GMT+8)). 
A. João Cotrim de Figueiredo qualify for the second round of the 2026 Portugal presidential election
B. Joana Amaral Dias qualify for the second round of the 2026 Portugal presidential election
C. André Ventura qualify for the second round of the 2026 Portugal presidential election
D. Aristides Teixeira qualify for the second round of the 2026 Portugal presidential election
E. Luís Marques Mendes qualify for the second round of the 2026 Portugal presidential election
F. Henrique Gouveia e Melo qualify for the second round of the 2026 Portugal presidential election
G. Vitorino Silva qualify for the second round of the 2026 Portugal presidential election
H. António Filipe qualify for the second round of the 2026 Portugal presidential election
I. José Cardoso qualify for the second round of the 2026 Portugal presidential election
J. Jorge Pinto qualify for the second round of the 2026 Portugal presidential election
K. Tim Vieira qualify for the second round of the 2026 Portugal presidential election
L. André Pestana qualify for the second round of the 2026 Portugal presidential election
M. Orlando Cruz qualify for the second round of the 2026 Portugal presidential election
N. Manuela Magno qualify for the second round of the 2026 Portugal presidential election
O. Pedro Tinoco de Faria qualify for the second round of the 2026 Portugal presidential election
P. António José Seguro qualify for the second round of the 2026 Portugal presidential election
Q. Ângela Maryah qualify for the second round of the 2026 Portugal presidential election
R. Raul Perestrello qualify for the second round of the 2026 Portugal presidential election
S. Pedro Passos Coelho qualify for the second round of the 2026 Portugal presidential election
T. Catarina Martins qualify for the second round of the 2026 Portugal presidential election
U. Humberto Correia qualify for the second round of the 2026 Portugal presidential election
V. Manuel João Vieira qualify for the second round of the 2026 Portugal presidential election"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C, P}",
  "answer_tokens": [
    "C",
    "P"
  ]
}
```

## v14ga_0005 — 2025 CAF Cup of Nations (AFCON) Winner

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6957ba8a03568a006853e820`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2025 CAF Cup of Nations (AFCON) Winner (resolved around 2026-01-18 (GMT+8)). 
A. the outcome be Senegal
B. the outcome be Morocco
C. the outcome be Nigeria
D. the outcome be Egypt"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0006 — Global Average Temperature Dec 2025 per LOTI v4 vs 1951-1980 base period (NASA Gistemp)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6941510e41b9d1005effa734`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-15 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Global Average Temperature Dec 2025 per LOTI v4 vs 1951-1980 base period (NASA Gistemp) (resolved around 2026-01-15 (GMT+8)). 
A. the outcome be December 2025 less than 1.095C
B. the outcome be December 2025 1.095C or more and less than 1.145C
C. the outcome be December 2025 1.145C or more and less than 1.195C
D. the outcome be December 2025 1.195C or more and less than 1.245C
E. the outcome be December 2025 1.245C or more and less than 1.295C
F. the outcome be December 2025 1.295C or more and less than 1.345C
G. the outcome be December 2025 1.345C or more"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0007 — MCSR Ranked Playoffs Season 9 Winner

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69590c18deacd00066876767`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-15 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "MCSR Ranked Playoffs Season 9 Winner (resolved around 2026-01-15 (GMT+8)). 
A. the outcome be infume
B. the outcome be doogie
C. the outcome be hackingnoises
D. the outcome be lowk3y_
E. the outcome be edcr
F. the outcome be Other"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0008 — Who will post the winning guess in Ben’s puzzle (round 2) as yourself!

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695baf2f8b62560069adcdde`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will post the winning guess in Ben’s puzzle (round 2) as yourself! (resolved around 2026-01-18 (GMT+8)). 
A. the outcome be Winning guess is not posted
B. the outcome be Other
C. the outcome be Phenomist
D. the outcome be Eliza
E. the outcome be Jim Hays
F. the outcome be Q Breezy
G. the outcome be MachiNi
H. the outcome be @Jack1"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{D}",
  "answer_tokens": [
    "D"
  ]
}
```

## v14ga_0009 — Sept-Nov Unemployment Rate - U.K.

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a7993`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-20`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-20 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Sept-Nov Unemployment Rate - U.K. (resolved around 2026-01-20 (GMT+8)). 
A. the U.K.'s September–November 2025 unemployment rate be ≤4.9%
B. the U.K.'s September–November 2025 unemployment rate be 5.0%
C. the U.K.'s September–November 2025 unemployment rate be 5.1%
D. the U.K.'s September–November 2025 unemployment rate be 5.2%
E. the U.K.'s September–November 2025 unemployment rate be 5.3%
F. the U.K.'s September–November 2025 unemployment rate be ≥5.4%"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0010 — What will be true of the oil tanker Marinera on 14th January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695e521c255b39006c58f5af`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-15 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will be true of the oil tanker Marinera on 14th January? (resolved around 2026-01-15 (GMT+8)). 
A. the outcome be Under US control
B. the outcome be US claims to have found drugs on board
C. the outcome be US claims to have found weapons on board
D. the outcome be Sunk / scuppered / heavily damaged"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0011 — Which team will win the 2025-2026 College Football Playoff National Championship?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6956690c20a2e600672a78a6`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-20`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-20 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which team will win the 2025-2026 College Football Playoff National Championship? (resolved around 2026-01-20 (GMT+8)). 
A. the outcome be Ole miss
B. the outcome be Alabama
C. the outcome be Miami
D. the outcome be Texas Tech
E. the outcome be Georgia
F. the outcome be Indiana
G. the outcome be Oregon
H. the outcome be Other"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0012 — December Inflation Canada - Annual

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a796d`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-19`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-19 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "December Inflation Canada - Annual (resolved around 2026-01-19 (GMT+8)). 
A. Canada's annual inflation increase by 2.1% in December
B. Canada's annual inflation increase by 2.3% in December
C. Canada's annual inflation increase by ≤2.0% in December
D. Canada's annual inflation increase by 2.2% in December
E. Canada's annual inflation increase by ≥2.4% in December"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0013 — December Inflation Eurozone - Annual

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a79ab`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-19`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-19 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "December Inflation Eurozone - Annual (resolved around 2026-01-19 (GMT+8)). 
A. the Eurozone's annual inflation increase by 2.3% in December
B. the Eurozone's annual inflation increase by 2.2% in December
C. the Eurozone's annual inflation increase by ≤2.0% in December
D. the Eurozone's annual inflation increase by ≥2.4% in December
E. the Eurozone's annual inflation increase by 2.1% in December"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0014 — Coventry City FC vs. Leicester City FC

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a79eb`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Coventry City FC vs. Leicester City FC (resolved around 2026-01-18 (GMT+8)). 
A. Coventry City FC win on 2026-01-17
B. Coventry City FC vs. Leicester City FC end in a draw
C. Leicester City FC win on 2026-01-17"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0015 — “Inside CECOT” airs on 60 Minutes by January 18?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694a8b8fbd65d70068ad7da2`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "“Inside CECOT” airs on 60 Minutes by January 18? (resolved around 2026-01-18 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Yes} or \boxed{No}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0016 — Islanders vs. Oilers

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a79ba`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-16 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Islanders vs. Oilers (resolved around 2026-01-16 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Islanders} or \boxed{Oilers}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Islanders}",
  "answer_tokens": [
    "Islanders"
  ]
}
```

## v14ga_0017 — Lightning vs. Blues

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a79dd`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-17`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-17 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Lightning vs. Blues (resolved around 2026-01-17 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Lightning} or \boxed{Blues}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Blues}",
  "answer_tokens": [
    "Blues"
  ]
}
```

## v14ga_0018 — Southampton FC vs. Hull City AFC

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a79e5`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Southampton FC vs. Hull City AFC (resolved around 2026-01-18 (GMT+8)). 
A. Southampton FC win on 2026-01-17
B. Southampton FC vs. Hull City AFC end in a draw
C. Hull City AFC win on 2026-01-17"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0019 — Querétaro FC vs. Club Tijuana

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a799a`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-15 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Querétaro FC vs. Club Tijuana (resolved around 2026-01-15 (GMT+8)). 
A. Querétaro FC win on 2026-01-14
B. Querétaro FC vs. Club Tijuana end in a draw
C. Club Tijuana win on 2026-01-14"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0020 — Golden Knights vs. Kings

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a7998`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-15 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Golden Knights vs. Kings (resolved around 2026-01-15 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Golden Knights} or \boxed{Kings}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Golden Knights}",
  "answer_tokens": [
    "Golden Knights"
  ]
}
```

## v14ga_0021 — CF América vs. Atlético San Luis

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a799b`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-15 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "CF América vs. Atlético San Luis (resolved around 2026-01-15 (GMT+8)). 
A. CF América win on 2026-01-14
B. CF América vs. Atlético San Luis end in a draw
C. Atlético San Luis win on 2026-01-14"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0022 — Rams Başakşehir FK vs. Fatih Karagümrük SK

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69590f11deacd00066876794`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Rams Başakşehir FK vs. Fatih Karagümrük SK (resolved around 2026-01-18 (GMT+8)). 
A. Rams Başakşehir FK win on 2026-01-17
B. Rams Başakşehir FK vs. Fatih Karagümrük SK end in a draw
C. Fatih Karagümrük SK win on 2026-01-17"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0023 — Will @bens puzzle (round 2) get below 10%?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694bdd0b43684c005d3473e5`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will @bens puzzle (round 2) get below 10%? (resolved around 2026-01-18 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Yes} or \boxed{No}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0024 — Melbourne City FC vs. Auckland FC

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a79c0`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-17`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-17 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Melbourne City FC vs. Auckland FC (resolved around 2026-01-17 (GMT+8)). 
A. Melbourne City FC win on 2026-01-16
B. Melbourne City FC vs. Auckland FC end in a draw
C. Auckland FC win on 2026-01-16"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0025 — Sharks vs. Red Wings

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a79e0`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-17`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-17 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Sharks vs. Red Wings (resolved around 2026-01-17 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Sharks} or \boxed{Red Wings}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Red Wings}",
  "answer_tokens": [
    "Red Wings"
  ]
}
```

## v14ga_0026 — NAC Breda vs. NEC

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a7a33`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "NAC Breda vs. NEC (resolved around 2026-01-18 (GMT+8)). 
A. NAC Breda win on 2026-01-17
B. NAC Breda vs. NEC end in a draw
C. NEC win on 2026-01-17"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0027 — Al Ittihad Saudi Club vs. Al Ettifaq Saudi Club

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695e5562255b39006c58f5c5`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-17`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-17 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Al Ittihad Saudi Club vs. Al Ettifaq Saudi Club (resolved around 2026-01-17 (GMT+8)). 
A. Al Ittihad Saudi Club win on 2026-01-16
B. Al Ittihad Saudi Club vs. Al Ettifaq Saudi Club end in a draw
C. Al Ettifaq Saudi Club win on 2026-01-16"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0028 — In which city will Tetra be on January 15th 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69624695e87498005daa01d1`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-16 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "In which city will Tetra be on January 15th 2026? (resolved around 2026-01-16 (GMT+8)). 
A. the outcome be Blackpool
B. the outcome be Middlesbrough
C. the outcome be Other"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0029 — Sharks vs. Panthers

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6957c09b03568a006853e87d`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-20`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-20 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Sharks vs. Panthers (resolved around 2026-01-20 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Sharks} or \boxed{Panthers}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Sharks}",
  "answer_tokens": [
    "Sharks"
  ]
}
```

## v14ga_0030 — Deportivo Toluca FC vs. Club Santos Laguna

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a799d`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-15 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Deportivo Toluca FC vs. Club Santos Laguna (resolved around 2026-01-15 (GMT+8)). 
A. Deportivo Toluca FC win on 2026-01-14
B. Deportivo Toluca FC vs. Club Santos Laguna end in a draw
C. Club Santos Laguna win on 2026-01-14"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0031 — FC Köln vs. FC Bayern München

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695fa38be56c28005d3c324e`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-15 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "FC Köln vs. FC Bayern München (resolved around 2026-01-15 (GMT+8)). 
A. the outcome be FC Bayern München
B. the outcome be Tie
C. the outcome be FC Köln"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0032 — What will be the domestic box office gross in the opening weekend for "28 Years Later: The Bone Temple," according to Box Office Mojo?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6956690920a2e600672a7857`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-18`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-18 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will be the domestic box office gross in the opening weekend for "28 Years Later: The Bone Temple," according to Box Office Mojo? (resolved around 2026-01-18 (GMT+8)). 
A. the outcome be Less than $15 million
B. the outcome be At least $15 million, but less than $30 million
C. the outcome be At least $30 million, but less than $45 million
D. the outcome be At least $45 million, but less than $60 million
E. the outcome be At least $60 million, but less than $75 million
F. the outcome be At least $75 million, but less than $90 million"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0033 — 2026-01-19, what will be the books from rank 4 to 6 on the latest Amazon Charts of Most Read Fiction list? (Give the book titles only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685147092537419998691328`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-19`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-19 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-01-19, what will be the books from rank 4 to 6 on the latest Amazon Charts of Most Read Fiction list? (Give the book titles only)"
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{YOUR_PREDICTION}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{The Housemaid, Brimstone, The Correspondent}",
  "answer_tokens": [
    "The Housemaid",
    "Brimstone",
    "The Correspondent"
  ]
}
```

## v14ga_0034 — How much money will ClaudePlaysPokemon have left after completing Safari Zone?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6946970d97a129005dec27f7`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "How much money will ClaudePlaysPokemon have left after completing Safari Zone? (resolved around 2026-01-22 (GMT+8)). 
A.  the outcome be Does not complete Safari Zone
B.  the outcome be $0 - $9,999
C.  the outcome be $10,000-$19,999
D.  the outcome be $20,000-$29,999
E.  the outcome be $30,000-$39,999
F.  the outcome be $40,000-$49,999
G.  the outcome be $50,000-$59,999
H.  the outcome be $60,000-$69,999
I.  the outcome be $70,000+"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{I}",
  "answer_tokens": [
    "I"
  ]
}
```

## v14ga_0035 — Best Actress nominees? (2026 Oscars)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6956690c20a2e600672a7879`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Best Actress nominees? (2026 Oscars) (resolved around 2026-01-22 (GMT+8)). 
A.  the outcome be Jessie Buckley - Hamnet
B.  the outcome be Rose Byrne - If I Had Legs I'd Kick You
C.  the outcome be Renate Reinsve - Sentimental Value
D.  the outcome be Emma Stone - Bugonia
E.  the outcome be Chase Infiniti - One Battle After Another
F.  the outcome be Kate Hudson - Song Sung Blue
G.  the outcome be Amanda Seyfried - The Testament of Ann Lee
H.  the outcome be Cynthia Erivo - Wicked: For Good
I.  the outcome be Jennifer Lawrence - Die, My Love
J.  the outcome be June Squibb - Eleanor the Great
K.  the outcome be Sydney Sweeney - Christy
L.  the outcome be Julia Roberts - After the Hunt"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D, E}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D",
    "E"
  ]
}
```

## v14ga_0036 — Portugal Presidential Election First Round Head to Heads

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69663b097dc80a005b6df1cb`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-26`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-26`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Portugal Presidential Election First Round Head to Heads (resolved around 2026-01-26 (GMT+8)). 
A.  the outcome be André Ventura(YES) vs Henrique Gouveia e Melo(NO)
B.  the outcome be António José Seguro(YES) vs Henrique Gouveia e Melo(NO)
C.  the outcome be João Cotrim de Figueiredo(YES) vs Henrique Gouveia e Melo(NO)
D.  the outcome be António José Seguro(YES) vs João Cotrim de Figueiredo(NO)
E.  the outcome be André Ventura(YES) vs João Cotrim de Figueiredo(NO)
F.  the outcome be Luís Marques Mendes(YES) vs Henrique Gouveia e Melo(NO)
G.  the outcome be António José Seguro(YES) vs André Ventura(NO)
H.  the outcome be Luís Marques Mendes(YES) vs João Cotrim de Figueiredo(NO)
I.  the outcome be Luís Marques Mendes(YES) vs André Ventura(NO)
J.  the outcome be Luís Marques Mendes(YES) vs António José Seguro(NO)"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D, E, F}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F"
  ]
}
```

## v14ga_0037 — Oscars 2026: Achievement in Casting Nominations

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69493cb11e67de005c795a90`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Oscars 2026: Achievement in Casting Nominations  (resolved around 2026-01-22 (GMT+8)). 
A.  Cassandra Kulukundis (One Battle After Another) be nominated for Achievement in Casting at the 98th Academy Awards
B.  Francine Maisler (Sinners) be nominated for Achievement in Casting at the 98th Academy Awards
C.  Tiffany Little Canfield & Bernard Telsey (Wicked: For Good) be nominated for Achievement in Casting at the 98th Academy Awards
D.  Nina Gold (Hamnet) be nominated for Achievement in Casting at the 98th Academy Awards
E.  Jennifer Venditti (Marty Supreme) be nominated for Achievement in Casting at the 98th Academy Awards
F.  Yngvill Kolset Haga & Avy Kaufman (Sentimental Value) be nominated for Achievement in Casting at the 98th Academy Awards
G.  Bret Howe & Mary Vernieu (Wake Up Dead Man) be nominated for Achievement in Casting at the 98th Academy Awards
H.  Kei Kawamura & Yumi Takada (Rental Family) be nominated for Achievement in Casting at the 98th Academy Awards
I.  Margery Simkin (Avatar: Fire and Ash) be nominated for Achievement in Casting at the 98th Academy Awards
J.  Robin D. Cook (Frankenstein) be nominated for Achievement in Casting at the 98th Academy Awards
K.  Douglas Aibel & Nina Gold (Jay Kelly) be nominated for Achievement in Casting at the 98th Academy Awards
L.  Lucy Bevan & Emily Brockmann (F1) be nominated for Achievement in Casting at the 98th Academy Awards"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, D, E}",
  "answer_tokens": [
    "A",
    "B",
    "D",
    "E"
  ]
}
```

## v14ga_0038 — Oscars 2026: Best Director Nominations

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69493cb11e67de005c795a93`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Oscars 2026: Best Director Nominations  (resolved around 2026-01-22 (GMT+8)). 
A.  Kathryn Bigelow be nominated for Best Director at the 98th Academy Awards
B.  Paul Thomas Anderson be nominated for Best Director at the 98th Academy Awards
C.  Chloé Zhao be nominated for Best Director at the 98th Academy Awards
D.  Ryan Coogler be nominated for Best Director at the 98th Academy Awards
E.  Joachim Trier be nominated for Best Director at the 98th Academy Awards
F.  Jafar Panahi be nominated for Best Director at the 98th Academy Awards
G.  Josh Safdie be nominated for Best Director at the 98th Academy Awards
H.  Yorgos Lanthimos be nominated for Best Director at the 98th Academy Awards
I.  Benny Safdie be nominated for Best Director at the 98th Academy Awards
J.  Mona Fastvold be nominated for Best Director at the 98th Academy Awards
K.  James Cameron be nominated for Best Director at the 98th Academy Awards
L.  Park Chan-wook be nominated for Best Director at the 98th Academy Awards
M.  Jon M. Chu be nominated for Best Director at the 98th Academy Awards
N.  Guillermo del Toro be nominated for Best Director at the 98th Academy Awards
O.  Noah Baumbach be nominated for Best Director at the 98th Academy Awards
P.  Zach Cregger be nominated for Best Director at the 98th Academy Awards
Q.  Edward Berger be nominated for Best Director at the 98th Academy Awards
R.  Anthony Maras be nominated for Best Director at the 98th Academy Awards
S.  Clint Bentley be nominated for Best Director at the 98th Academy Awards
T.  Kleber Mendonça Filho be nominated for Best Director at the 98th Academy Awards"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{B, C, D, E, G}",
  "answer_tokens": [
    "B",
    "C",
    "D",
    "E",
    "G"
  ]
}
```

## v14ga_0039 — UEFA Champions League Week Prop Bets, Jan 20th-21st (Matchday 7)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695fa38ae56c28005d3c3241`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "UEFA Champions League Week Prop Bets, Jan 20th-21st (Matchday 7) (resolved around 2026-01-22 (GMT+8)). 
A.  the outcome be 3 (or more) penalty goals
B.  the outcome be 3 (or more) Players get red cards (in any fashion)
C.  the outcome be Goal in the first 5 minutes of any game
D.  the outcome be 7+ cards in a single match
E.  the outcome be Erling Haaland scores
F.  the outcome be Kylian Mbappe scores
G.  the outcome be Stoppage time winner
H.  the outcome be Stoppage time equalizer
I.  the outcome be 7+ goals in a single match
J.  the outcome be 2 (or more) 0-0 draws
K.  the outcome be 5 (or more) draws
L.  the outcome be From 2 goals down to level during a match
M.  the outcome be A penalty is missed or saved by the goalkeeper
N.  the outcome be 4+ Premier League teams win their matches"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D, E, F, G, H, I, J, K}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K"
  ]
}
```

## v14ga_0040 — Oscars 2026: Best Documentary Feature Nominations

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69493cb11e67de005c795a91`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Oscars 2026: Best Documentary Feature Nominations  (resolved around 2026-01-22 (GMT+8)). 
A.  The Perfect Neighbor be nominated for Best Documentary Feature at the 98th Academy Awards
B.  Put Your Soul on Your Hand and Walk be nominated for Best Documentary Feature at the 98th Academy Awards
C.  2000 Meters to Andriivka be nominated for Best Documentary Feature at the 98th Academy Awards
D.  Mr. Nobody Against Putin be nominated for Best Documentary Feature at the 98th Academy Awards
E.  Architecton be nominated for Best Documentary Feature at the 98th Academy Awards
F.  Cutting Through Rocks be nominated for Best Documentary Feature at the 98th Academy Awards
G.  Deaf President Now! be nominated for Best Documentary Feature at the 98th Academy Awards
H.  Apocalypse in the Tropics be nominated for Best Documentary Feature at the 98th Academy Awards
I.  Selena y Los Dinos be nominated for Best Documentary Feature at the 98th Academy Awards
J.  Endless Cookie be nominated for Best Documentary Feature at the 98th Academy Awards
K.  Springsteen: Deliver Me from Nowhere be nominated for Best Documentary Feature at the 98th Academy Awards
L.  Come See Me in the Good Light be nominated for Best Documentary Feature at the 98th Academy Awards
M.  Orwell: 2+2=5 be nominated for Best Documentary Feature at the 98th Academy Awards"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, D, F, L}",
  "answer_tokens": [
    "A",
    "D",
    "F",
    "L"
  ]
}
```

## v14ga_0041 — Best Picture nominees? (2026 Oscars)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6956690c20a2e600672a788c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Best Picture nominees? (2026 Oscars) (resolved around 2026-01-22 (GMT+8)). 
A.  the outcome be Hamnet
B.  the outcome be One Battle After Another
C.  the outcome be Sinners
D.  the outcome be Marty Supreme
E.  the outcome be Sentimental Value
F.  the outcome be Frankenstein
G.  the outcome be Bugonia
H.  the outcome be Train Dreams
I.  the outcome be It Was Just an Accident
J.  the outcome be The Secret Agent
K.  the outcome be F1
L.  the outcome be Weapons
M.  the outcome be Wicked: For Good
N.  the outcome be No Other Choice"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D, E, F, G, H, I, J}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J"
  ]
}
```

## v14ga_0042 — Who will win the main event of UFC 324? (Gaethje vs Pimblett)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694e8009028e36005d93d3cc`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-25`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-25`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the main event of UFC 324? (Gaethje vs Pimblett) (resolved around 2026-01-25 (GMT+8)). 
A.  the outcome be Justin Gaethje
B.  the outcome be Paddy Pimblett
C.  the outcome be Arman Tsarukyan
D.  the outcome be Charles Oliveira
E.  the outcome be Max Holloway
F.  the outcome be Other"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0043 — MLBB: M7 World Championship Winner

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69639b3e5a6f9800684ed6ab`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-25`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-25`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "MLBB: M7 World Championship Winner (resolved around 2026-01-25 (GMT+8)). 
A.  ONIC win the M7 World Championship
B.  Alter Ego win the M7 World Championship
C.  Team Liquid PH win the M7 World Championship
D.  Aurora Gaming PH win the M7 World Championship
E.  SRG.OG win the M7 World Championship
F.  CG Esports win the M7 World Championship
G.  Evil win the M7 World Championship
H.  CFU Gaming win the M7 World Championship
I.  Team Falcons win the M7 World Championship
J.  Yangon Galacticos win the M7 World Championship
K.  Team Spirit win the M7 World Championship
L.  Aurora Gaming win the M7 World Championship
M.  Black Sentence Esports win the M7 World Championship
N.  DianFengYaoGuai win the M7 World Championship
O.  RLG SE win the M7 World Championship
P.  Axe win the M7 World Championship
Q.  Boostgate Esports win the M7 World Championship
R.  Virtus.pro win the M7 World Championship
S.  Leon Esports win the M7 World Championship
T.  Guangzhou Gaming win the M7 World Championship
U.  Team Zone win the M7 World Championship
V.  ZETA DIVISION win the M7 World Championship
W.  another team win the M7 World Championship"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{D}",
  "answer_tokens": [
    "D"
  ]
}
```

## v14ga_0044 — Best Supporting Actress nominees? (2026 Oscars)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694a8b8fbd65d70068ad7db1`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Best Supporting Actress nominees? (2026 Oscars) (resolved around 2026-01-22 (GMT+8)). 
A.  the outcome be Teyana Taylor - One Battle After Another
B.  the outcome be Amy Madigan - Weapons
C.  the outcome be Inga Ibsdotter Lilleaas - Sentimental Value
D.  the outcome be Wunmi Mosaku - Sinners
E.  the outcome be Ariana Grande - Wicked: For Good
F.  the outcome be Odessa A'zion - Marty Supreme
G.  the outcome be Elle Fanning - Sentimental Value
H.  the outcome be Gwyneth Paltrow - Marty Supreme
I.  the outcome be Regina Hall - One Battle After Another
J.  the outcome be Laura Dern - Jay Kelly"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0045 — Best Director nominees? (2026 Oscars)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694a8b8fbd65d70068ad7db2`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Best Director nominees? (2026 Oscars) (resolved around 2026-01-22 (GMT+8)). 
A.  the outcome be Paul Thomas Anderson - One Battle After Another
B.  the outcome be Ryan Coogler - Sinners
C.  the outcome be Chloé Zhao - Hamnet
D.  the outcome be Joachim Trier - Sentimental Value
E.  the outcome be Jafar Panahi - It Was Just an Accident
F.  the outcome be Josh Safdie - Marty Supreme
G.  the outcome be Guillermo del Toro - Frankenstein
H.  the outcome be Yorgos Lanthimos - Bugonia
I.  the outcome be Mona Fastvold - The Testament of Ann Lee
J.  the outcome be James Cameron - Avatar: Fire and Ash"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D, E}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D",
    "E"
  ]
}
```

## v14ga_0046 — How long will it take Alex Honnold to free solo Taipei 101?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6957c09b03568a006853e86c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-23`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-23`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "How long will it take Alex Honnold to free solo Taipei 101? (resolved around 2026-01-23 (GMT+8)). 
A.  Alex Honnold free solo Taipei 101 in less than 1 hour
B.  Alex Honnold free solo Taipei 101 in between 1 hour and 30 minutes and 1 hour and 45 minutes
C.  Alex Honnold free solo Taipei 101 in between 1 hour and 45 minutes and 2 hours
D.  Alex Honnold free solo Taipei 101 in between 2 hours and 2 hours and 15 minutes
E.  Alex Honnold free solo Taipei 101 in between 2 hours and 15 minutes and 2 hours and 30 minutes
F.  Alex Honnold free solo Taipei 101 in over 2 hours and 30 minutes
G.  Alex Honnold free solo Taipei 101 in between 1 hour and 1 hour and 15 minutes
H.  Alex Honnold not complete a free solo of Taipei 101 by January 31
I.  Alex Honnold free solo Taipei 101 in between 1 hour and 15 minutes and 1 hour and 30 minutes"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0047 — Who will win the 2026 MIT Science Olympiad Invitational?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694e8009028e36005d93d3ce`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-25`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-25`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the 2026 MIT Science Olympiad Invitational? (resolved around 2026-01-25 (GMT+8)). 
A.  the outcome be Troy H.S. (Fullerton, CA)
B.  the outcome be Mason H.S. (Mason, OH)
C.  the outcome be Monta Vista H.S. (Cupertino, CA)
D.  the outcome be Seven Lakes H.S. (Katy, TX)
E.  the outcome be Harriton H.S. (Rosemont, PA)
F.  the outcome be Montgomery H.S. (Skillman, NJ)
G.  the outcome be Mountain View H.S. (Mountain View, CA)"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0048 — NFC Champion

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694e82d4028e36005d93d3f3`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-27`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-27`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "NFC Champion  (resolved around 2026-01-27 (GMT+8)). 
A.  the Cardinals win the NFC Championship
B.  the Falcons win the NFC Championship
C.  the Panthers win the NFC Championship
D.  the Bears win the NFC Championship
E.  the Cowboys win the NFC Championship
F.  the Lions win the NFC Championship
G.  the Packers win the NFC Championship
H.  the Rams win the NFC Championship
I.  the Vikings win the NFC Championship
J.  the Saints win the NFC Championship
K.  the Giants win the 2026 NFC Championship
L.  the Eagles win the 2026 NFC Championship
M.  the 49ers win the 2026 NFC Championship
N.  the Seahawks win the 2026 NFC Championship
O.  the Buccaneers win the 2026 NFC Championship
P.  the Commanders win the 2026 NFC Championship"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{N}",
  "answer_tokens": [
    "N"
  ]
}
```

## v14ga_0049 — Best Actor nominees? (2026 Oscars)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6956690c20a2e600672a787a`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Best Actor nominees? (2026 Oscars) (resolved around 2026-01-22 (GMT+8)). 
A.  the outcome be Leonardo DiCaprio - One Battle After Another
B.  the outcome be Timothée Chalamet - Marty Supreme
C.  the outcome be Michael B. Jordan - Sinners
D.  the outcome be Wagner Moura - The Secret Agent
E.  the outcome be Ethan Hawke - Blue Moon
F.  the outcome be Jesse Plemons - Bugonia
G.  the outcome be Joel Edgarton - Train Dreams
H.  the outcome be Daniel Day-Lewis - Anemone
I.  the outcome be Jeremy Allen White - Springsteen: Deliver Me From Nowhere
J.  the outcome be Dwayne Johnson - The Smashing Machine
K.  the outcome be George Clooney - Jay Kelly
L.  the outcome be Paul Mescal - The History of Sound"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0050 — Will Polo gram be revealed to be Marco's dad within 1 month

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694fd195ae81c200695c89be`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-26`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-26`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Polo gram be revealed to be Marco's dad within 1 month (resolved around 2026-01-26 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0051 — Will Bugonia get an Oscar nomination for best picture?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69493a091e67de005c79583b`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Bugonia get an Oscar nomination for best picture? (resolved around 2026-01-22 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0052 — The No-Bots Market. Which side will be automated-bots-free market close?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6964e98952029b005bc009b6`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-23`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-23`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "The No-Bots Market. Which side will be automated-bots-free market close? (resolved around 2026-01-23 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v13ra_001 — Bank of Brazil decision in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694fd4d0ae81c200695c89cf`
- Category: `central_bank_decision`
- Pattern: `winner market`
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
- Source id: `6956690920a2e600672a7864`
- Category: `central_bank_decision`
- Pattern: `winner market`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{B}",
  "answer_tokens": [
    "B"
  ]
}
```

## v14ga_0055 — RAS2026: Will One Battle After Another gather more Oscars nominations than Marty Supreme?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6964e98952029b005bc009c2`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "RAS2026: Will One Battle After Another gather more Oscars nominations than Marty Supreme? (resolved around 2026-01-22 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0056 — Will Alex Honnold successfully free solo Taipei 101 on January 23, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694d2e966344cf0067e820ae`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-23`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-01-24`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Alex Honnold successfully free solo Taipei 101 on January 23, 2026? (resolved around 2026-01-24 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0057 — Before 24 January 2026, will Paramount Skydance (Paramount) increase its offer to pay $30.00 per share for outstanding Warner Bros. Discovery (Warner Bros.) shares?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6956690920a2e600672a7865`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-24`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-01-25`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Before 24 January 2026, will Paramount Skydance (Paramount) increase its offer to pay $30.00 per share for outstanding Warner Bros. Discovery (Warner Bros.) shares? (resolved around 2026-01-25 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0058 — Will the US Storm Prediction Center issue a Tornado Watch between 12:00 am EST 1/18/26 and 11:59 pm EST 1/24/26?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6968de07e7876e006835e6b3`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-25`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-25`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will the US Storm Prediction Center issue a Tornado Watch between 12:00 am EST 1/18/26 and 11:59 pm EST 1/24/26? (resolved around 2026-01-25 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0059 — Juventus beats SSC Napoli | Soccer Serie A match 25th Jan 2026

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6956690c20a2e600672a786b`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-26`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-26`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Juventus beats SSC Napoli | Soccer Serie A match 25th Jan 2026 (resolved around 2026-01-26 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0060 — Will Adrian Gonzales be found guilty in Uvalde school shooting response trial?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695fa38ae56c28005d3c3234`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Adrian Gonzales be found guilty in Uvalde school shooting response trial? (resolved around 2026-01-22 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0061 — How will the winner of the portugal presidential election win

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6957ba8a03568a006853e828`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-27`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-27`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "How will the winner of the portugal presidential election win (resolved around 2026-01-27 (GMT+8)). 
A.  the outcome be Only candidate above 50% in round one
B.  the outcome be Wins first round and the runoff
C.  the outcome be 2nd place in the first round, wins runoff"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0062 — Will Pam Bondi be arrested over defying the Epstein Files Transparency Act

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6951230b943bd200688f9cd1`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-27`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-27`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Pam Bondi be arrested over defying the Epstein Files Transparency Act (resolved around 2026-01-27 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0063 — nasry Asfuras win overturned by a court?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `694e8009028e36005d93d3c6`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-26`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-26`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "nasry Asfuras win overturned by a court? (resolved around 2026-01-26 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0064 — Will there be a surprising Best Picture nomination? (2026 Oscars)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695d00ac4ef7b4005cb967ee`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will there be a surprising Best Picture nomination? (2026 Oscars) (resolved around 2026-01-22 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0065 — Al Hilal Saudi Club vs. Al Fayha Saudi Club

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695e5562255b39006c58f5d4`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-23`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-23`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Al Hilal Saudi Club vs. Al Fayha Saudi Club (resolved around 2026-01-23 (GMT+8)). 
A.  Al Hilal Saudi Club win on 2026-01-22
B.  Al Hilal Saudi Club vs. Al Fayha Saudi Club end in a draw
C.  Al Fayha Saudi Club win on 2026-01-22"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0066 — FC Arouca vs. Sporting CP

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695d03e74ef7b4005cb9682d`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-25`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-25`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "FC Arouca vs. Sporting CP (resolved around 2026-01-25 (GMT+8)). 
A.  FC Arouca win on 2026-01-24
B.  FC Arouca vs. Sporting CP end in a draw
C.  Sporting CP win on 2026-01-24"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0067 — Auckland FC vs. Central Coast Mariners FC

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6960f83c14d4fb0067208587`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-24`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-24`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Auckland FC vs. Central Coast Mariners FC (resolved around 2026-01-24 (GMT+8)). 
A.  Auckland FC win on 2026-01-23
B.  Auckland FC vs. Central Coast Mariners FC end in a draw
C.  Central Coast Mariners FC win on 2026-01-23"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0068 — 2026-01-27, who will be the players ranked from 12 to 14 in the latest Official World Golf Ranking? (Give the names only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6854dfb0a5e49700606af49d`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-27`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-27`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-01-27, who will be the players ranked from 12 to 14 in the latest Official World Golf Ranking? (Give the names only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Sepp Straka, Alex Noren, Alex Noren}",
  "answer_tokens": [
    "Sepp Straka",
    "Alex Noren",
    "Alex Noren"
  ]
}
```

## v14ga_0069 — 2026-01-26, what will be the books from rank 13 to 15 on the latest Amazon Charts of Most Read Fiction list? (Give the book titles only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685147092537420060414059`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-26`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-26`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-01-26, what will be the books from rank 13 to 15 on the latest Amazon Charts of Most Read Fiction list? (Give the book titles only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Heated Rivalry, Fourth Wing, Quicksilver}",
  "answer_tokens": [
    "Heated Rivalry",
    "Fourth Wing",
    "Quicksilver"
  ]
}
```

## v14ga_0070 — 2026-01-23, what will the high of Apple stock (AAPL) be for the day (in US$)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6851736beb11c800614780df`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-23`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-23`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-01-23, what will the high of Apple stock (AAPL) be for the day (in US$)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{249.41}",
  "answer_tokens": [
    "249.41"
  ]
}
```

## v14ga_0071 — 2026-01-26, what will be the day's open of the S&P 500 Index (INDEXSP:.INX)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6851737f59f71f006037a1e4`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-26`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-26`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-01-26, what will be the day's open of the S&P 500 Index (INDEXSP:.INX)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{6923.23}",
  "answer_tokens": [
    "6923.23"
  ]
}
```

## v14ga_0072 — 2026-01-22, what will be the day's close for the Dow Jones Industrial Average (INDEXDJX:.DJI)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685173d659f71f006037a1eb`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-22`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-22`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-01-22, what will be the day's close for the Dow Jones Industrial Average (INDEXDJX:.DJI)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{49384.01}",
  "answer_tokens": [
    "49384.01"
  ]
}
```

## v14ga_0073 — 2026-01-23, what will be the Nikkei Stock Average (Nikkei 225)'s close for the day?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6851741059f71f006037a1ee`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-23`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-23`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-01-23, what will be the Nikkei Stock Average (Nikkei 225)'s close for the day?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{53846.87}",
  "answer_tokens": [
    "53846.87"
  ]
}
```

## v14ga_0074 — 2026-01-27, what will be the high for Li Auto (NASDAQ:LI) for the day (in US$)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `68528da19193260061abd8f6`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-27`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-27`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-01-27, what will be the high for Li Auto (NASDAQ:LI) for the day (in US$)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{16.85}",
  "answer_tokens": [
    "16.85"
  ]
}
```

## v14ga_0075 — 2026-01-27, what will the NASDAQ Composite Index (.IXIC)'s open be for the day?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `687df3b6ff05a4003c601bc2`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-27`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-27`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-01-27, what will the NASDAQ Composite Index (.IXIC)'s open be for the day?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{23734.75}",
  "answer_tokens": [
    "23734.75"
  ]
}
```

## v14ga_0076 — Will Palantir (PLTR) close above ___ end of January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695bb4008b62560069adce4b`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-31`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-31 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Palantir (PLTR) close above ___ end of January? (resolved around 2026-01-31 (GMT+8)). 
A. Palantir (PLTR) close above $192 end of January
B. Palantir (PLTR) close above $196 end of January
C. Palantir (PLTR) close above $206 end of January
D. Palantir (PLTR) close above $182 end of January
E. Palantir (PLTR) close above $184 end of January
F. Palantir (PLTR) close above $186 end of January
G. Palantir (PLTR) close above $188 end of January
H. Palantir (PLTR) close above $190 end of January
I. Palantir (PLTR) close above $194 end of January
J. Palantir (PLTR) close above $198 end of January
K. Palantir (PLTR) close above $200 end of January
L. Palantir (PLTR) close above $202 end of January
M. Palantir (PLTR) close above $204 end of January"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{None of the above}",
  "answer_tokens": [
    "None of the above"
  ]
}
```

## v14ga_0077 — What will Trump say in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69663e477dc80a005b6df1ea`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-31`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-31 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will Trump say in January? (resolved around 2026-01-31 (GMT+8)). 
A. Trump say "Heart Attack" in January
B. Trump say "N Word" in January
C. Trump say "Banana Republic" in January
D. Trump say "Martin Luther King" in January
E. Trump say "Ego" in January
F. Trump say "Communist" in January
G. Trump say "Jerome Too Late Powell" in January
H. Trump say "Teleprompter" in January
I. Trump say "F-47" in January
J. Trump say "Food stamps" in January
K. Trump say "Fuck" or "Fucking" or "Fucked" in January
L. Trump say "Breaking News" in January
M. Trump say "Rolex" in January
N. Trump say "TrumpRx.gov" or "TrumpRx.com" or "TrumpRx" in January
O. Trump say "Trump Derangement Syndrome" in January
P. Trump say "Bitcoin" in January
Q. Trump say "Skyrocket" or "Skyrocketed" in January
R. Trump say "McDonald's" in January
S. Trump say "Dell computer" in January
T. Trump say "Truth Social" in January"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{F, G, H, I, J, L, M, N, O, P, Q, S}",
  "answer_tokens": [
    "F",
    "G",
    "H",
    "I",
    "J",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "S"
  ]
}
```

## v14ga_0078 — Price of DDR5-6000 2x16GB RAM at the end of January 2026

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6957ba8a03568a006853e83f`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Price of DDR5-6000 2x16GB RAM at the end of January 2026 (resolved around 2026-02-01 (GMT+8)). 
A. the outcome be Less than $100
B. the outcome be $100-$200
C. the outcome be $200-$300
D. the outcome be $300-$400
E. the outcome be $400-$500
F. the outcome be $500-$600
G. the outcome be Other"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0079 — Turnout in 2026 Costa Rica Presidential Election First Round

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a78fd`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Turnout in 2026 Costa Rica Presidential Election First Round (resolved around 2026-02-01 (GMT+8)). 
A. turnout in the first round of the 2026 Costa Rican Presidential Election be less than 55%
B. turnout in the first round of the 2026 Costa Rican Presidential Election be between 58% and 60%
C. turnout in the first round of the 2026 Costa Rican Presidential Election be between 62% and 64%
D. turnout in the first round of the 2026 Costa Rican Presidential Election be between 66% and 68%
E. turnout in the first round of the 2026 Costa Rican Presidential Election be between 70% and 72%
F. turnout in the first round of the 2026 Costa Rican Presidential Election be between 55% and 58%
G. turnout in the first round of the 2026 Costa Rican Presidential Election be between 60% and 62%
H. turnout in the first round of the 2026 Costa Rican Presidential Election be between 64% and 66%
I. turnout in the first round of the 2026 Costa Rican Presidential Election be between 68% and 70%
J. turnout in the first round of the 2026 Costa Rican Presidential Election be at least 72%"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{I}",
  "answer_tokens": [
    "I"
  ]
}
```

## v14ga_0080 — GPT 5.2 METR time horizon

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `693c0b13a23921005c8d53ce`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-31`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-31 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "GPT 5.2 METR time horizon (resolved around 2026-01-31 (GMT+8)). 
A. the outcome be <2h
B. the outcome be 2h00 - 2h15
C. the outcome be 2h15 - 2h30
D. the outcome be 2h30 - 2h45
E. the outcome be 2h45 - 3h00
F. the outcome be 3h00 - 3h15
G. the outcome be 3h15 - 3h30
H. the outcome be 3h30 - 3h45
I. the outcome be 3h45 - 4h
J. the outcome be >= 4h"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{J}",
  "answer_tokens": [
    "J"
  ]
}
```

## v14ga_0081 — Precipitation in NYC in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69639b3e5a6f9800684ed69a`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-31`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-31 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Precipitation in NYC in January? (resolved around 2026-01-31 (GMT+8)). 
A. NYC have between 3 and 4 inches of precipitation in January
B. NYC have more than 7 inches of precipitation in January
C. NYC have less than 3 inches of precipitation in January
D. NYC have between 4 and 5 inches of precipitation in January
E. NYC have between 5 and 6 inches of precipitation in January
F. NYC have between 6 and 7 inches of precipitation in January"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0082 — Which nation will be the focus of Stellaris Invicta Season 3?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6972189f11cfd2006997649c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-02`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-02 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which nation will be the focus of Stellaris Invicta Season 3? (resolved around 2026-02-02 (GMT+8)). 
A. the outcome be United Federation of Nations
B. the outcome be Tripartite of Sol
C. the outcome be Holy Solar Empire
D. the outcome be House Triton
E. the outcome be Eternal Kreventum"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v13ra_005 — Gold (GC) above ___ end of January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695bb4008b62560069adce53`
- Category: `commodity_thresholds`
- Pattern: `statement-truth set`
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

## v13ra_008 — What will Crude Oil (CL) settle at in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695bb4008b62560069adce59`
- Category: `commodity_bucket`
- Pattern: `interval bin`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{F}",
  "answer_tokens": [
    "F"
  ]
}
```

## v14ga_0085 — Which soccer players will sign with new clubs in winter window?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69590f11deacd00066876793`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-03`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-03 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which soccer players will sign with new clubs in winter window? (resolved around 2026-02-03 (GMT+8)). 
A. Jean-Philippe Mateta sign with a new club during the winter transfer window
B. Carlos Baleba sign with a new club during the winter transfer window
C. Scott McTominay sign with a new club during the winter transfer window
D. James Ward-Prowse sign with a new club during the winter transfer window
E. Federico Chiesa sign with a new club during the winter transfer window
F. Mathys Tel sign with a new club during the winter transfer window
G. Sergio Ramos sign with a new club during the winter transfer window
H. Adama Traore sign with a new club during the winter transfer window
I. Niclas Füllkrug sign with a new club during the winter transfer window
J. Antoine Semenyo sign with a new club during the winter transfer window
K. Conor Gallagher sign with a new club during the winter transfer window
L. Richarlison sign with a new club during the winter transfer window
M. Timo Werner sign with a new club during the winter transfer window
N. Joshua Zirkzee sign with a new club during the winter transfer window
O. Endrick sign with a new club during the winter transfer window
P. Bruno Fernandes sign with a new club during the winter transfer window
Q. Marc Guehi sign with a new club during the winter transfer window
R. Vinicius Jr. sign with a new club during the winter transfer window
S. Malo Gusto sign with a new club during the winter transfer window
T. Robert Lewandowski sign with a new club during the winter transfer window
U. Rúben Neves sign with a new club during the winter transfer window
V. Morten Hjulmand sign with a new club during the winter transfer window
W. Marc-André ter Stegen sign with a new club during the winter transfer window
X. Kobbie Mainoo sign with a new club during the winter transfer window
Y. Julian Brandt sign with a new club during the winter transfer window
Z. Neymar sign with a new club during the winter transfer window
[. Dayot Upamecano sign with a new club during the winter transfer window
\. Dušan Vlahović sign with a new club during the winter transfer window
]. Ibrahima Konaté sign with a new club during the winter transfer window
^. Mason Greenwood sign with a new club during the winter transfer window
_. Jobe Bellingham sign with a new club during the winter transfer window
`. Kalvin Phillips sign with a new club during the winter transfer window
a. Adam Wharton sign with a new club during the winter transfer window
b. Kenan Yildiz sign with a new club during the winter transfer window"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{D, H, I, J, K, M, O, Q, W, `}",
  "answer_tokens": [
    "D",
    "H",
    "I",
    "J",
    "K",
    "M",
    "O",
    "Q",
    "W",
    "`"
  ]
}
```

## v14ga_0086 — Measles cases in U.S. by January 31?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6974bec1b31670005dd8d72a`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-31`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-01-31 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Measles cases in U.S. by January 31? (resolved around 2026-01-31 (GMT+8)). 
A. there be at least 300 measles cases in the U.S. by January 31, 2026
B. there be at least 500 measles cases in the U.S. by January 31, 2026
C. there be at least 400 measles cases in the U.S. by January 31, 2026
D. there be at least 750 measles cases in the U.S. by January 31, 2026
E. there be at least 40 measles cases in the U.S. by January 31, 2026
F. there be at least 20 measles cases in the U.S. by January 31, 2026
G. there be at least 150 measles cases in the U.S. by January 31, 2026
H. there be at least 175 measles cases in the U.S. by January 31, 2026
I. there be at least 200 measles cases in the U.S. by January 31, 2026
J. there be at least 600 measles cases in the U.S. by January 31, 2026
K. there be at least 700 measles cases in the U.S. by January 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, E, F, G, H, I}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "E",
    "F",
    "G",
    "H",
    "I"
  ]
}
```

## v14ga_0087 — Grammys: Songwriter of the Year Winner

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a78fb`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Grammys: Songwriter of the Year Winner (resolved around 2026-02-01 (GMT+8)). 
A. Amy Allen win Songwriter of the Year, Non-Classical at the 68th annual GRAMMY Awards
B. Laura Veltz win Songwriter of the Year, Non-Classical at the 68th annual GRAMMY Awards
C. Songwriter D win Songwriter of the Year, Non-Classical at the 68th annual GRAMMY Awards
D. Edgar Barrera win Songwriter of the Year, Non-Classical at the 68th annual GRAMMY Awards
E. Songwriter A win Songwriter of the Year, Non-Classical at the 68th annual GRAMMY Awards
F. Songwriter E win Songwriter of the Year, Non-Classical at the 68th annual GRAMMY Awards
G. Jessie Jo Dillon win Songwriter of the Year, Non-Classical at the 68th annual GRAMMY Awards
H. Songwriter B win Songwriter of the Year, Non-Classical at the 68th annual GRAMMY Awards
I. another person win Songwriter of the Year, Non-Classical at the 68th annual GRAMMY Awards
J. Tobias Jesso Jr. win Songwriter of the Year, Non-Classical at the 68th annual GRAMMY Awards
K. Songwriter C win Songwriter of the Year, Non-Classical at the 68th annual GRAMMY Awards"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0088 — What will Opendoor (OPEN) hit in January 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695bb4008b62560069adce04`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will Opendoor (OPEN) hit in January 2026? (resolved around 2026-02-01 (GMT+8)). 
A. Opendoor reach $11.50 in January
B. Opendoor reach $10.25 in January
C. Opendoor reach $9.25 in January
D. Opendoor reach $8.25 in January
E. Opendoor reach $7.50 in January
F. Opendoor reach $7 in January
G. Opendoor reach $6.50 in January
H. Opendoor dip to $6 in January
I. Opendoor dip to $5.50 in January
J. Opendoor dip to $5 in January
K. Opendoor dip to $4.25 in January
L. Opendoor dip to $3.50 in January
M. Opendoor dip to $2.50 in January
N. Opendoor dip to $1.25 in January"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{E, F, G, H, I}",
  "answer_tokens": [
    "E",
    "F",
    "G",
    "H",
    "I"
  ]
}
```

## v13ra_007 — What will Crude Oil (CL) hit__ by end of January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695bb4008b62560069adce56`
- Category: `commodity_hit_levels`
- Pattern: `threshold ladder`
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

## v13ra_006 — What will Gold (GC) settle at in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695bb4008b62560069adce54`
- Category: `commodity_bucket`
- Pattern: `interval bin`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{E}",
  "answer_tokens": [
    "E"
  ]
}
```

## v14ga_0091 — [January 2026] Top 10 cards in the MTG Arena Powered Cube (by 17Lands GIH WR)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695fa38ae56c28005d3c3248`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "[January 2026] Top 10 cards in the MTG Arena Powered Cube (by 17Lands GIH WR) (resolved around 2026-02-01 (GMT+8)). 
A. the outcome be Time Walk
B. the outcome be Black Lotus
C. the outcome be Ocelot Pride
D. the outcome be Orcish Bowmasters
E. the outcome be Mana Crypt
F. the outcome be Ancestral Recall
G. the outcome be Parallax Wave
H. the outcome be Comet, Stellar Pup
I. the outcome be Ajani, Nacatl Pariah
J. the outcome be Sol Ring
K. the outcome be Mox Sapphire
L. the outcome be Mox Pearl
M. the outcome be Flash
N. the outcome be Broadside Bombardiers"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D, E, F, G, H, I}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I"
  ]
}
```

## v14ga_0092 — Will Israel strike Gaza on...?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6964eca552029b005bc009f2`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-31`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-01-31 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Israel strike Gaza on...? (resolved around 2026-01-31 (GMT+8)). 
A. Israel strike Gaza on January 1, 2026
B. Israel strike Gaza on January 2, 2026
C. Israel strike Gaza on January 3, 2026
D. Israel strike Gaza on January 4, 2026
E. Israel strike Gaza on January 5, 2026
F. Israel strike Gaza on January 6, 2026
G. Israel strike Gaza on January 7, 2026
H. Israel strike Gaza on January 8, 2026
I. Israel strike Gaza on January 9, 2026
J. Israel strike Gaza on January 10, 2026
K. Israel strike Gaza on January 11, 2026
L. Israel strike Gaza on January 12, 2026
M. Israel strike Gaza on January 13, 2026
N. Israel strike Gaza on January 14, 2026
O. Israel strike Gaza on January 15, 2026
P. Israel strike Gaza on January 16, 2026
Q. Israel strike Gaza on January 17, 2026
R. Israel strike Gaza on January 18, 2026
S. Israel strike Gaza on January 19, 2026
T. Israel strike Gaza on January 20, 2026
U. Israel strike Gaza on January 21, 2026
V. Israel strike Gaza on January 22, 2026
W. Israel strike Gaza on January 23, 2026
X. Israel strike Gaza on January 24, 2026
Y. Israel strike Gaza on January 25, 2026
Z. Israel strike Gaza on January 26, 2026
[. Israel strike Gaza on January 27, 2026
\. Israel strike Gaza on January 28, 2026
]. Israel strike Gaza on January 29, 2026
^. Israel strike Gaza on January 30, 2026
_. Israel strike Gaza on January 31, 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C, E, G, H, J, K, L, M, O, U, X, [, ], ^, _}",
  "answer_tokens": [
    "C",
    "E",
    "G",
    "H",
    "J",
    "K",
    "L",
    "M",
    "O",
    "U",
    "X",
    "[",
    "]",
    "^",
    "_"
  ]
}
```

## v14ga_0093 — How Many Days will Arlington Virginia Public Schools be Cancelled Next Week?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6972189f11cfd20069976498`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-02`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-02 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "How Many Days will Arlington Virginia Public Schools be Cancelled Next Week? (resolved around 2026-02-02 (GMT+8)). 
A. the outcome be 0
B. the outcome be 1
C. the outcome be 2
D. the outcome be 3
E. the outcome be 4"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0094 — Which tennis player will win the Women's Singles Final at the 2026 Australian Open?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6956690920a2e600672a7867`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which tennis player will win the Women's Singles Final at the 2026 Australian Open? (resolved around 2026-02-01 (GMT+8)). 
A. the outcome be Mirra Andreeva
B. the outcome be Amanda Anisimova
C. the outcome be Coco Gauff
D. the outcome be Madison Keys
E. the outcome be Naomi Osaka
F. the outcome be Elena Rybakina
G. the outcome be Aryna Sabalenka
H. the outcome be Iga Swiatek"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0095 — Who will win the 2026 Grammy for Best Pop Vocal Album?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695a5d897b2e6a00694886b9`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-02`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-02 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the 2026 Grammy for Best Pop Vocal Album? (resolved around 2026-02-02 (GMT+8)). 
A. the outcome be "SWAG," Justin Bieber
B. the outcome be "Man's Best Friend," Sabrina Carpenter
C. the outcome be "Something Beautiful," Miley Cyrus
D. the outcome be "MAYHEM," Lady Gaga
E. the outcome be "I've Tried Everything But Therapy (Part 2)," Teddy Swims"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{D}",
  "answer_tokens": [
    "D"
  ]
}
```

## v14ga_0096 — Who will win the 2026 Grammy for Record of the Year?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695a5d897b2e6a00694886af`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-02`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-02 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the 2026 Grammy for Record of the Year? (resolved around 2026-02-02 (GMT+8)). 
A. the outcome be "DtMF," Bad Bunny
B. the outcome be "Manchild," Sabrina Carpenter
C. the outcome be "Anxiety," Doechii
D. the outcome be "Wildflower," Billie Eilish
E. the outcome be "Abracadabra," Lady Gaga
F. the outcome be "Luther," Kendrick Lamar with SZA
G. the outcome be "The Subway," Chappell Roan"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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
- Source id: `6957ba8a03568a006853e82e`
- Category: `first_hit`
- Pattern: `winner market`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{A}",
  "answer_tokens": [
    "A"
  ]
}
```

## v13ra_003 — Reserve Bank of Australia Decision in February

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695a609d7b2e6a00694886f6`
- Category: `central_bank_decision`
- Pattern: `winner market`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{B}",
  "answer_tokens": [
    "B"
  ]
}
```

## v14ga_0099 — Will thealignedapp.com have 100+ users by Jan 31, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695a5ee87b2e6a00694886d2`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will thealignedapp.com have 100+ users by Jan 31, 2026? (resolved around 2026-02-01 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Yes} or \boxed{No}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v13ra_010 — Nvidia hits 170, 200 or neither first by end of January 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6957ba8a03568a006853e82f`
- Category: `first_hit`
- Pattern: `winner market`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{A}",
  "answer_tokens": [
    "A"
  ]
}
```

## v14ga_0101 — Reeves or Lammy out first?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6957ba8a03568a006853e845`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-02-02 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Reeves or Lammy out first? (resolved around 2026-02-02 (GMT+8)). 
A. the outcome be Reeves first
B. the outcome be Lammy first
C. the outcome be Both are still in post by 1 February 2026"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0102 — New METR SOTA by end of January, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6972189f11cfd2006997647f`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "New METR SOTA by end of January, 2026? (resolved around 2026-02-01 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Yes} or \boxed{No}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0103 — Will the Doomsday Clock move by ten seconds or more?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69566c1320a2e600672a798d`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-31`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-31 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will the Doomsday Clock move by ten seconds or more? (resolved around 2026-01-31 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Yes} or \boxed{No}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0104 — Will they pull a Nasrallah on Khamenei by end of January 2025?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6968de07e7876e006835e6b8`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will they pull a Nasrallah on Khamenei by end of January 2025? (resolved around 2026-02-01 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Yes} or \boxed{No}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0105 — 2026 a dream year for trump?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6947e88aa66250005c9dc324`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-31`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-31 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026 a dream year for trump? (resolved around 2026-01-31 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Yes} or \boxed{No}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v13ra_011 — Will Bitcoin close above USD $100,000 on 31 January 2026 (UTC)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69590c18deacd00066876763`
- Category: `crypto_binary`
- Pattern: `binary`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{No}",
  "answer_tokens": [
    "No"
  ]
}
```

## v14ga_0107 — North Korea missile launch by January 31?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `696e274d183bed0068c24d04`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-31`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-31 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "North Korea missile launch by January 31? (resolved around 2026-01-31 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Yes} or \boxed{No}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v13ra_012 — Bitcoin below $82K in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69590c18deacd00066876764`
- Category: `crypto_binary`
- Pattern: `binary`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{Yes}",
  "answer_tokens": [
    "Yes"
  ]
}
```

## v14ga_0109 — Nicolás Maduro released from custody by...?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6968e150e7876e006835e6dc`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-31`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-01-31 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Nicolás Maduro released from custody by...? (resolved around 2026-01-31 (GMT+8)). 
A. the outcome be Nicolás Maduro released from custody by December 31, 2026?
B. the outcome be Nicolás Maduro released from custody by January 9, 2026?
C. the outcome be Nicolás Maduro released from custody by January 31, 2026?"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{None of the above}",
  "answer_tokens": [
    "None of the above"
  ]
}
```

## v14ga_0110 — Will something CRAZY happen in January (again)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695baf2f8b62560069adcdd8`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will something CRAZY happen in January (again)? (resolved around 2026-02-01 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Yes} or \boxed{No}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0111 — Kings vs. Hurricanes

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `696e274d183bed0068c24cfd`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-02`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-02 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Kings vs. Hurricanes (resolved around 2026-02-02 (GMT+8)). "
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{Kings} or \boxed{Hurricanes}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Hurricanes}",
  "answer_tokens": [
    "Hurricanes"
  ]
}
```

## v14ga_0112 — Al Fateh Saudi Club vs. Al Hazem SC

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `696cd5b0a4b036005c06a931`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-02`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-02 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Al Fateh Saudi Club vs. Al Hazem SC (resolved around 2026-02-02 (GMT+8)). 
A. Al Fateh Saudi Club win on 2026-02-01
B. Al Fateh Saudi Club vs. Al Hazem SC end in a draw
C. Al Hazem SC win on 2026-02-01"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0113 — CA Tucumán vs. CA Huracán

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69721bc011cfd200699764d5`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-01`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-01 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "CA Tucumán vs. CA Huracán (resolved around 2026-02-01 (GMT+8)). 
A. CA Tucumán win on 2026-01-31
B. CA Tucumán vs. CA Huracán end in a draw
C. CA Huracán win on 2026-01-31"
IMPORTANT: Your final answer MUST end with this exact format:

Your task is to identify all the correct option(s) based on your analysis.
Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
Your final answer MUST end with this exact format:
listing all correct option(s) you have identified, separated by commas, within the box.
For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 

Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0114 — 2026-01-30, what will be the movies ranked from 4 to 6 on the latest weekly word-of-mouth movie ranking (一周口碑电影榜) published by Douban (豆瓣)? (Give the movie titles only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685146342537419957469184`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-01-30`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-01-30 00:00:00`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-01-30, what will be the movies ranked from 4 to 6 on the latest weekly word-of-mouth movie ranking (一周口碑电影榜) published by Douban (豆瓣)? (Give the movie titles only)"
IMPORTANT: Your final answer MUST end with this exact format:
\boxed{YOUR_PREDICTION}
Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{翠湖, 密探, 奥利维娅与云}",
  "answer_tokens": [
    "翠湖",
    "密探",
    "奥利维娅与云"
  ]
}
```

## v14ga_0115 — Who will win Super Bowl LX MVP?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6972189f11cfd20069976499`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-10`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-10`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win Super Bowl LX MVP? (resolved around 2026-02-10 (GMT+8)). 
A.  the outcome be Matthew Stafford
B.  the outcome be Sam Darnold
C.  the outcome be Drake Maye
D.  the outcome be Jaxon Smith-Njigba
E.  the outcome be Puka Nacua
F.  the outcome be Stefon Diggs
G.  the outcome be Davante Adams
H.  the outcome be Rashid Shaheed
I.  the outcome be Jarrett Stidham
J.  the outcome be Other"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0116 — Which NBA players will be traded during the 2025-26 season before the Feb. 5 Trade Deadline?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695fa38ae56c28005d3c3245`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-05`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-05`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which NBA players will be traded during the 2025-26 season before the Feb. 5 Trade Deadline? (resolved around 2026-02-05 (GMT+8)). 
A.  the outcome be Trae Young
B.  the outcome be Jonathan Kuminga
C.  the outcome be Michael Porter Jr.
D.  the outcome be Zach LaVine
E.  the outcome be Giannis Antetokounmpo
F.  the outcome be Ja Morant
G.  the outcome be Bennedict Mathurin
H.  the outcome be Coby White
I.  the outcome be Anthony Davis
J.  the outcome be Malik Monk
K.  the outcome be Anfernee Simons
L.  the outcome be Domantas Sabonis
M.  the outcome be Lauri Markkanen
N.  the outcome be Ivica Zubac"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D, E, F, G}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G"
  ]
}
```

## v14ga_0117 — Which companies will run ads during Super Bowl LX?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69624695e87498005daa01da`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which companies will run ads during Super Bowl LX? (resolved around 2026-02-09 (GMT+8)). 
A.  the outcome be Robinhood
B.  the outcome be Google
C.  the outcome be Amazon
D.  the outcome be Hyundai
E.  the outcome be Toyota
F.  the outcome be Salesforce
G.  the outcome be Verizon/Visible
H.  the outcome be Progressive
I.  the outcome be OpenAI
J.  the outcome be State Farms
K.  the outcome be Coca Cola
L.  the outcome be Coinbase
M.  the outcome be Apple
N.  the outcome be Crypto.com"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D"
  ]
}
```

## v14ga_0118 — Who will make an appearance at the Super Bowl halftime show? Super Bowl LX

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69624695e87498005daa01e5`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-10`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-10`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will make an appearance at the Super Bowl halftime show? Super Bowl LX (resolved around 2026-02-10 (GMT+8)). 
A.  the outcome be J Balvin
B.  the outcome be Cardi B
C.  the outcome be E-40
D.  the outcome be Daddy Yankee
E.  the outcome be Fat Joe
F.  the outcome be Karol G
G.  the outcome be Ricky Martin
H.  the outcome be Taylor Swift
I.  the outcome be Pitbull
J.  the outcome be No Guest"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D"
  ]
}
```

## v14ga_0119 — Most streamed album of 2025

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69624695e87498005daa01db`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Most streamed album of 2025 (resolved around 2026-02-09 (GMT+8)). 
A.  the outcome be 'The Life of a Showgirl' by Taylor Swift
B.  the outcome be 'Debí Tirar Más Fotos' by Bad Bunny
C.  the outcome be 'I'm the Problem' by Morgan Wallen
D.  the outcome be KPop Demon Hunters Soundtrack
E.  the outcome be Other"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0120 — Who will win the Masters section of the 2026 Tata Steel Chess Tournament?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695e521c255b39006c58f5b8`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-06`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-06`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the Masters section of the 2026 Tata Steel Chess Tournament? (resolved around 2026-02-06 (GMT+8)). 
A.  the outcome be Nodirbek Abdusattorov
B.  the outcome be Javokhir Sindarov
C.  the outcome be Jorden van Foreest
D.  the outcome be Matthias Bluebaum
E.  the outcome be Hans Niemann"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0121 — Best New Artist at the 2026 Grammy Awards?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6963980f5a6f9800684ed67f`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-10`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-10`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Best New Artist at the 2026 Grammy Awards? (resolved around 2026-02-10 (GMT+8)). 
A.  the outcome be Olivia Dean
B.  the outcome be Katseye
C.  the outcome be The Marias
D.  the outcome be Addison Rae
E.  the outcome be Sombr
F.  the outcome be Leon Thomas
G.  the outcome be Alex Warren
H.  the outcome be Lola Young"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0122 — What will the percentage of positive reviews on Highguard be by Feb 9th?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6978b00cedd409005eef0fd0`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will the percentage of positive reviews on Highguard be by Feb 9th? (resolved around 2026-02-09 (GMT+8)). 
A.  the outcome be 0 - 9.99%
B.  the outcome be 10 - 19.99%
C.  the outcome be 20 - 29.99%
D.  the outcome be 30 - 39.99%
E.  the outcome be 40 - 49.99%
F.  the outcome be 50 - 59.99%
G.  the outcome be 60 - 69.99%
H.  the outcome be 70 - 79.99%
I.  the outcome be 80 - 89.99%"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0123 — For which team will Giannis Antetokounmpo play for after the 2026 trade deadline?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697b53276346c0006551acac`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-07`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-07`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "For which team will Giannis Antetokounmpo play for after the 2026 trade deadline? (resolved around 2026-02-07 (GMT+8)). 
A.  the outcome be Milwaukee Bucks (no trade)
B.  the outcome be Golden State Warriors
C.  the outcome be New York Knicks
D.  the outcome be Miami Heat
E.  the outcome be Atlanta Hawks
F.  the outcome be Other
G.  the outcome be Detroit Pistons
H.  the outcome be San Antonio Spurs
I.  the outcome be Houston Rockets
J.  the outcome be Los Angeles Lakers
K.  the outcome be Boston Celtics
L.  the outcome be Brooklyn Nets
M.  the outcome be Los Angeles Clippers
N.  the outcome be Phoenix Suns"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0124 — Which team will be the 2026 Super Bowl Champion?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69624695e87498005daa01d9`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which team will be the 2026 Super Bowl Champion? (resolved around 2026-02-09 (GMT+8)). 
A.  the outcome be Seattle Seahawks
B.  the outcome be Los Angeles Rams
C.  the outcome be Denver Broncos
D.  the outcome be Philadelphia Eagles
E.  the outcome be New England Patriots
F.  the outcome be Buffalo Bills
G.  the outcome be Jacksonville Jaguars
H.  the outcome be Houston Texans
I.  the outcome be San Francisco 49ers
J.  the outcome be Green Bay Packers
K.  the outcome be Los Angeles Chargers
L.  the outcome be Chicago Bears
M.  the outcome be Pittsburgh Steelers
N.  the outcome be Other"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0125 — SUPER BOWL STATS PREDICTIONS

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69775e8a96e2d900674cdd58`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "SUPER BOWL STATS PREDICTIONS (resolved around 2026-02-09 (GMT+8)). 
A.  the outcome be 5+ sacks
B.  the outcome be Completed FG over 50 yards
C.  the outcome be 6+ Touchdowns
D.  the outcome be Seahawks have longest punt
E.  the outcome be Patriots have longest kickoff return
F.  the outcome be 2+ fumbles
G.  the outcome be 2+ missed FGs / extra points"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C}",
  "answer_tokens": [
    "A",
    "B",
    "C"
  ]
}
```

## v14ga_0126 — Who will win the 2026 Superbowl?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69663b097dc80a005b6df1d4`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the 2026 Superbowl? (resolved around 2026-02-09 (GMT+8)). 
A.  the outcome be Chicago Bears
B.  the outcome be New England Patriots
C.  the outcome be San Fransisco 49ers
D.  the outcome be Denver Broncos
E.  the outcome be Buffalo Bills
F.  the outcome be Houston Texans
G.  the outcome be Pittsburg Steelers
H.  the outcome be Seattle Seahawks
I.  the outcome be Los Angels Rams
J.  the outcome be Other"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0127 — How many jobs added in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697761c796e2d900674cdd5f`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-06`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-06`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "How many jobs added in January? (resolved around 2026-02-06 (GMT+8)). 
A.  the US add between 75k and 100k jobs in January
B.  the US add between 100k and 125k jobs in January
C.  the US add more than 125k jobs in January
D.  the US add between 25k and 50k jobs in January
E.  the US lose jobs in January
F.  the US add between 0 and 25k jobs in January
G.  the US add between 50k and 75k jobs in January"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0128 — What is the highest Sharpe ratio of any Manifold user?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69624695e87498005daa01ea`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What is the highest Sharpe ratio of any Manifold user? (resolved around 2026-02-08 (GMT+8)). 
A.  the outcome be Below 5
B.  the outcome be 5 - 7.4
C.  the outcome be 7.5 - 9.9
D.  the outcome be 10 - 12.4
E.  the outcome be 12.5 - 14.9
F.  the outcome be 15 - 17.4
G.  the outcome be 17.5 - 20
H.  the outcome be Above 20"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{H}",
  "answer_tokens": [
    "H"
  ]
}
```

## v14ga_0129 — Who will win NFL Coach of the Year?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69736a06e543cb005f7b9363`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-06`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-06`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win NFL Coach of the Year? (resolved around 2026-02-06 (GMT+8)). 
A.  the outcome be Mike Vrabel (New England Patriots)
B.  the outcome be Ben Johnson (Chicago Bears)
C.  the outcome be Liam Coen (Jacksonville Jaguars)
D.  the outcome be Mike Macdonald (Seattle Seahawks)
E.  the outcome be Kyle Shanahan (San Francisco 49ers)
F.  the outcome be Sean Payton (Denver Broncos)
G.  the outcome be Other"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0130 — チームみらいが衆院選で獲得する議席数は？(How many seats will Team Mirai win in the Feb 2026 Japan lower house election?)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697b53276346c0006551acaa`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "チームみらいが衆院選で獲得する議席数は？(How many seats will Team Mirai win in the Feb 2026 Japan lower house election?) (resolved around 2026-02-08 (GMT+8)). 
A.  the outcome be 0～2
B.  the outcome be 3
C.  the outcome be 4
D.  the outcome be 5
E.  the outcome be 6
F.  the outcome be 7+"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0131 — Who will perform at the Super Bowl LX halftime show?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69624695e87498005daa01e8`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-10`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-10`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will perform at the Super Bowl LX halftime show? (resolved around 2026-02-10 (GMT+8)). 
A.  the outcome be Bad Bunny
B.  the outcome be Cardi B
C.  the outcome be Dua Lipa
D.  the outcome be Post Malone
E.  the outcome be Justin Bieber
F.  the outcome be Miley Cyrus
G.  the outcome be Metallica
H.  the outcome be Sabrina Carpenter
I.  the outcome be Morgan Wallen
J.  the outcome be Taylor Swift
K.  the outcome be Chappell Roan
L.  the outcome be Christina Aguilera
M.  the outcome be Jay-Z"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0132 — Who will win the NFL Most Valuable Player Award for the 2025 season?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6962468be87498005daa01c6`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-06`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-06`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the NFL Most Valuable Player Award for the 2025 season? (resolved around 2026-02-06 (GMT+8)). 
A.  the outcome be Josh Allen
B.  the outcome be Sam Darnold
C.  the outcome be Jordan Love
D.  the outcome be Drake Maye
E.  the outcome be Dak Prescott
F.  the outcome be Matthew Stafford
G.  the outcome be Caleb Williams
H.  the outcome be Someone else"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0133 — Who will win the Democratic Party primary for New Jersey's 11th Congressional District special election in 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `696f75a7e146ce005dcc46c6`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-06`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-06`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the Democratic Party primary for New Jersey's 11th Congressional District special election in 2026? (resolved around 2026-02-06 (GMT+8)). 
A.  the outcome be Brendan Gill
B.  the outcome be Analilia Mejia
C.  the outcome be Tom Malinowski
D.  the outcome be Tahasha Way
E.  the outcome be Someone else"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0134 — Which party will win Thailand’s legislative election?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697a01aaaaa579005fb3a51b`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which party will win Thailand’s legislative election? (resolved around 2026-02-08 (GMT+8)). 
A.  the outcome be People's Party (PPLE)
B.  the outcome be Bhumjaithai Party (BJT)
C.  the outcome be Pheu Thai Party (PTP)
D.  the outcome be Democrat Party (DP)"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0135 — United Rugby Championship: Ospreys vs Dragons

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697761c796e2d900674cdd7a`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "United Rugby Championship: Ospreys vs Dragons (resolved around 2026-02-08 (GMT+8)). 
A.  the match end in a draw
B.  Ospreys win
C.  Dragons win"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0136 — Who will win Jet Lag: The Game Season 16?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6956690c20a2e600672a7872`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-06`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-06`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win Jet Lag: The Game Season 16? (resolved around 2026-02-06 (GMT+8)). 
A.  the outcome be Sam
B.  the outcome be Ben
C.  the outcome be Adam"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0137 — United Rugby Championship: Leinster vs Edinburgh

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697761c796e2d900674cdd7e`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "United Rugby Championship: Leinster vs Edinburgh (resolved around 2026-02-08 (GMT+8)). 
A.  Leinster win
B.  Edinburgh win
C.  the match end in a draw"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0138 — Will Indiana change its congressional voting map for the 2026 elections?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6963980d5a6f9800684ed66b`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-06`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-06`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Indiana change its congressional voting map for the 2026 elections? (resolved around 2026-02-06 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v13ra_004 — At close of business on 5 February 2026, will the most recently announced European Central Bank (ECB) "Deposit facility" interest rate be lower, the same, or higher than it was at close of business on 18 December 2025?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6962468be87498005daa01c4`
- Category: `central_bank_decision`
- Pattern: `winner market`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{B}",
  "answer_tokens": [
    "B"
  ]
}
```

## v14ga_0140 — United Rugby Championship: Ulster vs Cardiff Rugby

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697761c796e2d900674cdd79`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "United Rugby Championship: Ulster vs Cardiff Rugby (resolved around 2026-02-08 (GMT+8)). 
A.  the match end in a draw
B.  Ulster win
C.  Cardiff Rugby win"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0141 — Will Dave Cole get angry at any KOH 26 Driver's meetings?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6974bba3b31670005dd8d70f`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Dave Cole get angry at any KOH 26 Driver's meetings? (resolved around 2026-02-09 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0142 — A team from the NFC West will win Super Bowl LX

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695e521c255b39006c58f5ae`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "A team from the NFC West will win Super Bowl LX (resolved around 2026-02-09 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0143 — Manchester City FC vs Newcastle United FC

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6976134126a255005c46be44`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-05`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-05`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Manchester City FC vs Newcastle United FC (resolved around 2026-02-05 (GMT+8)). 
A.  Newcastle United FC win on 2026-02-04
B.  Manchester City FC win on 2026-02-04
C.  Manchester City FC vs. Newcastle United FC end in a draw"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0144 — Top 14: Racing 92 vs Perpignan

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `696e274d183bed0068c24d11`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Top 14: Racing 92 vs Perpignan (resolved around 2026-02-08 (GMT+8)). 
A.  Racing 92 win
B.  the match end in a draw
C.  Perpignan win"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0145 — Transgender women be banned from the Olympics before Winter Games?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `695bb4008b62560069adcdeb`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-05`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-05`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Transgender women be banned from the Olympics before Winter Games? (resolved around 2026-02-05 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0146 — United Rugby Championship: Glasgow Warriors vs Munster

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697761c796e2d900674cdd7d`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-07`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-07`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "United Rugby Championship: Glasgow Warriors vs Munster (resolved around 2026-02-07 (GMT+8)). 
A.  Glasgow Warriors win
B.  Munster win
C.  the match end in a draw"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0147 — Will Gustavo Petro stay in the U.S. longer than 5 consecutive days starting Feb 3, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697a0186aaa579005fb3a50c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-10`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-10`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Gustavo Petro stay in the U.S. longer than 5 consecutive days starting Feb 3, 2026? (resolved around 2026-02-10 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0148 — Will the Seahawks beat the Patriots in the 2026 Superbowl?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69775e8a96e2d900674cdd4a`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will the Seahawks beat the Patriots in the 2026 Superbowl? (resolved around 2026-02-09 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0149 — West Bromwich Albion FC vs. Stoke City FC

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6978b359edd409005eef0fe2`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "West Bromwich Albion FC vs. Stoke City FC (resolved around 2026-02-08 (GMT+8)). 
A.  West Bromwich Albion FC win on 2026-02-07
B.  West Bromwich Albion FC vs. Stoke City FC end in a draw
C.  Stoke City FC win on 2026-02-07"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0150 — Preston North End FC vs. Portsmouth FC

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6978b359edd409005eef0fe3`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Preston North End FC vs. Portsmouth FC (resolved around 2026-02-08 (GMT+8)). 
A.  Preston North End FC win on 2026-02-07
B.  Preston North End FC vs. Portsmouth FC end in a draw
C.  Portsmouth FC win on 2026-02-07"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0151 — Querétaro FC vs. Club León FC

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697a04c5aaa579005fb3a538`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Querétaro FC vs. Club León FC (resolved around 2026-02-08 (GMT+8)). 
A.  Querétaro FC vs. Club León FC end in a draw
B.  Club León FC win on 2026-02-07
C.  Querétaro FC win on 2026-02-07"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0152 — 2026-02-05, who will be the athletes ranked from 10 to 12 in the latest World Athletics men's triple jump rankings? (Give the names only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `687756de9a85d40047c45626`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-05`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-05`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-02-05, who will be the athletes ranked from 10 to 12 in the latest World Athletics men's triple jump rankings? (Give the names only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Jonathan SEREMES, Thomas GOGOIS, Wen SU}",
  "answer_tokens": [
    "Jonathan SEREMES",
    "Thomas GOGOIS",
    "Wen SU"
  ]
}
```

## v14ga_0153 — 2026-02-05, who will be the athletes ranked from 12 to 14 in the latest World Athletics women's 200m rankings? (Give the names only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `686794c85407dd00602c1f79`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-05`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-05`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-02-05, who will be the athletes ranked from 12 to 14 in the latest World Athletics women's 200m rankings? (Give the names only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Ashanti MOORE, Jaël BESTUÉ, JaMeesia FORD}",
  "answer_tokens": [
    "Ashanti MOORE",
    "Jaël BESTUÉ",
    "JaMeesia FORD"
  ]
}
```

## v14ga_0154 — 2026-02-05, what will be the Agricultural Product Wholesale Price 200 Index (农产品批发价格200指数) monitored by China's National Agricultural Product Wholesale Market Price Information System (全国农产品批发市场价格信息系统)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6851735859f71f006037a1e2`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-02-05`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-02-05`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-02-05, what will be the Agricultural Product Wholesale Price 200 Index (农产品批发价格200指数) monitored by China's National Agricultural Product Wholesale Market Price Information System (全国农产品批发市场价格信息系统)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{129.83}",
  "answer_tokens": [
    "129.83"
  ]
}
```

## v14ga_0155 — Who will win the 2026 Prague Masters chess tournament?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `696b872b4a95de00666c1162`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the 2026 Prague Masters chess tournament? (resolved around 2026-03-08 (GMT+8)). 
A.  the outcome be Nodirbek Abdusattorov
B.  the outcome be Jorden van Foreest
C.  the outcome be Vincent Keymer
D.  the outcome be Gukesh Dommaraju
E.  the outcome be Nodirbek Yakubboev
F.  the outcome be David Navara OR David Antón Guijarro
G.  the outcome be Hans Niemann
H.  the outcome be Aravindh Chithambaram
I.  the outcome be Parham Maghsoodloo"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0156 — Which New York Rangers will be traded by the 2026 trade deadline?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69833c21c6c07e005d385694`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-07`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-07`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which New York Rangers will be traded by the 2026 trade deadline? (resolved around 2026-03-07 (GMT+8)). 
A.  the outcome be Vincent Trocheck
B.  the outcome be Brennan Othmann
C.  the outcome be Alexis Lafrenière
D.  the outcome be Carson Soucy
E.  the outcome be Mika Zibanejad"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C}",
  "answer_tokens": [
    "A",
    "B",
    "C"
  ]
}
```

## v14ga_0157 — Big East Men's College Basketball 2025-2026 Regular Season Champion

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6984912ec68c5e005dc9d05c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-07`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-07`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Big East Men's College Basketball 2025-2026 Regular Season Champion (resolved around 2026-03-07 (GMT+8)). 
A.  Butler win the 2025-2026 Big East Men’s Basketball regular season championship
B.  DePaul win the 2025-2026 Big East Men’s Basketball regular season championship
C.  Marquette win the 2025-2026 Big East Men’s Basketball regular season championship
D.  Seton Hall win the 2025-2026 Big East Men’s Basketball regular season championship
E.  UConn win the 2025-2026 Big East Men’s Basketball regular season championship
F.  Xavier win the 2025-2026 Big East Men’s Basketball regular season championship
G.  Creighton win the 2025-2026 Big East Men’s Basketball regular season championship
H.  Georgetown win the 2025-2026 Big East Men’s Basketball regular season championship
I.  Providence win the 2025-2026 Big East Men’s Basketball regular season championship
J.  St. John’s win the 2025-2026 Big East Men’s Basketball regular season championship
K.  Villanova win the 2025-2026 Big East Men’s Basketball regular season championship
L.  another team win the 2025-2026 Big East Men’s Basketball regular season championship"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{J}",
  "answer_tokens": [
    "J"
  ]
}
```

## v14ga_0158 — Nepal House of Representatives Election winner?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6989d39ba7590900681117ad`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-10`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-10`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Nepal House of Representatives Election winner? (resolved around 2026-03-10 (GMT+8)). 
A.  the outcome be Nepali congress
B.  the outcome be CPN-UML
C.  the outcome be RSP
D.  the outcome be RPP
E.  the outcome be Other"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0159 — Team of winning driver at Australian Grand Prix?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698b2b1f175d470068538759`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-10`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-10`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Team of winning driver at Australian Grand Prix? (resolved around 2026-03-10 (GMT+8)). 
A.  the outcome be McLaren
B.  the outcome be Mercedes
C.  the outcome be Ferrari
D.  the outcome be Other"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0160 — Ratio of sixes to fours in T20 World Cup 2026

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a03d178110930068600600`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-10`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-10`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Ratio of sixes to fours in T20 World Cup 2026 (resolved around 2026-03-10 (GMT+8)). 
A.  the outcome be Below 0.45
B.  the outcome be 0.45 - 0.49
C.  the outcome be 0.50 - 0.54
D.  the outcome be Above 0.55"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0161 — Will James Talarico win the Texas Democratic primary for se by....?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a18e890ff98b0068330737`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-06`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-06`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will James Talarico win the Texas Democratic primary for se by....? (resolved around 2026-03-06 (GMT+8)). 
A.  the outcome be 2.000% or more?
B.  the outcome be 4.000% or more?
C.  the outcome be 6.000% or more?
D.  the outcome be 7.00% or more?
E.  the outcome be 8.00% or more?
F.  the outcome be 10.00% or more?
G.  the outcome be 12.00% or more?"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D"
  ]
}
```

## v14ga_0162 — When will Dubai airport resume normal operations

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a4319df2cb3b006875e9cb`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "When will Dubai airport resume normal operations (resolved around 2026-03-08 (GMT+8)). 
A.  the outcome be March 2 or earlier
B.  the outcome be March 3 or 4
C.  the outcome be March 5 or 6
D.  the outcome be March 7 or later"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0163 — In what place will the Green Party (Bündnis 90/Die Grünen, or the Greens) rank in seats won in the 2026 Baden-Württemberg Landtag (state parliament) elections?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698b2507175d47006853871e`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "In what place will the Green Party (Bündnis 90/Die Grünen, or the Greens) rank in seats won in the 2026 Baden-Württemberg Landtag (state parliament) elections? (resolved around 2026-03-09 (GMT+8)). 
A.  the outcome be First
B.  the outcome be Second
C.  the outcome be Third
D.  the outcome be Fourth or lower"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v13ra_013 — Between 10 October 2025 and 6 March 2026, what will be the lowest closing price of soybeans?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698b2507175d47006853871d`
- Category: `agriculture_bucket`
- Pattern: `interval bin`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{E}",
  "answer_tokens": [
    "E"
  ]
}
```

## v14ga_0165 — Which party will win Colombia’s Chamber of Representatives election?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697f47970092a00068c32be3`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which party will win Colombia’s Chamber of Representatives election? (resolved around 2026-03-09 (GMT+8)). 
A.  the outcome be Pacto Histórico (PH)
B.  the outcome be Partido Liberal Colombiano (PLC)
C.  the outcome be Centro Democrático (CD)
D.  the outcome be Partido Conservador Colombiano"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v13ra_014 — Will global platinum availability fall below 2 million ounces by March 4, 2026, due to South African mine supply issues?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6981ea9930057a005cdb9e46`
- Category: `supply_shock_binary`
- Pattern: `binary`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{No}",
  "answer_tokens": [
    "No"
  ]
}
```

## v14ga_0167 — Brazil in the top 10-20% countries in the 2026 Democracy Report ranking?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6964e98652029b005bc009a2`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-10`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-10`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Brazil in the top 10-20% countries in the 2026 Democracy Report ranking? (resolved around 2026-03-10 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0168 — Will the Nepali Congress party win the most seats in the 2026 Nepali House of Representatives elections?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698b2507175d47006853871b`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-06`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-06`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will the Nepali Congress party win the most seats in the 2026 Nepali House of Representatives elections? (resolved around 2026-03-06 (GMT+8)). 
A.  the outcome be Yes
B.  the outcome be No
C.  the outcome be Another outcome"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0169 — Is the shrinking cut-off in Diamond League fully intentional?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6981ea9930057a005cdb9e49`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-05`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-05`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Is the shrinking cut-off in Diamond League fully intentional? (resolved around 2026-03-05 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0170 — Will Nornickel's palladium production fall below 2.4 million ounces in 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6981ea9930057a005cdb9e47`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-05`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-05`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Nornickel's palladium production fall below 2.4 million ounces in 2026? (resolved around 2026-03-05 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0171 — Which party will win Colombia’s Senate election?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `697f47970092a00068c32be2`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which party will win Colombia’s Senate election? (resolved around 2026-03-09 (GMT+8)). 
A.  the outcome be Pacto Histórico (PH)
B.  the outcome be Centro Democrático (CD)
C.  the outcome be Alianza Verde / Coalición Centro Esperanza (AV/CCE)"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0172 — Before 7 March 2026, will an NHL team other than the Pittsburgh Penguins publicly announce or acknowledge that Sidney Crosby will join its roster as a player eligible for the playoffs of the 2025/26 NHL season?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698b2507175d47006853871c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-07`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-03-07`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Before 7 March 2026, will an NHL team other than the Pittsburgh Penguins publicly announce or acknowledge that Sidney Crosby will join its roster as a player eligible for the playoffs of the 2025/26 NHL season? (resolved around 2026-03-07 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0173 — Will a NON mercedes engine car win the 2026 Formula 1 Australian Grand Prix?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6987308956940e0068395804`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will a NON mercedes engine car win the 2026 Formula 1 Australian Grand Prix? (resolved around 2026-03-08 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0174 — Ecuador to improve its score in the 2026 Democracy Report ranking?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6964e98652029b005bc009a4`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-10`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-10`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Ecuador to improve its score in the 2026 Democracy Report ranking? (resolved around 2026-03-10 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0175 — Trump Sucks?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a2e0165692ef005cdbf23e`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Trump Sucks? (resolved around 2026-03-08 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0176 — Can this AI Trading Bot turn $100 into $1,000 live on Twitch? Round 1

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a4319df2cb3b006875e9c2`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Can this AI Trading Bot turn $100 into $1,000 live on Twitch? Round 1 (resolved around 2026-03-08 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0177 — China's monthly consumer inflation (CPI) greater than 0.2% in February?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698f1987da7a8b006575442d`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "China's monthly consumer inflation (CPI) greater than 0.2% in February? (resolved around 2026-03-08 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0178 — Will this market get between 35 and 55 traders?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a03d1781109300686005e1`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-05`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-05`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will this market get between 35 and 55 traders? (resolved around 2026-03-05 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0179 — Will Tiger Zhang finish problem set 2 for 18.905 on time?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `699d9a1a098cca008728b6d1`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-06`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-06`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Tiger Zhang finish problem set 2 for 18.905 on time? (resolved around 2026-03-06 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0180 — Luke Fernandez vs. Rodolfo Bellato

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a43186f2cb3b006875e9ad`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Luke Fernandez vs. Rodolfo Bellato (resolved around 2026-03-08 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Luke Fernandez} or \boxed{Rodolfo Bellato}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Rodolfo Bellato}",
  "answer_tokens": [
    "Rodolfo Bellato"
  ]
}
```

## v14ga_0181 — Alberto Montes vs. Ricky Turcios

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a43186f2cb3b006875e9b1`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-08`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-08`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Alberto Montes vs. Ricky Turcios (resolved around 2026-03-08 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Alberto Montes} or \boxed{Ricky Turcios}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Ricky Turcios}",
  "answer_tokens": [
    "Ricky Turcios"
  ]
}
```

## v14ga_0182 — 2026-03-09, what will be the top-ranked short drama on the short drama hot list (短剧热度榜) of this date published by BiaNews (鞭牛士)? (Give the drama name only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `68774dbf27798c003c8a0dce`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-09`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-09`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-09, what will be the top-ranked short drama on the short drama hot list (短剧热度榜) of this date published by BiaNews (鞭牛士)? (Give the drama name only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{《金丝玉髓羹》}",
  "answer_tokens": [
    "《金丝玉髓羹》"
  ]
}
```

## v14ga_0183 — How many Oscars will "Sinners" win?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698dd05b7812fd005da4275d`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "How many Oscars will "Sinners" win? (resolved around 2026-03-15 (GMT+8)). 
A.  "Sinners" win 3 or fewer awards at the Oscars
B.  "Sinners" win exactly 7 awards at the Oscars
C.  "Sinners" win exactly 4 awards at the Oscars
D.  "Sinners" win exactly 8 awards at the Oscars
E.  "Sinners" win exactly 5 awards at the Oscars
F.  "Sinners" win exactly 9 awards at the Oscars
G.  "Sinners" win exactly 6 awards at the Oscars
H.  "Sinners" win 10 or more awards at the Oscars"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0184 — How many Oscars will "One Battle After Another" win?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698dd05b7812fd005da4275c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "How many Oscars will "One Battle After Another" win? (resolved around 2026-03-15 (GMT+8)). 
A.  "One Battle After Another" win 3 or fewer awards at the Oscars
B.  "One Battle After Another" win exactly 4 awards at the Oscars
C.  "One Battle After Another" win exactly 5 awards at the Oscars
D.  "One Battle After Another" win exactly 6 awards at the Oscars
E.  "One Battle After Another" win exactly 7 awards at the Oscars
F.  "One Battle After Another" win exactly 8 awards at the Oscars
G.  "One Battle After Another" win exactly 9 awards at the Oscars
H.  "One Battle After Another" win 10 or more awards at the Oscars"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{D}",
  "answer_tokens": [
    "D"
  ]
}
```

## v14ga_0185 — How many seats will Partido Popular win in the Castilla y Leon election?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698dd05b7812fd005da4276a`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "How many seats will Partido Popular win in the Castilla y Leon election? (resolved around 2026-03-15 (GMT+8)). 
A.  Partido Popular win <28 seats in the 2026 Castilla y León regional election
B.  Partido Popular win 28-31 seats in the 2026 Castilla y León regional election
C.  Partido Popular win 32-35 seats in the 2026 Castilla y León regional election
D.  Partido Popular win 36-39 seats in the 2026 Castilla y León regional election
E.  Partido Popular win 40-43 seats in the 2026 Castilla y León regional election
F.  Partido Popular win 44+ seats in the 2026 Castilla y León regional election
G.  the results be unknown by July 30 2026, 11:59 PM ET (resolving to Other)"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C, G}",
  "answer_tokens": [
    "C",
    "G"
  ]
}
```

## v14ga_0186 — How many Oscars will "Marty Supreme" win?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698dd05b7812fd005da4275a`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "How many Oscars will "Marty Supreme" win? (resolved around 2026-03-15 (GMT+8)). 
A.  "Marty Supreme" win exactly 3 awards at the Oscars
B.  "Marty Supreme" win exactly 5 awards at the Oscars
C.  "Marty Supreme" win 6 or more awards at the Oscars
D.  "Marty Supreme" win no awards at the Oscars
E.  "Marty Supreme" win exactly 1 award at the Oscars
F.  "Marty Supreme" win exactly 2 awards at the Oscars
G.  "Marty Supreme" win exactly 4 awards at the Oscars"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0187 — Who will win the 2026 BNP Paribas Open (Indian Wells WTA 1000)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69ac1a945b8448005d44c0ab`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the 2026 BNP Paribas Open (Indian Wells WTA 1000)? (resolved around 2026-03-16 (GMT+8)). 
A.  the outcome be Aryna Sabalenka (1)
B.  the outcome be Victoria Mboko (10)
C.  the outcome be Amanda Anisimova (6)
D.  the outcome be Coco Gauff (4)
E.  the outcome be Jessica Pegula (5)
F.  the outcome be Elena Rybakina (3)
G.  the outcome be Iga Swiatek (2)
H.  the outcome be Other"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0188 — Who will win the Women's SVNS Series?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69906b09ffd613006910b808`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the Women's SVNS Series? (resolved around 2026-03-16 (GMT+8)). 
A.  the outcome be Australia
B.  the outcome be Canada
C.  the outcome be Fiji
D.  the outcome be France
E.  the outcome be Great Britain
F.  the outcome be Japan
G.  the outcome be New Zealand
H.  the outcome be United States"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0189 — Which 2026 Oscar winner will have the highest audience tomatometer?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a6d48ee78a390068a1875a`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which 2026 Oscar winner will have the highest audience tomatometer? (resolved around 2026-03-16 (GMT+8)). 
A.  the outcome be KPop Demon Hunters (99% audience score)
B.  the outcome be F1 (97% audience score)
C.  the outcome be Kokuo (97% audience score)
D.  the outcome be Sinners (96% audience score)
E.  the outcome be Frankenstein (94% audience score)
F.  the outcome be Sentimental Value (94% audience score)
G.  the outcome be Hamnet (93% audience score)
H.  the outcome be Train Dreams (90% audience score)"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0190 — Best International Feature winner? (2026 Oscars)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698f198bda7a8b006575445f`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Best International Feature winner? (2026 Oscars) (resolved around 2026-03-15 (GMT+8)). 
A.  the outcome be Sentimental Value
B.  the outcome be The Secret Agent
C.  the outcome be It Was Just an Accident
D.  the outcome be Sirat
E.  the outcome be The Voice of Hind Rajab"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0191 — Best Lead Actress winner? (2026 Oscars)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698f198bda7a8b0065754455`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Best Lead Actress winner? (2026 Oscars) (resolved around 2026-03-15 (GMT+8)). 
A.  the outcome be Jessie Buckley - Hamnet
B.  the outcome be Rose Byrne - If I Had Legs I'd Kick You
C.  the outcome be Kate Hudson - Song Sung Blue
D.  the outcome be Renate Reinsve - Sentimental Value
E.  the outcome be Emma Stone - Bugonia"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0192 — Which movies will win multiple Oscars? (2026)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698f198bda7a8b006575444c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which movies will win multiple Oscars? (2026) (resolved around 2026-03-15 (GMT+8)). 
A.  the outcome be One Battle After Another
B.  the outcome be Sinners
C.  the outcome be Frankenstein
D.  the outcome be KPop Demon Hunters
E.  the outcome be F1
F.  the outcome be Sentimental Value
G.  the outcome be Hamnet
H.  the outcome be Marty Supreme
I.  the outcome be The Secret Agent
J.  the outcome be Avatar: Fire and Ash
K.  the outcome be Train Dreams
L.  the outcome be Bugonia
M.  the outcome be Blue Moon
N.  the outcome be It Was Just An Accident"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{A, B, C, D}",
  "answer_tokens": [
    "A",
    "B",
    "C",
    "D"
  ]
}
```

## v14ga_0193 — Oscars 2026: Best Live Action Short Film Winner

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698dd05b7812fd005da42762`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Oscars 2026: Best Live Action Short Film Winner (resolved around 2026-03-15 (GMT+8)). 
A.  A Friend of Dorothy win Best Live Action Short Film at the 98th Academy Awards
B.  The Singers win Best Live Action Short Film at the 98th Academy Awards
C.  Movie A win Best Live Action Short Film at the 98th Academy Awards
D.  Movie C win Best Live Action Short Film at the 98th Academy Awards
E.  Movie I win Best Live Action Short Film at the 98th Academy Awards
F.  Movie K win Best Live Action Short Film at the 98th Academy Awards
G.  Two People Exchanging Saliva win Best Live Action Short Film at the 98th Academy Awards
H.  Movie E win Best Live Action Short Film at the 98th Academy Awards
I.  another movie win Best Live Action Short Film at the 98th Academy Awards
J.  Jane Austen's Period Drama win Best Live Action Short Film at the 98th Academy Awards
K.  Movie B win Best Live Action Short Film at the 98th Academy Awards
L.  Movie D win Best Live Action Short Film at the 98th Academy Awards
M.  Movie F win Best Live Action Short Film at the 98th Academy Awards
N.  Movie G win Best Live Action Short Film at the 98th Academy Awards
O.  Movie H win Best Live Action Short Film at the 98th Academy Awards
P.  Movie J win Best Live Action Short Film at the 98th Academy Awards
Q.  Butcher's Stain win Best Live Action Short Film at the 98th Academy Awards"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0194 — What will the average score be on the second ECON 1014 exam at the University of Missouri?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a830e529c5bb005eeeb118`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-12`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-12`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "What will the average score be on the second ECON 1014 exam at the University of Missouri? (resolved around 2026-03-12 (GMT+8)). 
A.  the outcome be Above 50
B.  the outcome be Above 55
C.  the outcome be Above 60
D.  the outcome be Above 65
E.  the outcome be Above 70
F.  the outcome be Above 75
G.  the outcome be Above 80"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0195 — Best Casting winner? (2026 Oscars)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698f198bda7a8b0065754457`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Best Casting winner? (2026 Oscars) (resolved around 2026-03-15 (GMT+8)). 
A.  the outcome be Sinners
B.  the outcome be One Battle after Another
C.  the outcome be Marty Supreme
D.  the outcome be The Secret Agent
E.  the outcome be Hamnet"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0196 — IL-08 Democratic Primary Winner

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69906e76ffd613006910b815`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-17`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-17`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "IL-08 Democratic Primary Winner (resolved around 2026-03-17 (GMT+8)). 
A.  Junaid Ahmed be the Democratic Nominee for IL-08
B.  Yasmeen Bankole be the Democratic Nominee for IL-08
C.  Melissa Bean be the Democratic Nominee for IL-08
D.  Sanjyot Dunung be the Democratic Nominee for IL-08
E.  Neil Khot be the Democratic Nominee for IL-08
F.  Kevin Morrison be the Democratic Nominee for IL-08
G.  Dan Tully be the Democratic Nominee for IL-08
H.  Ryan Vetticad be the Democratic Nominee for IL-08
I.  another person be the Democratic Nominee for IL-08
J.  Person A be the Democratic Nominee for IL-08
K.  Person B be the Democratic Nominee for IL-08
L.  Person C be the Democratic Nominee for IL-08
M.  Person D be the Democratic Nominee for IL-08
N.  Person E be the Democratic Nominee for IL-08
O.  Person F be the Democratic Nominee for IL-08
P.  Person G be the Democratic Nominee for IL-08
Q.  Person H be the Democratic Nominee for IL-08
R.  Person I be the Democratic Nominee for IL-08
S.  Person J be the Democratic Nominee for IL-08
T.  Person K be the Democratic Nominee for IL-08
U.  Person L be the Democratic Nominee for IL-08
V.  Person M be the Democratic Nominee for IL-08
W.  Person N be the Democratic Nominee for IL-08
X.  Person O be the Democratic Nominee for IL-08
Y.  Person P be the Democratic Nominee for IL-08
Z.  Person Q be the Democratic Nominee for IL-08
[.  Person R be the Democratic Nominee for IL-08
\.  Person S be the Democratic Nominee for IL-08
].  Person T be the Democratic Nominee for IL-08
^.  Person U be the Democratic Nominee for IL-08
_.  Person V be the Democratic Nominee for IL-08
`.  Person W be the Democratic Nominee for IL-08
a.  Person X be the Democratic Nominee for IL-08
b.  Person Y be the Democratic Nominee for IL-08
c.  Person Z be the Democratic Nominee for IL-08"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0197 — Best Documentary Short winner? (2026 Oscars)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698f198bda7a8b006575444e`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Best Documentary Short winner? (2026 Oscars) (resolved around 2026-03-15 (GMT+8)). 
A.  the outcome be All the Empty Rooms
B.  the outcome be Armed Only with a Camera: The Life and Death of Brent Renaud
C.  the outcome be The Devil Is Busy
D.  the outcome be Perfectly a Strangeness
E.  the outcome be Children No More: "Were and Are Gone""
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0198 — How many Oscars will "Frankenstein" win?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `698dd05b7812fd005da4275b`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "How many Oscars will "Frankenstein" win? (resolved around 2026-03-15 (GMT+8)). 
A.  "Frankenstein" win exactly 5 awards at the Oscars
B.  "Frankenstein" win 6 or more awards at the Oscars
C.  "Frankenstein" win exactly 3 awards at the Oscars
D.  "Frankenstein" win exactly 4 awards at the Oscars
E.  "Frankenstein" win no awards at the Oscars
F.  "Frankenstein" win exactly 1 award at the Oscars
G.  "Frankenstein" win exactly 2 awards at the Oscars"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0199 — Who will win the 2026 BNP Paribas Open (Indian Wells ATP 1000)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6998540873bcba006869e614`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-17`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-17`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the 2026 BNP Paribas Open (Indian Wells ATP 1000)? (resolved around 2026-03-17 (GMT+8)). 
A.  the outcome be Carlos Alcaraz (1)
B.  the outcome be Jannik Sinner (2)
C.  the outcome be Novak Djokovic (3)
D.  the outcome be Alexander Zverev (4)
E.  the outcome be Alex de Minaur (6)
F.  the outcome be Taylor Fritz (7)
G.  the outcome be Félix Auger-Aliassime (8)
H.  the outcome be Other"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0200 — Who will win the 2026 Rugby Europe Championship?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69906b09ffd613006910b80a`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Who will win the 2026 Rugby Europe Championship? (resolved around 2026-03-16 (GMT+8)). 
A.  the outcome be Georgia
B.  the outcome be Portugal
C.  the outcome be Romania
D.  the outcome be Spain
E.  the outcome be Other"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0201 — Which men's basketball team will win in the Southeastern Conference (SEC) Championship tournament in the 2025-26 season?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6995b1073ea64b005b11f288`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which men's basketball team will win in the Southeastern Conference (SEC) Championship tournament in the 2025-26 season? (resolved around 2026-03-15 (GMT+8)). 
A.  the outcome be Alabama
B.  the outcome be Arkansas
C.  the outcome be Auburn
D.  the outcome be Florida
E.  the outcome be Kentucky
F.  the outcome be Ole Miss
G.  the outcome be Tennessee"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0202 — Which men's basketball team will win the Big 12 Conference Championship tournament in the 2025-26 season?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6995b1073ea64b005b11f285`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-14`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-14`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which men's basketball team will win the Big 12 Conference Championship tournament in the 2025-26 season? (resolved around 2026-03-14 (GMT+8)). 
A.  the outcome be Arizona
B.  the outcome be Baylor
C.  the outcome be Brigham Young University (BYU)
D.  the outcome be Houston
E.  the outcome be Iowa State
F.  the outcome be Kansas
G.  the outcome be Kansas State"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0203 — Which men's basketball team will win in the Atlantic Coast Conference (ACC) Championship tournament in the 2025-26 season?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6995b1073ea64b005b11f286`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-14`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-14`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which men's basketball team will win in the Atlantic Coast Conference (ACC) Championship tournament in the 2025-26 season? (resolved around 2026-03-14 (GMT+8)). 
A.  the outcome be Clemson
B.  the outcome be Duke
C.  the outcome be Louisville
D.  the outcome be North Carolina
E.  the outcome be North Carolina State
F.  the outcome be Southern Methodist University (SMU)"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0204 — Which song will win the 2026 Oscar for Best Original Song?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6995b1073ea64b005b11f293`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Which song will win the 2026 Oscar for Best Original Song? (resolved around 2026-03-15 (GMT+8)). 
A.  the outcome be "Dear Me" from "Diane Warren: Relentless"
B.  the outcome be "Golden" from "KPop Demon Hunters"
C.  the outcome be "I Lied to You" from "Sinners"
D.  the outcome be "Sweet Dreams of joy" from "Viva Verdi"
E.  the outcome be "Train Dreams" from "Train Dreams""
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0205 — Brazil's monthly inflation rate in February

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6999a58717d430006670a388`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-12`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-12`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Brazil's monthly inflation rate in February (resolved around 2026-03-12 (GMT+8)). 
A.  the outcome be 0.45 or more
B.  the outcome be Between 0.25 and 0.45
C.  the outcome be More than zero, less than 0.25
D.  the outcome be Zero or less"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0206 — Stock prices on March 13: higher than on March 6?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69aebd8793e1240067e5c00c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-13`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-13`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Stock prices on March 13: higher than on March 6? (resolved around 2026-03-13 (GMT+8)). 
A.  the outcome be Apple Inc. (AAPL)
B.  the outcome be Oracle Corp (ORCL)
C.  the outcome be Tesla, Inc. (TSLA)
D.  the outcome be Nvidia Corporation (NVDA)
E.  the outcome be Amazon.com, Inc. (AMZN)
F.  the outcome be Alphabet Inc. (GOOGL) (Class A stock)
G.  the outcome be Microsoft Corporation (MSFT)"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0207 — Reserve Bank of Australia decision in March?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69906e76ffd613006910b816`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-17`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-17`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Reserve Bank of Australia decision in March? (resolved around 2026-03-17 (GMT+8)). 
A.  the Reserve Bank of Australia make no change to the target for the cash rate after the March Meeting
B.  the Reserve Bank of Australia increase the target for the cash rate after the March Meeting
C.  the Reserve Bank of Australia decrease the target for the cash rate after the March Meeting"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{C}",
  "answer_tokens": [
    "C"
  ]
}
```

## v14ga_0208 — Will the US PCE annual inflation be greater than 2.9% in January?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `699d9ffc098cca008728b6f0`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-13`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-13`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will the US PCE annual inflation be greater than 2.9% in January? (resolved around 2026-03-13 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0209 — Will Teyana Taylor win best supporting actress at OSCAR 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `699d9a1a098cca008728b6df`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Teyana Taylor win best supporting actress at OSCAR 2026? (resolved around 2026-03-16 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0210 — Will foreign airlines resume commercial passenger flights to Aviv (TLV) by March 15, 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a5830b7554ef0068e464be`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `latest_explicit_date_in_prompt`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will foreign airlines resume commercial passenger flights to Aviv (TLV) by March 15, 2026? (resolved around 2026-03-16 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0211 — Mexico City (CDMX) above "Exercise increased caution" trav advisory by mid march?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `699d9a1a098cca008728b6cf`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Mexico City (CDMX) above "Exercise increased caution" trav advisory by mid march? (resolved around 2026-03-16 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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
- Source id: `69a977a47e9d43005df0d703`
- Category: `single_stock_direction`
- Pattern: `binary`
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

Ground truth:
```json
{
  "answer_box": "\\boxed{No}",
  "answer_tokens": [
    "No"
  ]
}
```

## v14ga_0213 — Will there be a ceasefire announced between US/Israel and Iran between 11th and 15th March 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69aebd8a93e1240067e5c02c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will there be a ceasefire announced between US/Israel and Iran between 11th and 15th March 2026? (resolved around 2026-03-16 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0214 — 2026 American Cup chess tournament winner (Open division)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a03d1781109300686005fd`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026 American Cup chess tournament winner (Open division) (resolved around 2026-03-15 (GMT+8)). 
A.  the outcome be Wesley So
B.  the outcome be Fabiano Caruana
C.  the outcome be Levon Aronian"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0215 — Will Marty Supreme win any Oscars in 2026?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69a5830b7554ef0068e464af`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-17`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-17`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Will Marty Supreme win any Oscars in 2026? (resolved around 2026-03-17 (GMT+8)). "
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{Yes} or \boxed{No}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0216 — Deportes Tolima vs. O'Higgins

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69aebd8793e1240067e5c00b`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-12`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-12`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Deportes Tolima vs. O'Higgins (resolved around 2026-03-12 (GMT+8)). 
A.  the outcome be Deportes Tolima
B.  the outcome be Tie
C.  the outcome be O'Higgins"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0217 — Borussia Mönchengladbach vs. St. Pauli

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69aebd8793e1240067e5c019`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-14`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-14`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Borussia Mönchengladbach vs. St. Pauli (resolved around 2026-03-14 (GMT+8)). 
A.  the outcome be Borussia Mönchengladbach
B.  the outcome be Tie
C.  the outcome be St. Pauli"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0218 — Independiente Medellín vs. Juventud

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `69aebd8793e1240067e5c017`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-13`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-13`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "Independiente Medellín vs. Juventud (resolved around 2026-03-13 (GMT+8)). 
A.  the outcome be Independiente Medellín
B.  the outcome be Tie
C.  the outcome be Juventud"
        IMPORTANT: Your final answer MUST end with this exact format:
        
        Your task is to identify all the correct option(s) based on your analysis.
        Your prediction will be scored based on its accuracy. You will only receive points if your answer includes ALL correct options and NO incorrect options. Selecting any wrong option or failing to select all correct options will result in a penalty.
        Your final answer MUST end with this exact format:
        listing all correct option(s) you have identified, separated by commas, within the box.
        For example: \boxed{A} for a single correct option, or \boxed{B, C} for multiple correct options. 
        
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
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

## v14ga_0219 — 2026-03-16, what variety shows will be ranked from 2 to 4 on the latest overseas word-of-mouth variety show ranking (国外口碑综艺榜) published by Douban (豆瓣)? (Give the show names only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `68774eaf0fc811003bd35b6d`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-16, what variety shows will be ranked from 2 to 4 on the latest overseas word-of-mouth variety show ranking (国外口碑综艺榜) published by Douban (豆瓣)? (Give the show names only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{怪奇谜案限时破 第二季, 单身即地狱 第五季, 天机试炼场}",
  "answer_tokens": [
    "怪奇谜案限时破 第二季",
    "单身即地狱 第五季",
    "天机试炼场"
  ]
}
```

## v14ga_0220 — 2026-03-13, what will be the movies ranked from 4 to 6 on the latest weekly word-of-mouth movie ranking (一周口碑电影榜) published by Douban (豆瓣)? (Give the movie titles only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685146342537420060414055`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-13`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-13`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-13, what will be the movies ranked from 4 to 6 on the latest weekly word-of-mouth movie ranking (一周口碑电影榜) published by Douban (豆瓣)? (Give the movie titles only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{遇见世界, 好孩子, 后来的我们}",
  "answer_tokens": [
    "遇见世界",
    "好孩子",
    "后来的我们"
  ]
}
```

## v14ga_0221 — 2026-03-12, what will the price index for fruits be in the Agricultural Product Wholesale Price 200 Index from China's National Agricultural Product Wholesale Market Price Information System (全国农产品批发市场价格信息系统)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `68517362eb11c800614780de`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-12`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-12`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-12, what will the price index for fruits be in the Agricultural Product Wholesale Price 200 Index from China's National Agricultural Product Wholesale Market Price Information System (全国农产品批发市场价格信息系统)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{129.57}",
  "answer_tokens": [
    "129.57"
  ]
}
```

## v14ga_0222 — 2026-03-16, what will be the value in Chinese Yuan of 100 units of British Pound at the central parity rate?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685173c159f71f006037a1e9`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-16, what will be the value in Chinese Yuan of 100 units of British Pound at the central parity rate?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{914.49}",
  "answer_tokens": [
    "914.49"
  ]
}
```

## v14ga_0223 — 2026-03-12, what will be the Weibo accounts (微博昵称) ranked from 3 to 5 on the daily chart of Weibo Accounts Influence Ranking for Political and Legal Affairs Commissions (政法委微博账号影响力排行榜日榜) of this date published by Youmei (铀媒), Midu (蜜度)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685e494b6e8dbd006cdc6f7c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-12`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-12`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-12, what will be the Weibo accounts (微博昵称) ranked from 3 to 5 on the daily chart of Weibo Accounts Influence Ranking for Political and Legal Affairs Commissions (政法委微博账号影响力排行榜日榜) of this date published by Youmei (铀媒), Midu (蜜度)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{广西政法, 安徽反邪教, 广西反邪教}",
  "answer_tokens": [
    "广西政法",
    "安徽反邪教",
    "广西反邪教"
  ]
}
```

## v14ga_0224 — 2026-03-17, which self-media accounts will be ranked from 7 to 9 on KolRank's daily WeChat self-media overall ranking?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `687071f2d3d00b006b624a8c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-17`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-17`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-17, which self-media accounts will be ranked from 7 to 9 on KolRank's daily WeChat self-media overall ranking?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{视觉志, 人物, 第一财经}",
  "answer_tokens": [
    "视觉志",
    "人物",
    "第一财经"
  ]
}
```

## v14ga_0225 — 2026-03-17, which self-media accounts will be ranked from 2 to 4 on KolRank's daily Weibo self-media overall ranking?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `687071faab86ea0060215bc7`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-17`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-17`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-17, which self-media accounts will be ranked from 2 to 4 on KolRank's daily Weibo self-media overall ranking?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{爱生活的Yoyo酱, 在下科技君, 池九粒Jolie}",
  "answer_tokens": [
    "爱生活的Yoyo酱",
    "在下科技君",
    "池九粒Jolie"
  ]
}
```

## v14ga_0226 — 2026-03-15, what will be the movies ranked from 5 to 7 on Maoyan's 'Ticket Purchase vs Rating' list (猫眼电影购票评分榜)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685e489b6e8dbd006cdc6f70`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-15, what will be the movies ranked from 5 to 7 on Maoyan's 'Ticket Purchase vs Rating' list (猫眼电影购票评分榜)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{星河入梦, 夜王, 镖人：风起大漠}",
  "answer_tokens": [
    "星河入梦",
    "夜王",
    "镖人：风起大漠"
  ]
}
```

## v14ga_0227 — 2026-03-13, what will be the vehicles ranked from 1 to 3 on the hot list across China for SUVs (SUV全国热门榜) of this date published by Dongchedi (DCar, 懂车帝)? (Give the vehicle names only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685e48b9e582f0005f9cd2c9`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-13`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-13`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-13, what will be the vehicles ranked from 1 to 3 on the hot list across China for SUVs (SUV全国热门榜) of this date published by Dongchedi (DCar, 懂车帝)? (Give the vehicle names only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{RAV4荣放, 星越L, Model Y}",
  "answer_tokens": [
    "RAV4荣放",
    "星越L",
    "Model Y"
  ]
}
```

## v14ga_0228 — 2026-03-12, what will be the vehicles ranked from 1 to 3 on the hot list across China for sedans (轿车全国热门榜) of this date published by Dongchedi (DCar, 懂车帝)? (Give the vehicle names only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685e48ac6e8dbd006cdc6f71`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-12`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-12`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-12, what will be the vehicles ranked from 1 to 3 on the hot list across China for sedans (轿车全国热门榜) of this date published by Dongchedi (DCar, 懂车帝)? (Give the vehicle names only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{奥迪A6L, 迈腾, 速腾}",
  "answer_tokens": [
    "奥迪A6L",
    "迈腾",
    "速腾"
  ]
}
```

## v14ga_0229 — 2026-03-13, according to the latest China Influenza Weekly Report (中国流感监测周报) from the Chinese Center for Disease Control and Prevention, how many outbreaks of influenza-like illness (流感样病例暴发疫情) will be reported nationwide?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `68514628aca664006bceb217`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-13`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-13`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-13, according to the latest China Influenza Weekly Report (中国流感监测周报) from the Chinese Center for Disease Control and Prevention, how many outbreaks of influenza-like illness (流感样病例暴发疫情) will be reported nationwide?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{0.0}",
  "answer_tokens": [
    "0.0"
  ]
}
```

## v14ga_0230 — 2026-03-16, what will be the day's close for India Market Fund LOF (SZ:164824) (in CNY)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6851740359f71f006037a1ed`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-16, what will be the day's close for India Market Fund LOF (SZ:164824) (in CNY)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{1.285}",
  "answer_tokens": [
    "1.285"
  ]
}
```

## v14ga_0231 — 2026-03-12, what will be the projects ranked from 5 to 7 on OpenGithubs' github-daily-rank of this date? (Give the project names only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6854dcb27df94a0060eb86cf`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-12`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-12`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-12, what will be the projects ranked from 5 to 7 on OpenGithubs' github-daily-rank of this date? (Give the project names only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{alibaba/page-agent, anthropics/skills, NousResearch/hermes-agent}",
  "answer_tokens": [
    "alibaba/page-agent",
    "anthropics/skills",
    "NousResearch/hermes-agent"
  ]
}
```

## v14ga_0232 — 2026-03-16, what will be the

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6854dcbc7df94a0060eb86d0`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-16, what will be the "most recent" number for "Waiting for response" of this date in the Support Stats published by Steam?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{51261.0}",
  "answer_tokens": [
    "51261.0"
  ]
}
```

## v14ga_0233 — 2026-03-16, what will be the projects ranked from 8 to 10 on the latest OpenGithubs' github-weekly-rank? (Give the project names only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6854e0397ff26400687d2031`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-16, what will be the projects ranked from 8 to 10 on the latest OpenGithubs' github-weekly-rank? (Give the project names only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{pbakaus/impeccable, NousResearch/hermes-agent, promptfoo/promptfoo}",
  "answer_tokens": [
    "pbakaus/impeccable",
    "NousResearch/hermes-agent",
    "promptfoo/promptfoo"
  ]
}
```

## v14ga_0234 — 2026-03-16, which works will be ranked from 18 to 20 on the latest weekly tipping chart for audio dramas (广播剧打赏榜周榜) on Maoer (猫耳) FM (MissEvan)? (Give the work names only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `68774e69336fa8003b890146`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-16, which works will be ranked from 18 to 20 on the latest weekly tipping chart for audio dramas (广播剧打赏榜周榜) on Maoer (猫耳) FM (MissEvan)? (Give the work names only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{一颗苹果, 逐玉 第一季, 双面恶人}",
  "answer_tokens": [
    "一颗苹果",
    "逐玉 第一季",
    "双面恶人"
  ]
}
```

## v14ga_0235 — 2026-03-13, what will the high of CanSino (SH:688185) be for the day (in CNY)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `687df3a41d972f003b8ba68c`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-13`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-13`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-13, what will the high of CanSino (SH:688185) be for the day (in CNY)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{70.97}",
  "answer_tokens": [
    "70.97"
  ]
}
```

## v14ga_0236 — 2026-03-16, what will be the stock market capitalization (市价总值) of Bank of China (601988) on the Shanghai Stock Exchange in ten thousand yuan (two decimal places)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685171b65b1af900600a3306`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-16, what will be the stock market capitalization (市价总值) of Bank of China (601988) on the Shanghai Stock Exchange in ten thousand yuan (two decimal places)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{128838673.13}",
  "answer_tokens": [
    "128838673.13"
  ]
}
```

## v14ga_0237 — 2026-03-15, what songs will be ranked from 1 to 3 on the latest QQ Music Soaring Chart (QQ音乐飙升榜)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `685173fb59f71f006037a1ec`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-15, what songs will be ranked from 1 to 3 on the latest QQ Music Soaring Chart (QQ音乐飙升榜)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{一念, 青火 (Lars ver.), 初遇街口}",
  "answer_tokens": [
    "一念",
    "青火 (Lars ver.)",
    "初遇街口"
  ]
}
```

## v14ga_0238 — 2026-03-16, what will be the average price (in yuan per kilogram) of pork at the national agricultural product wholesale market monitored by the Ministry of Agriculture and Rural Affairs of China?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6851743b59f71f006037a1f1`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-16, what will be the average price (in yuan per kilogram) of pork at the national agricultural product wholesale market monitored by the Ministry of Agriculture and Rural Affairs of China?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{16.18}",
  "answer_tokens": [
    "16.18"
  ]
}
```

## v14ga_0239 — 2026-03-13, what will be the low for the CSI 300 Index for the day?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6851738859f71f006037a1e5`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-13`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-13`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-13, what will be the low for the CSI 300 Index for the day?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{4659.5}",
  "answer_tokens": [
    "4659.5"
  ]
}
```

## v14ga_0240 — 2026-03-16, what will be the technologies ranked from 8 to 10 on the latest Smart Technologies Ranking (智能科技榜) published by Autohome (汽车之家)?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6870731ba3a7fb0061457aab`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-16, what will be the technologies ranked from 8 to 10 on the latest Smart Technologies Ranking (智能科技榜) published by Autohome (汽车之家)?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{哨兵模式, AR-HUD, 智能电驱系统}",
  "answer_tokens": [
    "哨兵模式",
    "AR-HUD",
    "智能电驱系统"
  ]
}
```

## v14ga_0241 — 2026-03-12, what will be the songs from rank 15 to 17 on the latest NetEase Cloud Music Europe and America Hot Songs Chart (网易云音乐欧美热歌榜)? (Give the song titles only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6854dffd0635c0005f0a1d2f`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-12`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-12`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-12, what will be the songs from rank 15 to 17 on the latest NetEase Cloud Music Europe and America Hot Songs Chart (网易云音乐欧美热歌榜)? (Give the song titles only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Zoo (From \"Zootopia 2\"/Soundtrack Version) - (《疯狂动物城2》主题曲), Lonely, never meant to hurt you (acoustic)}",
  "answer_tokens": [
    "Zoo (From \"Zootopia 2\"/Soundtrack Version) - (《疯狂动物城2》主题曲)",
    "Lonely",
    "never meant to hurt you (acoustic)"
  ]
}
```

## v14ga_0242 — 2026-03-16, what will the value (in hundreds of millions of yuan, two decimal places) of Daily Total Turnover (当日成交总额) of Shanghai-Hong Kong Stock Connect's Southbound Trading (港股通) be?

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `68774ddd3083b1003c629ca8`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-16`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-16`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-16, what will the value (in hundreds of millions of yuan, two decimal places) of Daily Total Turnover (当日成交总额) of Shanghai-Hong Kong Stock Connect's Southbound Trading (港股通) be?"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{697.32}",
  "answer_tokens": [
    "697.32"
  ]
}
```

## v14ga_0243 — 2026-03-15, which movies will be ranked from 5 to 7 in the TOP 10 on Apple TV Store in the World chart issued by FlixPatrol? (give the movies only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6944fde51834a500697575da`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-15`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-15`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-15, which movies will be ranked from 5 to 7 in the TOP 10 on Apple TV Store in the World chart issued by FlixPatrol? (give the movies only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Anaconda 303, One Battle After Another 266, The Housemaid 256}",
  "answer_tokens": [
    "Anaconda 303",
    "One Battle After Another 266",
    "The Housemaid 256"
  ]
}
```

## v14ga_0244 — 2026-03-17, what songs will be ranked from 13 to 15 in the latest UK's Official Singles Chart Top 100? (Give the songs only)

- Track: `agentic_live_analysis`
- Task family: `futurex_style_live_prediction`
- Evaluation regime: `historical_asof_search_cutoff`
- Source id: `6945061ed2f0e700661f17a1`
- Category: `unlabeled`
- Pattern: `unknown`
- Search cutoff: `2026-03-17`
- Search cutoff source: `resolved_around_fallback`
- Resolved around: `2026-03-17`

Prompt:
```text
You are an agent that can predict future events. The event to be predicted: "2026-03-17, what songs will be ranked from 13 to 15 in the latest UK's Official Singles Chart Top 100? (Give the songs only)"
        IMPORTANT: Your final answer MUST end with this exact format:
        \boxed{YOUR_PREDICTION}
        Do not use any other format. Do not refuse to make a prediction. Do not say "I cannot predict the future." You must make a clear prediction based on the best data currently available, using the box format specified above.
```

Ground truth:
```json
{
  "answer_box": "\\boxed{Babydoll, Just the Way You Are, Opalite}",
  "answer_tokens": [
    "Babydoll",
    "Just the Way You Are",
    "Opalite"
  ]
}
```
