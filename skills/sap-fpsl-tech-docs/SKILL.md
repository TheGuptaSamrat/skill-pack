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

## Workflow

1. Inventory the available metadata.
2. Separate confirmed metadata from inferred relationships.
3. Build documentation that helps later generation, review, and validation.
4. Prefer concise, structured, reusable technical artifacts.

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

## Expected Output

- metadata inventory
- technical interpretation
- source-to-target mapping notes
- code-generation guidance
- validation references
