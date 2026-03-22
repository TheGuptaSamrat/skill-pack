#!/usr/bin/env python3
"""Estimate skill context cost and efficiency using deterministic repo-local heuristics.

This script does not depend on model-specific tokenizers. It uses a stable
character-to-token heuristic so metrics remain comparable over time.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List

LOAD_ORDER_HEADER_RE = re.compile(r"^##\s+Load Order\s*$", re.MULTILINE)
SECTION_HEADER_RE = re.compile(r"^##\s+", re.MULTILINE)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
BACKTICK_PATH_RE = re.compile(r"`([^`]+)`")


@dataclass
class FileMetric:
    path: str
    lines: int
    chars: int
    estimated_tokens: int


def estimate_tokens(text: str) -> int:
    return math.ceil(len(text) / 4) if text else 0


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def file_metric(path: Path, repo_root: Path) -> FileMetric:
    text = read_text(path)
    return FileMetric(
        path=path.relative_to(repo_root).as_posix(),
        lines=len(text.splitlines()),
        chars=len(text),
        estimated_tokens=estimate_tokens(text),
    )


def extract_load_order_paths(skill_path: Path) -> List[str]:
    text = read_text(skill_path)
    load_match = LOAD_ORDER_HEADER_RE.search(text)
    if not load_match:
        return []

    remainder = text[load_match.end():]
    next_section = SECTION_HEADER_RE.search(remainder)
    load_block = remainder[: next_section.start()] if next_section else remainder

    paths: List[str] = []
    for match in MARKDOWN_LINK_RE.finditer(load_block):
        paths.append(match.group(1).strip())
    for match in BACKTICK_PATH_RE.finditer(load_block):
        candidate = match.group(1).strip()
        if "/" in candidate and candidate.endswith(".md"):
            paths.append(candidate)
    return paths


def resolve_paths(base_path: Path, raw_paths: Iterable[str]) -> List[Path]:
    resolved: List[Path] = []
    seen: set[Path] = set()
    for raw in raw_paths:
        candidate = (base_path.parent / raw).resolve()
        if candidate.exists() and candidate not in seen:
            seen.add(candidate)
            resolved.append(candidate)
    return resolved


def collect_skill_metrics(repo_root: Path) -> Dict[str, object]:
    skill_files = sorted(repo_root.glob("skills/*/SKILL.md"))
    instruction_files = {
        path.stem.replace(".instructions", ""): path
        for path in repo_root.glob(".github/instructions/*.instructions.md")
    }

    per_skill: List[Dict[str, object]] = []

    for skill_file in skill_files:
        skill_name = skill_file.parent.name
        instruction_file = instruction_files.get(skill_name)
        load_refs = resolve_paths(skill_file, extract_load_order_paths(skill_file))

        instruction_metric = (
            file_metric(instruction_file, repo_root) if instruction_file else None
        )
        skill_metric = file_metric(skill_file, repo_root)

        ref_metrics: List[FileMetric] = []
        for ref in load_refs:
            if ref == skill_file:
                continue
            ref_metrics.append(file_metric(ref, repo_root))

        entry_tokens = skill_metric.estimated_tokens + (
            instruction_metric.estimated_tokens if instruction_metric else 0
        )
        full_tokens = entry_tokens + sum(m.estimated_tokens for m in ref_metrics)
        full_chars = skill_metric.chars + (
            instruction_metric.chars if instruction_metric else 0
        ) + sum(m.chars for m in ref_metrics)
        load_steps = len(extract_load_order_paths(skill_file))

        per_skill.append(
            {
                "skill": skill_name,
                "instruction": instruction_metric.__dict__ if instruction_metric else None,
                "skill_file": skill_metric.__dict__,
                "references": [m.__dict__ for m in ref_metrics],
                "load_steps": load_steps,
                "reference_count": len(ref_metrics),
                "entrypoint_tokens": entry_tokens,
                "full_load_tokens": full_tokens,
                "entrypoint_chars": skill_metric.chars
                + (instruction_metric.chars if instruction_metric else 0),
                "full_load_chars": full_chars,
                "expansion_ratio": round(full_tokens / entry_tokens, 2)
                if entry_tokens
                else 0.0,
                "avg_tokens_per_step": round(full_tokens / load_steps, 1)
                if load_steps
                else 0.0,
            }
        )

    per_skill.sort(key=lambda row: int(row["full_load_tokens"]), reverse=True)

    full_loads = [int(row["full_load_tokens"]) for row in per_skill]
    entry_loads = [int(row["entrypoint_tokens"]) for row in per_skill]

    summary = {
        "skill_count": len(per_skill),
        "mean_entrypoint_tokens": round(sum(entry_loads) / len(entry_loads), 1)
        if entry_loads
        else 0.0,
        "mean_full_load_tokens": round(sum(full_loads) / len(full_loads), 1)
        if full_loads
        else 0.0,
        "max_full_load_skill": per_skill[0]["skill"] if per_skill else None,
        "max_full_load_tokens": per_skill[0]["full_load_tokens"] if per_skill else 0,
        "min_full_load_skill": per_skill[-1]["skill"] if per_skill else None,
        "min_full_load_tokens": per_skill[-1]["full_load_tokens"] if per_skill else 0,
    }

    return {"summary": summary, "skills": per_skill}


def render_markdown(data: Dict[str, object]) -> str:
    summary = data["summary"]
    skills = data["skills"]

    lines = [
        "# Skill Efficiency Report",
        "",
        "Deterministic heuristics report generated by `scripts/measure_skill_efficiency.py`.",
        "Estimated tokens use a simple `chars / 4` heuristic for trend tracking, not model-exact billing.",
        "",
        "## Summary",
        "",
        f"- skill count: `{summary['skill_count']}`",
        f"- mean entrypoint tokens: `{summary['mean_entrypoint_tokens']}`",
        f"- mean full-load tokens: `{summary['mean_full_load_tokens']}`",
        f"- heaviest full-load skill: `{summary['max_full_load_skill']}` at `{summary['max_full_load_tokens']}` tokens",
        f"- lightest full-load skill: `{summary['min_full_load_skill']}` at `{summary['min_full_load_tokens']}` tokens",
        "",
        "## Per-Skill Metrics",
        "",
        "| Skill | Load Steps | Refs | Entrypoint Tokens | Full-Load Tokens | Expansion Ratio | Avg Tokens/Step |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]

    for row in skills:
        lines.append(
            "| {skill} | {load_steps} | {reference_count} | {entrypoint_tokens} | {full_load_tokens} | {expansion_ratio} | {avg_tokens_per_step} |".format(
                **row
            )
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- `Entrypoint Tokens` approximates the cost of the GHCP instruction + `SKILL.md` entry surface.",
            "- `Full-Load Tokens` approximates the declared load-order cost if all load-order references are opened.",
            "- `Expansion Ratio` shows how much context grows from entrypoint to full load.",
            "- Use this report alongside developer feedback for accuracy and usability scoring.",
            "",
        ]
    )

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Measure skill efficiency heuristics")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to repository root",
    )
    parser.add_argument(
        "--out-md",
        default="docs-context/indexes/skill-efficiency-report.md",
        help="Markdown output path relative to repo root",
    )
    parser.add_argument(
        "--out-json",
        default="docs-context/indexes/skill-efficiency-report.json",
        help="JSON output path relative to repo root",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    data = collect_skill_metrics(repo_root)

    out_md = repo_root / args.out_md
    out_json = repo_root / args.out_json
    out_md.parent.mkdir(parents=True, exist_ok=True)

    out_md.write_text(render_markdown(data), encoding="utf-8")
    out_json.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Saved markdown report: {out_md.relative_to(repo_root).as_posix()}")
    print(f"Saved json report: {out_json.relative_to(repo_root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())