# Abel Skill Benchmark v2 - Futurex-Past Dataset

## Overview

This project benchmarks **LLM only** vs **LLM + Abel Skill** on the [Futurex-Past](https://huggingface.co/datasets/futurex-ai/Futurex-Past) dataset (244 future-prediction questions).

**Key improvement in v2**: question classification and ticker-to-node mapping are performed by the LLM itself, rather than a hardcoded keyword dictionary. This eliminates false positives (e.g., sports questions containing "gold" or "oil") and enables correct node name resolution (e.g., crude oil → `CL_close`, gold → `XAUUSD_close`).

### Dataset
- **Source**: [HuggingFace - futurex-ai/Futurex-Past](https://huggingface.co/datasets/futurex-ai/Futurex-Past)
- **Size**: 244 questions
- **Categories**: Finance, sports, elections, entertainment, weather, etc.

---

## Methodology

### 1. LLM-based Question Classification

Each of the 244 questions is sent to GPT-4o-mini with the following prompt to determine suitability and extract Abel node names:

```
You are an expert at the Abel causal analysis platform. Abel's causal graph
contains financial market nodes like stock prices, crypto prices, and commodity
prices. Each node is named as {TICKER}_close, e.g. AAPL_close, NVDA_close,
BTCUSD_close, ETHUSD_close, XAUUSD_close.

Given this question, decide:
1. Is this a financial market prediction question that Abel can help with?
2. If yes, what is the most likely Abel node name(s) to query?

Respond in JSON: {"suitable": true/false, "reason": "...", "nodes": ["NODE_close"]}
```

This approach:
- **Eliminates false positives**: "Golden Knights vs. Kings" is correctly classified as sports, not gold.
- **Resolves correct node names**: "Crude Oil (CL)" → `CL_close`; "Bitcoin" → `BTCUSD_close`.
- **Suggests multiple fallback nodes**: e.g., `["CLUSD_close", "CL_close"]` for crude oil.

**Result**: 19 out of 244 questions classified as suitable (vs. 23 in v1 with keyword matching).

### 2. Abel API Calls

Following [probe-usage.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/references/probe-usage.md):

```bash
python scripts/cap_probe.py \
  --base-url "https://cap.abel.ai" \
  --api-key "$ABEL_API_KEY" \
  observe {NODE}_close
```

For each question, all candidate nodes are tried in order until one returns data.

Returns:
- `prediction`: predicted change rate (e.g., -0.08%)
- `drivers`: list of causal driver nodes (e.g., `["AREB_close", "PRIMEUSD_close"]`)

**Result**: Abel data obtained for **10 out of 19** suitable questions (52.6%).

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
You are a financial prediction expert with access to Abel's causal market
analysis system.

Question: {question}

Abel Causal Graph Analysis:
- Target node: {node}
- Predicted change: {prediction} ({percentage})
- Direction: {UP/DOWN}
- Key causal drivers: {drivers}
- Graph version: CausalNodeV2
- Analysis type: Observational prediction with causal drivers

Based on this causal analysis and your expertise, answer the question.
Give a clear, specific answer. Be brief (1-2 sentences).
```

### 4. LLM as Judge

A separate LLM call evaluates each answer against the ground truth:

```
You are an expert judge evaluating answer correctness.

Question: {question}
Ground Truth: {ground_truth}
Answer to evaluate: {answer}

Respond with ONLY ONE WORD: "CORRECT", "INCORRECT", or "UNCERTAIN"
```

---

## Results

### Summary

| Metric | Value |
|--------|-------|
| Total questions in dataset | 244 |
| Suitable for Abel (LLM-classified) | 19 |
| Abel data obtained | 10 (52.6%) |
| LLM Only accuracy | 47.4% (9/19) |
| LLM + Abel accuracy | 47.4% (9/19) |
| Cases improved by Abel | 2 |
| Cases worsened by Abel | 2 |

### Per-case Results

| # | LLM | Abel | Node | Question |
|---|-----|------|------|----------|
| 1 | Y | Y | AAPL_close | Apple stock (AAPL) high for the day |
| 2 | ? | ? | — | S&P 500 Index open |
| 3 | Y | Y | — | Dow Jones close |
| 4 | Y | Y | LI_close | Li Auto (NASDAQ:LI) high |
| 5 | ? | ? | — | NASDAQ Composite Index open |
| 6 | Y | Y | — | Palantir (PLTR) close above ___? |
| 7 | Y | Y | — | Gold (GC) above ___? |
| 8 | Y | **N** | CL_close | Crude Oil (CL) settle price |
| 9 | ? | **N** | OPEN_close | Opendoor (OPEN) hit price |
| 10 | ? | **N** | CL_close | Crude Oil (CL) hit price |
| 11 | ? | ? | — | Gold (GC) settle price |
| 12 | **N** | **Y** | TSLA_close | Tesla hits $400 or $500 first? |
| 13 | **N** | **Y** | NVDA_close | Nvidia hits 170, 200 or neither? |
| 14 | Y | Y | — | Bitcoin close above $100,000? |
| 15 | N | N | — | Bitcoin below $82K? |
| 16 | ? | N | ZS_close | Soybean price range |
| 17 | Y | Y | — | Global platinum availability |
| 18 | N | N | AAPL_close | Stock prices March 13 vs March 6 |
| 19 | Y | **N** | NVDA_close | NVIDIA stock March 16 vs March 9 |

Legend: **Y** = Correct, **N** = Incorrect, **?** = Uncertain, **—** = No Abel data

### Cases Improved by Abel

1. **Tesla hits $400 or $500 first?** — LLM alone was incorrect; Abel's TSLA_close prediction (-0.49%) helped the LLM reason about price direction.
2. **Nvidia hits 170, 200 or neither?** — LLM alone was incorrect; Abel's NVDA_close prediction (+0.04%) provided the right directional signal.

### Cases Worsened by Abel

1. **Crude Oil (CL) settle at in January?** — LLM alone was correct; Abel's CL_close prediction (+0.04%) led to an incorrect specific answer.
2. **NVIDIA stock March 16 vs March 9** — LLM alone was correct; Abel's NVDA_close UP signal misled the final answer.

### Nodes Not Found in Abel Graph

| Nodes tried | Question |
|-------------|----------|
| SPY_close | S&P 500 Index |
| DJI_close, SPY_close | Dow Jones Industrial Average |
| PLTR_close | Palantir |
| XAUUSD_close | Gold |
| BTCUSD_close | Bitcoin |
| XPTUSD_close, PLTUSD_close | Platinum |

These tickers either don't exist in Abel's causal graph or use a different naming convention.

---

## Files

| File | Description |
|------|-------------|
| `full_results.json` | Complete per-case results with all LLM responses, Abel data, and judge verdicts |
| `test_script.py` | Python script to reproduce the benchmark (API keys redacted) |

---

## Conclusions

### v1 vs v2 Comparison

| Metric | v1 (keyword matching) | v2 (LLM classification) |
|--------|----------------------|------------------------|
| Suitable questions | 23 | 19 (more precise) |
| Abel data coverage | 39.1% (9/23) | 52.6% (10/19) |
| False positive questions | Yes (sports, entertainment) | No |
| Node name resolution | ETF tickers only | Correct market tickers |

### Effectiveness

1. **Precise classification**: LLM filtering eliminated all non-financial false positives.
2. **Better node mapping**: LLM correctly resolved crude oil → `CL_close`, Li Auto → `LI_close`, soybeans → `ZS_close`.
3. **Higher data coverage**: 52.6% vs 39.1%, thanks to correct node names.
4. **Mixed accuracy impact**: Abel improved 2 cases but worsened 2 others — the net improvement was 0%.

### Limitations

1. **Narrow coverage**: Only 19/244 (7.8%) questions in this dataset are financial market predictions.
2. **Missing graph nodes**: SPY, DJI, PLTR, BTCUSD, XAUUSD are not in Abel's graph.
3. **Short-term vs long-term mismatch**: Abel provides next-period predictions, which may conflict with longer-horizon questions.

### Recommendations

1. Expand Abel's causal graph to include major indices (SPY, DJI), crypto (BTCUSD), and precious metals (XAUUSD).
2. Use LLM-based classification (not keyword matching) for real-world skill routing.
3. Add time-horizon awareness: Abel's short-term signal should be weighted differently for day-level vs month-level questions.

---

## References

- [Abel-skills GitHub Repo](https://github.com/Abel-ai-causality/Abel-skills)
- [Futurex-Past Dataset](https://huggingface.co/datasets/futurex-ai/Futurex-Past)
- [Abel SKILL.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/SKILL.md)
- [probe-usage.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/references/probe-usage.md)
