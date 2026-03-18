# SQL And Performance Rules

- Filter early and on all known dimensions.
- Avoid broad scans when partitioning or key predicates are available.
- Document expected volume and why pushdown is needed.
- Make sort stability explicit where downstream logic depends on order.
- State null handling, type conversion, and currency rounding assumptions.
- Prefer joins over row-by-row loops for high-volume transformations.
- Use placeholders instead of invented field names when metadata is incomplete.
