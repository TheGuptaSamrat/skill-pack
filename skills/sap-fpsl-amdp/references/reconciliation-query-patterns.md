# Reconciliation Query Patterns

- Prefer queries that check:
  - record counts
  - key uniqueness
  - amount totals
  - source-to-target grain
  - missing data along the flow
- If the user asks whether a process has run successfully, include:
  - data presence checks
  - log-oriented checks where available
  - comparison totals
