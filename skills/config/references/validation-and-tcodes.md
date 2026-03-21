# Validation And TCodes

Use only when relevant and confirmed by landscape reality.

## Core Object Checks

- `SE11` and `SE16N` for DDIC and table inspection
- `SE24` and `SE80` for class and object checks

## Runtime And Performance

- `ST05` for SQL trace
- `SAT` for runtime analysis
- `ST22` for dump analysis
- `SLG1` for application log checks

## Operations

- `SM37` for job review
- `SE09` or `SE10` for transport checks

## Validation Pattern

Validate in this order:

1. source rows and totals
2. transformation rows and totals
3. posting input rows and totals
4. downstream reconciliation result

Add manual reconciliation checks for:

- record counts
- amount totals
- sign conventions
- input versus output grain
- posting date
- currency consistency
