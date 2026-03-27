# Abel Skill Benchmark Results

## Overview

This repository collects multiple benchmarks comparing **LLM only** vs **LLM + [Abel Skill](https://github.com/Abel-ai-causality/Abel-skills)**.

The original benchmarks are on the [Futurex-Past](https://huggingface.co/datasets/futurex-ai/Futurex-Past) dataset (244 future-prediction questions), and newer additions include a direct live Abel CAP ablation plus a smaller FutureX financial-subset A/B run.

Benchmark versions currently included:

| Version | Skill Usage | Description |
|---------|-------------|-------------|
| **v3** | `observe.predict` only | Minimal skill usage — single prediction value + drivers |
| **v4** | `observe.predict` + `graph.neighbors` + `graph.markov_blanket` | Full skill usage — prediction + structural causal parents + Markov blanket |
| **v5** | Codex with and without installed `causal-abel` skill | Direct live Abel CAP A/B on six graph/intervention tasks |
| **v6** | Codex with and without installed `causal-abel` skill | FutureX financial-subset A/B: 10 scored `FutureX-Past` questions + 7 live `FutureX-Online` predictions |
| **v7** | Codex with and without installed `causal-abel` skill | `FutureX-Online` live-only A/B on 7 unresolved finance questions, including output-validity checks and observed skill-use evidence |
| **v8** | Codex with and without installed `causal-abel` skill | CAP-adapted causalbench aligned to Abel graph, intervention, and extension semantics; designed as a live contract/regression benchmark |
| **v9** | Casebook input layer for Codex with and without installed `causal-abel` skill | FutureX-style, LLM-authored casebook aligned to the updated `causal-abel` `1.0.7` skill and anchored to a live Abel CAP snapshot |
| **v10** | Natural-intent casebook input layer for Codex with and without installed `causal-abel` skill | FutureX-inspired but non-tool-facing benchmark cases written as questions a normal user could plausibly ask |
| **v11** | Natural-intent benchmark package with separated prompts, answers, and evidence | Successor to `v10` that splits `questions.json`, `ground_truth.json`, and raw Abel snapshot artifacts for cleaner evaluation |
| **v12** | General-finance challenge set plus high-signal proof subset for Codex with and without installed `causal-abel` skill | Adds harder proxy-choice and supportability cases, then evaluates a narrow crypto proxy-routing subset where unrestricted `codex + skill` outperforms unrestricted `codex` |
| **v13** | Split benchmark with a 100-case live-only main set plus a categorized resolved companion subset | Keeps the main benchmark third-party-resolved and forward-looking, with 93 LLM-authored custom live finance cases on top of 7 official `FutureX-Online` tasks, plus an immediately scoreable categorized `FutureX-Past` companion |
| **v14** | Industrial causal benchmark architecture plus public-dev prototype pack | New benchmark design layer that integrates formal causal benchmarks, data-grounded causal QA, natural event causality, finance/business reasoning, and industrial intervention/estimation into a unified industrial-grade causal benchmark spec, now with an instantiated public-dev case pack, separated answer key, and a focused causal/proxy/intervention stress pack |

The original `v3` / `v4` pipeline uses **LLM-based question classification** (GPT-4o-mini) to identify suitable financial questions and extract ticker symbols, then **`normalize-node`** from [cap_probe.py](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/scripts/cap_probe.py) to resolve correct Abel node IDs.

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

Initial v4 results used a lenient judge that incorrectly marked refusal answers ("I cannot predict...") as CORRECT. After applying a **strict judge** — where refusals, disclaimers, and vague hedging are always INCORRECT — the results are:

| Metric | Value |
|--------|-------|
| Suitable for Abel | 31 |
| Abel data obtained | 15 (48%) |
| **LLM Only accuracy** | **16.1% (5/31)** |
| **LLM + Abel accuracy** | **38.7% (12/31)** |
| **Improvement** | **+22.6%** |
| Cases improved by Abel | 8 |
| Cases worsened by Abel | 1 |

#### v4 Subset: Cases with Abel Data (15 cases)

| Metric | Value |
|--------|-------|
| LLM Only accuracy | 20.0% (3/15) |
| LLM + Abel accuracy | **66.7% (10/15)** |
| **Improvement (Abel-data subset)** | **+46.7%** |

#### v4 Cases Improved by Abel (8)

| Question | LLM | Abel | Node | Prediction |
|----------|-----|------|------|------------|
| Apple stock (AAPL) high for the day | N | **Y** | AAPL_close | -0.42% |
| Li Auto (LI) high for the day | N | **Y** | LI_close | +0.24% |
| Crude Oil (CL) settle in January | N | **Y** | CL_close | -0.04% |
| Tesla $400 or $500 first? | N | **Y** | TSLA_close | -0.32% |
| Lowest closing price of soybeans | N | **Y** | ZS_close | -0.01% |
| Agricultural Product Wholesale Price Index | N | **Y** | CL_close | -0.04% |
| Platinum availability below 2M oz? | N | **Y** | PL_close | -1.28% |
| Average diesel price (yuan/kg) | N | **Y** | CL_close | -0.04% |

#### v4 Cases Worsened by Abel (1)

| Question | LLM | Abel | Node | Prediction |
|----------|-----|------|------|------------|
| Stock prices March 13 vs March 6 | Y | **N** | AAPL_close | -0.42% |

#### v4 Analysis

With strict judging, the true value of Abel skill becomes clear:
- **LLM alone mostly refuses to answer** financial prediction questions ("I cannot predict stock prices"), resulting in only 16.1% accuracy.
- **Abel data enables concrete predictions**: Abel's causal signals (prediction + drivers + structural parents + Markov blanket) give the LLM enough grounding to produce specific answers instead of disclaimers.
- **+46.7% accuracy improvement on Abel-data subset**: For the 15 cases where Abel data was available, accuracy jumped from 20% to 66.7%.
- **Only 1 case worsened**: Multi-asset question where a single node's signal was insufficient.

Remaining issues:
- Abel predictions are next-period (hourly) forecasts; questions span days or weeks
- Multi-asset questions (6 stocks on March 13 vs March 6) used only one node's signal

---

## v3 vs v4 Comparison

| Metric | v3 (observe only) | v4 (full skill) |
|--------|-------------------|-----------------|
| Suitable questions | 27 | 31 |
| Abel data coverage | 48% | 48% |
| LLM Only accuracy | 70.4% | 16.1% |
| LLM + Abel accuracy | 63.0% | 38.7% |
| Improvement | -7.4% | **+22.6%** |
| Cases improved | 2 | 8 |
| Cases worsened | 4 | 1 |
| Judge | lenient (refusals = correct) | **strict (refusals = incorrect)** |
| Prompt context | Prediction + drivers | Prediction + drivers + parents + Markov blanket |

**Key insight**: Using the full causal structure (parents, Markov blanket) as per [SKILL.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/SKILL.md) guidelines gives the LLM better context to reason about predictions, avoiding over-reliance on a single number.

---

## v7 — FutureX-Online Live-Only A/B

This newer benchmark isolates only unresolved `FutureX-Online` finance questions, so the evaluation setup no longer benefits from already-resolved historical outcomes.

Headline results:

- **Base**: 7 predictions returned in `722.09s`, but only `6/7` were valid boxed answers because the BTC question came back as `\boxed{}`.
- **Skill**: 7 predictions returned in `1217.83s`, with `7/7` valid boxed answers.
- **Predictions differed on 3/7 tasks**: KOSPI threshold hits, BTC March price band, and the March Banxico decision.
- **Observed skill usage was real, not nominal**: the skill-side session log shows direct `cap_probe.py` calls such as `capabilities`, `normalize-node BTC`, `observe BTC`, `observe SPY`, `paths SPY BTC`, and multiple `traverse-parents` calls.
- **Auto-rescoring is now built in**: `v7/rescore_live.py` checks the latest `futurex-ai/Futurex-Past` dataset for matching resolved task IDs and rewrites `v7/results.json` plus `v7/cases.md` with any newly available scores.

Run it with:

```bash
python3 /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v7/rescore_live.py
```

This makes `v7` a cleaner benchmark for "live prediction with and without the skill" than any `FutureX-Past` setup, even though the questions are not yet scoreable until they resolve.

---

## v8 — CAP CausalBench v1

`v8` is the first benchmark in this repo designed directly around the real `causal-abel` capability surface instead of around generic future-prediction datasets.

Headline results:

- **15 tasks / 31 scored fields** across six categories: capability contract, node normalization, structural reads, reachability and validation, intervention boundaries, and extension semantics.
- **Base**: `31/31` in `970.70s`
- **Skill**: `31/31` in `1017.36s`
- **Takeaway**: `v8` is useful as a live CAP contract and regression suite, but it is **not yet discriminative** for `llm only` vs `llm + skill` when the prompts are explicit and structured.

Why this matters:

- `FutureX` is useful for live prediction, but many tasks are not good matches for graph-centric causal reasoning.
- `v8` instead checks whether the model can correctly inspect and use the live Abel CAP interface that the skill is built around.
- This includes tricky semantics such as `invalid_intervention`, `no_directed_path_found`, preview-only counterfactuals, and extension method signatures.

The benchmark spec is documented in [`v8/benchmark_spec.md`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v8/benchmark_spec.md), and the runnable harness is [`v8/test_script.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v8/test_script.py).

---

## v9 — FutureX-Style LLM Casebook

`v9` is not another finished A/B run. It is the new casebook layer that should feed the next benchmark after the local `causal-abel` skill update to `1.0.7`.

Headline properties:

- human-authored casebook shapes modeled after FutureX scoring formats
- grounded to a live `2026-03-25 (GMT+8)` Abel CAP snapshot
- useful as a diagnostic or internal-skills regression set
- too tool-facing to serve as the main headline benchmark, because some prompts still read like Abel-aware questions

---

## v10 — Natural-Intent Casebook

`v10` is the corrected successor to `v9`.

The design goal is simple: every prompt should sound like something a smart user with no knowledge of Abel, CAP verbs, node IDs, or skill internals might naturally ask.

Headline properties:

- **40 cases** anchored to the same `2026-03-25 (GMT+8)` live snapshot
- **FutureX-inspired scoring shapes**: interval bins, threshold ladders, winner markets, top-k membership, roster membership, and statement-truth sets
- **Natural-user framing** across seven categories: directional buckets, directional thresholds, ranking, transmission, pressure tests, coverage, and market-story reads
- **Non-tool-facing prompts**: no direct Abel / CAP / verb-contract questions in the prompt layer

Files:

- Dataset: [`v10/natural_intent_cases.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v10/natural_intent_cases.json)
- Overview: [`v10/cases.md`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v10/cases.md)
- Spec: [`v10/casebook_spec.md`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v10/casebook_spec.md)
- Generator: [`v10/build_natural_intent_casebook.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v10/build_natural_intent_casebook.py)

---

## v11 — Split Benchmark Package

`v11` keeps the same natural-intent benchmark direction as `v10`, but repackages it into a cleaner dataset layout:

- `questions.json` contains only prompts, options, and metadata
- `ground_truth.json` contains only answer keys and grounding
- `artifacts/` stores the raw Abel snapshot evidence used to derive the ground truth

Why this matters:

- it avoids leaking answer keys in the main question file
- it makes evaluation harnesses cleaner
- it preserves the original live snapshot evidence instead of only keeping derived labels

Files:

- Questions: [`v11/questions.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/questions.json)
- Ground Truth: [`v11/ground_truth.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/ground_truth.json)
- Overview: [`v11/cases.md`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/cases.md)
- Spec: [`v11/casebook_spec.md`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/casebook_spec.md)
- Snapshot Facts: [`v11/artifacts/snapshot_facts.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/artifacts/snapshot_facts.json)
- Artifact Manifest: [`v11/artifacts/manifest.json`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/artifacts/manifest.json)
- Builder: [`v11/build_natural_intent_casebook.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/build_natural_intent_casebook.py)
- Capture: [`v11/capture_snapshot_artifacts.py`](/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11/capture_snapshot_artifacts.py)

---

## Files

| File | Description |
|------|-------------|
| `v3/results.json` | v3 full per-case results |
| `v3/test_script.py` | v3 benchmark script (API keys redacted) |
| `v4/results.json` | v4 full per-case results (strict judge) |
| `v4/test_script.py` | v4 benchmark script (API keys redacted) |
| `v4/cases.md` | v4 detailed per-case report (strict judge) |
| `v5/results.json` | Direct Abel CAP live A/B summary for Codex base vs skill |
| `v5/test_script.py` | Reproducible live CAP benchmark harness |
| `v5/cases.md` | Per-task comparison and notable failure analysis |
| `v6/results.json` | FutureX financial-subset A/B summary |
| `v6/test_script.py` | Reproducible FutureX-Past / FutureX-Online harness |
| `v6/cases.md` | Past scoring summary plus current-week live predictions |
| `v7/results.json` | FutureX-Online live-only A/B summary with validity and divergence notes |
| `v7/test_script.py` | Reproducible FutureX-Online live-only harness |
| `v7/rescore_live.py` | Auto-backfill scorer for resolved `FutureX-Online` questions via `FutureX-Past` |
| `v7/cases.md` | Live-only per-task comparison and observed skill-usage evidence |
| `v8/results.json` | CAP-adapted causalbench summary for live Codex base vs skill |
| `v8/test_script.py` | Reproducible live CAP-aligned benchmark harness |
| `v8/cases.md` | Case taxonomy, category scores, and timing notes |
| `v8/benchmark_spec.md` | Design rationale, scoring philosophy, and next-step benchmark plan |
| `v9/futurex_style_cases.json` | LLM-authored FutureX-style casebook with snapshot-grounded answer keys |
| `v9/cases.md` | Compact index of the v9 casebook and answer boxes |
| `v9/casebook_spec.md` | Why the v9 cases are LLM-authored and how they adapt FutureX formats to Abel |
| `v10/natural_intent_cases.json` | Natural-intent casebook with snapshot-grounded answer keys and non-tool-facing prompts |
| `v10/cases.md` | Compact index of the v10 casebook and answer boxes |
| `v10/casebook_spec.md` | Benchmark design rule for natural-user prompts |
| `v10/build_natural_intent_casebook.py` | Reproducible generator for the v10 natural-intent casebook |
| `v11/questions.json` | Prompt-only benchmark input file |
| `v11/ground_truth.json` | Answer keys and grounding for the v11 casebook |
| `v11/cases.md` | Compact prompt index without exposed answer keys |
| `v11/casebook_spec.md` | Packaging rule for the split natural-intent benchmark |
| `v11/build_natural_intent_casebook.py` | Reproducible builder for `questions.json` and `ground_truth.json` |
| `v11/capture_snapshot_artifacts.py` | Live Abel capture script for raw snapshot evidence |
| `v11/artifacts/snapshot_facts.json` | Derived snapshot facts used by the v11 builder |
| `v11/artifacts/manifest.json` | Raw artifact index and capture commands |

---

## Conclusions

### Effectiveness

1. **Abel enables concrete predictions**: LLM alone refuses most financial prediction questions; Abel data gives it enough grounding to commit to specific answers.
2. **+22.6% overall accuracy improvement** with full skill usage and strict judging.
3. **+46.7% improvement on Abel-data subset**: For cases where Abel data was available, accuracy jumped from 20% to 66.7%.
4. **Full skill usage matters**: Using `observe` + `neighbors` + `markov-blanket` (v4) provides richer context than `observe` alone (v3).
5. **Strict judging reveals the real picture**: Lenient judges that accept refusals as "correct" mask Abel's true value.
6. **Capability-aligned benchmarking is a separate need**: `v8` shows that a benchmark can be well aligned to Abel CAP semantics even if it does not yet create an A/B gap between base and skill.
7. **Casebook quality matters**: `v9` revealed the need for a more natural prompt layer, `v10` corrected the prompt style, and `v11` turns that into a cleaner benchmark package with separated prompts, answers, and raw evidence.

### Limitations

1. **Temporal mismatch**: Abel's next-period forecasts vs. days/weeks-ahead questions.
2. **Graph coverage gaps**: SPY, DJI, BTC, XAUUSD, CSI300, Chinese A-shares not in graph.
3. **Multi-asset questions**: Current approach uses one node; should aggregate signals across all mentioned assets.
4. **Explicit prompts reduce separation**: In `v8`, a strong base model can inspect the same live CAP surface and match the skill-assisted run.
5. **Snapshot drift**: `v9`, `v10`, and `v11` are intentionally tied to a `2026-03-25` live CAP snapshot, so answers should be refreshed when the graph or public prediction history changes.

### Recommendations

1. Always use the full skill surface (`observe` + `neighbors` + `markov-blanket`) rather than `observe` alone.
2. Expand Abel's graph to cover major indices, crypto pairs, and precious metals.
3. Add time-horizon awareness to prompts: weight short-term Abel signals differently for day-level vs. month-level questions.
4. For multi-asset questions, query Abel for each mentioned asset and present aggregated signals.
5. Keep `v8` as the regression core, then add a more natural intent-level benchmark layer where routing, workflow choice, and proxy selection matter.
6. Use `v11` as the next A/B input layer, keep `v10` as the readable natural-intent predecessor, and keep `v9` only as a diagnostic set for explicit skill-surface regressions.

---

## References

- [Abel-skills GitHub Repo](https://github.com/Abel-ai-causality/Abel-skills)
- [Futurex-Past Dataset](https://huggingface.co/datasets/futurex-ai/Futurex-Past)
- [Abel SKILL.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/SKILL.md)
- [probe-usage.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/references/probe-usage.md)
- [question-routing.md](https://github.com/Abel-ai-causality/Abel-skills/blob/main/causal-abel/references/question-routing.md)
