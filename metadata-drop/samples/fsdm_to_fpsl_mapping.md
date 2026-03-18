# Sample FSDM To FPSL Mapping

Classification: `synthetic-example`

This file is a safe illustrative mapping shape. It is not copied from SAP documentation and must not be treated as official product mapping.

Source example:

- structure: `/BA1/F1_CON_FLAT`
- grain: contract + cashflow date

Target example:

- posting-ready FPSL input
- grain: ledger + company code + contract + posting date

Mapping concerns:

- amount sign logic
- posting date derivation
- ledger assignment
- duplicate prevention
- reconciliation totals
