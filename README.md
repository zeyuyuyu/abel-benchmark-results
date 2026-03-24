# Abel Skill Benchmark - Futurex-Past Dataset

## Overview

This project benchmarks **LLM only** vs **LLM + [Abel Skill](https://github.com/Abel-ai-causality/Abel-skills)** on the [Futurex-Past](https://huggingface.co/datasets/futurex-ai/Futurex-Past) dataset (244 future-prediction questions).

Two benchmark versions are included:

| Version | Skill Usage | Description |
|---------|-------------|-------------|
| **v3** | `observe.predict` only | Minimal skill usage — single prediction value + drivers |
| **v4** | `observe.predict` + `graph.neighbors` + `graph.markov_blanket` | Full skill usage — prediction + structural causal parents + Markov blanket |

Both versions use **LLM-based question classification** (GPT-4o-mini) to identify suitable financial questions and extract ticker symbols, then **`normalize-node`** from [cap_probe.py](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/scripts/cap_probe.py) to resolve correct Abel node IDs.

### Dataset
- **Source**: [HuggingFace - futurex-ai/Futurex-Past](https://huggingface.co/datasets/futurex-ai/Futurex-Past)
- **Size**: 244 questions (finance, sports, elections, entertainment, weather, etc.)

---

## Methodology

### 1. LLM-based Question Classification

Each of the 244 questions is sent to GPT-4o-mini to determine:
- Whether it is a financial market prediction question suitable for Abel
- The relevant ticker symbol(s) (e.g., `AAPL`, `NVDA`, `CL` for crude oil, `GC` for gold)

This eliminates false positives such as "Golden Knights vs. Kings" (sports, not gold) and correctly resolves tickers like crude oil → `CL`, soybeans → `ZS`.

### 2. Node Normalization

Tickers are passed through `cap_probe.py normalize-node` to get the correct Abel node ID:
```bash
python scripts/cap_probe.py normalize-node NVDA
# -> {"normalized_node_id": "NVDA_close"}
```

### 3. Abel API Calls

Following [probe-usage.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/references/probe-usage.md):

**v3** (minimal):
```bash
python scripts/cap_probe.py --base-url https://cap.abel.ai observe NVDA_close
```

**v4** (full):
```bash
# Observational prediction
python scripts/cap_probe.py --base-url https://cap.abel.ai observe NVDA_close

# Structural causal parents
python scripts/cap_probe.py --base-url https://cap.abel.ai neighbors NVDA_close --scope parents --max-neighbors 10

# Full causal neighborhood (Markov blanket)
python scripts/cap_probe.py --base-url https://cap.abel.ai markov-blanket NVDA_close --max-neighbors 15
```

### 4. LLM Answer Generation

**Model**: GPT-4o-mini (temperature 0.1)

**LLM Only**: Standard financial prediction prompt.

**LLM + Abel (v3)**: Prompt includes prediction value, direction, and driver list.

**LLM + Abel (v4)**: Prompt includes:
- Observational prediction (value, direction, drivers)
- Structural parents from `graph.neighbors`
- Markov blanket nodes with roles (parent / child / spouse)
- Graph metadata (11,315 nodes, 42M+ edges, PCMCI algorithm)
- Explicit note that prediction is short-term and structural context should inform longer-horizon reasoning

### 5. LLM as Judge

A separate LLM call evaluates each answer against the ground truth, returning `CORRECT`, `INCORRECT`, or `UNCERTAIN`.

---

## Results

### v3 — Minimal Skill Usage (observe only)

| Metric | Value |
|--------|-------|
| Suitable for Abel | 27 |
| Abel data obtained | 13 (48%) |
| **LLM Only accuracy** | **70.4% (19/27)** |
| **LLM + Abel accuracy** | **63.0% (17/27)** |
| **Improvement** | **-7.4%** |
| Cases improved by Abel | 2 |
| Cases worsened by Abel | 4 |

#### v3 Per-case Results

| # | LLM | Abel | Node | Question |
|---|-----|------|------|----------|
| 1 | Y | Y | AAPL_close | Apple stock (AAPL) high for the day |
| 2 | ? | ? | — | S&P 500 Index open |
| 3 | Y | Y | — | Dow Jones close |
| 4 | Y | Y | LI_close | Li Auto (LI) high |
| 5 | ? | ? | — | NASDAQ Composite Index open |
| 6 | Y | Y | — | Palantir (PLTR) close above ___? |
| 7 | Y | Y | — | Gold (GC) above ___? |
| 8 | Y | Y | CL_close | Crude Oil (CL) settle |
| 9 | Y | Y | OPEN_close | Opendoor (OPEN) hit price |
| 10 | ? | ? | CL_close | Crude Oil (CL) hit price |
| 11 | Y | Y | — | Gold (GC) settle |
| 12 | N | N | TSLA_close | Tesla $400 or $500 first? |
| 13 | N | **Y** | NVDA_close | Nvidia 170, 200, or neither? |
| 14 | Y | Y | — | Bitcoin above $100K? |
| 15 | Y | Y | — | Bitcoin below $82K? |
| 16 | Y | Y | ZS_close | Soybean price range |
| 17 | N | **Y** | PL_close | Platinum availability |
| 18 | Y | **N** | PD_close | Nornickel palladium production |
| 19 | Y | **N** | AAPL_close | Stock prices March 13 vs March 6 |
| 20 | Y | **N** | NVDA_close | NVIDIA stock March 16 vs March 9 |

*(Remaining cases had no Abel data, scores carried from LLM Only)*

#### v3 Analysis

Abel worsened more cases than it improved because:
- The prompt only included a single prediction number (e.g., +0.07%), which the LLM over-anchored on
- Short-term predictions misled answers to longer-horizon questions
- No structural context to temper the point prediction

---

### v4 — Full Skill Usage (observe + neighbors + markov-blanket)

| Metric | Value |
|--------|-------|
| Suitable for Abel | 31 |
| Abel data obtained | 15 (48%) |
| **LLM Only accuracy** | **77.4% (24/31)** |
| **LLM + Abel accuracy** | **77.4% (24/31)** |
| **Improvement** | **0.0%** |
| Cases improved by Abel | 3 |
| Cases worsened by Abel | 3 |

#### v4 Subset: Cases with Abel Data (15 cases)

| Metric | Value |
|--------|-------|
| LLM Only accuracy | 73.3% (11/15) |
| LLM + Abel accuracy | 73.3% (11/15) |

#### v4 Cases Improved by Abel

| Question | LLM | Abel | Node | Prediction |
|----------|-----|------|------|------------|
| Tesla $400 or $500 first? | N | **Y** | TSLA_close | -0.32% DOWN |
| Nvidia 170, 200, or neither? | N | **Y** | NVDA_close | +0.07% UP |
| Platinum availability below 2M oz? | N | **Y** | PL_close | -1.28% DOWN |

#### v4 Cases Worsened by Abel

| Question | LLM | Abel | Node | Prediction |
|----------|-----|------|------|------------|
| Opendoor (OPEN) hit price | Y | **N** | OPEN_close | +2.84% UP |
| Stock prices March 13 vs March 6 | Y | **N** | AAPL_close | -0.42% DOWN |
| NVIDIA stock March 16 vs March 9 | Y | **N** | NVDA_close | +0.06% UP |

#### v4 Analysis

Adding structural context (parents + Markov blanket) improved outcomes vs v3:
- **Fewer worsened cases**: 3 (down from 4 in v3)
- **More improved cases**: 3 (up from 2 in v3)
- The richer prompt gave the LLM structural context to temper the point prediction, reducing over-anchoring
- Net effect moved from -7.4% to 0.0%

Remaining issues:
- Abel predictions are next-period (hourly) forecasts; questions span days or weeks
- Multi-asset questions (6 stocks on March 13 vs March 6) used only one node's signal

---

## v3 vs v4 Comparison

| Metric | v3 (observe only) | v4 (full skill) |
|--------|-------------------|-----------------|
| Suitable questions | 27 | 31 |
| Abel data coverage | 48% | 48% |
| LLM Only accuracy | 70.4% | 77.4% |
| LLM + Abel accuracy | 63.0% | 77.4% |
| Improvement | -7.4% | 0.0% |
| Cases improved | 2 | 3 |
| Cases worsened | 4 | 3 |
| Prompt context | Prediction + drivers | Prediction + drivers + parents + Markov blanket |

**Key insight**: Using the full causal structure (parents, Markov blanket) as per [SKILL.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/SKILL.md) guidelines gives the LLM better context to reason about predictions, avoiding over-reliance on a single number.

---

## Files

| File | Description |
|------|-------------|
| `v3/results.json` | v3 full per-case results |
| `v3/test_script.py` | v3 benchmark script (API keys redacted) |
| `v4/results.json` | v4 full per-case results |
| `v4/test_script.py` | v4 benchmark script (API keys redacted) |

---

## Conclusions

### Effectiveness

1. **Full skill usage matters**: v4 (full context) eliminated the negative impact seen in v3 (observe only).
2. **Structural context reduces over-anchoring**: Markov blanket and parent nodes help the LLM reason beyond a single prediction value.
3. **Abel improves specific cases**: Tesla, Nvidia, and platinum predictions benefited from causal signals.

### Limitations

1. **Temporal mismatch**: Abel's next-period forecasts vs. days/weeks-ahead questions.
2. **Graph coverage gaps**: SPY, DJI, BTC, XAUUSD, CSI300, Chinese A-shares not in graph.
3. **Multi-asset questions**: Current approach uses one node; should aggregate signals across all mentioned assets.

### Recommendations

1. Always use the full skill surface (`observe` + `neighbors` + `markov-blanket`) rather than `observe` alone.
2. Expand Abel's graph to cover major indices, crypto pairs, and precious metals.
3. Add time-horizon awareness to prompts: weight short-term Abel signals differently for day-level vs. month-level questions.
4. For multi-asset questions, query Abel for each mentioned asset and present aggregated signals.

---

## References

- [Abel-skills GitHub Repo](https://github.com/Abel-ai-causality/Abel-skills)
- [Futurex-Past Dataset](https://huggingface.co/datasets/futurex-ai/Futurex-Past)
- [Abel SKILL.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/SKILL.md)
- [probe-usage.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/references/probe-usage.md)
- [question-routing.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/references/question-routing.md)
