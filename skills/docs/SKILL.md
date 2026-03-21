---
name: docs
description: Generate technical documentation and code-generation context from FPSL/FSDM metadata. Use for design notes, technical specs, handoff docs, and metadata-driven interpretation of DDIC, CDS, interfaces, and existing code.
---

# Docs

Use this skill when the user needs high-quality technical documentation or metadata-driven context building for code generation.

## Load Order

1. Read this file.
2. Read [metadata-sources.md](./references/metadata-sources.md).
3. Read [documentation-core-rules.md](./references/documentation-core-rules.md).
4. Read [mapping-spec-rules.md](./references/mapping-spec-rules.md) when the task is mapping-driven.
5. Read [official-sources.md](./references/official-sources.md) when you need official FPSL, FSDM, or data-model anchors.
6. Read `../../metadata-drop/normalized/` first when active normalized metadata exists.
7. Read `../../metadata-drop/` only for the specific input type provided by the user.

## Trust Order

1. Official SAP documentation for product scope, standard data-model framing, and supported terminology
2. Active normalized repository metadata for actual structures and mappings
3. Trusted raw metadata when normalization is missing or under comparison
4. Training-derived conceptual guidance for architecture and process framing
5. Synthetic examples only for shape

Do not derive landscape-specific names, joins, or mappings from public SAP documentation alone.

## Workflow

1. Inventory the available metadata.
2. Prefer active normalized metadata as the default working source.
3. Use trusted raw Excel only when normalization is missing or when comparing changes.
4. If metadata changes are marked in `change-review.md`, tell the user whether reverification is needed.
5. Build mapping specifications when the task is source-to-target design.
6. Separate confirmed metadata from inferred relationships.
7. Build documentation that helps later generation, review, and validation.
8. Prefer concise, structured, reusable technical artifacts.

## Accepted Inputs

- FPSL metadata
- FSDM 2023 metadata
- CDS definitions
- DDIC extracts
- interface layouts
- existing ABAP, AMDP, and SQL artifacts
- profiling or reconciliation outputs

## Non-Negotiables

- Do not fabricate field lists, joins, object names, or mappings.
- Label inferred relationships explicitly.
- Keep docs generation-oriented, not presentation-heavy.
- Produce output that can be reused for later code generation.
- Prefer metadata-drop evidence over free-form assumptions whenever both exist.
- If normalized metadata is marked `reverify-required`, tell the user impacted code or docs must be revalidated.
- When using public SAP help as a source, label clearly what is official framing versus what comes from landscape metadata.

## Expected Output

- metadata inventory
- technical interpretation
- source-to-target mapping notes
- code-generation guidance
- validation references
- confirmed, inferred, and unresolved mapping sections when mapping specs are requested
