# Change Review

Use this file to summarize whether a new source metadata drop changes active behavior.

## Status Values

- `no-impact`
- `minor-review`
- `reverify-required`

## Current State

- active metadata set:
  - safe sample baseline + FPSL RDL table extractions (2026-03-24)
- current status:
  - `no-impact`
- reason:
  - FPSL RDL tables extracted from live HANA DDIC (photographed IMG_1791–1803); FIELDNAME and DDTEXT confirmed from live system; DATATYPE/LENG/DOMNAME are convention-inferred and accepted as working state — type verification bypassed by decision on 2026-03-24

## 2026-03-24 — FPSL RDL Image Extraction

- **Source**: Live HANA DDIC export photographed from Excel (IMG_1791–IMG_1802) + join diagram email (IMG_1803)
- **Provenance**: Confirmed live system — field names (FIELDNAME) and descriptions (DDTEXT) are authoritative
- **Tables added**:
  - `/BA1/HFSPD` — Subledger Document — 230 fields
  - `/BA1/HKAPA` — Accounting Portfolio Assignment — 46 fields
  - `/BA1/HKAPD` — Accounting Portfolio Definition — 53 fields
- **Confirmed from live system**: TABNAME, FIELDNAME, DDTEXT (field descriptions), table cardinality
- **Status**: `no-impact` — accepted as working state; type verification bypassed by decision on 2026-03-24
- **Next action**: use these CSVs directly in skill prompts, AMDP generation, and quality checks
- **Requirement-specific note**: the photographed netting join logic is tracked in the netting implementation pack, not in shared metadata

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
