---
name: projections
description: "Use for FPSL/FSDM volume and storage projections, including transaction growth estimates, database sizing trends, assumption-driven scenarios, and sensitivity notes that support planning decisions, capacity conversations, and roadmap discussions when users need forward-looking projections instead of implementation-level ABAP, AMDP, or configuration output."
---

# Projections

Use this skill for planning and estimation work around FPSL and FSDM data growth.

See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md) for clarification on when to use this skill vs. others.

## Load Order

1. Read this file.
2. Read [projections-core-rules.md](./references/projections-core-rules.md).
3. Read [projections-core-concepts.md](./references/projections-core-concepts.md) for sizing assumptions, storage formulas, and projection methods.
4. Read [sizing-assumptions.md](./references/sizing-assumptions.md) when translating business inputs into storage or trend outputs.
5. Read [projections-examples.md](./references/projections-examples.md) for real-world examples (HFPPD 3-year projection, intra-daily growth patterns).
6. Read [official-sources.md](../../docs-context/shared/official-sources-router.md) when official product framing is needed.
7. Read [projection-context-routes.md](./references/projection-context-routes.md) when you need the exact curated concept and metadata sources to load.

## Trust Order

1. Official SAP documentation for product and deployment framing
2. Active normalized metadata and provided sizing inputs
3. Trusted raw metadata if normalized inputs are missing
4. Curated concept notes for sizing logic
5. Synthetic examples only for shape

## Workflow

1. Confirm baseline inputs: current volume, growth assumptions, retention horizon, and average record-size assumptions.
2. Build a base-case estimate first, then add one or two sensitivity scenarios (for example conservative and aggressive growth).
3. Separate transaction-volume projections from storage-growth projections and state where assumptions drive each result.
4. Label uncertainty clearly and avoid presenting estimates as measured production truth.
5. Return the smallest useful projection artifact first, then extend only if the user asks for additional scenarios.

## Accepted Inputs

- monthly transaction volume
- growth assumptions
- retention assumptions
- average record size assumptions
- current DB size
- separate FPSL and FSDM components if known

## Non-Negotiables

- Never present estimates as actual system truth.
- Always label assumptions explicitly.
- Separate base estimate from sensitivity notes.
- State whether sizing is transaction-count based, storage-based, or mixed.

## Expected Output

- assumptions table
- monthly and yearly trend table
- storage-growth view
- sensitivity and uncertainty notes
- clear statement that output is an estimate
