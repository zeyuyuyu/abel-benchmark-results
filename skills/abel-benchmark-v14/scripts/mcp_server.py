#!/usr/bin/env python3
"""MCP server exposing benchmark tools for any LLM agent."""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
from pathlib import Path
from typing import Any

from mcp.server import FastMCP

from benchmark_api import (
    get_cases,
    get_pack,
    list_packs,
    resolve_repo_root,
    run_repo_pack,
    score_predictions,
)


HERE = Path(__file__).resolve()
SCRIPTS_DIR = HERE.parent
BOOTSTRAP_SCRIPT = SCRIPTS_DIR / "bootstrap_repo.py"


def _resolve_repo_or_error(repo: str | None) -> Path:
    return resolve_repo_root(repo)


def build_server(*, host: str, port: int) -> FastMCP:
    server = FastMCP(
        name="abel-benchmark-v14",
        instructions=(
            "Use these tools to list benchmark packs, fetch cases, score predictions, "
            "and run benchmark commands across Track G and Track H."
        ),
        host=host,
        port=port,
    )

    @server.tool(
        name="list_benchmark_packs",
        description="List publicly available benchmark packs with evaluation regimes.",
    )
    def list_benchmark_packs(repo: str | None = None) -> dict[str, Any]:
        repo_root = _resolve_repo_or_error(repo)
        return {"repo_root": str(repo_root), "packs": list_packs(repo_root)}

    @server.tool(
        name="describe_benchmark_pack",
        description="Return full metadata for one benchmark pack by pack_id.",
    )
    def describe_benchmark_pack(pack_id: str, repo: str | None = None) -> dict[str, Any]:
        repo_root = _resolve_repo_or_error(repo)
        return {"repo_root": str(repo_root), "pack": get_pack(repo_root, pack_id)}

    @server.tool(
        name="get_benchmark_cases",
        description=(
            "Fetch cases from a benchmark pack. Set include_ground_truth=true only "
            "for scoring/debug flows, not for model-answer generation."
        ),
    )
    def get_benchmark_cases(
        pack_id: str,
        repo: str | None = None,
        include_ground_truth: bool = False,
        limit: int | None = None,
        case_ids_csv: str | None = None,
    ) -> dict[str, Any]:
        repo_root = _resolve_repo_or_error(repo)
        case_ids = None
        if case_ids_csv:
            case_ids = [item.strip() for item in case_ids_csv.split(",") if item.strip()]
        return get_cases(
            repo_root,
            pack_id,
            include_ground_truth=include_ground_truth,
            limit=limit,
            case_ids=case_ids,
        )

    @server.tool(
        name="score_benchmark_predictions",
        description=(
            "Score predictions against benchmark ground truth. predictions_json may be "
            "a dict with predictions list, a list of {id,prediction}, or id->prediction map."
        ),
    )
    def score_benchmark_predictions(
        pack_id: str,
        predictions_json: str,
        repo: str | None = None,
    ) -> dict[str, Any]:
        repo_root = _resolve_repo_or_error(repo)
        payload = json.loads(predictions_json)
        return score_predictions(repo_root, pack_id, payload)

    @server.tool(
        name="run_benchmark_pack",
        description=(
            "Run a benchmark pack via scripts/run_benchmark.py. This is optional and "
            "mainly used for benchmark automation in environments with codex CLI."
        ),
    )
    def run_benchmark_pack(
        pack: str,
        repo: str | None = None,
        extra_args: str = "",
    ) -> dict[str, Any]:
        repo_root = _resolve_repo_or_error(repo)
        parsed_args = shlex.split(extra_args) if extra_args.strip() else []
        return run_repo_pack(repo_root, pack, parsed_args)

    @server.tool(
        name="bootstrap_benchmark_repo",
        description="Clone the public abel-benchmark-results repo locally for this benchmark skill.",
    )
    def bootstrap_benchmark_repo(
        dest: str = "~/abel-benchmark-results",
        ref: str = "main",
        repo_url: str = "https://github.com/zeyuyuyu/abel-benchmark-results.git",
        force: bool = False,
    ) -> dict[str, Any]:
        cmd = [
            "python3",
            str(BOOTSTRAP_SCRIPT),
            "--dest",
            dest,
            "--ref",
            ref,
            "--repo-url",
            repo_url,
        ]
        if force:
            cmd.append("--force")
        completed = subprocess.run(cmd, capture_output=True, text=True, check=False)
        return {
            "command": cmd,
            "returncode": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }

    return server


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run abel-benchmark-v14 MCP server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse", "streamable-http"],
        default="stdio",
        help="MCP transport mode",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    server = build_server(host=args.host, port=args.port)
    server.run(transport=args.transport)


if __name__ == "__main__":
    main()
