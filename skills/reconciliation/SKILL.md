---
name: reconciliation
description: Business data verification - DDIC-aware reconciliation SQL, data-flow checks, totals validation, key integrity across processes, and process-run verification queries for FPSL and FSDM flows.
---

# Reconciliation (Business Data Verification)

Use this skill for investigative SQL and process-level validation. Do not use for structural schema compliance—use `quality` for DDIC rule definitions. Use `reconciliation` only for cross-process totals, control balancing, and operational run verification.

## Load Order

1. Read this file.
2. Read [reconciliation-core-rules.md](./references/reconciliation-core-rules.md) for rule types (totals, row counts, key integrity, data flow, cross-system) and core principles.
3. Read [reconciliation-core-patterns.md](./references/reconciliation-core-patterns.md) for 4 real-world SQL patterns (daily totals, source-to-target completeness, FK orphans, amount reconciliation).
4. Read [query-rules.md](./references/query-rules.md).
5. Read [fpsl-monitoring-operations.md](./references/fpsl-monitoring-operations.md) for FPSL process-run validation, periodic task verification, error handling, and operational checkpoints.
6. Read [official-sources.md](./references/official-sources.md).
7. Read [adt-handoff-rules.md](./references/adt-handoff-rules.md) when output is meant for Eclipse SQL Console or ADT paste.

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
