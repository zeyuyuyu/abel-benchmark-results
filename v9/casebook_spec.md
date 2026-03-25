# v9 Casebook Spec

## Goal

`v9` is a human-authored, FutureX-inspired casebook for `causal-abel` after the local skill was updated to `1.0.7`.

The key change from the earlier draft is methodological:

- cases are now written by the LLM as benchmark questions
- live Abel CAP facts are used only to anchor the answer key
- the result should feel closer to real benchmark markets and less like a wrapper-generated template set

## What We Borrow From FutureX

We are not copying generic future-event domains like sports or elections.

We are borrowing the parts of `FutureX` that make cases easy to score and compare:

- interval bins
- monotonic threshold ladders
- winner markets
- top-k membership
- roster / semifinal membership
- statement-truth sets

## What We Adapt To Abel

Those same formats are mapped onto `causal-abel` abilities that the updated skill actually emphasizes:

- graph-first local reads
- path reasoning
- intervention-based pressure testing
- counterfactual preview
- observation availability boundaries
- latest node-normalization rules, especially crypto aliases such as `BTCUSD_close` and `ETHUSD_close`

## Updated Skill Constraints Incorporated

This casebook follows the latest local `causal-abel` guidance:

1. structure first, prediction second
2. use the public CAP surface directly
3. use `BTCUSD_close` / `ETHUSD_close` style crypto nodes
4. treat unavailable observation history as an important benchmark boundary
5. keep prompts natural and benchmark-like instead of protocol-documentation-like

## Scope

`v9` focuses on direct-graph and pressure-test cases because those are easiest to score exactly.

It intentionally includes:

- observation range and threshold questions
- winner and top-k baskets
- driver and parent membership questions
- path-existence questions
- intervention semantics
- counterfactual-preview semantics
- latest availability and crypto-normalization consequences

## Intended Use

This casebook is the input layer for the next A/B benchmark:

- `llm only`
- `llm + causal-abel`

Compared with `v8`, these prompts should create more pressure on workflow choice because they look more like benchmark markets and less like direct contract-inspection asks.

## Note On Snapshot Semantics

Answers in `v9` are tied to a live CAP snapshot from `2026-03-25 (GMT+8)`.

That is intentional:

- the prompts are human-authored
- the answer key is snapshot-grounded
- if the CAP graph or public prediction history changes later, the casebook should be refreshed rather than silently reused
