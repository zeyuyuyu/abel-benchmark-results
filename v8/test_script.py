#!/usr/bin/env python3
"""Run a CAP-adapted causal benchmark for Codex with and without causal-abel."""

from __future__ import annotations

import json
import os
import re
import subprocess
import time
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


WORKDIR = Path("/Users/zeyu/Documents/bach_private_cache")
BENCH_DIR = WORKDIR / ".bench"
SKILL_ROOT = Path("/Users/zeyu/.codex/skills/causal-abel")
CAP_PROBE = SKILL_ROOT / "scripts" / "cap_probe.py"
ENV_FILE = SKILL_ROOT / ".env.skills"
BASE_HOME = BENCH_DIR / "codex_home_base"
SKILL_HOME = BENCH_DIR / "codex_home_skill"
BASE_URL = "https://cap.abel.ai"
MODEL = "gpt-5.4"
REASONING_EFFORT = "low"
TIMEOUT_SECONDS = 240
TASK_ORDER = [
    "capability_core_verbs",
    "capability_extension_verbs",
    "methods_graph_paths_required_arguments",
    "methods_counterfactual_preview_required_arguments",
    "normalize_nvda",
    "neighbors_parents_nvda",
    "traverse_parents_nvda",
    "abel_markov_blanket_nvda",
    "observe_nvda_drivers",
    "path_nvda_amd",
    "validate_connectivity",
    "intervene_nvda_amd",
    "intervene_soxx_amd",
    "counterfactual_preview_nvda_amd",
    "intervene_time_lag_nvda_amd",
]


@dataclass(frozen=True)
class RunConfig:
    name: str
    codex_home: Path


RUNS = [
    RunConfig(name="base", codex_home=BASE_HOME),
    RunConfig(name="skill", codex_home=SKILL_HOME),
]


def resolve_api_key() -> str:
    direct = os.getenv("ABEL_API_KEY", "").strip()
    if direct:
        return direct
    if ENV_FILE.exists():
        for raw in ENV_FILE.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            if key.strip() == "ABEL_API_KEY":
                candidate = value.strip().strip('"').strip("'")
                if candidate:
                    return candidate
    raise SystemExit("Missing ABEL_API_KEY in environment and .env.skills")


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


def probe_env(api_key: str) -> dict[str, str]:
    env = os.environ.copy()
    env["ABEL_API_KEY"] = api_key
    return env


def run_probe(api_key: str, *args: str) -> dict[str, Any]:
    cmd = [
        "python3",
        str(CAP_PROBE),
        "--base-url",
        BASE_URL,
        "--compact",
        *args,
    ]
    last_payload: dict[str, Any] | None = None
    for attempt in range(3):
        completed = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=WORKDIR,
            env=probe_env(api_key),
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
        last_payload = payload
        transient_timeout = (
            payload.get("ok") is False
            and payload.get("status_code") == -1
            and "timed out" in str(payload.get("message", "")).lower()
        )
        if not transient_timeout or attempt == 2:
            return payload
        time.sleep(1.5 * (attempt + 1))
    if last_payload is not None:
        return last_payload
    raise RuntimeError(f"Probe failed without payload for args={args!r}")


def connected_pair_key(a: str, b: str) -> str:
    left, right = sorted([a, b])
    return f"{left}|{right}"


