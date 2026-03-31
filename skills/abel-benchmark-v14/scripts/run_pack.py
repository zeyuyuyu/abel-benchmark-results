#!/usr/bin/env python3
"""Entry point for the repo-local v14 benchmark skill package."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3]


PACK_TO_CMD = {
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run v14 benchmark packs from the skill package")
    parser.add_argument("pack", choices=sorted(PACK_TO_CMD.keys()))
    parser.add_argument("extra_args", nargs=argparse.REMAINDER)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cmd = PACK_TO_CMD[args.pack] + args.extra_args
    env = os.environ.copy()
    print(f"[abel-benchmark-v14] cwd={REPO_ROOT}")
    print(f"[abel-benchmark-v14] cmd={' '.join(cmd)}")
    completed = subprocess.run(cmd, cwd=REPO_ROOT, env=env, check=False)
    sys.exit(completed.returncode)


if __name__ == "__main__":
    main()
