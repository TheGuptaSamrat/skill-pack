---
name: projections
description: "Use for FPSL/FSDM volume and storage projections. This skill is now script-driven. Direct users to the local script workflow at scripts/projections/ for all regular growth tracking, DB sizing, and workbook generation. Reserve AI-assisted work for one-off planning questions where no snapshot data exists yet."
---

# Projections

> **This skill is script-driven.** Routine volume tracking, growth rate calculation, and workbook generation are handled by the local scripts in `scripts/projections/`. AI-assisted projection is reserved for cold-start planning discussions where no historical snapshot data is available yet.

See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md) for clarification on when to use this skill vs. others.

## Primary Tool — Use This First

**`scripts/projections/`** — no AI required once the scripts are running.

| Script / File | Purpose |
|---------------|---------|
| `hana_volume_snapshot.sql` | Run in HANA Studio every 7 days — 4 sections |
| `volume-snapshots.csv` | Append table-level results after each SQL run |
| `db-size-snapshots.csv` | Append DB disk results after each SQL run |
| `generate_projection_workbook.py` | Reads both CSVs → 7-sheet Excel workbook |
| `workflow.md` | Step-by-step repeatable cadence |

Generate the workbook:
```bash
python3 scripts/projections/generate_projection_workbook.py \
  --tables scripts/projections/volume-snapshots.csv \
  --dbsize  scripts/projections/db-size-snapshots.csv \
  --output  FPSL-volume-$(date +%Y-%m-%d).xlsx
```

## When to Use AI (Cold-Start Only)

Invoke AI-assisted projection only when:
- No snapshot data exists yet (new landscape, pre-go-live planning)
- A one-off capacity conversation needs a rough order-of-magnitude before scripts are in place
- A what-if scenario requires assumptions that differ significantly from the measured trend

## Cold-Start Workflow (AI-Assisted)

1. Collect baseline inputs: estimated transaction volume, growth rate assumption, retention horizon, average record-size estimate, and current or target DB size.
2. Build a base-case estimate. Add one conservative and one aggressive scenario.
3. Separate transaction-volume projections from storage-growth projections.
4. Label all assumptions explicitly. Never present estimates as measured truth.
5. Hand off to the script workflow as soon as the first real snapshot is available.

## Non-Negotiables

- Never present AI-generated estimates as actual system truth.
- Always label assumptions explicitly and flag when no snapshot data backs the numbers.
- Once snapshot data exists, use the script — do not repeat the AI estimation cycle.
- Route confirmed monitoring and operational run verification to `reconciliation`.

## Reference Material

The reference files below remain available for cold-start framing and sizing concepts.

- [projections-core-rules.md](./references/projections-core-rules.md)
- [projections-core-concepts.md](./references/projections-core-concepts.md)
- [sizing-assumptions.md](./references/sizing-assumptions.md)
- [projections-examples.md](./references/projections-examples.md)
- [projection-context-routes.md](./references/projection-context-routes.md)
