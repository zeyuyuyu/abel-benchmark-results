# Cross-Agent Usage (Claude Code / OpenClaw / Any MCP Client)

This skill now exposes a **generic benchmark API** and an **MCP server** so it
can be used by non-Codex agents too.

## 1) Generic CLI (works in any shell-enabled agent)

```bash
python3 ~/.codex/skills/abel-benchmark-v14/scripts/benchmark_cli.py --repo /path/to/abel-benchmark-results list-packs
python3 ~/.codex/skills/abel-benchmark-v14/scripts/benchmark_cli.py --repo /path/to/abel-benchmark-results describe-pack --pack-id track_g_past_asof
python3 ~/.codex/skills/abel-benchmark-v14/scripts/benchmark_cli.py --repo /path/to/abel-benchmark-results get-cases --pack-id track_h_causal_ops --limit 5
python3 ~/.codex/skills/abel-benchmark-v14/scripts/benchmark_cli.py --repo /path/to/abel-benchmark-results score-predictions --pack-id track_h_causal_ops --predictions-file /path/to/preds.json
```

## 2) MCP Server (stdio transport)

```bash
python3 ~/.codex/skills/abel-benchmark-v14/scripts/mcp_server.py --transport stdio
```

Server tools:

- `list_benchmark_packs`
- `describe_benchmark_pack`
- `get_benchmark_cases`
- `score_benchmark_predictions`
- `run_benchmark_pack`
- `bootstrap_benchmark_repo`

## 3) MCP Client Wiring (generic template)

Use a stdio MCP config entry with:

- command: `python3`
- args: `["~/.codex/skills/abel-benchmark-v14/scripts/mcp_server.py", "--transport", "stdio"]`
- env (optional): `ABEL_BENCHMARK_REPO=/path/to/abel-benchmark-results`

Most MCP-compatible agents (including Claude Code/OpenClaw style clients) can
reuse this pattern with their own MCP config format.
