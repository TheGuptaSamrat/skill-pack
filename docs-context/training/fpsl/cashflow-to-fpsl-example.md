Classification: training-derived-concepts
Source basis: older repo worked example
Trust usage: ABAP and AMDP split for FSDM cashflow to FPSL design
Do not use for: exact DDIC names or customizing-derived component logic
Topics covered: design split, aggregation grain, validation checks

# Cashflow To FPSL Example

Use this as a shape reference when transforming FSDM cashflow rows into FPSL posting input.

## Suggested Split

- ABAP handles validation, orchestration, and output normalization
- AMDP handles set-based aggregation and transformation
- tests cover empty input, invalid input, and grouped totals

## Validation Focus

- grouped totals by contract and posting date
- posting component derivation
- empty-input behavior
- expected exception path for invalid input
