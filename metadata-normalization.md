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

Easier wrapper:

```bash
./scripts/run-normalization.sh <workbook>.xlsx
```

If you omit the workbook name, the wrapper picks the latest `.xlsx` file in `metadata-drop/raw-excel/`.

Optional explicit artifact id:

```bash
python3 scripts/normalize_excel.py metadata-drop/raw-excel/<workbook>.xlsx --artifact-id fpsl-fsdm-2023-drop-01
```

## VS Code

With this repo open in VS Code, run:

1. `Terminal: Run Task`
2. choose `Metadata: Normalize latest workbook`

That runs the wrapper script and normalizes the newest workbook from `metadata-drop/raw-excel/`.

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

## Document Ingestion

For PDF or text-based documentation ingestion, run:

```bash
python3 scripts/ingest_pdf_context.py docs-context/inbox/example.pdf docs-context/inbox/section-config.json
```

Cross-platform note:

- On Windows 11, prefer installing `pdftotext` or providing a preconverted `.txt` or `.md` file.
- The ingestion script does not depend on macOS-only `PDFKit`.
