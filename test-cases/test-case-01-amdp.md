# Test Case 01: AMDP Transformation

Skill:

- `amdp`

Scenario:

- design the smallest ABAP wrapper and AMDP method for transforming FSDM cashflow-style rows into FPSL posting input

Use this metadata:

- `metadata-drop/ddic/current/tables-template.csv`
- `metadata-drop/ddic/current/fields-template.csv`
- `metadata-drop/samples/cashflow_rows.sample.csv`
- `metadata-drop/samples/fsdm_to_fpsl_mapping.md`

Expected evaluation points:

- clear ABAP vs AMDP split
- no invented SAP object names
- test scaffold included
- validation and reconciliation checks included
