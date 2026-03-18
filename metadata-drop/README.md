# Metadata Drop

Use this area for structured inputs that improve generation quality.

Evidence classes:

- `reference-derived`
  - based on public SAP-style object names, technical notes, or repository-confirmed metadata
- `synthetic-example`
  - invented only for safe illustration, testing, or shape guidance

Principles:

- keep inputs reusable and non-confidential
- prefer CSV, markdown, or plain-text extracts
- separate confirmed metadata from interpretation
- update only the relevant folder for each new evidence type
- label synthetic content clearly so it is not mistaken for official SAP-delivered content

Suggested folders:

- `ddic/`
- `cds/`
- `fpsl/`
- `fsdm/`
- `configuration/`
- `samples/`
