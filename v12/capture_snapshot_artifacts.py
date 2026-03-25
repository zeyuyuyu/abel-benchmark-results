#!/usr/bin/env python3
"""Capture raw Abel snapshot evidence for the v12 general-finance challenge."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


V12_DIR = Path("/Users/zeyu/Documents/bach_private_cache/abel-benchmark-results/v12")
ARTIFACTS_DIR = V12_DIR / "artifacts"
RAW_DIR = ARTIFACTS_DIR / "raw"
CAP_PROBE = Path("/Users/zeyu/.codex/skills/causal-abel/scripts/cap_probe.py")
BASE_URL = "https://cap.abel.ai"
SNAPSHOT_LABEL = "March 25, 2026 (GMT+8)"

NORMALIZE_INPUTS = ["BTC", "ETH"]
OBSERVE_NODES = {
    "AAPL": "AAPL_close",
    "AMD": "AMD_close",
    "AVGO": "AVGO_close",
    "BTC": "BTCUSD_close",
    "CL": "CL_close",
    "ETH": "ETHUSD_close",
    "GC": "GC_close",
    "NVDA": "NVDA_close",
    "QQQ": "QQQ_close",
    "SOXX": "SOXX_close",
    "SPY": "SPY_close",
    "TSM": "TSM_close",
    "USO": "USO_close",
    "XLE": "XLE_close",
}
PATH_TASKS = {
    "AAPL->NVDA": ("AAPL_close", "NVDA_close"),
    "AMD->NVDA": ("AMD_close", "NVDA_close"),
    "AVGO->NVDA": ("AVGO_close", "NVDA_close"),
    "TSM->NVDA": ("TSM_close", "NVDA_close"),
    "QQQ->NVDA": ("QQQ_close", "NVDA_close"),
    "SPY->NVDA": ("SPY_close", "NVDA_close"),
    "SOXX->NVDA": ("SOXX_close", "NVDA_close"),
    "AAPL->AMD": ("AAPL_close", "AMD_close"),
    "NVDA->AMD": ("NVDA_close", "AMD_close"),
    "AVGO->AMD": ("AVGO_close", "AMD_close"),
    "TSM->AMD": ("TSM_close", "AMD_close"),
    "QQQ->AMD": ("QQQ_close", "AMD_close"),
    "SPY->AMD": ("SPY_close", "AMD_close"),
    "SOXX->AMD": ("SOXX_close", "AMD_close"),
    "NVDA->AVGO": ("NVDA_close", "AVGO_close"),
    "AMD->AVGO": ("AMD_close", "AVGO_close"),
    "NVDA->TSM": ("NVDA_close", "TSM_close"),
    "AMD->TSM": ("AMD_close", "TSM_close"),
}
INTERVENTION_TASKS = {
    "NVDA->AMD": ("NVDA_close", "AMD_close"),
    "SOXX->AMD": ("SOXX_close", "AMD_close"),
}

TRANSIENT_ERROR_MARKERS = (
    "timed out",
    "connection reset",
    "remote end closed connection",
    "unexpected eof",
    "temporarily unavailable",
)


def _looks_transient(text: str | None) -> bool:
    if not text:
        return False
    lowered = text.lower()
    return any(marker in lowered for marker in TRANSIENT_ERROR_MARKERS)


def _should_retry(stdout_json: object, stderr_text: str) -> bool:
    if isinstance(stdout_json, dict):
        if stdout_json.get("status_code") == -1 and _looks_transient(str(stdout_json.get("message", ""))):
            return True
        if stdout_json.get("ok") is False:
            message = str(stdout_json.get("message", ""))
            error = stdout_json.get("error", {})
            error_message = error.get("message") if isinstance(error, dict) else ""
            if _looks_transient(message) or _looks_transient(str(error_message)):
                return True
    return _looks_transient(stderr_text)


def run_probe(slug: str, args: list[str], *, include_base_url: bool = True) -> dict[str, object]:
    cmd = [sys.executable, str(CAP_PROBE)]
    if include_base_url:
        cmd += ["--base-url", BASE_URL]
    cmd += args + ["--compact"]

    payload: dict[str, object] | None = None
    for attempt in range(4):
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
        if not _should_retry(stdout_json, stderr_text):
            break

    assert payload is not None
    (RAW_DIR / f"{slug}.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return payload


def extract_normalized_node(payload: dict[str, object]) -> str | None:
    stdout = payload.get("stdout")
    if not isinstance(stdout, dict) or not stdout.get("ok"):
        return None
    value = stdout.get("normalized_node_id")
    return str(value) if value else None


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
                "attempt": payload["attempt"],
            }
        )
        return payload

    normalize_payloads: dict[str, dict[str, object]] = {}
    for alias in NORMALIZE_INPUTS:
        normalize_payloads[alias] = capture(f"normalize_{alias}", ["normalize-node", alias], include_base_url=False)

    observe_payloads: dict[str, dict[str, object]] = {}
    for alias, node in OBSERVE_NODES.items():
        observe_payloads[alias] = capture(f"observe_{node}", ["observe", node])

    path_payloads: dict[str, dict[str, object]] = {}
    for key, (source_node, target_node) in PATH_TASKS.items():
        path_payloads[key] = capture(
            f"path_{source_node}__{target_node}",
            ["paths", source_node, target_node, "--max-paths", "3"],
        )

    intervention_payloads: dict[str, dict[str, object]] = {}
    for key, (treatment_node, outcome_node) in INTERVENTION_TASKS.items():
        intervention_payloads[key] = capture(
            f"intervene_{treatment_node}__{outcome_node}",
            ["intervene-do", treatment_node, "0.05", "--outcome-node", outcome_node],
        )

    facts = {
        "snapshot_meta": {
            "version": "v12-general-finance-challenge",
            "snapshot_label": SNAPSHOT_LABEL,
            "captured_at": datetime.now(timezone.utc).isoformat(),
            "base_url": BASE_URL,
            "artifacts_manifest": "artifacts/manifest.json",
        },
        "normalized_nodes": {
            alias: extract_normalized_node(payload)
            for alias, payload in normalize_payloads.items()
        },
        "availability": {
            alias: extract_status(payload)
            for alias, payload in observe_payloads.items()
        },
        "observe_pct": {
            alias: value
            for alias, payload in observe_payloads.items()
            if (value := extract_prediction_pct(payload)) is not None
        },
        "graph_paths": {
            key: extract_path_fact(payload)
            for key, payload in path_payloads.items()
        },
        "interventions": {
            key: extract_intervention_fact(payload)
            for key, payload in intervention_payloads.items()
        },
    }

    (ARTIFACTS_DIR / "snapshot_facts.json").write_text(
        json.dumps(facts, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (ARTIFACTS_DIR / "manifest.json").write_text(
        json.dumps({"entries": manifest_entries}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(facts, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
