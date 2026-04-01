#!/usr/bin/env python3
"""Entry point for the v14 benchmark skill package."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve()
SCRIPTS_DIR = HERE.parent


REPO_PACK_TO_CMD = {
    "list-packs": ["python3", "scripts/run_benchmark.py", "list-packs"],
    "check-skill": ["python3", "scripts/run_benchmark.py", "check-skill"],
    "v14-public-dev": ["python3", "scripts/run_benchmark.py", "v14-public-dev"],
    "v14-track-g-past-asof": ["python3", "scripts/run_benchmark.py", "v14-track-g-past-asof"],
    "v14-track-g-past-asof-finance15": [
        "python3",
        "scripts/run_benchmark.py",
        "v14-track-g-past-asof-finance15",
    ],
    "v14-track-g-true-live": ["python3", "scripts/run_benchmark.py", "v14-track-g-true-live"],
    "v14-track-g-true-live-official": [
        "python3",
        "scripts/run_benchmark.py",
        "v14-track-g-true-live-official",
    ],
    "v14-track-g-true-live-custom": [
        "python3",
        "scripts/run_benchmark.py",
        "v14-track-g-true-live-custom",
    ],
    "v14-track-g-true-live-status": [
        "python3",
        "scripts/run_benchmark.py",
        "v14-track-g-true-live-status",
    ],
    "v14-track-h-causal-ops": ["python3", "v14/run_track_h_causal_ops_benchmark.py"],
    "v14-track-h-build-results": ["python3", "v14/build_track_h_causal_ops_results.py"],
    "v14-build-public-manifest": ["python3", "v14/build_public_benchmark_manifest.py"],
}

NON_REPO_PACK_TO_CMD = {
    "bootstrap-repo": ["python3", str(SCRIPTS_DIR / "bootstrap_repo.py")],
}


def looks_like_repo(path: Path) -> bool:
    return (path / "v14").exists() and (path / "scripts" / "run_benchmark.py").exists()


def resolve_repo_root(cli_repo: str | None) -> Path:
    if cli_repo:
        path = Path(cli_repo).expanduser().resolve()
        if looks_like_repo(path):
            return path
        raise SystemExit(f"--repo does not look valid: {path}")

    override = os.getenv("ABEL_BENCHMARK_REPO", "").strip()
    if override:
        path = Path(override).expanduser().resolve()
        if looks_like_repo(path):
            return path
        raise SystemExit(f"ABEL_BENCHMARK_REPO does not look valid: {path}")

    for parent in HERE.parents:
        if looks_like_repo(parent):
            return parent

    cwd = Path.cwd().resolve()
    if looks_like_repo(cwd):
        return cwd

    home_candidates = [
        Path.home() / "abel-benchmark-results",
        Path.home() / "workspace" / "abel-benchmark-results",
    ]
    for path in home_candidates:
        if looks_like_repo(path):
            return path

    raise SystemExit(
        "Could not find abel-benchmark-results repo. Run `bootstrap-repo` first, "
        "or set ABEL_BENCHMARK_REPO=/path/to/abel-benchmark-results."
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run v14 benchmark packs from the skill package")
    parser.add_argument("--repo", help="Path to abel-benchmark-results (optional)")
    parser.add_argument("pack", choices=sorted({*REPO_PACK_TO_CMD.keys(), *NON_REPO_PACK_TO_CMD.keys()}))
    parser.add_argument("extra_args", nargs=argparse.REMAINDER)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.pack in NON_REPO_PACK_TO_CMD:
        cmd = NON_REPO_PACK_TO_CMD[args.pack] + args.extra_args
        print(f"[abel-benchmark-v14] cwd={SCRIPTS_DIR}")
        print(f"[abel-benchmark-v14] cmd={' '.join(cmd)}")
        completed = subprocess.run(cmd, cwd=SCRIPTS_DIR, env=os.environ.copy(), check=False)
        sys.exit(completed.returncode)

    repo_root = resolve_repo_root(args.repo)
    cmd = REPO_PACK_TO_CMD[args.pack] + args.extra_args
    env = os.environ.copy()
    print(f"[abel-benchmark-v14] cwd={repo_root}")
    print(f"[abel-benchmark-v14] cmd={' '.join(cmd)}")
    completed = subprocess.run(cmd, cwd=repo_root, env=env, check=False)
    sys.exit(completed.returncode)


if __name__ == "__main__":
    main()
