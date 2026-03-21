#!/usr/bin/env python3
"""Validate local markdown links and skill/instruction routing consistency.

This script is deterministic and uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def is_external_link(link: str) -> bool:
    lowered = link.lower().strip()
    return lowered.startswith("http://") or lowered.startswith("https://") or lowered.startswith("mailto:")


def normalize_target(target: str) -> str:
    target = re.sub(r"\s+", "", target)
    if "#" in target:
        target = target.split("#", 1)[0]
    return target


def collect_markdown_files(repo_root: Path) -> List[Path]:
    paths: List[Path] = []
    paths.extend(sorted(repo_root.glob("skills/*/SKILL.md")))
    paths.extend(sorted(repo_root.glob(".github/instructions/*.instructions.md")))
    return paths


def validate_links(repo_root: Path, path: Path) -> List[str]:
    errors: List[str] = []
    text = path.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(text):
        raw_target = normalize_target(match.group(1))
        if not raw_target or is_external_link(raw_target):
            continue
        resolved = (path.parent / raw_target).resolve()
        if not resolved.exists():
            rel_path = path.relative_to(repo_root).as_posix()
            errors.append(f"{rel_path}: missing link target -> {raw_target}")
    return errors


def validate_instruction_mapping(repo_root: Path) -> List[str]:
    errors: List[str] = []
    for instruction in sorted(repo_root.glob(".github/instructions/*.instructions.md")):
        skill_name = instruction.name.replace(".instructions.md", "")
        expected = f"skills/{skill_name}/SKILL.md"
        text = instruction.read_text(encoding="utf-8")
        if expected not in text:
            rel = instruction.relative_to(repo_root).as_posix()
            errors.append(f"{rel}: does not reference {expected}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate markdown links and skill mappings")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to repository root",
    )
    parser.add_argument(
        "--out-json",
        default="docs-context/indexes/validation-skill-pack.json",
        help="Output report path relative to repo root",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()

    files = collect_markdown_files(repo_root)
    link_errors: List[str] = []
    for md_file in files:
        link_errors.extend(validate_links(repo_root, md_file))

    mapping_errors = validate_instruction_mapping(repo_root)

    report: Dict[str, object] = {
        "checked_files": [p.relative_to(repo_root).as_posix() for p in files],
        "link_errors": link_errors,
        "mapping_errors": mapping_errors,
        "ok": not link_errors and not mapping_errors,
    }

    out_json = repo_root / args.out_json
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(report, indent=2), encoding="utf-8")

    if link_errors or mapping_errors:
        print("Validation failed.", file=sys.stderr)
        for err in link_errors + mapping_errors:
            print(f"- {err}", file=sys.stderr)
        print(f"Saved report: {out_json.relative_to(repo_root)}", file=sys.stderr)
        return 1

    print("Validation passed.")
    print(f"Saved report: {out_json.relative_to(repo_root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
