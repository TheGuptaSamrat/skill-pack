---
name: mapping
description: Generate source-to-target mapping specifications for FSDM, FPSL, and adjacent source-system flows using DDIC, CDS, and metadata evidence.
---

# Mapping

Use this skill for mapping-spec work rather than general technical documentation.

## Load Order

1. Read this file.
2. Read [mapping-rules.md](./references/mapping-rules.md).
3. Read [metadata-sources.md](./references/metadata-sources.md).
4. Read [official-sources.md](./references/official-sources.md).

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
