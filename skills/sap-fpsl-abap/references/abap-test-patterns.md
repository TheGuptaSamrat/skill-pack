# ABAP Test Patterns

- include ABAP Unit by default when generating build output
- use simple fixtures and explicit expected keys, counts, and amounts
- use exception chaining with `previous =` for propagated technical failures
- call out where integration tests or manual checks are still needed
- keep test data neutral unless real metadata confirms exact structures
- generate functional test data, insert scripts, or fixture builders when scenario validation is requested
- keep production code and test support cleanly separated
- keep synthetic data clearly labeled
- include mandatory scenario attributes when data shape matters
- use deterministic fixtures and expose only the variables tests really need
