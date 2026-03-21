# Scenario-Based Test Data

Testing scenarios for functional test preparation:

## Scenario 1: Happy Path
- All fields valid and populated
- Business rules satisfied
- FK references exist
- Expected outcome: Process succeeds, no errors

## Scenario 2: Boundary Cases
- Minimum/maximum values
- Exactly NULL vs NOT NULL variations
- Domain boundaries (e.g., first/last valid codes)
- Expected outcome: Process handles edge cases gracefully

## Scenario 3: Error Cases
- Invalid FK references (orphaned records)
- Type mismatches (string in numeric field)
- Business rule violations
- Expected outcome: Error handling and rejection logic works

## Scenario 4: Volume/Stress
- 100K+ records
- Large transactions
- Memory constraints
- Expected outcome: Performance acceptable (<5s)
