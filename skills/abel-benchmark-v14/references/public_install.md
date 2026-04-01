# Public Install Guide

This skill is published in:

- `https://github.com/zeyuyuyu/abel-benchmark-results`
- skill path: `skills/abel-benchmark-v14`

## 1) Clone The Public Repository

```bash
git clone https://github.com/zeyuyuyu/abel-benchmark-results.git
cd abel-benchmark-results
export ABEL_BENCHMARK_REPO="$PWD"
export ABEL_BENCHMARK_SKILL_ROOT="$PWD/skills/abel-benchmark-v14"
```

## 2) Install Skill Into Codex (Optional)

If you want Codex-native installation, install the GitHub skill bundle with:

- repo: `zeyuyuyu/abel-benchmark-results`
- path: `skills/abel-benchmark-v14`

Then set:

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export ABEL_BENCHMARK_SKILL_ROOT="$CODEX_HOME/skills/abel-benchmark-v14"
```

Restart Codex after install if your environment requires it.

## 3) Bootstrap Benchmark Repository

```bash
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/run_pack.py" --repo "$ABEL_BENCHMARK_REPO" list-packs
```

If your repository path is different:

```bash
export ABEL_BENCHMARK_REPO=/path/to/abel-benchmark-results
export ABEL_BENCHMARK_SKILL_ROOT="$ABEL_BENCHMARK_REPO/skills/abel-benchmark-v14"
```

Or pass the repo path per command:

```bash
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/run_pack.py" \
  --repo /path/to/abel-benchmark-results \
  list-packs
```

## 4) Run Packs

```bash
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/run_pack.py" --repo "$ABEL_BENCHMARK_REPO" list-packs
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/run_pack.py" --repo "$ABEL_BENCHMARK_REPO" check-skill
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/run_pack.py" --repo "$ABEL_BENCHMARK_REPO" v14-track-g-past-asof
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/run_pack.py" --repo "$ABEL_BENCHMARK_REPO" v14-track-h-causal-ops
```

## 5) Use From Any LLM Agent

MCP is **not required**. If your agent can run shell commands, use CLI directly.

CLI:

```bash
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/benchmark_cli.py" \
  --repo /path/to/abel-benchmark-results \
  list-packs
```

MCP server:

```bash
export ABEL_BENCHMARK_REPO=/path/to/abel-benchmark-results
python3 "$ABEL_BENCHMARK_SKILL_ROOT/scripts/mcp_server.py" --transport stdio
```
