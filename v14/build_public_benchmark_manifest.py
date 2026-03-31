#!/usr/bin/env python3
"""Build a public benchmark manifest/index for v14."""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
MANIFEST_PATH = ROOT / "public_benchmark_manifest.json"
MARKDOWN_PATH = ROOT / "public_benchmark_index.md"


PACK_SPECS = [
    {
        "pack_id": "public_dev_seed_pack",
        "name": "v14 Public Dev Seed Pack",
        "track": "multi_track_public_dev",
        "split": "public_dev",
        "task_family": "public_dev_seed_set",
        "evaluation_regime": "frozen_evidence_public_dev",
        "questions_file": "public_dev_cases.json",
        "ground_truth_file": "public_dev_ground_truth.json",
        "cases_markdown_file": "public_dev_case_results.md",
        "results_json_file": "public_dev_results.json",
        "results_markdown_file": "public_dev_benchmark_report.md",
        "run_command": "python3 scripts/run_benchmark.py v14-public-dev",
        "search_policy": "web_search_allowed_without_cutoff",
    },
    {
        "pack_id": "causal_proxy_intervention",
        "name": "v14 Causal/Proxy/Intervention Stress Pack",
        "track": "multi_track_public_dev",
        "split": "public_dev",
        "task_family": "causal_proxy_intervention_mix",
        "evaluation_regime": "frozen_evidence_public_dev",
        "questions_file": "causal_proxy_intervention_cases.json",
        "ground_truth_file": "causal_proxy_intervention_ground_truth.json",
        "cases_markdown_file": "causal_proxy_intervention_cases.md",
        "results_json_file": "",
        "results_markdown_file": "",
        "search_policy": "web_search_allowed_without_cutoff",
    },
    {
        "pack_id": "track_g_true_live",
        "name": "Track G True Live",
        "track": "agentic_live_analysis",
        "split": "track_g_true_live",
        "task_family": "futurex_style_live_prediction",
        "evaluation_regime": "live_forward_resolution",
        "questions_file": "track_g_true_live_questions.json",
        "ground_truth_file": "track_g_true_live_ground_truth.json",
        "cases_markdown_file": "track_g_true_live_cases.md",
        "results_json_file": "",
        "results_markdown_file": "",
        "run_command": "python3 scripts/run_benchmark.py v14-track-g-true-live",
        "search_policy": "web_search_allowed_live",
    },
    {
        "pack_id": "track_g_past_asof",
        "name": "Track G Past As-Of",
        "track": "agentic_live_analysis",
        "split": "track_g_past_asof",
        "task_family": "futurex_style_live_prediction",
        "evaluation_regime": "historical_asof_search_cutoff",
        "questions_file": "track_g_past_asof_questions.json",
        "ground_truth_file": "track_g_past_asof_ground_truth.json",
        "cases_markdown_file": "track_g_past_asof_cases.md",
        "results_json_file": "track_g_past_asof_results.json",
        "results_markdown_file": "track_g_past_asof_results.md",
        "run_command": "python3 scripts/run_benchmark.py v14-track-g-past-asof",
        "search_policy": "search_must_not_exceed_search_cutoff",
    },
    {
        "pack_id": "track_h_causal_ops",
        "name": "Track H Causal Network Operations",
        "track": "causal_network_operations",
        "split": "public_dev",
        "task_family": "causal_network_operations",
        "evaluation_regime": "frozen_evidence_public_dev",
        "questions_file": "track_h_causal_ops_questions.json",
        "ground_truth_file": "track_h_causal_ops_ground_truth.json",
        "cases_markdown_file": "track_h_causal_ops_cases.md",
        "results_json_file": "track_h_causal_ops_results.json",
        "results_markdown_file": "track_h_causal_ops_results.md",
        "run_command": "python3 v14/run_track_h_causal_ops_benchmark.py",
        "search_policy": "web_search_allowed_without_cutoff",
    },
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def has_truth(case: dict[str, Any]) -> bool:
    answer_box_raw = case.get("answer_box")
    answer_box = "" if answer_box_raw is None else str(answer_box_raw).strip()
    if answer_box:
        return True

    canonical_raw = case.get("canonical_answer")
    canonical = "" if canonical_raw is None else str(canonical_raw).strip()
    if canonical:
        return True

    answer_tokens = case.get("answer_tokens")
    if isinstance(answer_tokens, list):
        return bool([token for token in answer_tokens if str(token).strip()])

    return False


def summarize_pack(spec: dict[str, Any]) -> dict[str, Any]:
    questions_path = ROOT / spec["questions_file"]
    truth_path = ROOT / spec["ground_truth_file"]
    cases_path = ROOT / spec["cases_markdown_file"]
    results_json_file = spec.get("results_json_file") or None
    results_markdown_file = spec.get("results_markdown_file") or None
    results_json_path = ROOT / results_json_file if results_json_file else None
    results_markdown_path = ROOT / results_markdown_file if results_markdown_file else None

    question_doc = load_json(questions_path)
    truth_doc = load_json(truth_path)
    questions = question_doc.get("cases", [])
    truth_cases = truth_doc.get("cases", [])
    truth_by_id = {item.get("id"): item for item in truth_cases}

    case_count = len(questions)
    truth_count = 0
    unresolved_count = 0
    missing_truth_ids: list[str] = []

    for case in questions:
        case_id = case.get("id")
        truth = truth_by_id.get(case_id)
        if truth is None:
            missing_truth_ids.append(str(case_id))
            unresolved_count += 1
            continue
        if has_truth(truth):
            truth_count += 1
        else:
            unresolved_count += 1

    summary = dict(spec)
    summary.update(
        {
            "visibility": "public",
            "case_count": case_count,
            "ground_truth_available_count": truth_count,
            "ground_truth_pending_count": unresolved_count,
            "missing_ground_truth_count": len(missing_truth_ids),
            "missing_ground_truth_ids": missing_truth_ids,
            "questions_path": str(questions_path.relative_to(ROOT.parent)),
            "ground_truth_path": str(truth_path.relative_to(ROOT.parent)),
            "cases_markdown_path": str(cases_path.relative_to(ROOT.parent)),
            "results_json_path": str(results_json_path.relative_to(ROOT.parent))
            if results_json_path and results_json_path.exists()
            else "",
            "results_markdown_path": str(results_markdown_path.relative_to(ROOT.parent))
            if results_markdown_path and results_markdown_path.exists()
            else "",
        }
    )
    return summary


def build_manifest() -> dict[str, Any]:
    packs = [summarize_pack(spec) for spec in PACK_SPECS]
    return {
        "version": "v14-public-benchmark-manifest",
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "scope": "v14",
        "visibility": "public",
        "notes": [
            "All benchmark packs listed here are public artifacts in this repository.",
            "Track G past-asof enforces per-case search cutoff when running evaluation.",
            "Track G true-live keeps ground truth blank until future resolution.",
        ],
        "packs": packs,
    }


def build_markdown(manifest: dict[str, Any]) -> str:
    lines = [
        "# v14 Public Benchmark Index",
        "",
        "This file marks the `v14` benchmark as a **public benchmark suite**.",
        "",
        "- Scope: `v14`",
        "- Visibility: `public`",
        "- Generated from: `build_public_benchmark_manifest.py`",
        "",
        "## Public Rules",
        "",
        "- `historical_asof_search_cutoff` cases allow search, but search must not use evidence after each case's `search_cutoff` timestamp.",
        "- `live_forward_resolution` cases are unresolved by design; answer keys remain blank until third-party resolution.",
        "- Public dev packs can include answer keys for reproducible A/B development and harness debugging.",
        "",
        "## Pack Index",
        "",
        "| Pack | Track | Regime | Cases | Truth Ready | Questions | Ground Truth | Cases Markdown | Results |",
        "|---|---|---|---:|---:|---|---|---|---|",
    ]

    for pack in manifest["packs"]:
        results_display = (
            f"`{pack['results_markdown_path']}`"
            if pack.get("results_markdown_path")
            else "-"
        )
        lines.append(
            "| "
            f"`{pack['pack_id']}` | "
            f"`{pack['track']}` | "
            f"`{pack['evaluation_regime']}` | "
            f"{pack['case_count']} | "
            f"{pack['ground_truth_available_count']}/{pack['case_count']} | "
            f"`{pack['questions_path']}` | "
            f"`{pack['ground_truth_path']}` | "
            f"`{pack['cases_markdown_path']}` | "
            f"{results_display} |"
        )

    lines.extend(
        [
            "",
            "## Quick Commands",
            "",
            "```bash",
            "cd /Users/zeyu/Documents/bach_private_cache/abel-benchmark-results",
            "python3 v14/build_public_benchmark_manifest.py",
            "python3 scripts/run_benchmark.py check-skill",
            "python3 scripts/run_benchmark.py v14-track-g-past-asof",
            "python3 scripts/run_benchmark.py v14-track-g-true-live",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    manifest = build_manifest()
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    MARKDOWN_PATH.write_text(build_markdown(manifest), encoding="utf-8")
    print(f"Wrote {MANIFEST_PATH}")
    print(f"Wrote {MARKDOWN_PATH}")


if __name__ == "__main__":
    main()
