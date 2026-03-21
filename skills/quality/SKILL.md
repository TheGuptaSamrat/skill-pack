---
name: quality
description: Structural data conformance - DDIC-driven data quality rules for FPSL and FSDM flows. Use for completeness, consistency, key, null, type, domain, and cross-field checks.
---

# Quality (Structural Data Conformance)

Use this skill for structural data quality rule generation (schema compliance, field validation). Do not use for cross-process verification or business logic validation—use `reconciliation` for that.

## Load Order

1. Read this file.
2. Read [quality-rules.md](./references/quality-rules.md).
3. Read [metadata-sources.md](./references/metadata-sources.md).
4. Read [official-sources.md](./references/official-sources.md).
5. Read [adt-handoff-rules.md](./references/adt-handoff-rules.md) when output is meant for SQL Console or ADT paste.

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
