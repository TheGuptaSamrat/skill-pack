# Integration Testing

Use this reference when the task needs test strategy for orchestration.

## Test Types

- happy-path full load
- happy-path delta load
- restart after extract success but load failure
- retry after transient connectivity failure
- quarantine of bad source records
- idempotent rerun of the same batch

## What to Verify

- control marker progression
- no duplicate loads after restart
- bad records are isolated, not silently dropped
- counts are preserved across extract, stage, and load
- technical status reflects the real checkpoint reached

## Useful Test Output

- scenario definition
- trigger and expected checkpoint behavior
- counts before and after rerun
- explicit failure and recovery notes

## Companion Skills

- route synthetic datasets to `test-data`
- route implementation code to `abap` or `amdp`
- route mapping-specific assertions to `mapping`
