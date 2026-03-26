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
- GL and GR posting blocks shown in the sample workbook are excluded from the netting source set

## Netting model

- netting group excludes contract ID
- minimum confirmed netting-group dimensions from current evidence:
  - `/BA1/C55POSTD`
  - `/BA1/C11NODENO`
  - `/BA1/C55ACCSY`
- contract ID is part of the result row, not the aggregation key for net calculation
- additional business grouping dimensions visible in the workbook, such as legal entity and profit center, should be preserved when confirmed in the target landscape

## Allocation rule

- compute net at the netting-group level using `/BA1/K5SAMGRP`
- if net > 0, allocate only across positive-contract balances
- if net < 0, allocate only across negative-contract balances
- if net = 0, emit no allocation rows unless the business confirms a zero-output convention
- preserve source precision unless a later posting constraint explicitly requires rounding
