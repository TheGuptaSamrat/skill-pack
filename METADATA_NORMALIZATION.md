# Metadata Normalization

Use this workflow when a trusted FPSL, FSDM 2023, CDS, or DDIC workbook is uploaded.

## Goal

Convert large Excel workbooks into smaller normalized artifacts that the skills can use by default.

## Input

Place the source workbook in:

- `metadata-drop/raw-excel/`

Current script support:

- `.xlsx` only

## Command

```bash
python3 scripts/normalize_excel.py metadata-drop/raw-excel/<workbook>.xlsx
```

Optional explicit artifact id:

```bash
python3 scripts/normalize_excel.py metadata-drop/raw-excel/<workbook>.xlsx --artifact-id fpsl-fsdm-2023-drop-01
```

## Output

The script writes to:

- `metadata-drop/normalized/<artifact-id>/`

For each sheet it creates:

- one CSV file

It also updates:

- `metadata-drop/manifest.csv`
- `metadata-drop/change-review.md`

## Review Standard

After normalization:

1. inspect the generated CSV files
2. compare them with previous active normalized metadata
3. decide whether `change-review.md` should remain `minor-review` or be raised to `reverify-required`
4. use normalized files as the default context for skills

## Why This Works

- raw Excel stays as the trusted source input
- normalized files stay Git-friendly and Copilot-friendly
- skills can consume smaller artifacts without loading a whole workbook
- metadata refreshes become repeatable
