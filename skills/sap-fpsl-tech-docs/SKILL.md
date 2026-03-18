---
name: sap-fpsl-tech-docs
description: Generate and maintain technical documentation for SAP FPSL and FSDM development using metadata evidence such as DDIC extracts, CDS definitions, FPSL structures, FSDM 2023 model details, interfaces, and existing code artifacts. Use for design notes, technical specs, mapping docs, handoff docs, and metadata-driven context for high-quality code generation.
---

# SAP FPSL Tech Docs

Use this skill when the user needs high-quality technical documentation or metadata-driven context building for code generation.

## Load Order

1. Read this file.
2. Read [metadata-sources.md](./references/metadata-sources.md).
3. Read [documentation-output-rules.md](./references/documentation-output-rules.md).
4. Read `../../metadata-drop/normalized/` first when active normalized metadata exists.
5. Read `../../metadata-drop/` only for the specific input type provided by the user.

## Workflow

1. Inventory the available metadata.
2. Prefer active normalized metadata as the default working source.
3. Use trusted raw Excel only when normalization is missing or when comparing changes.
4. If metadata changes are marked in `change-review.md`, tell the user whether reverification is needed.
5. Separate confirmed metadata from inferred relationships.
6. Build documentation that helps later generation, review, and validation.
7. Prefer concise, structured, reusable technical artifacts.

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

## Expected Output

- metadata inventory
- technical interpretation
- source-to-target mapping notes
- code-generation guidance
- validation references
