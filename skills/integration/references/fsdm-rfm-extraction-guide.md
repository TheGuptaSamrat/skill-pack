# FSDM RFM Extraction Guide

Use this reference when the user asks how extraction is triggered or sequenced.

## Extraction Framing

- Treat RFMs as extraction interfaces, not as business logic containers.
- Keep destination, selection criteria, and control markers explicit.
- Prefer delta extraction when change pointers are confirmed and reliable.

## Typical Sequence

1. Read last successful control timestamp or batch marker.
2. Resolve eligible source objects.
3. Call the confirmed extraction interface.
4. Capture result code, count, and extract identifier.
5. Stage the payload before target load.

## Control Inputs to Clarify

- source object type: contracts, instruments, transactions, cashflows, events
- full versus delta load
- change-pointer basis or alternate selection logic
- restart marker and batch identity
- destination or logical source system name

## Common Failure Modes

- missing or stale change pointers
- RFC destination or transport failure
- timestamp drift between systems
- duplicate extraction after unsafe restart
- payload accepted by extract but rejected in staging

## Delivery Rule

When the exact RFM name is not confirmed from repo evidence or official SAP references, keep it as a placeholder and describe the sequence rather than inventing an interface name.
