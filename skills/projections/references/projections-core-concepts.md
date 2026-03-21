# Projections Core Concepts

Foundation concepts for storage and volume estimation:

## Sizing Assumptions

- **Row length**: Estimated from DDIC field definitions
- **Growth rate**: Historical trend or business forecast
- **Retention period**: How many years/months retained?
- **Replication factor**: Multi-tenant or single-tenant?

## Storage Calculation Formula

```
Estimated Size (GB) = (Num Records × Avg Row Size) / 1,000,000,000
Annual Growth (GB) = Est Size × Growth Rate %
DB Size (Year-end) = Current Size + (Annual Growth × Num Years)
```

## Projection Methods

1. Linear extrapolation (assume constant growth)
2. Seasonal adjustment (peak months differ)
3. Trend analysis (growth accelerates/decelerates)
4. Capacity planning (when do we hit limits?)
