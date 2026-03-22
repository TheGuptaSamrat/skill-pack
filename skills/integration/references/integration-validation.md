# Integration Validation

Use this reference for technical flow validation rather than business balancing.

## Extraction Checks

- source object count captured
- extraction count captured
- missing mandatory keys flagged
- duplicate batch/object combinations flagged
- delta marker recorded

## Staging Checks

- staged row count matches accepted extraction count
- rejected row count is explicit
- mandatory technical fields exist
- batch identifier is consistent across staged records
- restartability marker exists

## Load Checks

- loaded row count matches staged accepted count
- failed rows are isolated with reason codes
- load status transitions are durable
- restart does not duplicate already loaded records

## Minimal Validation Output

- counts at each checkpoint
- reject counts and reasons
- restart point
- unresolved placeholders for runtime tables or jobs

## Boundary Reminder

If the user asks whether accounting totals or postings balance after processing, route that follow-up to `reconciliation`.
