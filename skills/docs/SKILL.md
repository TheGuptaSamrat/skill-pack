---
name: docs
description: "Use for technical documentation and code-generation context in FPSL/FSDM work, including design notes, implementation specs, handoff artifacts, and metadata-driven interpretation of DDIC, CDS, interfaces, and existing code when the goal is accurate, structured, evidence-backed documentation rather than speculative object creation."
---

# Docs

Use this skill when the user needs high-quality technical documentation or metadata-driven context building for code generation.

See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md) for clarification on when to use this skill vs. others.

## Load Order

1. Read this file.
2. Read [metadata-sources.md](./references/metadata-sources.md).
3. Read [documentation-core-rules.md](./references/documentation-core-rules.md).
4. Read [mapping-spec-rules.md](./references/mapping-spec-rules.md) when the task is mapping-driven.
5. Read [fpsl-architecture-overview.md](./references/fpsl-architecture-overview.md) for FPSL product architecture, Universal Journal, and multi-GAAP data model framing.
6. Read [fpsl-deployment-architecture.md](./references/fpsl-deployment-architecture.md) for FPSL system architecture, deployment options, and landscape planning.
7. Read [official-sources.md](../../docs-context/shared/official-sources-router.md) when you need official FPSL, FSDM, or data-model anchors.
8. Read `../../metadata-drop/normalized/` first when active normalized metadata exists.
9. Read `../../metadata-drop/` only for the specific input type provided by the user.

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
4. If metadata changes are marked in `change-log.md`, tell the user whether reverification is needed.
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
