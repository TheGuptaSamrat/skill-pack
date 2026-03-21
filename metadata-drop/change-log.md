# Change Review

Use this file to summarize whether a new source metadata drop changes active behavior.

## Status Values

- `no-impact`
- `minor-review`
- `reverify-required`

## Current State

- active metadata set:
  - safe sample baseline only
- current status:
  - `minor-review`
- reason:
  - repository currently contains illustrative metadata and awaits real normalized FPSL/FSDM drops

## Review Rules

Mark `reverify-required` when any of these change:

- key fields
- table names used by active mappings
- CDS entity names or projected fields
- data types, domains, or conversion-sensitive fields
- source-to-target grain
- configuration navigation or validation sequence tied to active artifacts

## Developer Rule

If `reverify-required` is active, generated code, mappings, and technical docs that depend on the changed metadata must be rechecked before reuse.
