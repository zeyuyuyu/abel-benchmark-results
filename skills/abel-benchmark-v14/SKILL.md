---
name: abel-benchmark-v14
description: >
  Repo-local skill for running and publishing the v14 Abel benchmark packs,
  including Track G (true-live / past-asof with search cutoff) and Track H.
---

Use this skill when the task is to run, score, compare, or publish benchmark
results for:

- `codex only` vs `codex + skill`
- v14 public-dev and Track G/Track H packs
- public benchmark index / manifest updates

Workspace:
- `/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results`

## Prerequisites

1. `codex` CLI is available in PATH.
2. `ABEL_API_KEY` is configured (or available via causal-abel `.env.skills`).
3. The latest `causal-abel` skill is installed if running `+ skill` A/B.

## Command Router

Use the wrapper:

```bash
python3 /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/skills/abel-benchmark-v14/scripts/run_pack.py <pack> [extra args...]
```

Supported packs:

- `list-packs`
- `check-skill`
- `v14-public-dev`
- `v14-track-g-past-asof`
- `v14-track-g-past-asof-finance15`
- `v14-track-g-true-live`
- `v14-track-g-true-live-official`
- `v14-track-g-true-live-custom`
- `v14-track-g-true-live-status`
- `v14-track-h-causal-ops`
- `v14-track-h-build-results`
- `v14-build-public-manifest`

## Track-G Semantics

- `historical_asof_search_cutoff`: search allowed, but never after each case's
  `search_cutoff`.
- `live_forward_resolution`: unresolved future cases; ground truth remains blank
  until resolution.

Reference:
- `references/track_routing.md`
