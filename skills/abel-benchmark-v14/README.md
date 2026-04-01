# abel-benchmark-v14 (Public Skill)

This folder packages the v14 benchmark workflow as a reusable public skill
bundle that can be installed from GitHub.

## What Is Included

- `SKILL.md`: skill contract and supported packs
- `scripts/run_pack.py`: command router to benchmark packs
- `scripts/bootstrap_repo.py`: clone helper for benchmark repo bootstrap
- `scripts/benchmark_cli.py`: cross-agent CLI (not Codex-specific)
- `scripts/mcp_server.py`: MCP server for any MCP-compatible agent
- `references/track_routing.md`: track family and evaluation regime mapping
- `references/public_install.md`: internet installation instructions
- `references/cross_agent_usage.md`: Claude/OpenClaw/generic MCP usage
- `.env.example`: required API key variable template

## Install

### Repo-local mode (works for any shell-enabled agent)

```bash
git clone https://github.com/zeyuyuyu/abel-benchmark-results.git
cd abel-benchmark-results
export ABEL_BENCHMARK_REPO="$PWD"
export ABEL_BENCHMARK_SKILL_ROOT="$PWD/skills/abel-benchmark-v14"
```

### Codex-installed mode

Install the GitHub skill bundle with:

- repo: `zeyuyuyu/abel-benchmark-results`
- path: `skills/abel-benchmark-v14`

Then point to the installed skill root:

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export ABEL_BENCHMARK_SKILL_ROOT="$CODEX_HOME/skills/abel-benchmark-v14"
```

## Cross-Agent (Any LLM Agent)

MCP is optional. The minimal path is:
- load `questions` / `ground_truth` json files
- run scoring via `benchmark_cli.py`

CLI mode:

```bash
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/benchmark_cli.py" \
  --repo /path/to/abel-benchmark-results \
  list-packs
```

MCP mode:

```bash
export ABEL_BENCHMARK_REPO=/path/to/abel-benchmark-results
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/mcp_server.py" --transport stdio
```

See:
- `references/cross_agent_usage.md`

## Quick Start

```bash
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/run_pack.py" --repo "$ABEL_BENCHMARK_REPO" list-packs
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/run_pack.py" --repo "$ABEL_BENCHMARK_REPO" check-skill
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/run_pack.py" --repo "$ABEL_BENCHMARK_REPO" v14-track-g-past-asof
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/run_pack.py" --repo "$ABEL_BENCHMARK_REPO" v14-build-public-manifest
```
