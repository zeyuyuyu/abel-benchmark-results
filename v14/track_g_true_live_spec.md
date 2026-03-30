# v14 Track G True Live Spec

## Purpose

This pack is the canonical `v14` materialization of true Track G live cases.

It exists to enforce one strict rule:

- `evaluation_regime = live_forward_resolution` must mean the case is genuinely
  unresolved at benchmark authoring time.

## Source

This pack mirrors the current `v13` live benchmark:

- source questions: `v13/questions.json`
- source pending truth metadata: `v13/ground_truth.json`

## Files

- `track_g_true_live_questions.json`
- `track_g_true_live_ground_truth.json`
- `track_g_true_live_cases.md`

## Ground Truth Policy

- Questions are visible.
- Resolution metadata is visible.
- Final answers must remain blank until third-party forward resolution occurs.

That means:

- `answer_box = null`
- `answer_tokens = []`
- `status` is preserved from the source live pack

## Relationship To `public_dev`

`public_dev` may contain FutureX-style exemplars, but if a case already ships
with a visible answer key, it must not use
`evaluation_regime = live_forward_resolution`.

Those development exemplars belong under:

- `evaluation_regime = frozen_evidence_public_dev`

## Current Count

- mirrored live cases: `100`
