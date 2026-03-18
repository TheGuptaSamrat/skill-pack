# Update Policy

Use this policy when a newer SAP or SAP Fioneer document is received.

## Core Rule

Newer source PDFs do not automatically change the active curated context.

They must first be:

1. reviewed outside the public repo if raw source conversion is needed
2. reviewed against current curated files
3. promoted into `official/` or `training/` only after review

## Status Model

Use these values in `ingestion-manifest.csv`:

- `active`
  - current preferred source for curated context
- `superseded`
  - older source retained for traceability
- `candidate`
  - newly ingested source awaiting review

Use these review states:

- `reviewed`
- `pending-review`
- `promoted`
- `rejected`

## Promotion Rule

A new source version becomes active only when:

- the relevant curated markdown has been updated if needed
- `topic-map.md` still points to the preferred files
- the prior source is marked `superseded` if replaced

## Tech Head Review Lens

Review these questions before promoting a new source version:

- does this change product scope or terminology?
- does this change operational setup guidance?
- does this change integration framing?
- does this invalidate older curated notes?
- do any skill-routing files need updating?
