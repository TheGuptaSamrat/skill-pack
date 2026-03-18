---
name: sap-fpsl-amdp
description: Design, review, and troubleshoot SAP FPSL and FSDM AMDP, SQLScript, CDS table-function, and pushdown-heavy implementations. Use for HANA set-based transformations, performance-sensitive joins, aggregation logic, SQL writing standards, and ABAP wrapper design around AMDP artifacts.
---

# SAP FPSL AMDP

Use this skill for HANA pushdown work in FPSL and FSDM landscapes.

## Load Order

1. Read this file.
2. Read [amdp-delivery-rules.md](./references/amdp-delivery-rules.md) for implementation guidance.
3. Read [sql-and-performance-rules.md](./references/sql-and-performance-rules.md) when writing or reviewing SQLScript.

## Workflow

1. Confirm source dataset, target dataset, and output grain.
2. Keep orchestration and business checks in ABAP unless the task is clearly set-based.
3. Use AMDP for heavy joins, windowing, aggregation, deduplication, or high-volume filtering.
4. Keep SQL staged and readable.
5. Return the smallest paste-ready artifact set:
   - ABAP wrapper
   - AMDP method
   - test scaffold
   - validation checks

## Non-Negotiables

- Do not invent CDS names, classes, tables, or fields.
- Keep placeholder names explicit if exact metadata is missing.
- Make client handling, null handling, deduplication keys, and currency logic explicit.
- Prefer deterministic filters and multi-dimension predicates over broad scans.
- Explain why AMDP is justified instead of plain ABAP SQL.

## Expected Output

- short context and assumptions
- ABAP versus AMDP responsibility split
- production-style AMDP and wrapper code
- ABAP Unit or integration test scaffold
- validation and reconciliation checks
