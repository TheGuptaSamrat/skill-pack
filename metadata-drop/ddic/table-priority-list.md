# Table Priority List

Use this as the first extraction target if you do not want to export everything at once.

## FPSL Core

- `/BA1/HFSPD`
- `/BA1/HFPPD`
- `/BA1/HKTVR`
- `/BA1/HKTVL`
- `/BA1/F1_CON_FLAT`
- `/BA1/HKAPA`
- `/BA1/HKAPD`

## Project-Specific Additions

Add:

- custom `Z*` staging tables
- FSDM harmonization tables used in your landscape
- custom interface or mapping tables
- enrichment and rule tables

## Extraction Rule

If a table appears in production logic, validation logic, or reconciliation logic, include it in the DDIC drop.
