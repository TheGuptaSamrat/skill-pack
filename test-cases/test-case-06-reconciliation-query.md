# Test Case 06: Reconciliation Query Generation

Skill:

- `sap-fpsl-amdp`

Scenario:

- generate SQL checks to validate data presence, key integrity, and totals across an FSDM-to-FPSL flow

Use this metadata:

- `metadata-drop/ddic/tables.sample.csv`
- `metadata-drop/ddic/fields.sample.csv`
- `metadata-drop/samples/fsdm_to_fpsl_mapping.md`

Expected evaluation points:

- DDIC-aware query structure
- checks counts, keys, and totals
- no invented fields
- labels unresolved placeholders if metadata is incomplete
