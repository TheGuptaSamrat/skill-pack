---
name: mapping
description: Generate source-to-target mapping specifications for FSDM, FPSL, and adjacent source-system flows using DDIC, CDS, and metadata evidence.
---

# Mapping

Use this skill for mapping-spec work rather than general technical documentation.

See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md) for clarification on when to use this skill vs. others.

## Load Order

1. Read this file.
2. Read [mapping-core-rules.md](./references/mapping-core-rules.md) for foundational guardrails on evidence, section discipline, artifact clarity.
3. Read [mapping-core-patterns.md](./references/mapping-core-patterns.md) for 6 real-world mapping patterns (direct, derived, multi-join, conditional, lookup, aggregation) with examples.
4. Read [metadata-sources.md](./references/metadata-sources.md) for evidence hierarchy and metadata artifact types.
5. Read [mapping-edge-cases.md](./references/mapping-edge-cases.md) for complex scenarios (nullable fields, duplicate keys, type incompatibility, cardinality mismatches, temporal changes).
6. Read [adt-handoff-rules.md](./references/adt-handoff-rules.md) when output is mapping specs ready for implementation handoff.
7. Read [official-sources.md](./references/official-sources.md) when cross-system mapping requires standard SAP terminology.

## Trust Order

1. Official SAP documentation for product scope and terminology
2. Active normalized metadata for actual structures and fields
3. Trusted raw metadata when normalization is missing
4. Synthetic examples only for shape

## Workflow

1. Inventory source and target evidence.
2. Build confirmed mappings first.
3. Separate inferred mappings and unresolved gaps.
4. Include handoff notes for implementation and validation.

## Non-Negotiables

- Do not fabricate fields, joins, or mapping logic.
- Keep confirmed, inferred, and unresolved sections explicit.
- State what evidence is still required.

## Expected Output

- metadata inventory
- confirmed mappings
- inferred mappings
- unresolved gaps
- implementation and validation notes
