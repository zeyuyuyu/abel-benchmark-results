#!/usr/bin/env python3
"""Shared benchmark API for cross-agent usage."""

from __future__ import annotations

import json
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


MANIFEST_REL = Path("v14/public_benchmark_manifest.json")
MANIFEST_BUILDER_REL = Path("v14/build_public_benchmark_manifest.py")
RUN_BENCHMARK_REL = Path("scripts/run_benchmark.py")

BOXED_RE = re.compile(r"^\\boxed\{(.+)\}$")


@dataclass(frozen=True)
class PackFiles:
    pack_id: str
    questions_path: Path
    ground_truth_path: Path
    cases_markdown_path: Path | None
    results_markdown_path: Path | None


def _looks_like_repo(path: Path) -> bool:
    return (path / "v14").exists() and (path / RUN_BENCHMARK_REL).exists()


def resolve_repo_root(repo_override: str | None = None) -> Path:
    if repo_override:
        path = Path(repo_override).expanduser().resolve()
        if _looks_like_repo(path):
            return path
        raise ValueError(f"Invalid repo path: {path}")

    env_repo = os.getenv("ABEL_BENCHMARK_REPO", "").strip()
    if env_repo:
        path = Path(env_repo).expanduser().resolve()
        if _looks_like_repo(path):
            return path
        raise ValueError(f"ABEL_BENCHMARK_REPO is invalid: {path}")

    cwd = Path.cwd().resolve()
    if _looks_like_repo(cwd):
        return cwd

    for parent in cwd.parents:
        if _looks_like_repo(parent):
            return parent

    fallback = Path.home() / "abel-benchmark-results"
    if _looks_like_repo(fallback):
        return fallback

    raise ValueError(
        "Could not locate abel-benchmark-results. Set ABEL_BENCHMARK_REPO "
        "or pass --repo."
    )


def _run(cmd: list[str], *, cwd: Path) -> tuple[int, str, str]:
    completed = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=False)
    return completed.returncode, completed.stdout, completed.stderr


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_manifest(repo_root: Path) -> Path:
    manifest_path = repo_root / MANIFEST_REL
    if manifest_path.exists():
        return manifest_path

    builder = repo_root / MANIFEST_BUILDER_REL
    if not builder.exists():
        raise ValueError(f"Manifest missing and builder not found: {builder}")

    code, stdout, stderr = _run(["python3", str(builder)], cwd=repo_root)
    if code != 0:
        raise ValueError(
            "Failed to build public manifest.\n"
            f"stdout:\n{stdout[-1000:]}\n"
            f"stderr:\n{stderr[-1000:]}"
        )
    if not manifest_path.exists():
        raise ValueError(f"Manifest still missing after build: {manifest_path}")
    return manifest_path


def load_manifest(repo_root: Path) -> dict[str, Any]:
    manifest_path = ensure_manifest(repo_root)
    return _load_json(manifest_path)


def list_packs(repo_root: Path) -> list[dict[str, Any]]:
    manifest = load_manifest(repo_root)
    packs = manifest.get("packs", [])
    out: list[dict[str, Any]] = []
    for pack in packs:
        out.append(
            {
                "pack_id": pack.get("pack_id"),
                "name": pack.get("name"),
                "track": pack.get("track"),
                "split": pack.get("split"),
                "task_family": pack.get("task_family"),
                "evaluation_regime": pack.get("evaluation_regime"),
                "case_count": pack.get("case_count"),
                "ground_truth_ready": f"{pack.get('ground_truth_available_count', 0)}/{pack.get('case_count', 0)}",
                "search_policy": pack.get("search_policy"),
            }
        )
    return out


def get_pack(repo_root: Path, pack_id: str) -> dict[str, Any]:
    manifest = load_manifest(repo_root)
    for pack in manifest.get("packs", []):
        if pack.get("pack_id") == pack_id:
            return pack
    raise ValueError(f"Unknown pack_id: {pack_id}")


def get_pack_files(repo_root: Path, pack_id: str) -> PackFiles:
    pack = get_pack(repo_root, pack_id)
    questions_rel = pack.get("questions_path")
    truth_rel = pack.get("ground_truth_path")
    if not questions_rel or not truth_rel:
        raise ValueError(f"Pack {pack_id} does not include questions/ground truth path.")
    questions_path = repo_root / questions_rel
    ground_truth_path = repo_root / truth_rel
    cases_markdown_rel = pack.get("cases_markdown_path") or None
    results_markdown_rel = pack.get("results_markdown_path") or None
    return PackFiles(
        pack_id=pack_id,
        questions_path=questions_path,
        ground_truth_path=ground_truth_path,
        cases_markdown_path=(repo_root / cases_markdown_rel) if cases_markdown_rel else None,
        results_markdown_path=(repo_root / results_markdown_rel) if results_markdown_rel else None,
    )


def _truth_answer_string(truth_case: dict[str, Any]) -> str | None:
    status = str(truth_case.get("status", "")).strip().lower()
    if status == "pending":
        return None

    answer_box = truth_case.get("answer_box")
    if isinstance(answer_box, str):
        cleaned = answer_box.strip()
        if cleaned and cleaned.lower() not in {"none", "null"}:
            return cleaned

    canonical = truth_case.get("canonical_answer")
    if isinstance(canonical, str) and canonical.strip():
        return canonical.strip()

    tokens = truth_case.get("answer_tokens")
    if isinstance(tokens, list):
        cleaned_tokens = [str(token).strip() for token in tokens if str(token).strip()]
        if cleaned_tokens:
            return "\\boxed{" + ", ".join(cleaned_tokens) + "}"

    return None


