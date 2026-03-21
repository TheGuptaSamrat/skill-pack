#!/usr/bin/env python3
"""Audit skill-pack redundancy to reduce context pressure.

This script is deterministic and uses only the Python standard library.
It scans skill and instruction markdown files for repeated section blocks and
reference-file duplication patterns.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")
DESCRIPTION_RE = re.compile(r"^description:\s*(.+?)\s*$", re.MULTILINE)


@dataclass
class SectionBlock:
    name: str
    content: str


def normalize_text(value: str) -> str:
    lines = [line.rstrip() for line in value.strip().splitlines()]
    # Normalize whitespace while preserving semantic structure.
    compact = "\n".join(line for line in lines if line)
    compact = re.sub(r"\s+", " ", compact).strip().lower()
    return compact


def parse_sections(path: Path) -> List[SectionBlock]:
    lines = path.read_text(encoding="utf-8").splitlines()
    sections: List[SectionBlock] = []
    current_name: str | None = None
    current_lines: List[str] = []

    for line in lines:
        match = SECTION_RE.match(line)
        if match:
            if current_name is not None:
                sections.append(SectionBlock(current_name, "\n".join(current_lines).strip()))
            current_name = match.group(1).strip()
            current_lines = []
            continue
        if current_name is not None:
            current_lines.append(line)

    if current_name is not None:
        sections.append(SectionBlock(current_name, "\n".join(current_lines).strip()))

    return sections


def parse_description(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    frontmatter = parts[1]
    match = DESCRIPTION_RE.search(frontmatter)
    if not match:
        return ""
    raw = match.group(1).strip()
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        raw = raw[1:-1]
    return raw


def file_count(paths: Iterable[Path], suffix: str) -> int:
    return sum(1 for p in paths if p.as_posix().endswith(suffix))


def collect(repo_root: Path) -> Dict[str, object]:
    skills = sorted(repo_root.glob("skills/*/SKILL.md"))
    instructions = sorted(repo_root.glob(".github/instructions/*.instructions.md"))
    references = sorted(repo_root.glob("skills/*/references/*.md"))

    section_index: Dict[str, Dict[str, List[str]]] = defaultdict(lambda: defaultdict(list))
    section_presence: Dict[str, List[str]] = defaultdict(list)

    description_audit: List[Dict[str, object]] = []

    for skill_file in skills:
        skill_name = skill_file.parent.name
        description = parse_description(skill_file)
        desc_len = len(description)
        in_recommended_range = 250 <= desc_len <= 500
        description_audit.append(
            {
                "skill": skill_name,
                "length": desc_len,
                "recommended": in_recommended_range,
            }
        )
        for section in parse_sections(skill_file):
            digest = hashlib.sha256(normalize_text(section.content).encode("utf-8")).hexdigest()
            section_index[section.name][digest].append(skill_name)
            section_presence[section.name].append(skill_name)

    repeated_sections: List[Dict[str, object]] = []
    for section_name, digests in section_index.items():
        for digest, skill_names in digests.items():
            if len(skill_names) > 1:
                repeated_sections.append(
                    {
                        "section": section_name,
                        "skills": sorted(skill_names),
                        "count": len(skill_names),
                        "digest": digest[:12],
                    }
                )

    repeated_sections.sort(key=lambda row: (-int(row["count"]), row["section"]))

    metrics = {
        "skill_files": len(skills),
        "instruction_files": len(instructions),
        "reference_files": len(references),
        "official_sources_wrappers": file_count(references, "references/official-sources.md"),
        "adt_handoff_wrappers": file_count(references, "references/adt-handoff-rules.md"),
        "metadata_sources_wrappers": file_count(references, "references/metadata-sources.md"),
        "repeated_section_groups": len(repeated_sections),
        "descriptions_in_250_500": sum(1 for row in description_audit if row["recommended"]),
        "descriptions_outside_250_500": sum(1 for row in description_audit if not row["recommended"]),
    }

    section_presence_rows = [
        {
            "section": section,
            "count": len(sorted(set(skill_names))),
            "skills": sorted(set(skill_names)),
        }
        for section, skill_names in section_presence.items()
    ]
    section_presence_rows.sort(key=lambda row: (-int(row["count"]), row["section"]))

    return {
        "metrics": metrics,
        "repeated_sections": repeated_sections,
        "section_presence": section_presence_rows,
        "description_audit": sorted(description_audit, key=lambda row: row["skill"]),
        "skills": [p.relative_to(repo_root).as_posix() for p in skills],
        "instructions": [p.relative_to(repo_root).as_posix() for p in instructions],
    }


def render_markdown(data: Dict[str, object]) -> str:
    metrics = data["metrics"]
    repeated = data["repeated_sections"]
    section_presence = data["section_presence"]
    description_audit = data["description_audit"]

    lines = [
        "# Skill Pack Redundancy Audit",
        "",
        "This report is generated by `scripts/audit_skill_pack_redundancy.py`.",
        "",
        "## Metrics",
        "",
        f"- skill files: `{metrics['skill_files']}`",
        f"- instruction files: `{metrics['instruction_files']}`",
        f"- reference markdown files: `{metrics['reference_files']}`",
        f"- `official-sources.md` wrappers: `{metrics['official_sources_wrappers']}`",
        f"- `adt-handoff-rules.md` wrappers: `{metrics['adt_handoff_wrappers']}`",
        f"- `metadata-sources.md` wrappers: `{metrics['metadata_sources_wrappers']}`",
        f"- repeated section groups across skills: `{metrics['repeated_section_groups']}`",
        f"- skill descriptions in recommended 250-500 char range: `{metrics['descriptions_in_250_500']}`",
        f"- skill descriptions outside 250-500 char range: `{metrics['descriptions_outside_250_500']}`",
        "",
        "## Highest-Impact Duplicate Section Groups",
        "",
    ]

    if not repeated:
        lines.append("- No repeated section groups detected.")
    else:
        for row in repeated[:20]:
            skill_list = ", ".join(row["skills"])  # type: ignore[index]
            lines.append(
                f"- section `{row['section']}` repeats in `{row['count']}` skills: {skill_list} "
                f"(fingerprint `{row['digest']}`)"
            )

    lines.extend(
        [
            "",
            "## Structural Duplication (Section Presence)",
            "",
        ]
    )

    common_rows = [row for row in section_presence if int(row["count"]) >= 8]
    if not common_rows:
        lines.append("- No highly repeated section headings detected.")
    else:
        for row in common_rows:
            skill_list = ", ".join(row["skills"])  # type: ignore[index]
            lines.append(
                f"- section `{row['section']}` appears in `{row['count']}` skills: {skill_list}"
            )

    lines.extend(
        [
            "",
            "## Skill Description Length Audit",
            "",
            "Best-practice note: keep `description` between 250 and 500 characters for better capability targeting without excess context load.",
            "",
        ]
    )

    for row in description_audit:
        status = "OK" if row["recommended"] else "OUTSIDE"
        lines.append(f"- `{row['skill']}`: `{row['length']}` chars -> `{status}`")

    lines.extend(
        [
            "",
            "## Scriptable Next Steps",
            "",
            "- Keep repeated policy text in one shared reference and point skills to that file.",
            "- Validate links and load-order references in CI or local smoke checks.",
            "- Use generated reports for review instead of loading all skill files in prompts.",
            "",
        ]
    )

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit redundancy in the skill pack")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[1]),
        help="Path to repository root",
    )
    parser.add_argument(
        "--out-md",
        default="docs-context/indexes/redundancy-audit.md",
        help="Markdown output path relative to repo root",
    )
    parser.add_argument(
        "--out-json",
        default="docs-context/indexes/redundancy-audit.json",
        help="JSON output path relative to repo root",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    data = collect(repo_root)

    out_md = repo_root / args.out_md
    out_json = repo_root / args.out_json
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.parent.mkdir(parents=True, exist_ok=True)

    out_md.write_text(render_markdown(data), encoding="utf-8")
    out_json.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print(f"Wrote markdown report: {out_md.relative_to(repo_root)}")
    print(f"Wrote json report: {out_json.relative_to(repo_root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
