# Test And Exception Patterns

- Include ABAP Unit by default when generating build output.
- Use simple fixtures and explicit expected keys, counts, and amounts.
- Use exception chaining with `previous =` for propagated technical failures.
- Call out where integration tests or manual checks are still needed.
- Keep test data neutral unless real metadata confirms exact structures.
