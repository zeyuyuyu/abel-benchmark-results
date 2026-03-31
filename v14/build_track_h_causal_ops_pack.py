#!/usr/bin/env python3
"""Build Track H (causal network operations) benchmark pack.

This pack is designed to measure practical causal-tool advantage in analyst-style
tasks without directly naming Abel in question wording.
"""

from __future__ import annotations

import json
import random
import re
import subprocess
import time
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
ARTIFACTS_DIR = ROOT / "artifacts"

QUESTIONS_PATH = ROOT / "track_h_causal_ops_questions.json"
GROUND_TRUTH_PATH = ROOT / "track_h_causal_ops_ground_truth.json"
CASES_MD_PATH = ROOT / "track_h_causal_ops_cases.md"
SPEC_MD_PATH = ROOT / "track_h_causal_ops_spec.md"
SNAPSHOT_PATH = ARTIFACTS_DIR / "track_h_causal_ops_snapshot.json"

CAP_PROBE = Path.home() / ".codex/skills/causal-abel/scripts/cap_probe.py"

RNG_SEED = 20260331
TARGET_TOTAL_CASES = 24
EACH_FAMILY_CASES = 6

# Start with liquid names plus a few crypto majors.
TICKER_POOL = [
    "SPY",
    "QQQ",
    "DIA",
    "IWM",
    "NVDA",
    "AAPL",
    "MSFT",
    "AMZN",
    "META",
    "GOOGL",
    "TSLA",
    "AMD",
    "AVGO",
    "INTC",
    "NFLX",
    "COIN",
    "MSTR",
    "PYPL",
    "JPM",
    "GS",
    "XOM",
    "CVX",
    "UAL",
    "DAL",
    "BTC",
    "ETH",
    "SOL",
    "XRP",
    "DOGE",
    "ADA",
]

LABELS = ["A", "B", "C", "D"]


def run_cap(args: list[str]) -> dict[str, Any]:
    cmd = ["python3", str(CAP_PROBE), *args, "--compact"]
    completed = subprocess.run(cmd, capture_output=True, text=True, check=False)
    raw = (completed.stdout or "").strip()
    if completed.returncode != 0:
        # cap_probe often returns JSON even on non-zero codes.
        if raw.startswith("{"):
            try:
                return json.loads(raw)
            except Exception:  # noqa: BLE001
                pass
        return {
            "ok": False,
            "status_code": completed.returncode,
            "message": (completed.stderr or "").strip()[-800:],
            "raw_stdout": raw[-800:],
        }
    if not raw:
        return {"ok": False, "status_code": -1, "message": "empty response"}
    try:
        return json.loads(raw)
    except Exception as exc:  # noqa: BLE001
        return {
            "ok": False,
            "status_code": -1,
            "message": f"json_parse_error: {exc}",
            "raw_stdout": raw[-800:],
        }


def normalize_node(ticker: str) -> str | None:
    payload = run_cap(["normalize-node", ticker])
    if payload.get("ok"):
        return str(payload.get("normalized_node_id"))
    return None


def fetch_observe(node_or_ticker: str) -> dict[str, Any] | None:
    payload = run_cap(
        [
            "observe",
            node_or_ticker,
            "--pick-fields",
            "result.target_node,result.prediction,result.drivers,result.driver_nodes",
        ]
    )
    if not payload.get("ok"):
        return None
    result = payload.get("result", {})
    if not isinstance(result, dict):
        return None
    pred = result.get("prediction")
    if not isinstance(pred, (int, float)):
        return None
    return {
        "target_node": str(result.get("target_node", node_or_ticker)),
        "prediction": float(pred),
        "drivers": result.get("drivers", []),
    }


def fetch_parents(node_or_ticker: str) -> list[str]:
    payload = run_cap(
        [
            "neighbors",
            node_or_ticker,
            "--scope",
            "parents",
            "--max-neighbors",
            "12",
            "--pick-fields",
            "result.neighbors",
        ]
    )
    if not payload.get("ok"):
        return []
    neighbors = payload.get("result", {}).get("neighbors", [])
    if not isinstance(neighbors, list):
        return []
    out: list[str] = []
    for row in neighbors:
        if isinstance(row, dict) and isinstance(row.get("node_id"), str):
            out.append(row["node_id"])
    return sorted(set(out))


