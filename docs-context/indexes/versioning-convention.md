# Versioning Convention

Use source identifiers that are stable and comparable.

## Source ID Format

Recommended pattern:

`<topic>-<document-family>-<version>`

Examples:

- `fpsl-admin-guide-2306-sp04`
- `fpsl-admin-guide-2025-q4`
- `fsdm-fpsl-integration-2026-01`
- `hana-sql-training-week3-2020`

## Folder Naming

For `full-source-md/`, use:

- `fpsl-admin-guide-2306-sp04`
- `fpsl-training-rev01`
- `hana-sql-week3-2020`

Avoid vague names like:

- `latest`
- `new`
- `training-derived`

## Curated Files

Curated files in `official/` and `training/` should remain topic-based, not version-based.

Example:

- keep `fpsl-client-setup.md`
- update its provenance header when a newer source replaces the older one

This keeps skill references stable while allowing source versions to evolve.
