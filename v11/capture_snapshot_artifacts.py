#!/usr/bin/env python3
"""Capture raw Abel snapshot evidence for the v11 natural-intent benchmark."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


V11_DIR = Path("/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v11")
ARTIFACTS_DIR = V11_DIR / "artifacts"
RAW_DIR = ARTIFACTS_DIR / "raw"
CAP_PROBE = Path("/Users/zeyu/.codex/skills/causal-abel/scripts/cap_probe.py")
BASE_URL = "https://cap.abel.ai"
SNAPSHOT_LABEL = "March 25, 2026 (GMT+8)"

OBSERVE_NODES = {
    "AAPL": "AAPL_close",
    "TSLA": "TSLA_close",
    "AMD": "AMD_close",
    "NVDA": "NVDA_close",
    "INTC": "INTC_close",
    "AVGO": "AVGO_close",
    "TSM": "TSM_close",
    "CL": "CL_close",
    "ETH": "ETHUSD_close",
    "SOXX": "SOXX_close",
    "QQQ": "QQQ_close",
    "SPY": "SPY_close",
    "BTC": "BTCUSD_close",
    "GC": "GC_close",
    "GLD": "GLD_close",
    "XLE": "XLE_close",
    "USO": "USO_close",
}

PATH_TASKS = {
    "NVDA->AMD": ("NVDA_close", "AMD_close"),
    "SOXX->AMD": ("SOXX_close", "AMD_close"),
    "AVGO->NVDA": ("AVGO_close", "NVDA_close"),
    "TSM->NVDA": ("TSM_close", "NVDA_close"),
    "AMD->NVDA": ("AMD_close", "NVDA_close"),
    "QQQ->NVDA": ("QQQ_close", "NVDA_close"),
    "SPY->NVDA": ("SPY_close", "NVDA_close"),
    "BTC->ETH": ("BTCUSD_close", "ETHUSD_close"),
    "XLK->AAPL": ("XLK_close", "AAPL_close"),
}

INTERVENTION_TASKS = {
    "NVDA->AMD": ("NVDA_close", "AMD_close"),
    "SOXX->AMD": ("SOXX_close", "AMD_close"),
}

COUNTERFACTUAL_TASKS = {
    "NVDA->AMD": {
        "intervene_node": "NVDA_close",
        "observe_node": "AMD_close",
        "intervene_time": "2026-03-24T00:00:00Z",
        "observe_time": "2026-03-24T01:00:00Z",
        "intervene_new_value": "0.05",
    },
    "SOXX->AMD": {
        "intervene_node": "SOXX_close",
        "observe_node": "AMD_close",
        "intervene_time": "2026-03-24T00:00:00Z",
        "observe_time": "2026-03-24T01:00:00Z",
        "intervene_new_value": "0.05",
    },
}


def _should_retry(stdout_json: object) -> bool:
    return (
        isinstance(stdout_json, dict)
        and stdout_json.get("status_code") == -1
        and stdout_json.get("message") == "timed out"
    )


def run_probe(slug: str, args: list[str], *, include_base_url: bool = True) -> dict[str, object]:
    cmd = [sys.executable, str(CAP_PROBE)]
    if include_base_url:
        cmd += ["--base-url", BASE_URL]
    cmd += args + ["--compact"]

    payload: dict[str, object] | None = None
    for attempt in range(3):
        proc = subprocess.run(cmd, capture_output=True, text=True, check=False)
        stdout_text = proc.stdout.strip()
        stderr_text = proc.stderr.strip()
        try:
            stdout_json = json.loads(stdout_text) if stdout_text else None
        except json.JSONDecodeError:
            stdout_json = {"raw": stdout_text}

        payload = {
            "slug": slug,
            "captured_at": datetime.now(timezone.utc).isoformat(),
            "command": cmd,
            "exit_code": proc.returncode,
            "attempt": attempt + 1,
            "stdout": stdout_json,
            "stderr": stderr_text,
        }
        if not _should_retry(stdout_json):
            break

    assert payload is not None
    (RAW_DIR / f"{slug}.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return payload


def extract_prediction_pct(payload: dict[str, object]) -> float | None:
    stdout = payload.get("stdout")
    if not isinstance(stdout, dict) or not stdout.get("ok"):
        return None
    result = stdout.get("result", {})
    if not isinstance(result, dict) or "prediction" not in result:
        return None
    return float(result["prediction"]) * 100.0


def extract_status(payload: dict[str, object]) -> str:
    stdout = payload.get("stdout")
    if not isinstance(stdout, dict):
        return "error"
    if stdout.get("ok"):
        return "ok"
    error = stdout.get("error", {})
    if isinstance(error, dict) and error.get("code") == "service_unavailable":
        return "unavailable"
    return "error"


def extract_path_fact(payload: dict[str, object]) -> dict[str, object]:
    stdout = payload.get("stdout")
    if not isinstance(stdout, dict):
        return {"connected": False, "path_count": 0}
    result = stdout.get("result", {})
    if not isinstance(result, dict):
        return {"connected": False, "path_count": 0}
    return {
        "connected": bool(result.get("connected", False)),
        "path_count": int(result.get("path_count", 0)),
    }


def extract_intervention_fact(payload: dict[str, object]) -> dict[str, object]:
    stdout = payload.get("stdout")
    if not isinstance(stdout, dict):
        return {
            "path_exists": False,
            "intervention_skipped": False,
            "skip_reason": None,
            "error_code": None,
            "effect_returned": False,
        }

    structural_check = stdout.get("structural_check", {})
    structural_result = structural_check.get("result", {}) if isinstance(structural_check, dict) else {}
    path_exists = bool(structural_result.get("connected", False))
    effect_returned = bool(stdout.get("ok") and isinstance(stdout.get("result"), dict))
    error = stdout.get("error", {})
    return {
        "path_exists": path_exists,
        "intervention_skipped": bool(stdout.get("intervention_skipped", False)),
        "skip_reason": stdout.get("skip_reason"),
        "error_code": error.get("code") if isinstance(error, dict) else None,
        "effect_returned": effect_returned,
    }


def extract_counterfactual_fact(payload: dict[str, object]) -> dict[str, object]:
    stdout = payload.get("stdout")
    if not isinstance(stdout, dict):
        return {"status": "error", "error_code": "invalid_payload"}
    if stdout.get("ok"):
        result = stdout.get("result", {})
        if not isinstance(result, dict):
            return {"status": "error", "error_code": "missing_result"}
        return {
            "status": "ok",
            "reachable": bool(result.get("reachable", False)),
            "effect_support": result.get("effect_support"),
            "path_count": int(result.get("path_count", 0)),
            "preview_only": bool(result.get("preview_only", False)),
        }
    error = stdout.get("error", {})
    return {
        "status": "error",
        "error_code": error.get("code") if isinstance(error, dict) else None,
    }


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    manifest_entries: list[dict[str, object]] = []

    def capture(slug: str, args: list[str], *, include_base_url: bool = True) -> dict[str, object]:
        payload = run_probe(slug, args, include_base_url=include_base_url)
        manifest_entries.append(
            {
                "slug": slug,
                "file": f"artifacts/raw/{slug}.json",
                "command": payload["command"],
                "exit_code": payload["exit_code"],
            }
        )
        return payload

    capture("capabilities", ["capabilities"])
    capture("normalize_BTC", ["normalize-node", "BTC"], include_base_url=False)
    capture("normalize_ETH", ["normalize-node", "ETH"], include_base_url=False)

    observe_payloads: dict[str, dict[str, object]] = {}
    for alias, node in OBSERVE_NODES.items():
        observe_payloads[alias] = capture(f"observe_{node}", ["observe", node])

    path_payloads: dict[str, dict[str, object]] = {}
    for key, (source_node, target_node) in PATH_TASKS.items():
        slug = f"path_{source_node}__{target_node}"
        path_payloads[key] = capture(slug, ["paths", source_node, target_node, "--max-paths", "3"])

    intervention_payloads: dict[str, dict[str, object]] = {}
    for key, (treatment_node, outcome_node) in INTERVENTION_TASKS.items():
        slug = f"intervene_{treatment_node}__{outcome_node}"
        intervention_payloads[key] = capture(
            slug,
            ["intervene-do", treatment_node, "0.05", "--outcome-node", outcome_node],
        )

    counterfactual_payloads: dict[str, dict[str, object]] = {}
    for key, params in COUNTERFACTUAL_TASKS.items():
        slug = f"counterfactual_{params['intervene_node']}__{params['observe_node']}"
        counterfactual_payloads[key] = capture(
            slug,
            [
                "counterfactual-preview",
                "--intervene-node",
                params["intervene_node"],
                "--intervene-time",
                params["intervene_time"],
                "--observe-node",
                params["observe_node"],
                "--observe-time",
                params["observe_time"],
                "--intervene-new-value",
                params["intervene_new_value"],
            ],
        )

    facts = {
        "snapshot_meta": {
            "version": "v11-natural-intent-casebook",
            "snapshot_label": SNAPSHOT_LABEL,
            "snapshot_date": "2026-03-25",
            "timezone": "GMT+8",
            "captured_at": datetime.now(timezone.utc).isoformat(),
            "base_url": BASE_URL,
            "probe_script": str(CAP_PROBE),
            "artifacts_manifest": "artifacts/manifest.json",
        },
        "backing_nodes": OBSERVE_NODES,
        "observe_pct": {
            alias: extract_prediction_pct(payload)
            for alias, payload in observe_payloads.items()
            if extract_prediction_pct(payload) is not None
        },
        "graph_paths": {
            key: extract_path_fact(payload) for key, payload in path_payloads.items()
        },
        "interventions": {
            key: extract_intervention_fact(payload)
            for key, payload in intervention_payloads.items()
        },
        "counterfactuals": {
            key: extract_counterfactual_fact(payload)
            for key, payload in counterfactual_payloads.items()
        },
        "availability": {
            alias: extract_status(payload) for alias, payload in observe_payloads.items()
        },
        "artifact_refs": {
            "capabilities": "artifacts/raw/capabilities.json",
            "normalize": {
                "BTC": "artifacts/raw/normalize_BTC.json",
                "ETH": "artifacts/raw/normalize_ETH.json",
            },
            "observe": {
                alias: f"artifacts/raw/observe_{node}.json"
                for alias, node in OBSERVE_NODES.items()
            },
            "paths": {
                key: f"artifacts/raw/path_{source}__{target}.json"
                for key, (source, target) in PATH_TASKS.items()
            },
            "interventions": {
                key: f"artifacts/raw/intervene_{treatment}__{outcome}.json"
                for key, (treatment, outcome) in INTERVENTION_TASKS.items()
            },
            "counterfactuals": {
                key: (
                    "artifacts/raw/"
                    f"counterfactual_{params['intervene_node']}__{params['observe_node']}.json"
                )
                for key, params in COUNTERFACTUAL_TASKS.items()
            },
        },
    }

    manifest = {
        "version": "v11-natural-intent-casebook",
        "snapshot_label": SNAPSHOT_LABEL,
        "captured_at": facts["snapshot_meta"]["captured_at"],
        "base_url": BASE_URL,
        "artifact_count": len(manifest_entries),
        "artifacts": manifest_entries,
    }

    (ARTIFACTS_DIR / "snapshot_facts.json").write_text(
        json.dumps(facts, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (ARTIFACTS_DIR / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "artifact_count": manifest["artifact_count"],
                "observe_pct_count": len(facts["observe_pct"]),
                "path_count": len(facts["graph_paths"]),
                "intervention_count": len(facts["interventions"]),
                "counterfactual_count": len(facts["counterfactuals"]),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
