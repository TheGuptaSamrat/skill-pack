#!/usr/bin/env python3
"""Normalize trusted metadata workbooks into repo-friendly CSV outputs.

This script intentionally uses only the Python standard library so it can run
in constrained environments without extra package installs.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "main": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "rel": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pkgrel": "http://schemas.openxmlformats.org/package/2006/relationships",
}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "sheet"


def load_shared_strings(zf: zipfile.ZipFile) -> list[str]:
    try:
        data = zf.read("xl/sharedStrings.xml")
    except KeyError:
        return []

    root = ET.fromstring(data)
    values: list[str] = []
    for si in root.findall("main:si", NS):
        parts = []
        for node in si.iter():
            if node.tag == f"{{{NS['main']}}}t":
                parts.append(node.text or "")
        values.append("".join(parts))
    return values


def sheet_targets(zf: zipfile.ZipFile) -> dict[str, str]:
    workbook_rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rel_map: dict[str, str] = {}
    for rel in workbook_rels.findall("pkgrel:Relationship", NS):
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target")
        if rid and target:
            rel_map[rid] = target
    return rel_map


def ordered_sheet_meta(zf: zipfile.ZipFile) -> list[tuple[str, str]]:
    workbook = ET.fromstring(zf.read("xl/workbook.xml"))
    targets = sheet_targets(zf)
    sheets: list[tuple[str, str]] = []
    for sheet in workbook.findall("main:sheets/main:sheet", NS):
        name = sheet.attrib.get("name", "Sheet")
        rid = sheet.attrib.get(f"{{{NS['rel']}}}id")
        if not rid or rid not in targets:
            continue
        target = targets[rid]
        if not target.startswith("xl/"):
            target = f"xl/{target}"
        sheets.append((name, target))
    return sheets


def cell_value(cell: ET.Element, shared_strings: list[str]) -> str:
    cell_type = cell.attrib.get("t")
    value_node = cell.find("main:v", NS)
    if cell_type == "inlineStr":
        inline = cell.find("main:is/main:t", NS)
        return (inline.text or "").strip() if inline is not None else ""
    if value_node is None:
        return ""
    raw = value_node.text or ""
    if cell_type == "s":
        try:
            return shared_strings[int(raw)]
        except (ValueError, IndexError):
            return raw
    return raw


def col_index(ref: str) -> int:
    letters = "".join(ch for ch in ref if ch.isalpha()).upper()
    total = 0
    for ch in letters:
        total = total * 26 + (ord(ch) - ord("A") + 1)
    return max(total - 1, 0)


def sheet_rows(zf: zipfile.ZipFile, target: str, shared_strings: list[str]) -> list[list[str]]:
    root = ET.fromstring(zf.read(target))
    rows: list[list[str]] = []
    for row in root.findall("main:sheetData/main:row", NS):
        values: list[str] = []
        current_idx = 0
        for cell in row.findall("main:c", NS):
            ref = cell.attrib.get("r", "")
            idx = col_index(ref)
            while current_idx < idx:
                values.append("")
                current_idx += 1
            values.append(cell_value(cell, shared_strings))
            current_idx += 1
        rows.append(values)
    return rows


def write_csv(path: Path, rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def update_manifest(repo_root: Path, artifact_id: str, source_name: str, output_dir: Path) -> None:
    manifest_path = repo_root / "metadata-drop" / "manifest.csv"
    today = dt.date.today().isoformat()
    rel_output = output_dir.relative_to(repo_root).as_posix()
    row = [
        artifact_id,
        "raw-excel",
        source_name,
        "normalized",
        today,
        today,
        rel_output,
        "Normalized from trusted workbook via scripts/normalize_excel.py",
    ]

    existing: list[list[str]] = []
    if manifest_path.exists():
        with manifest_path.open("r", encoding="utf-8", newline="") as handle:
            existing = list(csv.reader(handle))

    if not existing:
        existing = [[
            "artifact_id",
            "source_type",
            "source_name",
            "status",
            "uploaded_on",
            "normalized_on",
            "active_path",
            "notes",
        ]]

    existing.append(row)
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(existing)


def update_change_log(repo_root: Path, artifact_id: str, source_name: str, sheet_count: int) -> None:
    review_path = repo_root / "metadata-drop" / "change-log.md"
    today = dt.date.today().isoformat()
    note = (
        "\n## Latest Normalization Event\n\n"
        f"- date: `{today}`\n"
        f"- artifact id: `{artifact_id}`\n"
        f"- source workbook: `{source_name}`\n"
        f"- sheets normalized: `{sheet_count}`\n"
        "- default status: `minor-review`\n"
        "- next action: compare normalized output with prior active metadata and upgrade to "
        "`reverify-required` if model-critical structures changed\n"
    )
    content = review_path.read_text(encoding="utf-8") if review_path.exists() else "# Change Log\n"
    marker = "## Latest Normalization Event"
    if marker in content:
        content = content.split(marker)[0].rstrip() + "\n"
    review_path.write_text(content + note, encoding="utf-8")


def normalize_workbook(repo_root: Path, workbook_path: Path, artifact_id: str) -> Path:
    output_dir = repo_root / "metadata-drop" / "normalized" / artifact_id
    output_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(workbook_path) as zf:
        shared_strings = load_shared_strings(zf)
        sheets = ordered_sheet_meta(zf)
        if not sheets:
            raise ValueError("No worksheets found in workbook")

        summary_lines = [
            "# Normalization Summary",
            "",
            f"- source workbook: `{workbook_path.name}`",
            f"- artifact id: `{artifact_id}`",
            f"- sheet count: `{len(sheets)}`",
            "",
            "## Sheets",
            "",
        ]

        for sheet_name, target in sheets:
            rows = sheet_rows(zf, target, shared_strings)
            csv_name = f"{slugify(sheet_name)}.csv"
            write_csv(output_dir / csv_name, rows)
            summary_lines.append(f"- `{sheet_name}` -> `{csv_name}`")

    (output_dir / "SUMMARY.md").write_text("\n".join(summary_lines) + "\n", encoding="utf-8")
    update_manifest(repo_root, artifact_id, workbook_path.name, output_dir)
    update_change_log(repo_root, artifact_id, workbook_path.name, len(sheets))
    return output_dir


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize a trusted metadata workbook")
    parser.add_argument("workbook", help="Path to a .xlsx workbook in metadata-drop/raw-excel/")
    parser.add_argument(
        "--artifact-id",
        help="Artifact identifier for normalized output. Defaults to workbook name slug.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    workbook_path = Path(args.workbook).resolve()
    if workbook_path.suffix.lower() != ".xlsx":
        print("Only .xlsx workbooks are supported by this lightweight normalizer.", file=sys.stderr)
        return 2
    if not workbook_path.exists():
        print(f"Workbook not found: {workbook_path}", file=sys.stderr)
        return 2

    artifact_id = args.artifact_id or slugify(workbook_path.stem)
    try:
        output_dir = normalize_workbook(repo_root, workbook_path, artifact_id)
    except Exception as exc:  # noqa: BLE001
        print(f"Normalization failed: {exc}", file=sys.stderr)
        return 1

    print(f"Normalized workbook into {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
