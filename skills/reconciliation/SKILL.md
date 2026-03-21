---
name: reconciliation
description: Generate and review DDIC-aware reconciliation SQL, data-flow checks, totals validation, key integrity checks, and process-run verification queries for FPSL and FSDM flows.
---

# Reconciliation

Use this skill for investigative SQL and data-validation work.

## Load Order

1. Read this file.
2. Read [query-rules.md](./references/query-rules.md).
3. Read [official-sources.md](./references/official-sources.md).
4. Read [adt-handoff-rules.md](./references/adt-handoff-rules.md) when output is meant for Eclipse SQL Console or ADT paste.

## Trust Order

1. Official SAP documentation for supported product behavior and terminology
2. Active normalized metadata for actual tables, fields, and keys
3. Trusted raw metadata when normalization is missing
4. Synthetic examples only for shape

## Workflow

1. Confirm the source step, target step, and expected control totals.
2. Prefer SQL checks for counts, keys, totals, and run-state indicators.
3. Keep unresolved names as placeholders when metadata is incomplete.
4. Return the smallest useful query set first.

## Non-Negotiables

- Do not invent fields, totals, or run markers.
- Separate confirmed checks from inferred checks.
- Prefer narrow, DDIC-aware queries over generic table scans.

## Expected Output

- short assumptions
- reconciliation query set
- what each query validates
- unresolved placeholders if evidence is missing
- validation notes
