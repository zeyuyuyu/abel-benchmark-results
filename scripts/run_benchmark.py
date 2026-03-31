#!/usr/bin/env python3
"""Unified benchmark router for the Abel benchmark repository."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
BENCH = REPO.parent / ".bench"
V14_DIR = REPO / "v14"
V13_DIR = REPO / "v13"
CAUSAL_ABEL = Path.home() / ".codex/skills/causal-abel"
CAUSAL_ABEL_ENV = CAUSAL_ABEL / ".env.skills"


def run(cmd: list[str], *, cwd: Path | None = None, env: dict[str, str] | None = None) -> str:
    completed = subprocess.run(
        cmd,
        cwd=str(cwd or REPO),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        sys.stderr.write(completed.stdout)
        sys.stderr.write(completed.stderr)
        raise SystemExit(completed.returncode)
    return completed.stdout


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_api_key() -> str:
    direct = os.getenv("ABEL_API_KEY", "").strip()
    if direct:
        return direct
    if not CAUSAL_ABEL_ENV.exists():
        raise SystemExit(f"Missing ABEL_API_KEY and missing {CAUSAL_ABEL_ENV}")
    for raw in CAUSAL_ABEL_ENV.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.strip() == "ABEL_API_KEY":
            parsed = value.strip().strip('"').strip("'")
            if parsed:
                return parsed
    raise SystemExit("ABEL_API_KEY not found in causal-abel .env.skills")


def newest_summary(prefix: str) -> Path:
    matches = sorted(
        BENCH.glob(f"{prefix}-*/summary.json"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    if not matches:
        raise SystemExit(f"No summary found for prefix {prefix}")
    return matches[0]


def track_g_true_live_case_ids(*, source_type: str | None = None) -> list[str]:
    data = load_json(V14_DIR / "track_g_true_live_questions.json")
    cases = data["cases"]
    if source_type:
        cases = [case for case in cases if case.get("source_type") == source_type]
    return [case["id"] for case in cases]


def track_g_past_asof_finance_case_ids() -> list[str]:
    data = load_json(V14_DIR / "track_g_past_asof_questions.json")
    return [case["id"] for case in data["cases"] if case.get("category") != "unlabeled"]


def copy_track_g_past_asof_results(label: str) -> tuple[Path, Path]:
    src_json = V14_DIR / "track_g_past_asof_results.json"
    src_md = V14_DIR / "track_g_past_asof_results.md"
    dst_json = V14_DIR / f"track_g_past_asof_results.{label}.json"
    dst_md = V14_DIR / f"track_g_past_asof_results.{label}.md"
    shutil.copy2(src_json, dst_json)
    shutil.copy2(src_md, dst_md)
    return dst_json, dst_md


def list_packs() -> None:
    packs = {
        "check-skill": "Verify causal-abel runtime health",
        "v14-public-dev": "Run v14 public-dev A/B and write repo reports",
        "v14-track-g-past-asof": "Run full Track G past-asof (historical_asof_search_cutoff)",
        "v14-track-g-past-asof-finance15": "Run Track G past-asof finance-tagged 15-case slice",
        "v14-track-g-past-asof-case-ids": "Run Track G past-asof for explicit case IDs",
        "v14-track-g-true-live": "Run Track G true-live prediction pass (no scoring yet)",
        "v14-track-g-true-live-official": "Run only official FutureX-Online slice",
        "v14-track-g-true-live-custom": "Run only custom live slice",
        "v14-track-g-true-live-status": "Show Track G true-live pending/resolved status",
        "v14-track-h-causal-ops": "Run Track H causal network operations A/B",
        "v14-track-h-build-results": "Build Track H repo-facing json/markdown from summary",
        "v14-build-public-manifest": "Build v14 public benchmark index and manifest",
    }
    print(json.dumps(packs, indent=2, ensure_ascii=False))


def check_skill() -> None:
    api_key = read_api_key()
    probe = CAUSAL_ABEL / "scripts" / "cap_probe.py"
    if not probe.exists():
        raise SystemExit(f"Missing causal-abel probe at {probe}")
    env = os.environ.copy()
    env["ABEL_API_KEY"] = api_key
    outputs = {
        "normalize": run(["python3", str(probe), "normalize-node", "NVDA"], env=env),
        "capabilities": run(
            ["python3", str(probe), "--base-url", "https://cap.abel.ai/api", "capabilities"],
            env=env,
        ),
        "methods": run(
            [
                "python3",
                str(probe),
                "--base-url",
                "https://cap.abel.ai/api",
                "methods",
                "extensions.abel.observe_predict_resolved_time",
            ],
            env=env,
        ),
    }
    print(json.dumps({k: json.loads(v) for k, v in outputs.items()}, indent=2, ensure_ascii=False))


def v14_public_dev() -> None:
    runner = V14_DIR / "run_public_dev_benchmark.py"
    print(run(["python3", str(runner)]).strip())


def v14_track_g_past_asof(
    timeout_seconds: int,
    *,
    case_ids: list[str] | None = None,
    label: str | None = None,
) -> None:
    runner = V14_DIR / "run_track_g_past_asof_benchmark.py"
    formatter = V14_DIR / "build_track_g_past_asof_results.py"
    cmd = ["python3", str(runner), "--batch-size", "1", "--timeout-seconds", str(timeout_seconds)]
    if case_ids:
        cmd.extend(["--case-ids", *case_ids])
    print(run(cmd).strip())
    summary = newest_summary("v14-track-g-past-asof-results")
    print(run(["python3", str(formatter), str(summary)]).strip())
    if label:
        dst_json, dst_md = copy_track_g_past_asof_results(label)
        print(f"Copied results to {dst_json}")
        print(f"Copied results to {dst_md}")


def run_v13_live_with_filters(
    *,
    case_ids: list[str] | None = None,
    source_types: list[str] | None = None,
    max_batch_prompt_chars: int | None = None,
) -> None:
    runner = V13_DIR / "test_script.py"
    env = os.environ.copy()
    if case_ids:
        env["BENCH_CASE_IDS"] = ",".join(case_ids)
    if source_types:
        env["BENCH_SOURCE_TYPES"] = ",".join(source_types)
    if max_batch_prompt_chars:
        env["BENCH_MAX_BATCH_PROMPT_CHARS"] = str(max_batch_prompt_chars)
    print(run(["python3", str(runner)], env=env).strip())


def v14_track_g_true_live(*, source_type: str | None = None, max_batch_prompt_chars: int | None = None) -> None:
    if source_type is None:
        case_ids = track_g_true_live_case_ids()
    else:
        case_ids = track_g_true_live_case_ids(source_type=source_type)
    if not case_ids:
        raise SystemExit("No Track G true-live case IDs selected.")
    run_v13_live_with_filters(
        case_ids=case_ids,
        source_types=[source_type] if source_type else None,
        max_batch_prompt_chars=max_batch_prompt_chars,
    )


def v14_track_g_true_live_status() -> None:
    gt = load_json(V14_DIR / "track_g_true_live_ground_truth.json")
    q = load_json(V14_DIR / "track_g_true_live_questions.json")
    pending = sum(1 for case in gt["cases"] if case.get("status") == "pending")
    resolved = sum(1 for case in gt["cases"] if case.get("status") == "resolved")
    official = sum(1 for case in q["cases"] if case.get("source_type") == "futurex_online")
    custom = sum(1 for case in q["cases"] if case.get("source_type") == "custom_live")
    payload = {
        "track": "v14-track-g-true-live",
        "case_count": q.get("case_count", len(q["cases"])),
        "status": {"pending": pending, "resolved": resolved},
        "source_breakdown": {"futurex_online": official, "custom_live": custom},
        "files": {
            "questions": str(V14_DIR / "track_g_true_live_questions.json"),
            "ground_truth": str(V14_DIR / "track_g_true_live_ground_truth.json"),
        },
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def v14_track_h_causal_ops(batch_size: int, timeout_seconds: int, case_ids: list[str] | None = None) -> None:
    runner = V14_DIR / "run_track_h_causal_ops_benchmark.py"
    cmd = ["python3", str(runner), "--batch-size", str(batch_size), "--timeout-seconds", str(timeout_seconds)]
    if case_ids:
        cmd.extend(["--case-ids", *case_ids])
    print(run(cmd).strip())


def v14_track_h_build_results(summary_path: Path) -> None:
    formatter = V14_DIR / "build_track_h_causal_ops_results.py"
    print(run(["python3", str(formatter), str(summary_path)]).strip())


def v14_build_public_manifest() -> None:
    builder = V14_DIR / "build_public_benchmark_manifest.py"
    print(run(["python3", str(builder)]).strip())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list-packs")
    sub.add_parser("check-skill")
    sub.add_parser("v14-public-dev")

    past = sub.add_parser("v14-track-g-past-asof")
    past.add_argument("--timeout-seconds", type=int, default=420)

    past_finance15 = sub.add_parser("v14-track-g-past-asof-finance15")
    past_finance15.add_argument("--timeout-seconds", type=int, default=420)
    past_finance15.add_argument("--label", default="finance15")

    past_case_ids = sub.add_parser("v14-track-g-past-asof-case-ids")
    past_case_ids.add_argument("--timeout-seconds", type=int, default=420)
    past_case_ids.add_argument("--case-ids", nargs="+", required=True)
    past_case_ids.add_argument("--label")

    true_live = sub.add_parser("v14-track-g-true-live")
    true_live.add_argument("--max-batch-prompt-chars", type=int)

    true_live_official = sub.add_parser("v14-track-g-true-live-official")
    true_live_official.add_argument("--max-batch-prompt-chars", type=int)

    true_live_custom = sub.add_parser("v14-track-g-true-live-custom")
    true_live_custom.add_argument("--max-batch-prompt-chars", type=int)

    sub.add_parser("v14-track-g-true-live-status")

    track_h = sub.add_parser("v14-track-h-causal-ops")
    track_h.add_argument("--batch-size", type=int, default=3)
    track_h.add_argument("--timeout-seconds", type=int, default=300)
    track_h.add_argument("--case-ids", nargs="*")

    track_h_results = sub.add_parser("v14-track-h-build-results")
    track_h_results.add_argument("summary_path", type=Path)

    sub.add_parser("v14-build-public-manifest")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.command == "list-packs":
        list_packs()
    elif args.command == "check-skill":
        check_skill()
    elif args.command == "v14-public-dev":
        v14_public_dev()
    elif args.command == "v14-track-g-past-asof":
        v14_track_g_past_asof(args.timeout_seconds)
    elif args.command == "v14-track-g-past-asof-finance15":
        v14_track_g_past_asof(
            args.timeout_seconds,
            case_ids=track_g_past_asof_finance_case_ids(),
            label=args.label,
        )
    elif args.command == "v14-track-g-past-asof-case-ids":
        v14_track_g_past_asof(
            args.timeout_seconds,
            case_ids=args.case_ids,
            label=args.label,
        )
    elif args.command == "v14-track-g-true-live":
        v14_track_g_true_live(max_batch_prompt_chars=args.max_batch_prompt_chars)
    elif args.command == "v14-track-g-true-live-official":
        v14_track_g_true_live(source_type="futurex_online", max_batch_prompt_chars=args.max_batch_prompt_chars)
    elif args.command == "v14-track-g-true-live-custom":
        v14_track_g_true_live(source_type="custom_live", max_batch_prompt_chars=args.max_batch_prompt_chars)
    elif args.command == "v14-track-g-true-live-status":
        v14_track_g_true_live_status()
    elif args.command == "v14-track-h-causal-ops":
        v14_track_h_causal_ops(
            batch_size=args.batch_size,
            timeout_seconds=args.timeout_seconds,
            case_ids=args.case_ids,
        )
    elif args.command == "v14-track-h-build-results":
        v14_track_h_build_results(args.summary_path)
    elif args.command == "v14-build-public-manifest":
        v14_build_public_manifest()
    else:
        raise SystemExit(f"Unknown command: {args.command}")


if __name__ == "__main__":
    main()
