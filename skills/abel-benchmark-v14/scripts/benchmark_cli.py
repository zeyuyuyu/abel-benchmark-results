#!/usr/bin/env python3
"""Cross-agent CLI for the Abel benchmark packs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark_api import (
    get_cases,
    get_pack,
    list_packs,
    resolve_repo_root,
    run_repo_pack,
    score_predictions,
)


def _print_json(payload: Any) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def _load_predictions(path: Path) -> Any:
    if not path.exists():
        raise ValueError(f"Predictions file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Cross-agent benchmark CLI")
    parser.add_argument("--repo", help="Path to abel-benchmark-results repo")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list-packs")

    describe = sub.add_parser("describe-pack")
    describe.add_argument("--pack-id", required=True)

    get_cases_cmd = sub.add_parser("get-cases")
    get_cases_cmd.add_argument("--pack-id", required=True)
    get_cases_cmd.add_argument("--include-ground-truth", action="store_true")
    get_cases_cmd.add_argument("--limit", type=int)
    get_cases_cmd.add_argument("--case-ids", nargs="*")

    score_cmd = sub.add_parser("score-predictions")
    score_cmd.add_argument("--pack-id", required=True)
    score_cmd.add_argument("--predictions-file", required=True)

    run_cmd = sub.add_parser("run-pack")
    run_cmd.add_argument("--pack", required=True)
    run_cmd.add_argument("extra_args", nargs=argparse.REMAINDER)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = resolve_repo_root(args.repo)

    if args.command == "list-packs":
        _print_json({"repo_root": str(repo_root), "packs": list_packs(repo_root)})
        return

    if args.command == "describe-pack":
        _print_json({"repo_root": str(repo_root), "pack": get_pack(repo_root, args.pack_id)})
        return

    if args.command == "get-cases":
        payload = get_cases(
            repo_root,
            args.pack_id,
            include_ground_truth=args.include_ground_truth,
            limit=args.limit,
            case_ids=args.case_ids,
        )
        _print_json(payload)
        return

    if args.command == "score-predictions":
        predictions_path = Path(args.predictions_file).expanduser().resolve()
        predictions = _load_predictions(predictions_path)
        payload = score_predictions(repo_root, args.pack_id, predictions)
        payload["predictions_file"] = str(predictions_path)
        _print_json(payload)
        return

    if args.command == "run-pack":
        payload = run_repo_pack(repo_root, args.pack, args.extra_args)
        _print_json(payload)
        return

    raise ValueError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
