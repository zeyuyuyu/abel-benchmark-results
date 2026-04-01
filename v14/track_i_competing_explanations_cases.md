# v14 Track I Competing Explanations Cases

Frozen pack variant: `track_i_market_only_frozen_v1`.

Curated market-only analyst-style cases designed to avoid obvious skill-shaped prompts.

## v14i_001 — Three Plausible Stories, One Dominant Driver

- Source case: `v14d_015`
- Family: `multi_factor_finance_synthesis`
- Primary question: What is the most plausible dominant explanation for the move?
- Canonical primary answer: `channel inventory correction and weak sell-through`
- Follow-up question: What is the most important next verification or uncertainty to keep live?
- Canonical follow-up answer: `watch sell-through and inventory-days normalization`
- Inputs:
  - `document_excerpt` — Analyst note
    - Management cited three factors for the quarter: a one-point constant-currency headwind, a 40 bps legal reserve, and weaker channel sell-through that pushed inventory days higher.
  - `table` — Operating summary
    - Revenue miss versus plan: -6%. Constant-currency impact: -1 point. Legal reserve impact on operating margin: -0.4 points. Channel inventory days: +12 days. End-market sell-through: -9%.

## v14i_003 — Build The Event Memo, Not Just The Answer

- Source case: `v14d_020`
- Family: `analyst_workflow_agent`
- Primary question: What is the best-supported causal explanation for the selloff right now?
- Canonical primary answer: `funding-cost and deposit-beta concern`
- Follow-up question: What would you verify next before strengthening that view?
- Canonical follow-up answer: `verify uninsured-deposit mix or wholesale-funding dependence`
- Inputs:
  - `retrieval_bundle` — Snippet 1
    - A regional bank's shares fell after a policy official commented that deposit competition remains intense for smaller lenders.
  - `retrieval_bundle` — Snippet 2
    - The bank's last quarterly filing showed a relatively high share of interest-bearing deposits and rising funding costs.
  - `retrieval_bundle` — Snippet 3
    - A rumor about a capital raise circulated online, but no primary-source filing or company statement confirmed it.

## v14i_004 — One Event, Multiple Conflicting Narratives

- Source case: `v14d_021`
- Family: `cross_source_event_integration`
- Primary question: What is the most causally plausible primary driver of the rally?
- Canonical primary answer: `positive FDA panel vote improving approval odds`
- Follow-up question: What uncertainty or alternative is still live enough to monitor?
- Canonical follow-up answer: `short-squeeze amplification remains possible, so verify timing and short interest`
- Inputs:
  - `retrieval_bundle` — Snippet 1
    - A biotech stock rallied after an FDA advisory panel voted in favor of its therapy.
  - `retrieval_bundle` — Snippet 2
    - Social media accounts also circulated an acquisition rumor, but no credible outlet confirmed it.
  - `retrieval_bundle` — Snippet 3
    - Short interest was elevated heading into the vote, which may have amplified the magnitude of the move.

## v14i_005 — Homebuilder Miss: Funding Stress Or Demand Softness?

- Source case: `v14cpi_001`
- Family: `proxy_family_selection`
- Primary question: Which explanation is cleaner for the move right now?
- Canonical primary answer: `financing conditions and mortgage affordability`
- Follow-up question: What would make you revisit that view first?
- Canonical follow-up answer: `if orders stay weak after financing proxies normalize, demand softness gains weight`
- Inputs:
  - `document_excerpt` — Morning note
    - The stock fell 11% after management guided to lower near-term orders. Analysts noted no major land or permitting update. Channel checks described buyer hesitation around monthly payments rather than reduced tour activity.
  - `table` — Market and operating snapshot
    - 30-year mortgage rate: +55 bps over 6 weeks. Mortgage applications: -12%. Builder CDS: +38 bps. Website traffic: -1%. Model-home visits: flat. Cancellation rate: +1.2 points. Backlog burn: stable.

## v14i_006 — Regional Bank Stress And A Small-Cap SaaS Selloff

- Source case: `v14cpi_006`
- Family: `transmission_supportability`
- Primary question: What is the most supportable transmission path from the bank stress to the software move?
- Canonical primary answer: `valuation-duration and refinancing channel`
- Follow-up question: What additional evidence would most strengthen or weaken that path?
- Canonical follow-up answer: `watch spreads and duration-sensitive peers while company metrics stay intact`
- Inputs:
  - `document_excerpt` — Market note
    - The company stated that cash is spread across money-center banks and disclosed no unusual financing event. The stock still sold off with other long-duration software names when regional banks weakened.
  - `table` — Factor snapshot
    - Regional bank ETF: -14%. Small-cap software basket: -9%. HY OAS: +48 bps. Company net cash: positive. Revenue guidance: unchanged.

## v14i_007 — Airline Selloff: Fuel Shock Or Demand Crack?

- Source case: `v14cpi_003`
- Family: `proxy_family_selection`
- Primary question: What is the cleaner primary read for the airline selloff?
- Canonical primary answer: `fuel and input-cost pressure`
- Follow-up question: What would make you change that view first?
- Canonical follow-up answer: `if bookings or unit revenue break while fuel pressure eases`
- Inputs:
  - `document_excerpt` — Airline sector note
    - The stock fell after a sharp move in energy markets. Management did not cut capacity or demand commentary, and no labor disruption was disclosed.
  - `table` — Operating and market snapshot
    - Jet fuel crack spread: +18%. Front-month crude: +11%. Forward bookings: +1%. Load factor guidance: unchanged. Unit revenue guidance: flat. Wage agreement updates: none. FX basket: flat.

## v14i_008 — Small-Cap Software De-Rate: Duration Pressure Or Product Trouble?

- Source case: `v14cpi_004`
- Family: `proxy_family_selection`
- Primary question: What is the cleaner explanation for the de-rate?
- Canonical primary answer: `duration pressure and financing conditions`
- Follow-up question: What would make you shift toward an idiosyncratic company problem instead?
- Canonical follow-up answer: `if renewal or churn metrics break while rates and credit stabilize`
- Inputs:
  - `document_excerpt` — Software note
    - The company reiterated annual ARR guidance and disclosed no outage, product recall, or major customer loss. The stock fell alongside a broader selloff in long-duration software names.
  - `table` — Factor and operating snapshot
    - High-yield OAS: +75 bps. 10Y real yield: +19 bps. Small-cap software basket: -11%. ARR guidance: unchanged. Net revenue retention: 112% -> 111%. Churn: flat. Major incident count: 0.

## v14i_009 — Rare-Earth Spike Into EV Gross Margin

- Source case: `v14cpi_007`
- Family: `transmission_strength_judgment`
- Primary question: How much should the commodity shock matter near-term for the EV maker?
- Canonical primary answer: `weak near-term pass-through because contracts and cost share limit it`
- Follow-up question: What would you verify before promoting it into a bigger thesis?
- Canonical follow-up answer: `verify contract coverage or cost share before promoting the shock`
- Inputs:
  - `document_excerpt` — Supply-chain note
    - Rare-earth spot prices jumped after export restrictions. The automaker’s procurement note says the focal materials are covered by fixed contracts for the next two quarters.
  - `table` — Cost-structure snapshot
    - Rare-earth component share of COGS: 1.2%. Fixed-price coverage horizon: 2 quarters. Battery metals and logistics remain the larger variable exposures.
