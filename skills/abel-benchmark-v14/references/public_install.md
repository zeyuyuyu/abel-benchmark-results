# Public Install Guide

This skill is published in:

- `https://github.com/zeyuyuyu/abel-benchmark-results`
- skill path: `skills/abel-benchmark-v14`

## 1) Install Skill Into Codex

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo zeyuyuyu/abel-benchmark-results \
  --path skills/abel-benchmark-v14
```

Restart Codex after install.

## 2) Bootstrap Benchmark Repository

```bash
python3 ~/.codex/skills/abel-benchmark-v14/scripts/run_pack.py bootstrap-repo
export ABEL_BENCHMARK_REPO=~/abel-benchmark-results
```

If your repository path is different:

```bash
export ABEL_BENCHMARK_REPO=/path/to/abel-benchmark-results
```

Or pass the repo path per command:

```bash
python3 ~/.codex/skills/abel-benchmark-v14/scripts/run_pack.py \
  --repo /path/to/abel-benchmark-results \
  list-packs
```

## 3) Run Packs

```bash
python3 ~/.codex/skills/abel-benchmark-v14/scripts/run_pack.py list-packs
python3 ~/.codex/skills/abel-benchmark-v14/scripts/run_pack.py check-skill
python3 ~/.codex/skills/abel-benchmark-v14/scripts/run_pack.py v14-track-g-past-asof
python3 ~/.codex/skills/abel-benchmark-v14/scripts/run_pack.py v14-track-h-causal-ops
```

## 4) Use From Any LLM Agent

MCP is **not required**. If your agent can run shell commands, use CLI directly.

CLI:

```bash
python3 ~/.codex/skills/abel-benchmark-v14/scripts/benchmark_cli.py \
  --repo /path/to/abel-benchmark-results \
  list-packs
```

MCP server:

```bash
python3 ~/.codex/skills/abel-benchmark-v14/scripts/mcp_server.py --transport stdio
```
