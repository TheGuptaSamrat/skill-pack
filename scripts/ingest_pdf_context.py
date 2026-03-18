#!/usr/bin/env python3
"""Ingest a PDF into docs-context/full-source-md using a section config."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def extract_page_text(pdf_path: Path, page_index: int) -> str:
    swift = f"""
import Foundation
import PDFKit
let url = URL(fileURLWithPath: "{pdf_path}")
guard let doc = PDFDocument(url: url), let page = doc.page(at: {page_index}) else {{
    exit(2)
}}
print(page.string ?? "")
"""
    proc = subprocess.run(
        ["swift", "-"],
        input=swift,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"Failed to read page {page_index + 1}")
    return proc.stdout.strip()


def write_section(out_path: Path, section: dict, pdf_name: str, body: str) -> None:
    header = [
        f"Classification: {section['classification']}",
        f"Source basis: {pdf_name}, pages {section['start_page']}-{section['end_page']}",
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
    parser = argparse.ArgumentParser(description="Ingest PDF to docs-context markdown")
    parser.add_argument("pdf")
    parser.add_argument("config")
    args = parser.parse_args()

    pdf_path = Path(args.pdf).resolve()
    config_path = Path(args.config).resolve()
    if not pdf_path.exists() or not config_path.exists():
        print("PDF or config file not found", file=sys.stderr)
        return 2

    config = json.loads(config_path.read_text(encoding="utf-8"))
    repo_root = Path(__file__).resolve().parents[1]
    target_root = repo_root / config["target_root"]

    for section in config["sections"]:
        parts = []
        for page in range(section["start_page"] - 1, section["end_page"]):
            text = extract_page_text(pdf_path, page)
            if text:
                parts.append(text)
        out_path = target_root / section["filename"]
        write_section(out_path, section, pdf_path.name, "\n\n".join(parts))

    print(f"Ingested {pdf_path.name} into {target_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
