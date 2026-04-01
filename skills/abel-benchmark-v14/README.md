# abel-benchmark-v14 (Public Skill)

This folder packages the v14 benchmark workflow as a reusable public skill
bundle that can be installed from GitHub.

## What Is Included

- `SKILL.md`: skill contract and supported packs
- `scripts/run_pack.py`: command router to benchmark packs
- `scripts/bootstrap_repo.py`: clone helper for benchmark repo bootstrap
- `references/track_routing.md`: track family and evaluation regime mapping
- `references/public_install.md`: internet installation instructions
- `.env.example`: required API key variable template

## Install (From GitHub)

Use Codex skill installer:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo zeyuyuyu/abel-benchmark-results \
  --path skills/abel-benchmark-v14
```

Then restart Codex.

## Quick Start

```bash
python3 ~/.codex/skills/abel-benchmark-v14/scripts/run_pack.py bootstrap-repo
export ABEL_BENCHMARK_REPO=~/abel-benchmark-results

python3 ~/.codex/skills/abel-benchmark-v14/scripts/run_pack.py check-skill
python3 ~/.codex/skills/abel-benchmark-v14/scripts/run_pack.py v14-track-g-past-asof
python3 ~/.codex/skills/abel-benchmark-v14/scripts/run_pack.py v14-build-public-manifest
```
