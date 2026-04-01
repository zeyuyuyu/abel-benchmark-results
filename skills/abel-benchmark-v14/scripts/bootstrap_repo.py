#!/usr/bin/env python3
"""Bootstrap the public benchmark repository for this skill."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


DEFAULT_REPO_URL = "https://github.com/zeyuyuyu/abel-benchmark-results.git"
DEFAULT_DEST = Path.home() / "abel-benchmark-results"


def looks_like_repo(path: Path) -> bool:
    return (path / "v14").exists() and (path / "scripts" / "run_benchmark.py").exists()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clone benchmark repo for abel-benchmark-v14 skill.")
    parser.add_argument("--repo-url", default=DEFAULT_REPO_URL, help="GitHub clone URL")
    parser.add_argument("--dest", default=str(DEFAULT_DEST), help="Destination directory")
    parser.add_argument("--ref", default="main", help="Git ref to checkout")
    parser.add_argument("--force", action="store_true", help="Remove existing destination before clone")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    dest = Path(args.dest).expanduser().resolve()
    git = shutil.which("git")
    if not git:
        raise SystemExit("git is required for bootstrap-repo.")

    if dest.exists():
        if looks_like_repo(dest):
            print(f"[bootstrap] repo already present: {dest}")
            print(f"export ABEL_BENCHMARK_REPO=\"{dest}\"")
            return
        if any(dest.iterdir()) and not args.force:
            raise SystemExit(
                f"Destination exists and is not benchmark repo: {dest}. "
                "Use --force to replace."
            )
        if args.force:
            shutil.rmtree(dest)

    dest.parent.mkdir(parents=True, exist_ok=True)
    clone_cmd = [git, "clone", "--depth", "1", "--branch", args.ref, args.repo_url, str(dest)]
    completed = subprocess.run(clone_cmd, check=False)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)

    if not looks_like_repo(dest):
        raise SystemExit(f"Cloned repo does not contain expected benchmark files: {dest}")

    print(f"[bootstrap] cloned: {dest}")
    print(f"export ABEL_BENCHMARK_REPO=\"{dest}\"")


if __name__ == "__main__":
    main()
