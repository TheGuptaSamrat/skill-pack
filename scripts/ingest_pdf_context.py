#!/usr/bin/env python3
"""Ingest a PDF or preconverted text into docs-context/full-source-md.

This script is cross-platform. For PDF extraction it prefers ``pdftotext`` or
an installed ``pypdf`` package. If neither is available, users can provide a
preconverted `.txt` or `.md` file instead of a PDF.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def extract_page_text_with_pdftotext(pdf_path: Path, page_index: int) -> str:
    if shutil.which("pdftotext") is None:
        raise RuntimeError("pdftotext not available")

    proc = subprocess.run(
        [
            "pdftotext",
            "-f",
            str(page_index + 1),
            "-l",
            str(page_index + 1),
            "-layout",
            str(pdf_path),
            "-",
        ],
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"pdftotext failed for page {page_index + 1}")
    return proc.stdout.strip()


def extract_page_text_with_pypdf(pdf_path: Path, page_index: int) -> str:
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError as exc:
        raise RuntimeError("pypdf not installed") from exc

    reader = PdfReader(str(pdf_path))
    if page_index >= len(reader.pages):
        raise RuntimeError(f"Page {page_index + 1} out of range")
    return (reader.pages[page_index].extract_text() or "").strip()


def extract_page_text(pdf_path: Path, page_index: int) -> str:
    errors: list[str] = []
    for extractor in (extract_page_text_with_pdftotext, extract_page_text_with_pypdf):
        try:
            return extractor(pdf_path, page_index)
        except RuntimeError as exc:
            errors.append(str(exc))
    raise RuntimeError(
        "No supported PDF extractor available. Install pdftotext, install pypdf, "
        "or provide a preconverted .txt/.md source file instead. "
        f"Details: {'; '.join(errors)}"
    )


def read_text_source(source_path: Path) -> str:
    return source_path.read_text(encoding="utf-8")


def write_section(out_path: Path, section: dict, source_name: str, body: str) -> None:
    header = [
        f"Classification: {section['classification']}",
        f"Source basis: {source_name}, {section['source_range']}",
        f"Trust usage: {section['trust_usage']}",
        f"Do not use for: {section['do_not_use_for']}",
        f"Topics covered: {', '.join(section['topics'])}",
        "",
        f"# {section['title']}",
        "",
    ]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(header) + body.strip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Ingest PDF or text into docs-context markdown")
    parser.add_argument("source", help="Path to a .pdf, .txt, or .md source document")
    parser.add_argument("config")
    args = parser.parse_args()

    source_path = Path(args.source).resolve()
    config_path = Path(args.config).resolve()
    if not source_path.exists() or not config_path.exists():
        print("Source or config file not found", file=sys.stderr)
        return 2

    config = json.loads(config_path.read_text(encoding="utf-8"))
    repo_root = Path(__file__).resolve().parents[1]
    target_root = repo_root / config["target_root"]
    source_suffix = source_path.suffix.lower()

    for section in config["sections"]:
        if source_suffix == ".pdf":
            parts = []
            for page in range(section["start_page"] - 1, section["end_page"]):
                text = extract_page_text(source_path, page)
                if text:
                    parts.append(text)
            body = "\n\n".join(parts)
            section["source_range"] = f"pages {section['start_page']}-{section['end_page']}"
        elif source_suffix in {".txt", ".md"}:
            body = read_text_source(source_path)
            section["source_range"] = "preconverted text source"
        else:
            print("Supported source types: .pdf, .txt, .md", file=sys.stderr)
            return 2
        out_path = target_root / section["filename"]
        write_section(out_path, section, source_path.name, body)

    print(f"Ingested {source_path.name} into {target_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
