---
name: amdp
description: Design and review AMDP, SQLScript, CDS table-function, and pushdown-heavy FPSL/FSDM implementations. Use for set-based transformations, aggregation, performance-sensitive joins, and ABAP wrapper design.
---

# AMDP

Use this skill for HANA pushdown work in FPSL and FSDM landscapes.

See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md) for clarification on when to use this skill vs. others.

## Load Order

1. Read this file.
2. Read [amdp-core-rules.md](./references/amdp-core-rules.md) for implementation and senior-developer guidance.
3. Read [amdp-query-patterns.md](./references/amdp-query-patterns.md) when rerun safety, reconciliation, filtering, rounding, batching, or JOIN versus `FOR ALL ENTRIES` decisions matter.
4. Read [sql-and-performance-rules.md](./references/sql-and-performance-rules.md) when writing or reviewing SQLScript.
5. Read [adt-handoff-rules.md](./references/adt-handoff-rules.md) when output is meant for Eclipse ADT or SQL Console paste.
6. Read [official-sources.md](./references/official-sources.md) when you need SAP-supported AMDP, ADT, or FPSL/FSDM anchors.
7. Read [hana-query-analysis-concepts.md](./references/hana-query-analysis-concepts.md) when query-processing or performance-analysis concepts need strengthening.
8. Use this skill for pushdown-heavy implementation; route specialist reconciliation work to `reconciliation` and checklist-led operational walkthroughs to `config`.

## Trust Order

1. Official SAP documentation for product scope and supported capabilities
2. Active normalized metadata in the repository for actual object names and structures
3. Trusted raw metadata only when normalization is missing or under comparison
4. Training-derived conceptual guidance for performance reasoning only
5. Synthetic examples only for output shape

Do not derive landscape-specific class names, CDS entities, DDIC layouts, or package names from public SAP documentation alone.

## Workflow

1. Confirm source dataset, target dataset, and output grain.
2. Keep orchestration and business checks in ABAP unless the task is clearly set-based.
3. Use AMDP for heavy joins, windowing, aggregation, deduplication, or high-volume filtering.
4. Generate reconciliation or data-flow-check queries when the task is investigative rather than implementation-heavy.
5. Use DDIC-aware query shapes when metadata is available.
6. Keep SQL staged and readable.
7. Return one ADT-ready artifact block at a time with `Artifact`, `Paste target`, `Action`, code, and `Checks`.
8. Return the smallest paste-ready artifact set:
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
- Do not use public SAP examples as proof that a custom landscape object exists.

## Expected Output

- short context and assumptions
- ABAP versus AMDP responsibility split
- one artifact block at a time for ADT or SQL Console paste
- production-style AMDP and wrapper code
- ABAP Unit or integration test scaffold
- validation and reconciliation checks
- SQL checks for data flow or process-run verification when requested