def fetch_markov_neighbors(node_or_ticker: str) -> list[dict[str, Any]]:
    payload = run_cap(
        [
            "markov-blanket",
            node_or_ticker,
            "--max-neighbors",
            "15",
            "--pick-fields",
            "result.neighbors",
        ]
    )
    if not payload.get("ok"):
        return []
    neighbors = payload.get("result", {}).get("neighbors", [])
    if not isinstance(neighbors, list):
        return []
    out: list[dict[str, Any]] = []
    for row in neighbors:
        if not isinstance(row, dict):
            continue
        node_id = row.get("node_id")
        roles = row.get("roles")
        if isinstance(node_id, str) and isinstance(roles, list) and roles:
            out.append(
                {
                    "node_id": node_id,
                    "roles": [str(role) for role in roles],
                }
            )
    return out


def fetch_path_exists(source: str, target: str) -> tuple[bool | None, dict[str, Any]]:
    payload = run_cap(
        [
            "paths",
            source,
            target,
            "--max-paths",
            "1",
            "--pick-fields",
            "result.path_count,result.paths",
        ]
    )
    if not payload.get("ok"):
        return None, payload
    result = payload.get("result", {})
    if isinstance(result, dict):
        count = result.get("path_count")
        if isinstance(count, int):
            return count > 0, payload
        paths = result.get("paths")
        if isinstance(paths, list):
            return len(paths) > 0, payload
    return None, payload


def short_name(node_id: str) -> str:
    return node_id.replace(".price", "").replace(".volume", "")


def canonical_role(roles: list[str]) -> str:
    role_set = {role.lower() for role in roles}
    if "parent" in role_set:
        return "parent"
    if "child" in role_set:
        return "child"
    if "spouse" in role_set:
        return "spouse"
    return "other"


def mc_options_from_items(items: list[str], *, labels: list[str] = LABELS) -> list[dict[str, str]]:
    return [{"label": label, "text": item} for label, item in zip(labels, items, strict=False)]


def pick_distractors(
    rng: random.Random,
    pool_nodes: list[str],
    excluded: set[str],
    need: int,
) -> list[str]:
    candidates = [node for node in pool_nodes if node not in excluded]
    if len(candidates) < need:
        return []
    return rng.sample(candidates, need)


