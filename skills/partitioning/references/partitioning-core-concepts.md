# Partitioning Core Concepts

HANA partitioning strategy for performance and maintenance:

## Partitioning Types

1. **Range Partitioning**: By date (monthly), territory, or numeric range
   - Ideal for time-series data (/BA1/HFPPD by VALUATION_DATE)
   - Enables rolling windows (keep hot data, archive cold)

2. **Hash Partitioning**: Distribute by key for parallelism
   - Ideal for fact tables with large cardinality
   - Even distribution across nodes

3. **Round-Robin**: Simple distribution when order doesn't matter

## SAP Notes on Partitioning

- SAP Note 2722355: HANA partitioning strategies
- SAP Note 2874355: Scale-out architecture
- SAP Note 2637010: Data tiering recommendations
