# v14 Track I Competing Explanations Seed Ideas

This file lists realistic seed surfaces for `Track I`. None of these should
require the user to know or invoke any Abel-specific capability.

## Seed Families

### 1. Margin Miss: Cost Or Mix?

- Surface: earnings excerpt plus gross-margin bridge
- User question: "Which explanation best fits the margin miss?"
- Competing stories:
  - input-cost inflation
  - discounting / promo intensity
  - lower-end product mix
- Why this is natural:
  - this is a standard analyst disagreement after earnings
- Why causal skill may help:
  - it separates upstream cost drivers from downstream realized pricing

### 2. SaaS Growth Slowdown: Demand Or Seat Normalization?

- Surface: retention table, ACV commentary, hiring data
- User question: "What is the best-supported explanation for the slowdown?"
- Competing stories:
  - weaker demand generation
  - post-binge seat normalization
  - FX translation noise
- Shortcut trap:
  - headline revenue deceleration alone does not identify cause

### 3. Supplier Selloff: Commodity Shock Or Customer Inventory Reset?

- Surface: supplier stock move, commodity move, customer channel checks
- User question: "Which explanation is more causally defensible?"
- Competing stories:
  - upstream input shock
  - downstream inventory correction
  - company-specific execution issue
- Why this is natural:
  - exactly how industrial and semicap notes are written

### 4. Bank NIM Surprise: Deposit Beta Or Asset Mix?

- Surface: quarterly bank filing snippet, NIM bridge, deposit pricing table
- User question: "Which mechanism best explains the NIM change?"
- Competing stories:
  - deposit beta pressure
  - asset-mix shift
  - one-time accounting noise
- Falsifier target:
  - funding-cost behavior vs loan-yield behavior

### 5. Retail Comp Miss: Weather, Promo, Or Traffic Quality?

- Surface: comp sales table, gross-margin move, basket-size and traffic stats
- User question: "Which story survives the evidence packet?"
- Competing stories:
  - weather distortion
  - promo-led traffic but weak quality
  - category-specific demand softness
- Cause-vs-consequence trap:
  - traffic can be an outcome of promo strategy, not an exogenous driver

### 6. Drug Launch Delay: Access Or Supply?

- Surface: launch commentary, prescription trend chart, manufacturing note
- User question: "What is the most likely binding constraint?"
- Competing stories:
  - reimbursement / payer gating
  - physician adoption friction
  - manufacturing or fill-finish bottleneck
- Why this is natural:
  - mirrors biotech launch debates without asking for any tool-native move

### 7. Airline Ops Breakdown: Weather Or Scheduling?

- Surface: timeline of cancellations, airport mix, staffing note, FAA update
- User question: "Which explanation is upstream and which is symptomatic?"
- Competing stories:
  - system-wide weather
  - crew scheduling failure
  - ATC capacity constraints
- Implication target:
  - what pattern should appear in route mix if each story were true

### 8. EV Sales Miss: Credit Tightening Or Product Mix?

- Surface: monthly registrations, financing-rate data, model-level mix
- User question: "Which explanation best fits the miss, and what would falsify it?"
- Competing stories:
  - macro credit tightening
  - weaker mix / model refresh dynamics
  - supply bottlenecks
- Why this is natural:
  - common sell-side debate, not skill-shaped at all

## Authoring Notes

- Prefer cases with `2` or `3` plausible stories, not `5` vague ones.
- Every distractor should be something a smart analyst might genuinely believe.
- At least one field should test "cause vs consequence," not only explanation
  choice.
- Public-dev cases should keep anchored answer keys; hidden cases can add memo
  review.
- If a seed feels like a renamed graph query, delete it.
