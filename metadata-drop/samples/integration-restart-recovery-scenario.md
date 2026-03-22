# Integration Restart and Recovery Scenario

**Classification:** synthetic-example

Use this sample when the task is specifically about restartability, technical control points, and failure isolation.

## Scenario

An FSDM-to-FPSL extraction run processes securities positions and cashflow-related events. The extract step completes, staging succeeds for most records, but the target-load step fails midway because of a transient destination or application-layer issue.

## Expected design questions
- what checkpoint proves extract completion
- what checkpoint proves stage completion
- which records can be retried safely
- how to prevent duplicate loads after restart
- how to separate retryable technical failures from record-level data defects

## Expected control outputs
- extract count
- staged accepted count
- staged rejected count
- loaded count before failure
- restart marker or batch status
- quarantine handling for data defects

## Boundary reminder
- if the user asks how a field is transformed, route that follow-up to `mapping`
- if the user asks whether final totals balance after posting, route that follow-up to `reconciliation`
- if the user asks for implementation code, route that follow-up to `abap` or `amdp`
