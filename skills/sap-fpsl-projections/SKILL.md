---
name: sap-fpsl-projections
description: Estimate SAP FPSL and FSDM 2023 transaction volume, storage growth, and DB-size trends from monthly input assumptions. Use for year-long or forward-looking volume projections, storage planning, sensitivity notes, and simple trend-line estimation. Do not use for implementation or operational SAP changes.
---

# SAP FPSL Projections

Use this skill for planning and estimation work around FPSL and FSDM data growth.

## Load Order

1. Read this file.
2. Read [projection-rules.md](./references/projection-rules.md).
3. Read [sizing-assumptions.md](./references/sizing-assumptions.md) when translating business inputs into storage or trend outputs.
4. Read [official-sources.md](./references/official-sources.md) when official product framing is needed.
5. Read [projection-context-routes.md](./references/projection-context-routes.md) when you need the exact curated concept and metadata sources to load.

## Trust Order

1. Official SAP documentation for product and deployment framing
2. Active normalized metadata and provided sizing inputs
3. Trusted raw metadata if normalized inputs are missing
4. Curated concept notes for sizing logic
5. Synthetic examples only for shape

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
