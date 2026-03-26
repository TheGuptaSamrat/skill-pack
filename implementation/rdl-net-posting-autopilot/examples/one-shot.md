# One-Shot Netting Example

Use this when output shape matters and one representative example is enough.

## Scenario

Net posting for one posting date, one node, and one account system across multiple eligible contracts after applying the requirement-specific HKAPA and HKAPD filters.

## Input shape

Multiple `/BA1/HFSPD` rows share:

- the same posting date
- the same node number
- the same account system

The rows belong to multiple contracts inside the same netting group.

Only the rows whose related HKAPA and HKAPD records satisfy the approved filters are eligible.

## Transformation rule

- keep the latest valid related HKAPA and HKAPD record by key date
- compute net at the netting-group level without contract ID in the aggregation key
- allocate only across contracts whose sign matches the sign of the net
- emit one result row per eligible contract
- keep one anchor document strategy per contract result for traceability

## Expected output shape

One netted output row containing:

- posting date
- legal entity
- contract ID
- node number
- account system
- anchor document number and item
- original functional currency amount from the anchor row
- allocated netting delta in group currency
