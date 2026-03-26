# Netting Join Logic

This file is requirement-specific. It captures the join and filtering logic used for the RDL net-posting solution and should not be treated as generic FPSL shared metadata.

## Confirmed tables

- Driver table: `/BA1/HFSPD`
- Join table 1: `/BA1/HKAPA`
- Join table 2: `/BA1/HKAPD`

## Confirmed filters

- `/BA1/HKAPA-/BA1/CR4PFCT = '2100'`
- `/BA1/HKAPD-/BA1/C55ACCRCT = '601'`
- latest valid `/BA1/CR0KEYDAT <= /BA1/C55POSTD`
- `CURRENT_FLAG = 'X'`

## Grouping grain

- `/BA1/C55CONTID`
- `/BA1/C11NODENO`
- `/BA1/C55ACCSY`
- `/BA1/C55POSTD`

## Aggregates

- `SUM(/BA1/K5SAMBAL)`
- `SUM(/BA1/K5SAMGRP)`
