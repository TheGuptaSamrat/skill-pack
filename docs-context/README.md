# Docs Context

This folder stores markdown-derived document corpora used as AI context.

Document classes:

- `official-source-derived`
  - crisp, trusted markdown distilled from official SAP or SAP Fioneer sources
- `training-derived-concepts`
  - compact conceptual notes derived from training material
- `full-source-md`
  - section-split markdown converted from PDFs for retrieval and deeper lookup

Default loading order:

1. `official/`
2. `metadata-drop/normalized/`
3. `training/`
4. `full-source-md/`

Do not load `full-source-md/` by default unless deeper lookup is needed.

Lifecycle rules:

- newer source versions do not automatically replace curated context
- curated files remain active until an updated source has been reviewed and promoted
- source versions must be tracked in `indexes/ingestion-manifest.csv`
- superseded source versions should remain available for traceability
