# Docs Context

This folder stores markdown-derived document corpora used as AI context.

Document classes:

- `official-source-derived`
  - crisp, trusted markdown distilled from official SAP or SAP Fioneer sources
- `training-derived-concepts`
  - compact conceptual notes derived from training material

Public-repo rule:

- keep only short, paraphrased summaries in this folder
- do not commit raw or section-split source conversions of PDFs into the public repo

Default loading order:

1. `official/`
2. `metadata-drop/normalized/`
3. `training/`

Lifecycle rules:

- newer source versions do not automatically replace curated context
- curated files remain active until an updated source has been reviewed and promoted
- source versions must be tracked in `indexes/ingestion-manifest.csv`
- superseded source versions may be retained in a private/internal repo for traceability
