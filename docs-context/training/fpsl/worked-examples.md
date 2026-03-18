Classification: training-derived-concepts
Source basis: older repo worked examples
Trust usage: compact scenario framing for reconciliation and FSDM-to-FPSL design
Do not use for: exact object names, keys, or totals
Topics covered: checkpoint order, likely failure points, ABAP-AMDP split, validation focus

# Worked Examples

## Reconciliation Example

Use this when source totals match expectation but FPSL posting totals are lower.

Checkpoint order: source baseline, transformation checkpoint, enrichment checkpoint, posting-input checkpoint, then exception and filter checkpoint.

Likely failure points: wrong composite key used for deduplication, inner join removes rows without matching reference data, aggregation happens at the wrong grain, sign reversal is applied twice, or wrapper validation drops technically incomplete but business-valid rows.

## Cashflow To FPSL Example

Use this as a shape reference when transforming FSDM cashflow rows into FPSL posting input.

Suggested split: ABAP handles validation, orchestration, and output normalization; AMDP handles set-based aggregation and transformation; tests cover empty input, invalid input, and grouped totals.

Validation focus: grouped totals by contract and posting date, posting component derivation, empty-input behavior, and the expected exception path for invalid input.
