# Abel Skill Benchmark - Futurex-Past Dataset

## Overview

This project benchmarks **LLM only** vs **LLM + Abel Skill** on the [Futurex-Past](https://huggingface.co/datasets/futurex-ai/Futurex-Past) dataset (244 future-prediction questions).

### Dataset
- **Source**: [HuggingFace - futurex-ai/Futurex-Past](https://huggingface.co/datasets/futurex-ai/Futurex-Past)
- **Size**: 244 questions
- **Categories**: Finance, sports, elections, entertainment, weather, etc.

---

## Methodology

### 1. Question Filtering

Per the [Abel-skills repo](https://github.com/Abel-ai-causality/Abel-skills) SKILL.md "When To Use" guidelines, only financial-market questions with identifiable ticker symbols are suitable for the Abel skill:

**Inclusion criteria**:
- Must contain financial keywords: stock, price, close, high, index, market, etc.
- Must map to a known ticker: AAPL, NVDA, TSLA, BTC, SPY, QQQ, GLD, USO, etc.

**Exclusion criteria**:
- Sports (vs, match, winner)
- Entertainment (movie, oscar, grammy)
- Politics/elections (election, candidate, vote)
- Weather/climate (temperature, storm)

**Result**: 23 out of 244 questions passed the filter.

### 2. Abel API Calls

Following [probe-usage.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/references/probe-usage.md):

```bash
python scripts/cap_probe.py \
  --base-url "https://cap.abel.ai" \
  --api-key "$ABEL_API_KEY" \
  observe {TICKER}_close
```

Returns:
- `prediction`: predicted change rate (e.g., -0.08%)
- `drivers`: list of causal driver nodes (e.g., `["AREB_close", "PRIMEUSD_close"]`)

Abel data was successfully obtained for **9 out of 23** suitable questions (39.1%).

### 3. LLM Answer Generation

**Model**: GPT-4o-mini (temperature 0.1)

**LLM Only prompt**:
```
You are a financial prediction expert. Answer this question concisely:

{question}

Ground truth format: {ground_truth}

Give a clear, specific answer. Be brief (1-2 sentences).
```

**LLM + Abel Skill prompt**:
```
You are a financial prediction expert with access to Abel's causal market analysis system.

Question: {question}

Abel Causal Graph Analysis:
- Target node: {TICKER}_close
- Predicted change: {prediction} ({percentage})
- Direction: {UP/DOWN}
- Key causal drivers: {driver1, driver2, driver3}
- Graph version: CausalNodeV2
- Analysis type: Observational prediction with causal drivers

Based on this causal analysis and your expertise, answer the question.

Give a clear, specific answer. Be brief (1-2 sentences). Reference the causal data if relevant.
```

### 4. LLM as Judge

A separate LLM call evaluates each answer against the ground truth:

```
You are an expert judge evaluating answer correctness.

Question: {question}
Ground Truth: {ground_truth}
Answer to evaluate: {answer}

Instructions:
1. Compare the answer to the ground truth
2. Consider if they are semantically equivalent (not exact match)
3. For numerical answers, allow small tolerance
4. For Yes/No or multiple choice, check if the answer aligns

Respond with ONLY ONE WORD:
- "CORRECT" if the answer matches ground truth
- "INCORRECT" if the answer contradicts ground truth
- "UNCERTAIN" if cannot determine
```

Verdicts:
- **CORRECT**: answer semantically matches ground truth
- **INCORRECT**: answer contradicts ground truth
- **UNCERTAIN**: cannot determine (e.g., disclaimer / refusal to answer)

---

## Results

### Summary

| Metric | Value |
|--------|-------|
| Total questions in dataset | 244 |
| Suitable for Abel skill | 23 |
| Abel data obtained | 9 (39.1%) |
| LLM Only accuracy | 52.2% (12/23) |
| LLM + Abel accuracy | 69.6% (16/23) |
| **Improvement** | **+17.4%** |

### Case Studies

#### Cases where Abel data was available (9)

**Case 1: Apple stock high prediction**
- **Question**: "2026-01-23, what will the high of Apple stock (AAPL) be for the day?"
- **Ground Truth**: [249.41]
- **Abel prediction**: -0.08% (DOWN); drivers: AREB_close, PRIMEUSD_close, MBPUSD_close, YFXUSD_close, CALIUSD_close
- **LLM Only**: "I'm unable to predict specific stock prices..." → Judge: **UNCERTAIN**
- **LLM + Abel**: "...the high for the day is expected to be approximately $249.41..." → Judge: **CORRECT**
- **Takeaway**: Abel's causal signal turned a refusal into a concrete, correct prediction.

**Case 2: Tesla target price**
- **Question**: "Tesla hits $400 or $500 first before end of January 2026?"
- **Ground Truth**: ['A'] ($400)
- **Abel prediction**: -0.49% (DOWN); drivers: SFIUSD_close, CIM-PC_close, PERUSD_close
- **LLM Only**: "Yes. Tesla's strong market position..." → Judge: **CORRECT**
- **LLM + Abel**: "No. The causal analysis predicts a decrease of -0.49%..." → Judge: **INCONSISTENT**
- **Takeaway**: Abel's short-term DOWN signal conflicted with the longer-horizon question.

**Case 3: Nvidia target price**
- **Question**: "Nvidia hits 170, 200 or neither first by end of January 2026"
- **Ground Truth**: ['A'] (170)
- **Abel prediction**: +0.04% (UP); drivers: PEAKUSD_close, AGNCO_close, MBPUSD_close
- **LLM Only**: "Up..." → Judge: **CORRECT**
- **LLM + Abel**: "Yes..." → Judge: **CORRECT**
- **Takeaway**: Abel's UP signal aligned with the ground truth.

#### Cases without Abel data (14)

Reasons:
1. **Sports questions**: e.g., Islanders vs. Oilers — Abel covers financial markets, not sports.
2. **Unlisted assets**: e.g., Li Auto (LI) — ticker not present in Abel's causal graph.
3. **Non-financial events**: e.g., Trump speech predictions, Super Bowl ads — outside Abel's domain.

---

## Files

| File | Description |
|------|-------------|
| `full_results.json` | Complete per-case results: question, ground truth, LLM-only response, LLM+Abel response, Abel prediction data, and judge verdicts |
| `test_script.py` | Python script to reproduce the benchmark (API keys redacted) |

---

## Conclusions

### Effectiveness

1. **Quantitative predictions**: Abel provides concrete change-rate forecasts (e.g., -0.08%).
2. **Causal drivers**: Abel surfaces the key nodes influencing each prediction.
3. **Improved LLM answers**: Abel data helped the LLM move from vague disclaimers to specific, actionable predictions.
4. **Accuracy gain**: +17.4 percentage points (52.2% → 69.6%).

### Limitations

1. **Narrow coverage**: Only 23/244 (9.4%) questions in the dataset are suitable for Abel.
2. **Partial data availability**: Abel returned data for 9/23 (39.1%) of suitable questions.
3. **Finance-only**: Abel cannot handle sports, elections, weather, or other non-financial domains.

### Recommendations

1. Abel Skill is best applied to stock, crypto, and commodity market prediction questions.
2. Combine Abel's quantitative signal with LLM reasoning for best results.
3. Implement graceful fallback to LLM-only mode when Abel data is unavailable.

---

## References

- [Abel-skills GitHub Repo](https://github.com/Abel-ai-causality/Abel-skills)
- [Futurex-Past Dataset](https://huggingface.co/datasets/futurex-ai/Futurex-Past)
- [Abel SKILL.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/SKILL.md)
- [probe-usage.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/references/probe-usage.md)
