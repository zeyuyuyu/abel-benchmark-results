# v12 General-Finance Challenge Spec

## Why v12 Exists

`v11` fixed the prompt layer, but two problems remained:

1. Too many cases were still close to direct snapshot lookup.
2. The old harness ran inside the benchmark repo, so a model could theoretically inspect local answer files.

`v12` fixes both:

- the prompts stay general and user-facing
- the cases are biased toward proxy choice, guardrails, and route discrimination
- the harness runs in an isolated scratch workspace and explicitly forbids local answer-key lookup

## Design Rule

Every prompt should sound like a normal market question from a PM, trader, or strategist who has never heard of Abel, CAP, node IDs, or internal verbs.

Good examples:

- Which crypto proxy is safest to lean on right now?
- If you need a shortcut stand-in for Nvidia, which one is least misleading?
- Which names actually belong on the live watchlist for AMD?

Bad examples:

- Which Abel node normalizes from BTC?
- Which CAP verb should I call?
- What skip reason did the server return?

## What v12 Tries To Measure

This is a targeted challenge set, not a neutral broad benchmark.

It is designed to test whether `codex + causal-abel` is better than `codex only` at:

- choosing the right market proxy
- refusing weak but intuitive shortcuts
- separating real local transmission from broad beta placeholders
- respecting supportability boundaries
- handling stress-test claims without overclaiming

## Ground Truth Policy

Ground truth comes from the live Abel snapshot stored in `artifacts/`.

- `questions.json` contains only prompts
- `ground_truth.json` contains answer keys and grounding
- `artifacts/` stores the raw probe evidence used to derive those answers

## Prompt Shapes In v12

`v12` focuses on these natural question families:

1. Proxy selection
2. Coverage / supportability guardrails
3. Route membership
4. Shortcut rejection
5. Stress-test boundary handling

These are intentionally harder for a strong generic model than direct "what range is AMD in?" style prompts, because the wrong intuitive answer is often the tempting one.