def build_ground_truth(api_key: str) -> dict[str, Any]:
    capabilities = run_probe(api_key, "capabilities")
    methods = run_probe(
        api_key,
        "methods",
        "graph.paths",
        "extensions.abel.counterfactual_preview",
    )
    normalize_nvda = run_probe(api_key, "normalize-node", "NVDA")
    neighbors_parents = run_probe(
        api_key, "neighbors", "NVDA_close", "--scope", "parents", "--max-neighbors", "8"
    )
    traverse_parents = run_probe(api_key, "traverse-parents", "NVDA_close", "--top-k", "8")
    abel_blanket = run_probe(api_key, "abel-markov-blanket", "NVDA_close")
    observe_nvda = run_probe(api_key, "observe", "NVDA_close")
    path_nvda_amd = run_probe(api_key, "paths", "NVDA_close", "AMD_close", "--max-paths", "3")
    connectivity = run_probe(
        api_key,
        "validate-connectivity",
        "NVDA_close",
        "SOXX_close",
    )
    intervene_yes = run_probe(
        api_key,
        "intervene-do",
        "NVDA_close",
        "0.05",
        "--outcome-node",
        "AMD_close",
        "--max-paths",
        "3",
    )
    intervene_no = run_probe(
        api_key,
        "intervene-do",
        "SOXX_close",
        "0.05",
        "--outcome-node",
        "AMD_close",
        "--max-paths",
        "3",
    )
    cf_preview = run_probe(
        api_key,
        "counterfactual-preview",
        "--intervene-node",
        "NVDA_close",
        "--intervene-time",
        "2026-03-24T00:00:00Z",
        "--observe-node",
        "AMD_close",
        "--observe-time",
        "2026-03-24T01:00:00Z",
        "--intervene-new-value",
        "0.05",
    )
    lag_preview = run_probe(
        api_key,
        "intervene-time-lag",
        "NVDA_close",
        "0.05",
        "--outcome-node",
        "AMD_close",
        "--horizon-steps",
        "24",
        "--model",
        "linear",
    )

    methods_by_verb = {item["verb"]: item for item in methods["result"]["methods"]}
    pair_results = [
        connected_pair_key(item["node_a"], item["node_b"])
        for item in connectivity["result"]["pair_results"]
        if item["connected"]
    ]

    return {
        "capability_core_verbs": sorted(capabilities["result"]["supported_verbs"]["core"]),
        "capability_extension_verbs": sorted(
            capabilities["result"]["extensions"]["abel"]["verbs"]
        ),
        "methods_graph_paths_required_arguments": sorted(
            arg["name"]
            for arg in methods_by_verb["graph.paths"]["arguments"]
            if arg.get("required")
        ),
        "methods_counterfactual_preview_required_arguments": sorted(
            arg["name"]
            for arg in methods_by_verb["extensions.abel.counterfactual_preview"]["arguments"]
            if arg.get("required")
        ),
        "normalize_nvda": normalize_nvda["normalized_node_id"],
        "neighbors_parents_nvda": sorted(
            item["node_id"] for item in neighbors_parents["result"]["neighbors"]
        ),
        "traverse_parents_nvda": sorted(
            traverse_parents["result"].get("nodes", [])
        ),
        "abel_markov_blanket_nvda": {
            "drivers": sorted(abel_blanket["result"]["drivers"]),
            "blanket_size": len(abel_blanket["result"]["markov_blanket"]),
        },
        "observe_nvda": {
            "target_node": observe_nvda["result"]["target_node"],
            "drivers": sorted(observe_nvda["result"]["drivers"]),
        },
        "path_nvda_amd": {
            "connected": path_nvda_amd["result"]["connected"],
            "path_count": path_nvda_amd["result"]["path_count"],
        },
        "connectivity": {
            "passed": connectivity["result"]["passed"],
            "connected_pairs": sorted(pair_results),
            "invalid_variable_count": len(connectivity["result"]["invalid_variables"]),
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
        "counterfactual_preview_nvda_amd": {
            "reachable": cf_preview["result"]["reachable"],
            "effect_support": cf_preview["result"]["effect_support"],
            "path_count": cf_preview["result"]["path_count"],
            "preview_only": cf_preview["result"]["preview_only"],
        },
        "intervene_time_lag_nvda_amd": {
            "ok": lag_preview.get("ok", False),
            "status_code": lag_preview.get("status_code"),
            "error_code": lag_preview.get("error", {}).get("code"),
        },
    }


def task_specs(truth: dict[str, Any]) -> list[dict[str, Any]]:
    common = (
        "Use the live Abel CAP server at https://cap.abel.ai. "
        "An ABEL_API_KEY is available in the environment. "
        "If a specialized installed skill applies, use it. "
        "Inspect the live server or the installed probe tooling instead of guessing. "
        "Return only JSON with exactly the requested keys."
    )
    return [
        {
            "id": "capability_core_verbs",
            "category": "capability_contract",
            "prompt": (
                f"{common}\n"
                "Question: What core verbs are exposed by the live public CAP surface?\n"
                'Return {"verbs":["..."]} with the core verbs sorted alphabetically.'
            ),
            "checks": [("verbs", truth["capability_core_verbs"])],
        },
        {
            "id": "capability_extension_verbs",
            "category": "capability_contract",
            "prompt": (
                f"{common}\n"
                "Question: What verbs are exposed under extensions.abel on the live public CAP surface?\n"
                'Return {"verbs":["..."]} with the extension verbs sorted alphabetically.'
            ),
            "checks": [("verbs", truth["capability_extension_verbs"])],
        },
        {
            "id": "methods_graph_paths_required_arguments",
            "category": "capability_contract",
            "prompt": (
                f"{common}\n"
                "Question: For graph.paths, what are the required argument names?\n"
                'Return {"required_arguments":["..."]} with the names sorted alphabetically.'
            ),
            "checks": [("required_arguments", truth["methods_graph_paths_required_arguments"])],
        },
        {
            "id": "methods_counterfactual_preview_required_arguments",
            "category": "capability_contract",
            "prompt": (
                f"{common}\n"
                "Question: For extensions.abel.counterfactual_preview, what are the required argument names?\n"
                'Return {"required_arguments":["..."]} with the names sorted alphabetically.'
            ),
            "checks": [
                (
                    "required_arguments",
                    truth["methods_counterfactual_preview_required_arguments"],
                )
            ],
        },
        {
            "id": "normalize_nvda",
            "category": "node_normalization",
            "prompt": (
                f"{common}\n"
                "Question: Under the public Abel node naming rule, what does the bare ticker NVDA normalize to?\n"
                'Return {"normalized_node_id":"..."}'
            ),
            "checks": [("normalized_node_id", truth["normalize_nvda"])],
        },
        {
            "id": "neighbors_parents_nvda",
            "category": "structural_reads",
            "prompt": (
                f"{common}\n"
                "Question: What are the immediate parent neighbors of NVDA_close?\n"
                'Return {"neighbors":["..."]} with sorted unique node IDs.'
            ),
            "checks": [("neighbors", truth["neighbors_parents_nvda"])],
        },
        {
            "id": "traverse_parents_nvda",
            "category": "structural_reads",
            "prompt": (
                f"{common}\n"
                "Question: What parent node IDs are returned by traverse.parents for NVDA_close when top_k=8?\n"
                'Return {"nodes":["..."]} with sorted unique node IDs.'
            ),
            "checks": [("nodes", truth["traverse_parents_nvda"])],
        },
        {
            "id": "abel_markov_blanket_nvda",
            "category": "structural_reads",
            "prompt": (
                f"{common}\n"
                "Question: For extensions.abel.markov_blanket on NVDA_close, what driver node IDs are returned and how large is the Markov blanket?\n"
                'Return {"drivers":["..."],"blanket_size":0} with sorted driver node IDs.'
            ),
            "checks": [
                ("drivers", truth["abel_markov_blanket_nvda"]["drivers"]),
                ("blanket_size", truth["abel_markov_blanket_nvda"]["blanket_size"]),
            ],
        },
        {
            "id": "observe_nvda_drivers",
            "category": "structural_reads",
            "prompt": (
                f"{common}\n"
                "Question: For observe.predict on NVDA_close, what target node is echoed and which driver node IDs are surfaced?\n"
                'Return {"target_node":"...","drivers":["..."]} with sorted driver node IDs.'
            ),
            "checks": [
                ("target_node", truth["observe_nvda"]["target_node"]),
                ("drivers", truth["observe_nvda"]["drivers"]),
            ],
        },
        {
            "id": "path_nvda_amd",
            "category": "reachability_and_validation",
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
            "id": "validate_connectivity",
            "category": "reachability_and_validation",
            "prompt": (
                f"{common}\n"
                "Question: For validate-connectivity on NVDA_close and SOXX_close, did the validation pass, which node pairs were connected, and how many invalid_variables were returned?\n"
                'Return {"passed":false,"connected_pairs":["A|B"],"invalid_variable_count":0}. '
                "Format each pair as the two node IDs joined by | after alphabetic sorting, and sort the list."
            ),
            "checks": [
                ("passed", truth["connectivity"]["passed"]),
                ("connected_pairs", truth["connectivity"]["connected_pairs"]),
                ("invalid_variable_count", truth["connectivity"]["invalid_variable_count"]),
            ],
        },
        {
            "id": "intervene_nvda_amd",
            "category": "intervention_boundaries",
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
            "category": "intervention_boundaries",
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
        {
            "id": "counterfactual_preview_nvda_amd",
            "category": "extension_semantics",
            "prompt": (
                f"{common}\n"
                "Question: For extensions.abel.counterfactual_preview with intervene_node=NVDA_close at 2026-03-24T00:00:00Z, observe_node=AMD_close at 2026-03-24T01:00:00Z, and intervene_new_value=0.05, was the observe node reachable, what effect_support label was returned, how many structural paths were counted, and was the result marked preview_only?\n"
                'Return {"reachable":false,"effect_support":"...","path_count":0,"preview_only":true}.'
            ),
            "checks": [
                ("reachable", truth["counterfactual_preview_nvda_amd"]["reachable"]),
                ("effect_support", truth["counterfactual_preview_nvda_amd"]["effect_support"]),
                ("path_count", truth["counterfactual_preview_nvda_amd"]["path_count"]),
                ("preview_only", truth["counterfactual_preview_nvda_amd"]["preview_only"]),
            ],
        },
        {
            "id": "intervene_time_lag_nvda_amd",
            "category": "extension_semantics",
            "prompt": (
                f"{common}\n"
                "Question: For extensions.abel.intervene_time_lag with treatment NVDA_close=0.05, outcome AMD_close, horizon_steps=24, and model=linear, did the call succeed, what status_code was returned, and what error_code was surfaced?\n"
                'Return {"ok":false,"status_code":0,"error_code":"..."}'
            ),
            "checks": [
                ("ok", truth["intervene_time_lag_nvda_amd"]["ok"]),
                ("status_code", truth["intervene_time_lag_nvda_amd"]["status_code"]),
                ("error_code", truth["intervene_time_lag_nvda_amd"]["error_code"]),
            ],
        },
    ]


def run_codex(run: RunConfig, task: dict[str, Any], api_key: str, run_dir: Path) -> dict[str, Any]:
    output_path = run_dir / f"{task['id']}.txt"
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
        task["prompt"],
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
    duration = round(time.time() - started, 2)
    raw_output = output_path.read_text(encoding="utf-8") if output_path.exists() else ""
    parsed: Any = None
    parse_error = None
    try:
        parsed = parse_json_from_text(raw_output)
    except Exception as exc:  # noqa: BLE001
        parse_error = str(exc)
    return {
        "task_id": task["id"],
        "returncode": completed.returncode,
        "duration_seconds": duration,
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
    points = 0
    field_results = []
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
    api_key = resolve_api_key()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    out_dir = BENCH_DIR / f"cap-causalbench-results-{timestamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    truth = build_ground_truth(api_key)
    task_map = {task["id"]: task for task in task_specs(truth)}
    tasks = [task_map[task_id] for task_id in TASK_ORDER]

    benchmark: dict[str, Any] = {
        "timestamp": timestamp,
        "version": "cap-causalbench-v1",
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "base_url": BASE_URL,
        "task_count": len(tasks),
        "categories": sorted({task["category"] for task in tasks}),
        "ground_truth": truth,
        "task_specs": [
            {
                "id": task["id"],
                "category": task["category"],
                "checks": [field for field, _ in task["checks"]],
            }
            for task in tasks
        ],
        "runs": {},
    }

    for run in RUNS:
        (out_dir / run.name).mkdir(parents=True, exist_ok=True)
        benchmark["runs"][run.name] = {
            "total_points": 0,
            "max_points": 0,
            "accuracy": 0.0,
            "category_scores": {},
            "tasks": [],
        }

    for task in tasks:
        for run in RUNS:
            run_dir = out_dir / run.name
            result = run_codex(run, task, api_key, run_dir)
            score = score_result(result, task["checks"])
            run_bucket = benchmark["runs"][run.name]
            run_bucket["total_points"] += score["points"]
            run_bucket["max_points"] += score["max_points"]
            category_bucket = run_bucket["category_scores"].setdefault(
                task["category"],
                {"points": 0, "max_points": 0, "accuracy": 0.0},
            )
            category_bucket["points"] += score["points"]
            category_bucket["max_points"] += score["max_points"]
            run_bucket["tasks"].append(
                {
                    "task_id": task["id"],
                    "category": task["category"],
                    "score": score,
                    "result": result,
                }
            )
            print(
                f"[{run.name}] {task['id']} ({task['category']}): "
                f"{score['points']}/{score['max_points']} in {result['duration_seconds']}s",
                flush=True,
            )

    for run in RUNS:
        run_bucket = benchmark["runs"][run.name]
        total_points = run_bucket["total_points"]
        total_max = run_bucket["max_points"]
        run_bucket["accuracy"] = round(total_points / total_max, 4) if total_max else 0.0
        for category_bucket in run_bucket["category_scores"].values():
            category_bucket["accuracy"] = (
                round(category_bucket["points"] / category_bucket["max_points"], 4)
                if category_bucket["max_points"]
                else 0.0
            )

    summary_path = out_dir / "summary.json"
    summary_path.write_text(
        json.dumps(benchmark, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Saved summary to {summary_path}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.TimeoutExpired as exc:
        raise SystemExit(f"Command timed out: {exc.cmd}") from exc