def _parse_boxed_tokens(value: str | None) -> tuple[str, ...] | None:
    if not value:
        return None
    match = BOXED_RE.fullmatch(value.strip())
    if not match:
        return None
    inner = match.group(1).strip()
    if not inner:
        return tuple()
    tokens = [part.strip() for part in inner.split(",")]
    tokens = [token for token in tokens if token]
    return tuple(sorted(tokens))


def _normalize_text_answer(value: str | None) -> str:
    if not value:
        return ""
    return " ".join(value.strip().lower().split())


def _extract_prediction_map(pred_doc: Any) -> dict[str, str]:
    result: dict[str, str] = {}

    def push(case_id: Any, prediction: Any) -> None:
        if case_id is None or prediction is None:
            return
        key = str(case_id).strip()
        if not key:
            return
        result[key] = str(prediction).strip()

    if isinstance(pred_doc, dict):
        if "predictions" in pred_doc and isinstance(pred_doc["predictions"], list):
            for item in pred_doc["predictions"]:
                if isinstance(item, dict):
                    pred = item.get("prediction", item.get("answer", item.get("response")))
                    push(item.get("id"), pred)
            return result
        for key, value in pred_doc.items():
            if isinstance(value, str):
                push(key, value)
            elif isinstance(value, dict):
                pred = value.get("prediction", value.get("answer", value.get("response")))
                push(key, pred)
        return result

    if isinstance(pred_doc, list):
        for item in pred_doc:
            if isinstance(item, dict):
                pred = item.get("prediction", item.get("answer", item.get("response")))
                push(item.get("id"), pred)
        return result

    raise ValueError("Unsupported predictions payload format.")


def get_cases(
    repo_root: Path,
    pack_id: str,
    *,
    include_ground_truth: bool = False,
    limit: int | None = None,
    case_ids: list[str] | None = None,
) -> dict[str, Any]:
    files = get_pack_files(repo_root, pack_id)
    questions_doc = _load_json(files.questions_path)
    truth_doc = _load_json(files.ground_truth_path)
    truth_map = {item.get("id"): item for item in truth_doc.get("cases", [])}

    cases = questions_doc.get("cases", [])
    if case_ids:
        keep = set(case_ids)
        cases = [case for case in cases if case.get("id") in keep]
    if limit is not None:
        cases = cases[: max(0, limit)]

    output_cases: list[dict[str, Any]] = []
    for case in cases:
        item = dict(case)
        if include_ground_truth:
            truth_case = truth_map.get(case.get("id"), {})
            item["ground_truth"] = truth_case
            item["truth_answer"] = _truth_answer_string(truth_case)
        output_cases.append(item)

    return {
        "pack_id": pack_id,
        "case_count": len(output_cases),
        "source_questions_file": str(files.questions_path),
        "source_ground_truth_file": str(files.ground_truth_path),
        "cases": output_cases,
    }


def score_predictions(
    repo_root: Path,
    pack_id: str,
    predictions_payload: Any,
) -> dict[str, Any]:
    files = get_pack_files(repo_root, pack_id)
    questions_doc = _load_json(files.questions_path)
    truth_doc = _load_json(files.ground_truth_path)

    question_map = {case.get("id"): case for case in questions_doc.get("cases", [])}
    truth_map = {case.get("id"): case for case in truth_doc.get("cases", [])}
    pred_map = _extract_prediction_map(predictions_payload)

    evaluated: list[dict[str, Any]] = []
    correct_count = 0
    scored_count = 0
    truth_ready_count = 0
    missing_prediction_ids: list[str] = []
    pending_truth_ids: list[str] = []

    for case_id, question in question_map.items():
        truth_case = truth_map.get(case_id, {})
        truth_answer = _truth_answer_string(truth_case)
        prediction = pred_map.get(case_id)

        if truth_answer is None:
            pending_truth_ids.append(case_id)
            status = "pending_truth"
            is_correct = None
        else:
            truth_ready_count += 1
            if prediction is None:
                missing_prediction_ids.append(case_id)
                status = "missing_prediction"
                is_correct = False
            else:
                truth_boxed = _parse_boxed_tokens(truth_answer)
                pred_boxed = _parse_boxed_tokens(prediction)
                if truth_boxed is not None and pred_boxed is not None:
                    is_correct = truth_boxed == pred_boxed
                else:
                    is_correct = _normalize_text_answer(prediction) == _normalize_text_answer(truth_answer)
                status = "scored"
                scored_count += 1
                if is_correct:
                    correct_count += 1

        evaluated.append(
            {
                "id": case_id,
                "task_family": question.get("task_family"),
                "truth_answer": truth_answer,
                "prediction": prediction,
                "status": status,
                "correct": is_correct,
            }
        )

    accuracy = (correct_count / scored_count) if scored_count else None
    return {
        "pack_id": pack_id,
        "total_cases": len(question_map),
        "truth_ready_cases": truth_ready_count,
        "predicted_cases": len(pred_map),
        "scored_cases": scored_count,
        "correct_cases": correct_count,
        "accuracy": round(accuracy, 4) if accuracy is not None else None,
        "pending_truth_case_count": len(pending_truth_ids),
        "missing_prediction_case_count": len(missing_prediction_ids),
        "pending_truth_ids": pending_truth_ids,
        "missing_prediction_ids": missing_prediction_ids,
        "case_results": evaluated,
    }


def run_repo_pack(
    repo_root: Path,
    pack: str,
    extra_args: list[str] | None = None,
) -> dict[str, Any]:
    command = ["python3", str(repo_root / RUN_BENCHMARK_REL), pack]
    if extra_args:
        command.extend(extra_args)
    code, stdout, stderr = _run(command, cwd=repo_root)
    return {
        "pack": pack,
        "command": command,
        "returncode": code,
        "stdout": stdout,
        "stderr": stderr,
    }
