# One-Shot Netting Example

Use this when output shape matters and one representative example is enough.

## Scenario

Net posting for one posting date, one contract, one node, and one account system after applying the requirement-specific HKAPA and HKAPD filters.

## Input shape

Multiple `/BA1/HFSPD` rows share:

- the same posting date
- the same contract ID
- the same node number
- the same account system

Only the rows whose related HKAPA and HKAPD records satisfy the approved filters are eligible.

## Transformation rule

- keep the latest valid related HKAPA and HKAPD record by key date
- group eligible HFSPD rows by:
  - contract ID
  - node number
  - account system
  - posting date
- sum:
  - `/BA1/K5SAMBAL`
  - `/BA1/K5SAMGRP`
- keep one anchor document reference for traceability

## Expected output shape

One netted output row containing:

- posting date
- legal entity
- contract ID
- node number
- account system
- anchor document number and item
- summed functional currency amount
- summed group currency amount
