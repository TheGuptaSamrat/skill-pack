---
name: quality
description: Structural data conformance - DDIC-driven data quality rules for FPSL and FSDM flows. Use for completeness, consistency, key, null, type, domain, and cross-field checks.
---

# Quality (Structural Data Conformance)

Use this skill for structural data quality rule generation (schema compliance, field validation). Do not use for cross-process verification or business logic validation—use `reconciliation` for that.

See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md) for clarification on when to use this skill vs. others.

## Load Order

1. Read this file.
2. Read [quality-core-rules.md](./references/quality-core-rules.md) for rule generation hierarchy (confirmed/inferred/unresolved), rule categories (null, domain, key, type, cross-field, referential integrity).
3. Read [quality-core-patterns.md](./references/quality-core-patterns.md) for 7 real-world patterns: null checks, domain validation, key uniqueness, FK referential integrity, type/format validation, cross-field business logic, completeness checks.
4. Read [metadata-sources.md](./references/metadata-sources.md) for DDIC evidence hierarchy and artifact types.
5. Read [quality-validation-checklist.md](./references/quality-validation-checklist.md) for pre-deployment validation, testing strategies, and production readiness guidance.
6. Read [official-sources.md](./references/official-sources.md) for standard FPSL/FSDM terminology when framing quality rules.
7. Read [adt-handoff-rules.md](./references/adt-handoff-rules.md) when quality rule output is meant for SQL Console or automated deployment.

## Trust Order

1. Official SAP documentation for product terminology and standard framing
2. Active normalized metadata for actual fields, keys, and domains
3. Trusted raw metadata when normalization is missing
4. Synthetic examples only for shape

## Workflow

1. Confirm the layer or checkpoint being validated.
2. Inventory available DDIC, SDL, or RDL evidence.
3. Build confirmed rules first.
4. Separate inferred rules and unresolved gaps.
5. Return SQL or rule-spec outputs based on the evidence provided.

## Non-Negotiables

- Do not invent fields, domains, or rule semantics.
- Keep confirmed and inferred rules separate.
- Use placeholders when DDIC or rule meaning is incomplete.
- Prefer narrow, field-aware checks over generic boilerplate.

## Expected Output

- assumptions
- confirmed quality rules
- inferred quality rules
- unresolved evidence gaps
- SQL or rule-spec output
- validation notes
