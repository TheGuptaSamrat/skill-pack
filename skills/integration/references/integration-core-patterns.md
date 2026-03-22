# Integration Core Patterns

Use these patterns when shaping FSDM-to-FPSL movement and control flows.

## Pattern 1: Delta Extraction with Change Pointers

1. Read last successful load marker.
2. Identify changed source objects after that marker.
3. Extract only eligible objects.
4. Validate extracted count before staging.
5. Persist new marker only after successful downstream completion.

## Pattern 2: Extract -> Stage -> Validate -> Load

1. Extract from source using confirmed interfaces.
2. Land data in a staging checkpoint.
3. Run technical completeness checks.
4. Load into target consumption layer.
5. Record status, counts, and restart marker.

## Pattern 3: Restartable Batch Design

- keep batch identifiers explicit
- persist per-step status
- separate retryable failures from data defects
- restart from the last durable checkpoint, not from the beginning unless integrity requires it

## Pattern 4: Technical Validation Controls

- source count captured
- extracted count captured
- staged count captured
- rejected count captured
- loaded count captured
- status transition logged

## Pattern 5: Failure Isolation

- connectivity failures: retry transport or destination layer
- extract logic failures: isolate the failing object cohort
- staging rule failures: quarantine bad records
- load failures: preserve staged data and retry idempotently
