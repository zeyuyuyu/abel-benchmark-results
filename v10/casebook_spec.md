# v10 Natural-Intent Benchmark Spec

## Core Fix

`v9` is too tool-facing.

A normal user does not ask:

- "What range will Abel's next-step observational move for AMD_close fall into?"
- "Which observe.predict calls fail because public CAP has no materialized prediction history?"
- "What does BTC normalize to under the skill rules?"

Those are internal or Abel-aware questions.

`v10` should instead measure whether the skill helps on questions that a non-Abel user could naturally ask.

## Design Rule

Every benchmark prompt should pass this test:

> Would a smart user with no knowledge of Abel, CAP, node IDs, or internal verbs plausibly ask this question?

If the answer is no, the case should not be in the benchmark.

## Good Prompt Shapes

### 1. Natural directional questions

- Which semiconductor name looks strongest right now?
- Which one looks weakest on a short-term read?
- If you had to bucket AMD's next move, which range seems most plausible?

These still map cleanly to live observational signals, but the user intent is natural.

### 2. Natural transmission questions

- If Nvidia gets hit first, which of these names is the clearest spillover candidate?
- Which of these look like real upstream channels into Nvidia, rather than broad market placeholders?
- Is the better story here local company transmission or broad index beta?

These test `graph.paths`, local structure, and routing choices without exposing internal CAP language.

### 3. Natural pressure-test questions

- If you want to stress-test AMD, which shock is more defensible right now: Nvidia or SOXX?
- If you shock Nvidia, does the current graph support a meaningful downstream scenario into AMD or not?

These let the skill use intervention and preview surfaces, but the question stays user-facing.

### 4. Natural coverage / trust questions

- If you want a graph-grounded crypto read today, which is easier to support: ETH or BTC?
- Which of these assets can you actually ground with the current public graph right now?

These indirectly test normalization and availability without asking internal product questions.

## Bad Prompt Shapes

Avoid:

- explicit `Abel` in the user question
- explicit CAP verb names in the user question
- raw node IDs as the main subject of the question
- questions about internal error codes, skip reasons, normalization rules, or materialized-history behavior unless they are wrapped inside a natural user problem

## Benchmark Goal

The benchmark should test:

- whether the model recognizes that a causal graph skill is relevant
- whether it routes into the right graph workflow
- whether it extracts a useful answer to a natural question

It should not primarily test:

- whether the model can restate Abel internals
- whether it can answer direct wrapper-contract questions
- whether it can memorize CAP-specific wording

## Practical Consequence

`v9` should not be used as the main benchmark result.

It can still be kept as a diagnostic or internal-skills regression set.

But the next headline benchmark should be a new `v10` casebook built around natural user intent.
