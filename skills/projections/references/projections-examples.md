# Projections Examples

Real-world sizing examples for FPSL/FSDM tables:

## Example 1: HFPPD Projection

Table: /BA1/HFPPD (positions detail)
- Current rows: 5M, Avg row size: 150 bytes
- Growth: +20% YoY
- Projection period: 3 years

| Year | Estimated Rows | Est Size (GB) | Cumulative |
|------|---|---|---|
| Now | 5M | 0.75GB | 0.75GB |
| +1yr | 6M | 0.90GB | 1.65GB |
| +2yr | 7.2M | 1.08GB | 2.73GB |
| +3yr | 8.64M | 1.30GB | 4.03GB |

Partition Strategy: Monthly partitions, rolling window (keep 3 years, archive older)

## Example 2: Intra-Daily Growth

System: Trading platform (intra-day updates)
- Daily writes: 2M records
- Intra-day updates: 50M writes to 3M records
- Peak usage: 8am-4pm UTC

Key considerations:
- Compression ratio: 4:1 (historical data much more compressible)
- Hot vs cold storage: Keep 60 days hot, archive older
- Indexing strategy: PRIMARY on (TRADE_DATE, SECURITY_ID)
