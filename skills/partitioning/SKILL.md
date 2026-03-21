---
name: partitioning
description: "Use for HANA partitioning strategy and review for FPSL-relevant tables, including volume and growth assessment, access-pattern analysis, SAP-aligned partition recommendations, and validation planning when users need operationally safe partition guidance grounded in evidence rather than assumed table behavior or unsupported layouts."
---

# Partitioning

Use this skill for HANA table partitioning strategy and review in FPSL-relevant landscapes.

See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md) for clarification on when to use this skill vs. others.

## Load Order

1. Read this file.
2. Read [partitioning-core-rules.md](./references/partitioning-core-rules.md).
3. Read [partitioning-core-concepts.md](./references/partitioning-core-concepts.md) for partitioning types (range, hash, round-robin) and key SAP Notes references.
4. Read [fpsl-partitioning-sap-notes.md](./references/fpsl-partitioning-sap-notes.md) for critical SAP Notes on FPSL partitioning strategy, data tiering, scale-out architecture, and performance optimization.
5. Read [partitioning-examples.md](./references/partitioning-examples.md) for real-world examples (HFPPD date-range, HKTVR hash, reference tables).
6. Read [partitioning-validation.md](./references/partitioning-validation.md).
7. Read [official-sources.md](../../docs-context/shared/official-sources-router.md).

## Trust Order

1. Official SAP documentation and actual system evidence for table volume, access patterns, and supported partition behavior
2. Active normalized metadata for concrete table and key structure
3. Reviewed repository guidance for FPSL/HANA operational framing
4. Trusted raw metadata when normalization is missing
5. Synthetic examples only for shape

Do not invent table volumes, filter patterns, or approved partition layouts.

## Workflow

1. Confirm the exact table, result type, or storage area under discussion.
2. Measure or request evidence for volume, growth, access pattern, and runtime pain points.
3. Evaluate partitioning together with archiving, residence time, and Basis/HANA operations.
4. Return a recommendation only when the evidence supports it.
5. Include validation steps and operational cautions.

## Non-Negotiables

- Do not recommend partitioning as a default modeling pattern.
- Do not invent SAP-approved partition rules or customer-specific DB settings.
- Make archiving, growth, and access-pattern assumptions explicit.
- Route SQL validation to `reconciliation` and code changes to `amdp` or `abap`.

## Expected Output

- partitioning scope summary
- evidence and assumptions
- recommendation or no-go view
- operational implications
- validation and review steps
