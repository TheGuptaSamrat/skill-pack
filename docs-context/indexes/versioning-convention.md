# Versioning Convention

Use source identifiers that are stable and comparable.

## Source ID Format

Recommended pattern:

`<topic>-<document-family>-<version>`

Examples:

- `official-source-01-2306-sp04`
- `fpsl-admin-guide-2025-q4`
- `fsdm-fpsl-integration-2026-01`
- `hana-sql-training-week3-2020`

## Curated Files

Curated files in `official/` and `training/` should remain topic-based, not version-based.

Example:

- keep `fpsl-client-setup.md`
- update its provenance header when a newer source replaces the older one

This keeps skill references stable while allowing source versions to evolve.

If raw source conversions are required for review, keep them in a private/internal repo and do not publish them here.
