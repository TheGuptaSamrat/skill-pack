# Test Case 17: Integration Boundary Check

Skill:

- `integration`

Scenario:

- generate an integration design note for an FSDM-to-FPSL daily delta load where the user is unsure whether they need orchestration guidance, mapping guidance, or reconciliation checks

Use this metadata:

- `metadata-drop/samples/fsdm-fpsl-delta-load-scenario.md`
- `metadata-drop/samples/integration-restart-recovery-scenario.md`
- `docs-context/official/sap/fsdm-fpsl-integration.md`
- `docs-context/official/sap/fpsl-fsdm-2023-golden-source.md`

Expected evaluation points:

- keeps the main answer in `integration`
- explicitly routes field-level mapping follow-up to `mapping`
- explicitly routes posted-result balancing follow-up to `reconciliation`
- keeps runtime objects as placeholders when not confirmed
- includes restart and checkpoint guidance instead of drifting into field-spec detail
