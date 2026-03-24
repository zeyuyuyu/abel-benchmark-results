#!/usr/bin/env python3
"""Run a live Abel CAP benchmark with and without the causal-abel skill."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any


WORKDIR = Path("/Users/zeyu/Documents/bach_private_cache")
BENCH_DIR = WORKDIR / ".bench"
SKILL_ROOT = Path("/Users/zeyu/.codex/skills/causal-abel")
CAP_PROBE = SKILL_ROOT / "scripts" / "cap_probe.py"
BASE_HOME = BENCH_DIR / "codex_home_base"
SKILL_HOME = BENCH_DIR / "codex_home_skill"
BASE_URL = "https://cap.abel.ai"
MODEL = "gpt-5.4"
REASONING_EFFORT = "low"
TIMEOUT_SECONDS = 240
TASK_ORDER = [
    "methods_graph_paths",
    "nvda_parent_neighbors",
    "path_nvda_amd",
    "validate_connectivity",
    "intervene_nvda_amd",
    "intervene_soxx_amd",
]


@dataclass(frozen=True)
class RunConfig:
    name: str
    codex_home: Path


RUNS = [
    RunConfig(name="base", codex_home=BASE_HOME),
    RunConfig(name="skill", codex_home=SKILL_HOME),
]


def require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def parse_json_from_text(text: str) -> Any:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        pass

    match = re.search(r"\{.*\}", stripped, re.DOTALL)
    if match:
        return json.loads(match.group(0))
    raise ValueError(f"Could not parse JSON from output: {text[:300]!r}")


def run_probe(*args: str) -> dict[str, Any]:
    env = os.environ.copy()
    cmd = [
        "python3",
        str(CAP_PROBE),
        "--base-url",
        BASE_URL,
        "--compact",
        *args,
    ]
    completed = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        env=env,
        timeout=TIMEOUT_SECONDS,
        check=False,
    )
    output = completed.stdout.strip() or completed.stderr.strip()
    if not output:
        raise RuntimeError(f"Probe returned no output for args={args!r}")
    try:
        payload = json.loads(output)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON from probe args={args!r}: {output}") from exc
    return payload


def connected_pair_key(a: str, b: str) -> str:
    left, right = sorted([a, b])
    return f"{left}|{right}"


def build_ground_truth() -> dict[str, Any]:
    methods = run_probe("methods", "graph.paths")
    parents = run_probe("neighbors", "NVDA_close", "--scope", "parents", "--max-neighbors", "5")
    children = run_probe("neighbors", "NVDA_close", "--scope", "children", "--max-neighbors", "5")
    path_yes = run_probe("paths", "NVDA_close", "AMD_close", "--max-paths", "3")
    path_no = run_probe("paths", "SOXX_close", "AMD_close", "--max-paths", "3")
    observe = run_probe("observe", "NVDA_close")
    connectivity = run_probe("validate-connectivity", "NVDA_close", "AMD_close", "SOXX_close")
    intervene_yes = run_probe(
        "intervene-do",
        "NVDA_close",
        "0.05",
        "--outcome-node",
        "AMD_close",
        "--max-paths",
        "3",
    )
    intervene_no = run_probe(
        "intervene-do",
        "SOXX_close",
        "0.05",
        "--outcome-node",
        "AMD_close",
        "--max-paths",
        "3",
    )

    pair_results = [
        connected_pair_key(item["node_a"], item["node_b"])
        for item in connectivity["result"]["pair_results"]
        if item["connected"]
    ]

    return {
        "required_arguments": sorted(
            arg["name"]
            for arg in methods["result"]["methods"][0]["arguments"]
            if arg.get("required")
        ),
        "nvda_parents": sorted(
            item["node_id"] for item in parents["result"]["neighbors"]
        ),
        "nvda_children": sorted(
            item["node_id"] for item in children["result"]["neighbors"]
        ),
        "path_nvda_amd": {
            "connected": path_yes["result"]["connected"],
            "path_count": path_yes["result"]["path_count"],
        },
        "path_soxx_amd": {
            "connected": path_no["result"]["connected"],
            "path_count": path_no["result"]["path_count"],
        },
        "observe_nvda_drivers": sorted(observe["result"]["drivers"]),
        "connectivity": {
            "passed": connectivity["result"]["passed"],
            "connected_pairs": sorted(pair_results),
        },
        "intervene_nvda_amd": {
            "path_exists": intervene_yes["structural_check"]["result"]["connected"],
            "effect_returned": intervene_yes.get("ok", False),
            "intervention_skipped": intervene_yes.get("intervention_skipped", False),
            "error_code": intervene_yes.get("error", {}).get("code"),
        },
        "intervene_soxx_amd": {
            "path_exists": intervene_no["structural_check"]["result"]["connected"],
            "effect_returned": intervene_no.get("ok", False),
            "intervention_skipped": intervene_no.get("intervention_skipped", False),
            "skip_reason": intervene_no.get("skip_reason"),
        },
    }


def task_specs(truth: dict[str, Any]) -> list[dict[str, Any]]:
    common = (
        "Use the live Abel CAP server at https://cap.abel.ai. "
        "An ABEL_API_KEY is available in the environment. "
        "If a specialized installed skill applies, use it. "
        "Inspect the live server instead of guessing. "
        "Return only JSON with exactly the requested keys."
    )
    return [
        {
            "id": "methods_graph_paths",
            "prompt": (
                f"{common}\n"
                "Question: For the verb graph.paths, what are the required argument names?\n"
                'Return {"required_arguments":["..."]} with the argument names sorted alphabetically.'
            ),
            "checks": [
                ("required_arguments", truth["required_arguments"]),
            ],
        },
        {
            "id": "nvda_parent_neighbors",
            "prompt": (
                f"{common}\n"
                "Question: What are the immediate parent neighbors of NVDA_close?\n"
                'Return {"neighbors":["..."]} with sorted unique node IDs.'
            ),
            "checks": [
                ("neighbors", truth["nvda_parents"]),
            ],
        },
        {
            "id": "nvda_child_neighbors",
            "prompt": (
                f"{common}\n"
                "Question: What are the immediate child neighbors of NVDA_close?\n"
                'Return {"neighbors":["..."]} with sorted unique node IDs.'
            ),
            "checks": [
                ("neighbors", truth["nvda_children"]),
            ],
        },
        {
            "id": "path_nvda_amd",
            "prompt": (
                f"{common}\n"
                "Question: Does a directed path exist from NVDA_close to AMD_close, and how many paths are returned when max_paths=3?\n"
                'Return {"connected":true,"path_count":0}.'
            ),
            "checks": [
                ("connected", truth["path_nvda_amd"]["connected"]),
                ("path_count", truth["path_nvda_amd"]["path_count"]),
            ],
        },
        {
            "id": "path_soxx_amd",
            "prompt": (
                f"{common}\n"
                "Question: Does a directed path exist from SOXX_close to AMD_close, and how many paths are returned when max_paths=3?\n"
                'Return {"connected":true,"path_count":0}.'
            ),
            "checks": [
                ("connected", truth["path_soxx_amd"]["connected"]),
                ("path_count", truth["path_soxx_amd"]["path_count"]),
            ],
        },
        {
            "id": "observe_nvda_drivers",
            "prompt": (
                f"{common}\n"
                "Question: For observe.predict on NVDA_close, which driver node IDs are surfaced by the server?\n"
                'Return {"drivers":["..."]} with sorted unique node IDs.'
            ),
            "checks": [
                ("drivers", truth["observe_nvda_drivers"]),
            ],
        },
        {
            "id": "validate_connectivity",
            "prompt": (
                f"{common}\n"
                "Question: For validate-connectivity on NVDA_close, AMD_close, and SOXX_close, did the validation pass, and which pairs were connected?\n"
                'Return {"passed":false,"connected_pairs":["A|B"]}. '
                "Format each pair as the two node IDs joined by | after alphabetic sorting, and sort the list."
            ),
            "checks": [
                ("passed", truth["connectivity"]["passed"]),
                ("connected_pairs", truth["connectivity"]["connected_pairs"]),
            ],
        },
        {
            "id": "intervene_nvda_amd",
            "prompt": (
                f"{common}\n"
                "Question: For intervene-do with treatment NVDA_close=0.05 and outcome AMD_close, did the structural path check pass, did the intervention return an effect, was the intervention skipped, and what error code was returned?\n"
                'Return {"path_exists":true,"effect_returned":false,"intervention_skipped":false,"error_code":"..."}'
            ),
            "checks": [
                ("path_exists", truth["intervene_nvda_amd"]["path_exists"]),
                ("effect_returned", truth["intervene_nvda_amd"]["effect_returned"]),
                ("intervention_skipped", truth["intervene_nvda_amd"]["intervention_skipped"]),
                ("error_code", truth["intervene_nvda_amd"]["error_code"]),
            ],
        },
        {
            "id": "intervene_soxx_amd",
            "prompt": (
                f"{common}\n"
                "Question: For intervene-do with treatment SOXX_close=0.05 and outcome AMD_close, did the structural path check pass, did the intervention return an effect, was the intervention skipped, and what skip_reason was returned?\n"
                'Return {"path_exists":false,"effect_returned":false,"intervention_skipped":true,"skip_reason":"..."}'
            ),
            "checks": [
                ("path_exists", truth["intervene_soxx_amd"]["path_exists"]),
                ("effect_returned", truth["intervene_soxx_amd"]["effect_returned"]),
                ("intervention_skipped", truth["intervene_soxx_amd"]["intervention_skipped"]),
                ("skip_reason", truth["intervene_soxx_amd"]["skip_reason"]),
            ],
        },
    ]


def run_codex(run: RunConfig, task_id: str, prompt: str, api_key: str, run_dir: Path) -> dict[str, Any]:
    output_path = run_dir / f"{task_id}.txt"
    cmd = [
        "codex",
        "exec",
        "--skip-git-repo-check",
        "-C",
        str(WORKDIR),
        "-s",
        "danger-full-access",
        "-m",
        MODEL,
        "-c",
        f'reasoning_effort="{REASONING_EFFORT}"',
        "--color",
        "never",
        "-o",
        str(output_path),
        prompt,
    ]
    env = os.environ.copy()
    env["CODEX_HOME"] = str(run.codex_home)
    env["ABEL_API_KEY"] = api_key
    started = time.time()
    completed = subprocess.run(
        cmd,
        cwd=WORKDIR,
        capture_output=True,
        text=True,
        env=env,
        timeout=TIMEOUT_SECONDS,
        check=False,
    )
    duration = time.time() - started
    raw_output = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
    parsed: Any = None
    parse_error = None
    try:
        parsed = parse_json_from_text(raw_output)
    except Exception as exc:  # noqa: BLE001
        parse_error = str(exc)

    return {
        "task_id": task_id,
        "returncode": completed.returncode,
        "duration_seconds": round(duration, 2),
        "stdout": completed.stdout[-4000:],
        "stderr": completed.stderr[-4000:],
        "raw_output": raw_output,
        "parsed_output": parsed,
        "parse_error": parse_error,
    }


def normalize(value: Any) -> Any:
    if isinstance(value, list):
        return sorted(value)
    return value


def score_result(result: dict[str, Any], checks: list[tuple[str, Any]]) -> dict[str, Any]:
    parsed = result.get("parsed_output")
    if not isinstance(parsed, dict):
        return {
            "points": 0,
            "max_points": len(checks),
            "field_results": [
                {"field": field, "expected": expected, "actual": None, "correct": False}
                for field, expected in checks
            ],
        }

    field_results = []
    points = 0
    for field, expected in checks:
        actual = parsed.get(field)
        correct = normalize(actual) == normalize(expected)
        points += int(correct)
        field_results.append(
            {
                "field": field,
                "expected": expected,
                "actual": actual,
                "correct": correct,
            }
        )

    return {"points": points, "max_points": len(checks), "field_results": field_results}


def main() -> None:
    api_key = require_env("ABEL_API_KEY")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    out_dir = BENCH_DIR / f"results-{timestamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    truth = build_ground_truth()
    task_map = {task["id"]: task for task in task_specs(truth)}
    tasks = [task_map[task_id] for task_id in TASK_ORDER]

    benchmark: dict[str, Any] = {
        "timestamp": timestamp,
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "base_url": BASE_URL,
        "ground_truth": truth,
        "runs": {},
    }

    for run in RUNS:
        (out_dir / run.name).mkdir(parents=True, exist_ok=True)
        benchmark["runs"][run.name] = {
            "total_points": 0,
            "max_points": 0,
            "accuracy": 0.0,
            "tasks": [],
        }

    for task in tasks:
        for run in RUNS:
            run_dir = out_dir / run.name
            result = run_codex(run, task["id"], task["prompt"], api_key, run_dir)
            score = score_result(result, task["checks"])
            benchmark["runs"][run.name]["total_points"] += score["points"]
            benchmark["runs"][run.name]["max_points"] += score["max_points"]
            benchmark["runs"][run.name]["tasks"].append(
                {
                    "task_id": task["id"],
                    "score": score,
                    "result": result,
                }
            )
            print(
                f"[{run.name}] {task['id']}: {score['points']}/{score['max_points']} "
                f"in {result['duration_seconds']}s",
                flush=True,
            )

    for run in RUNS:
        total_points = benchmark["runs"][run.name]["total_points"]
        total_max = benchmark["runs"][run.name]["max_points"]
        benchmark["runs"][run.name]["accuracy"] = (
            round(total_points / total_max, 4) if total_max else 0.0
        )

    summary_path = out_dir / "summary.json"
    summary_path.write_text(json.dumps(benchmark, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved summary to {summary_path}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.TimeoutExpired as exc:
        raise SystemExit(f"Command timed out: {exc.cmd}") from exc
