# FSDM to FPSL Delta Load Scenario

**Classification:** synthetic-example

Use this sample when the task is about integration orchestration rather than field mapping.

## Scenario

A daily batch loads changed retail-loan contracts from FSDM into an FPSL consumption flow.

### Source-side assumptions
- source domain: financial contracts
- source change detection: change pointer or last-modified timestamp
- source cadence: daily
- source extraction granularity: contract header plus related business transactions

### Technical control assumptions
- batch identifier exists for each extraction run
- last successful delta marker is persisted after successful downstream completion
- rejected records are quarantined instead of silently skipped
- restart should resume from the last durable checkpoint, not reload everything by default

## Desired orchestration output

The integration design note should cover:
- source -> stage -> validate -> load sequence
- where delta marker is read and updated
- what counts are captured at extract, stage, reject, and load checkpoints
- what happens if extraction succeeds but load fails
- what follow-up should route to mapping, reconciliation, abap, or amdp

## Do Not Assume
- concrete RFC destination names
- customer-specific scheduler jobs
- customer-specific staging table names
- final FPSL posting reconciliation rules
