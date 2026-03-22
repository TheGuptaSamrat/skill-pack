# Integration Core Rules

Use this reference for scope control and evidence discipline.

## In Scope

- extraction orchestration
- change-pointer based delta flow
- RFM sequencing
- staging-layer design
- restart and retry controls
- technical validation of extraction and load checkpoints

## Out of Scope

- field-to-field mapping specs
- IMG or customizing walkthroughs
- schema-level quality rules
- posted-result reconciliation and accounting balancing
- CVPM-specific worklist or process-step design

## Boundary Rules

- If the user asks what fields map where, route to `mapping`.
- If the user asks whether totals balance after posting, route to `reconciliation`.
- If the user asks how to configure SAP customizing, route to `config`.
- If the user asks for implementation code, route to `abap` or `amdp`.

## Trust Discipline

1. Prefer official SAP/FSDM integration references first.
2. Use repo metadata or normalized extracts for actual structures.
3. Use placeholders when runtime objects are not confirmed.

## Delivery Rules

- Return the smallest useful orchestration view first.
- Keep source, stage, and target checkpoints explicit.
- Distinguish full-load advice from delta-load advice.
- State restart assumptions and failure boundaries clearly.
