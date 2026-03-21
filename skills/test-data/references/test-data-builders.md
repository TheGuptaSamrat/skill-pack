# Test Data Builders

Fixture builder patterns for synthetic scenario data:

## Pattern 1: Direct Insert Builder
```sql
INSERT INTO /BA1/HFPPD (PORTFOLIO_ID, SECURITY_ID, VALUE_DATE, AMOUNT)
SELECT
  'TEST_' || LPAD(ROW_NUMBER() OVER(), 3, '0') as PORTFOLIO_ID,
  'SECURITY_' || LPAD(ROW_NUMBER() OVER(), 5, '0') as SECURITY_ID,
  CURRENT_DATE as VALUE_DATE,
  1000 + (ROWNUM * 100) as AMOUNT
FROM (SELECT 1 FROM DUAL CONNECT BY LEVEL <= 100);
```

## Pattern 2: Parametrized Dataset
```
Parameters:
- @NUM_PORTFOLIOS: 10
- @NUM_SECURITIES: 500
- @BASE_AMOUNT: 1000
- @VOLATILITY: 0.1 (±10% variance)

Output: Deterministic fixture data
```

## Pattern 3: Scenario-Based Setup
- Happy Path: All valid values, no edge cases
- Boundary Cases: Min/max values, null fields, domain limits
- Error Cases: Invalid FK refs, type errors, business rule violations
