#!/usr/bin/env python3
"""Validate repository filename conventions.

Rules:
- prefer lowercase with hyphens or underscores for non-special files (no uppercase, no spaces)
- allow conventional special names: README.md and SKILL.md
- allow source PDFs in metadata-drop/pdf-resources as authoritative artifacts
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ALLOWED_BASENAMES = {"README.md", "SKILL.md", ".gitignore"}
ALLOWED_PREFIXES = {
    "metadata-drop/pdf-resources/",
    ".git/",
}
VALID_NAME_RE = re.compile(r"^[a-z0-9.][a-z0-9._-]*$")


def is_allowed(path: str) -> bool:
    base = Path(path).name
    if base in ALLOWED_BASENAMES:
        return True
    return any(path.startswith(prefix) for prefix in ALLOWED_PREFIXES)


def repo_files(repo_root: Path) -> list[str]:
    paths: list[str] = []
    for path in repo_root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(repo_root).as_posix()
        if rel.startswith(".git/"):
            continue
        paths.append(rel)
    return sorted(paths)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate repository filename conventions")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to repository root",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    violations: list[str] = []

    for path in repo_files(repo_root):
        if is_allowed(path):
            continue
        base = Path(path).name
        if not VALID_NAME_RE.match(base):
            violations.append(path)

    if violations:
        print("Filename convention violations found:", file=sys.stderr)
        for path in violations:
            print(f"- {path}", file=sys.stderr)
        print(
            "Rule: use lowercase filenames with hyphens or underscores unless explicitly allowed (README.md, SKILL.md, source PDFs).",
            file=sys.stderr,
        )
        return 1

    print("Filename convention check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
