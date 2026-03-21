# Partitioning Instructions

Use this instruction set when the task is primarily about:

- HANA partition strategy
- FPSL-relevant table partition review
- partition key reasoning
- archiving and growth implications
- SAP-aligned operational partition guidance

> **Evidence-first gate:** Before loading the skill, check whether `scripts/projections/volume-snapshots.csv` and `db-size-snapshots.csv` exist and contain data. If they do, those CSVs (and the generated workbook Growth Rates / Projection sheets) are the primary volume evidence — load them before forming any recommendation.

Load in this order:

1. `skills/partitioning/SKILL.md`
2. `scripts/projections/volume-snapshots.csv` (if available — review Growth Rates trend)
3. `skills/partitioning/references/partitioning-core-rules.md`
4. `skills/partitioning/references/partitioning-validation.md`
5. `docs-context/shared/official-sources-router.md`

Routing rule:

- Use `partitioning` for DB-side strategy and review.
- Route SQL validation to `reconciliation` and implementation changes to `amdp` or `abap`.
