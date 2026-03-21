# Test Case 10: Focused Reconciliation Checks

Skill:

- `reconciliation`

Scenario:

- generate a focused SQL check pack to validate counts, keys, totals, and likely breakpoints across an FSDM-to-FPSL flow after a batch-style run

Use this metadata:

- `metadata-drop/ddic/current/tables-template.csv`
- `metadata-drop/ddic/current/fields-template.csv`
- `metadata-drop/samples/fsdm_to_fpsl_mapping.md`

Expected evaluation points:

- clear checkpoint-based query structure
- counts, keys, and totals covered
- no invented fields or tables
- unresolved placeholders labeled when metadata is incomplete
