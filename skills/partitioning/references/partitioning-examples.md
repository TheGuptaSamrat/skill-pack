# Partitioning Strategy Examples

Real partitioning recommendations for FPSL tables:

## Example 1: HFPPD (Positions Detail) - Range Partition by Date

```
Partition Key: VALUATION_DATE (monthly)
Keep: Last 12 months in memory (hot)
Archive: Older months to warm storage
Reason: Daily revaluation queries filter on VALUATION_DATE; monthly chunks = optimal performance

Partition scheme:
- 2025-03: HFPPD_202503
- 2025-02: HFPPD_202502
- 2025-01: HFPPD_202501
- 2024-12: (archive) HFPPD_202412_archived
```

## Example 2: /BA1/HKTVR (Deal Header) - Hash Partition by PORTFOLIO_ID

```
Reason: Deal header has 5M records; PORTFOLIO_ID has high cardinality (~10K values)
Partition Count: 16 (matches HANA nodes × 2 for parallelism)
Benefit: Query joins (PORTFOLIO_ID = X) can execute on single partition partition

Query Performance:
Before: 5M scan, then filter
After: ~312K scan (5M/16), then filter
Speedup: ~16× on partition-pruning queries
```

## Example 3: SIZ Reference (Slowly Changing) - No Partition

```
Table size: 50K rows (too small to benefit from partitioning)
Recommendation: Keep in-memory, no partitioning (overhead not justified)
```
