Classification: training-derived-concepts
Source basis: older repo worked example
Trust usage: reconciliation checkpoint framing and defect isolation
Do not use for: exact object names, keys, or totals
Topics covered: checkpoint order, likely failure points, validation sequence

# Reconciliation Example

Use this as a compact walkthrough when source totals match expectation but FPSL posting totals are lower.

## Checkpoint Order

1. source baseline
2. transformation checkpoint
3. enrichment checkpoint
4. posting-input checkpoint
5. exception and filter checkpoint

## Likely Failure Points

- wrong composite key used for deduplication
- inner join removes rows without matching reference data
- aggregation happens at the wrong grain
- sign reversal is applied twice
- wrapper validation drops technically incomplete but business-valid rows
