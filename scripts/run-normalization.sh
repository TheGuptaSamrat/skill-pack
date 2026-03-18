#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
raw_dir="$repo_root/metadata-drop/raw-excel"

if [[ $# -gt 1 ]]; then
  echo "Usage: $0 [workbook.xlsx]" >&2
  exit 2
fi

if [[ $# -eq 1 ]]; then
  workbook="$1"
  if [[ "$workbook" != /* ]]; then
    workbook="$raw_dir/$workbook"
  fi
else
  workbook="$(find "$raw_dir" -maxdepth 1 -type f -name '*.xlsx' | sort | tail -n 1)"
fi

if [[ -z "${workbook:-}" || ! -f "$workbook" ]]; then
  echo "No .xlsx workbook found. Put a workbook in $raw_dir or pass a filename." >&2
  exit 2
fi

echo "Normalizing workbook: $workbook"
python3 "$repo_root/scripts/normalize_excel.py" "$workbook"
