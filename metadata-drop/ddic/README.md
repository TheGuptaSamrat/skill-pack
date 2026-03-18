# DDIC Inputs

Use this folder for DDIC exports that improve code generation, reconciliation checks, mapping specs, and technical documentation.

## Recommended Structure

- `current/`
  - latest approved DDIC baseline with stable filenames
- `archive/`
  - older DDIC baselines kept for comparison
- `sql/`
  - extraction SQL for Eclipse SQL Console or HANA Database Explorer
- `refresh-log.csv`
  - refresh history
- `table-priority-list.md`
  - first-pass FPSL extraction targets

## Stable Files

Keep these file names stable in `current/`:

- `tables.csv`
- `fields.csv`
- `keys.csv`
- `data-elements.csv`
- `domains.csv`
- `manifest.csv`

Use these to confirm:

- exact table names
- field layouts
- primary keys
- data elements and domains

Template headers are included in `current/`.

Use the sample CSVs in this folder only as a seed until real DDIC exports are available.