def build_cases() -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    rng = random.Random(RNG_SEED)

    normalized_nodes: list[str] = []
    for ticker in TICKER_POOL:
        node = normalize_node(ticker)
        if node:
            normalized_nodes.append(node)
    normalized_nodes = sorted(set(normalized_nodes))

    observe_map: dict[str, dict[str, Any]] = {}
    for node in normalized_nodes:
        observed = fetch_observe(node)
        if observed:
            observe_map[node] = observed

    parent_map: dict[str, list[str]] = {}
    blanket_map: dict[str, list[dict[str, Any]]] = {}
    for node in observe_map:
        parent_map[node] = fetch_parents(node)
        blanket_map[node] = fetch_markov_neighbors(node)

    # Build candidate pools.
    observe_nodes = sorted(observe_map.keys())
    parent_targets = [node for node, parents in parent_map.items() if parents]
    blanket_targets = [node for node, rows in blanket_map.items() if rows]

    cases: list[dict[str, Any]] = []
    truths: list[dict[str, Any]] = []
    artifacts: dict[str, Any] = {
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "seed": RNG_SEED,
        "source": "live_abel_cap_snapshot",
        "families": {},
    }

    case_index = 1

    def next_id() -> str:
        nonlocal case_index
        case_id = f"v14h_{case_index:03d}"
        case_index += 1
        return case_id

    # Family 1: Cross-asset upside selection (observe.predict ranking).
    fam_rows: list[dict[str, Any]] = []
    observe_candidates = observe_nodes[:]
    rng.shuffle(observe_candidates)
    while len(fam_rows) < EACH_FAMILY_CASES and len(observe_candidates) >= 4:
        picks = rng.sample(observe_candidates, 4)
        scored = sorted(
            ((node, observe_map[node]["prediction"]) for node in picks),
            key=lambda row: row[1],
            reverse=True,
        )
        # Require unique winner to avoid ambiguous key.
        if len(scored) >= 2 and abs(scored[0][1] - scored[1][1]) < 1e-12:
            continue
        answer_node = scored[0][0]
        option_texts = [f"{short_name(node)}" for node in picks]
        options = mc_options_from_items(option_texts)
        label_map = {short_name(node): options[i]["label"] for i, node in enumerate(picks)}
        answer_label = label_map[short_name(answer_node)]

        case_id = next_id()
        cases.append(
            {
                "id": case_id,
                "split": "public_dev",
                "track": "causal_network_operations",
                "source_family": ["Finance Agent", "XFinBench", "FutureX"],
                "task_family": "cross_asset_upside_selection",
                "evaluation_regime": "frozen_evidence_public_dev",
                "title": f"Cross-Asset Upside Pick ({short_name(picks[0])}/{short_name(picks[1])}/{short_name(picks[2])}/{short_name(picks[3])})",
                "category": "upside_selection",
                "question": (
                    "You are preparing a one-step tactical note from an internal causal market network. "
                    "Among the following assets, which one currently has the strongest upside signal?"
                ),
                "options": options,
                "answer_format": "boxed_letters",
            }
        )
        truths.append(
            {
                "id": case_id,
                "answer_box": f"\\boxed{{{answer_label}}}",
                "answer_tokens": [answer_label],
                "grounding": {
                    "family": "cross_asset_upside_selection",
                    "winner_node": answer_node,
                    "winner_prediction": observe_map[answer_node]["prediction"],
                    "option_nodes": picks,
                    "option_predictions": {node: observe_map[node]["prediction"] for node in picks},
                },
            }
        )
        fam_rows.append(
            {
                "id": case_id,
                "winner_node": answer_node,
                "winner_prediction": observe_map[answer_node]["prediction"],
                "option_nodes": picks,
                "option_predictions": {node: observe_map[node]["prediction"] for node in picks},
            }
        )
    artifacts["families"]["cross_asset_upside_selection"] = fam_rows

    # Family 2: Direct parent selection.
    fam_rows = []
    parent_targets_shuffled = parent_targets[:]
    rng.shuffle(parent_targets_shuffled)
    for target in parent_targets_shuffled:
        if len(fam_rows) >= EACH_FAMILY_CASES:
            break
        true_parent = rng.choice(parent_map[target])
        distractors = pick_distractors(
            rng,
            observe_nodes,
            excluded={target, *parent_map[target]},
            need=3,
        )
        if len(distractors) < 3:
            continue
        option_nodes = [true_parent, *distractors]
        rng.shuffle(option_nodes)
        options = mc_options_from_items([short_name(node) for node in option_nodes])
        label_map = {short_name(node): options[i]["label"] for i, node in enumerate(option_nodes)}
        answer_label = label_map[short_name(true_parent)]

        case_id = next_id()
        cases.append(
            {
                "id": case_id,
                "split": "public_dev",
                "track": "causal_network_operations",
                "source_family": ["Finance Agent", "XFinBench", "CLADDER"],
                "task_family": "direct_parent_identification",
                "evaluation_regime": "frozen_evidence_public_dev",
                "title": f"Direct Upstream Driver For {short_name(target)}",
                "category": "parent_identification",
                "question": (
                    f"For risk decomposition on {short_name(target)}, which candidate is currently a direct upstream driver "
                    "in the causal market network?"
                ),
                "options": options,
                "answer_format": "boxed_letters",
            }
        )
        truths.append(
            {
                "id": case_id,
                "answer_box": f"\\boxed{{{answer_label}}}",
                "answer_tokens": [answer_label],
                "grounding": {
                    "family": "direct_parent_identification",
                    "target_node": target,
                    "true_parent_node": true_parent,
                    "all_parent_nodes": parent_map[target],
                    "option_nodes": option_nodes,
                },
            }
        )
        fam_rows.append(
            {
                "id": case_id,
                "target_node": target,
                "true_parent_node": true_parent,
                "all_parent_nodes": parent_map[target],
                "option_nodes": option_nodes,
            }
        )
    artifacts["families"]["direct_parent_identification"] = fam_rows

    # Family 3: Markov-neighbor role classification.
    fam_rows = []
    blanket_targets_shuffled = blanket_targets[:]
    rng.shuffle(blanket_targets_shuffled)
    for target in blanket_targets_shuffled:
        if len(fam_rows) >= EACH_FAMILY_CASES:
            break
        row = rng.choice(blanket_map[target])
        neighbor = row["node_id"]
        role = canonical_role(row["roles"])
        if role not in {"parent", "child", "spouse"}:
            continue
        role_to_label = {"parent": "A", "child": "B", "spouse": "C"}
        answer_label = role_to_label[role]

        options = [
            {"label": "A", "text": "Parent (direct upstream driver)"},
            {"label": "B", "text": "Child (direct downstream receiver)"},
            {"label": "C", "text": "Spouse (shares a child but not a direct parent/child link)"},
            {"label": "D", "text": "None of the above"},
        ]

        case_id = next_id()
        cases.append(
            {
                "id": case_id,
                "split": "public_dev",
                "track": "causal_network_operations",
                "source_family": ["CounterBench", "Finance Agent", "XFinBench"],
                "task_family": "markov_role_classification",
                "evaluation_regime": "frozen_evidence_public_dev",
                "title": f"Role Of {short_name(neighbor)} Relative To {short_name(target)}",
                "category": "markov_role",
                "question": (
                    f"In the current causal market network, what is the relationship role of {short_name(neighbor)} "
                    f"relative to {short_name(target)}?"
                ),
                "options": options,
                "answer_format": "boxed_letters",
            }
        )
        truths.append(
            {
                "id": case_id,
                "answer_box": f"\\boxed{{{answer_label}}}",
                "answer_tokens": [answer_label],
                "grounding": {
                    "family": "markov_role_classification",
                    "target_node": target,
                    "neighbor_node": neighbor,
                    "neighbor_roles": row["roles"],
                },
            }
        )
        fam_rows.append(
            {
                "id": case_id,
                "target_node": target,
                "neighbor_node": neighbor,
                "neighbor_roles": row["roles"],
            }
        )
    artifacts["families"]["markov_role_classification"] = fam_rows

    # Family 4: Directed path reachability.
    fam_rows = []
    # positives from known parent links
    positive_pairs: list[tuple[str, str]] = []
    for target, parents in parent_map.items():
        for parent in parents:
            positive_pairs.append((parent, target))
    rng.shuffle(positive_pairs)

    # negatives sampled by testing random pairs with no path.
    negative_pairs: list[tuple[str, str]] = []
    attempts = 0
    while len(negative_pairs) < EACH_FAMILY_CASES and attempts < 500:
        attempts += 1
        source, target = rng.sample(observe_nodes, 2)
        ok, payload = fetch_path_exists(source, target)
        if ok is None:
            continue
        if not ok:
            negative_pairs.append((source, target))

    # pick up to 3 positives + 3 negatives.
    pos_take = min(EACH_FAMILY_CASES // 2, len(positive_pairs))
    neg_take = min(EACH_FAMILY_CASES - pos_take, len(negative_pairs))
    selected = [(pair, True) for pair in positive_pairs[:pos_take]] + [
        (pair, False) for pair in negative_pairs[:neg_take]
    ]
    rng.shuffle(selected)

    for (source, target), path_exists in selected:
        answer_label = "A" if path_exists else "B"
        options = [
            {"label": "A", "text": "Yes, there is at least one directed causal path."},
            {"label": "B", "text": "No, no directed causal path is present."},
        ]
        case_id = next_id()
        cases.append(
            {
                "id": case_id,
                "split": "public_dev",
                "track": "causal_network_operations",
                "source_family": ["CLADDER", "Finance Agent", "FutureX"],
                "task_family": "directed_path_reachability",
                "evaluation_regime": "frozen_evidence_public_dev",
                "title": f"Path Reachability: {short_name(source)} -> {short_name(target)}",
                "category": "path_reachability",
                "question": (
                    f"For fast shock-propagation screening, can a directed causal influence from {short_name(source)} "
                    f"reach {short_name(target)} in the current market network?"
                ),
                "options": options,
                "answer_format": "boxed_letters",
            }
        )
        truths.append(
            {
                "id": case_id,
                "answer_box": f"\\boxed{{{answer_label}}}",
                "answer_tokens": [answer_label],
                "grounding": {
                    "family": "directed_path_reachability",
                    "source_node": source,
                    "target_node": target,
                    "path_exists": path_exists,
                },
            }
        )
        fam_rows.append(
            {
                "id": case_id,
                "source_node": source,
                "target_node": target,
                "path_exists": path_exists,
            }
        )
    artifacts["families"]["directed_path_reachability"] = fam_rows

    # Keep exactly target total by stable truncation if we generated a bit more.
    cases = cases[:TARGET_TOTAL_CASES]
    truths = truths[:TARGET_TOTAL_CASES]

    # Synchronize IDs in truths after truncation.
    keep_ids = {case["id"] for case in cases}
    truths = [truth for truth in truths if truth["id"] in keep_ids]

    artifacts["summary"] = {
        "case_count": len(cases),
        "family_counts": {
            "cross_asset_upside_selection": len(artifacts["families"]["cross_asset_upside_selection"]),
            "direct_parent_identification": len(artifacts["families"]["direct_parent_identification"]),
            "markov_role_classification": len(artifacts["families"]["markov_role_classification"]),
            "directed_path_reachability": len(artifacts["families"]["directed_path_reachability"]),
        },
        "observe_nodes_count": len(observe_nodes),
        "parent_targets_count": len(parent_targets),
        "blanket_targets_count": len(blanket_targets),
    }
    return cases, truths, artifacts


def write_markdown(cases: list[dict[str, Any]], truths: dict[str, dict[str, Any]]) -> None:
    lines = [
        "# v14 Track H Causal Ops Cases",
        "",
        "This pack evaluates practical causal-network operations in analyst language.",
        "Ground truth is generated from a frozen CAP snapshot and stored separately.",
        "",
        f"- Case count: `{len(cases)}`",
        "- Track: `causal_network_operations`",
        "- Evaluation regime: `frozen_evidence_public_dev`",
        "",
    ]
    for case in cases:
        truth = truths[case["id"]]
        lines.extend(
            [
                f"## {case['id']} — {case['title']}",
                "",
                f"- Task family: `{case['task_family']}`",
                f"- Category: `{case['category']}`",
                "Question:",
                case["question"],
                "",
                "Options:",
            ]
        )
        for opt in case["options"]:
            lines.append(f"- {opt['label']}. {opt['text']}")
        lines.extend(
            [
                "",
                "Ground truth:",
                f"- {truth['answer_box']}",
                "",
            ]
        )
    CASES_MD_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_spec(case_count: int) -> None:
    lines = [
        "# v14 Track H Causal Ops Spec",
        "",
        "## Purpose",
        "",
        "Track H measures whether an agent can operationally use a causal market network",
        "for practical analyst tasks (selection, upstream attribution, role typing,",
        "reachability checks).",
        "",
        "## Design Principles",
        "",
        "- Natural analyst question wording, not direct 'Abel function' wording.",
        "- Programmatic ground truth from frozen CAP snapshot evidence.",
        "- Questions and answers are separated (`questions.json` vs `ground_truth.json`).",
        "",
        "## Composition",
        "",
        f"- Total cases: `{case_count}`",
        "- Families:",
        "  - `cross_asset_upside_selection`",
        "  - `direct_parent_identification`",
        "  - `markov_role_classification`",
        "  - `directed_path_reachability`",
        "",
        "## Files",
        "",
        "- `track_h_causal_ops_questions.json`",
        "- `track_h_causal_ops_ground_truth.json`",
        "- `track_h_causal_ops_cases.md`",
        "- `artifacts/track_h_causal_ops_snapshot.json`",
        "",
    ]
    SPEC_MD_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    cases, truths, artifacts = build_cases()

    questions = {
        "version": "v14-track-h-causal-ops-questions",
        "split": "public_dev",
        "track": "causal_network_operations",
        "task_family": "causal_network_operations",
        "evaluation_regime": "frozen_evidence_public_dev",
        "case_count": len(cases),
        "notes": [
            "Natural analyst-style causal-network operation tasks.",
            "Ground truth is generated from a frozen CAP snapshot.",
            "Answers are in a separate ground-truth file.",
        ],
        "cases": cases,
    }
    truth_payload = {
        "version": "v14-track-h-causal-ops-ground-truth",
        "split": "public_dev",
        "case_count": len(truths),
        "notes": [
            "Programmatic answer keys derived from CAP snapshot artifacts.",
            "Do not expose this file to the evaluated model during benchmark runs.",
        ],
        "cases": truths,
    }

    QUESTIONS_PATH.write_text(json.dumps(questions, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    GROUND_TRUTH_PATH.write_text(
        json.dumps(truth_payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    SNAPSHOT_PATH.write_text(json.dumps(artifacts, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    truth_map = {item["id"]: item for item in truths}
    write_markdown(cases, truth_map)
    write_spec(len(cases))

    print(f"wrote {QUESTIONS_PATH}")
    print(f"wrote {GROUND_TRUTH_PATH}")
    print(f"wrote {SNAPSHOT_PATH}")
    print(f"wrote {CASES_MD_PATH}")
    print(f"wrote {SPEC_MD_PATH}")
    print(f"built track_h_causal_ops with {len(cases)} cases")


if __name__ == "__main__":
    main()
