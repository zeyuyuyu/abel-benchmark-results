# abel-benchmark-v14 (Repo-Local Skill)

This folder packages the v14 benchmark workflow as a reusable skill bundle.

## What Is Included

- `SKILL.md`: skill contract and supported packs
- `scripts/run_pack.py`: command router to benchmark packs
- `references/track_routing.md`: track family and evaluation regime mapping
- `.env.example`: required API key variable template

## Quick Start

```bash
cd /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results
python3 skills/abel-benchmark-v14/scripts/run_pack.py check-skill
python3 skills/abel-benchmark-v14/scripts/run_pack.py v14-track-g-past-asof
python3 skills/abel-benchmark-v14/scripts/run_pack.py v14-build-public-manifest
```
