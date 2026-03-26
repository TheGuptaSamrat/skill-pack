# Zero-Shot Netting Prompt Context

Use this when the repo already has enough metadata evidence and you only need the task delta.

## Scenario

Build or review the RDL net-posting implementation using approved RDL table evidence and the requirement-specific netting logic in this pack.

## Confirmed evidence used

- `/BA1/HFSPD`
- `/BA1/HKAPA`
- `/BA1/HKAPD`
- approved field exports under `metadata-drop/ddic/current/`

## Transformation intent

- identify eligible HFSPD rows
- resolve latest valid HKAPA and HKAPD relationships
- aggregate at the approved netting grain
- write one netted output row per eligible group

## Expected output shape

- one output row per approved netting group
- aggregated functional and group currency amounts
- retained anchor document values for traceability

## Validation checks

- counts and sums reconcile with validation SQL
- filters are applied exactly once
- latest-valid-date logic is preserved
