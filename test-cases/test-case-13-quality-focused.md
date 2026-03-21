# Test Case 13: Focused Quality Rules

Skill:

- `quality`

Scenario:

- generate DDIC-driven quality checks for a staging-to-SDL or SDL-to-RDL style flow with explicit completeness, key, null, domain, and cross-field validation

Use this metadata:

- `metadata-drop/ddic/current/tables-template.csv`
- `metadata-drop/ddic/current/fields-template.csv`
- `metadata-drop/ddic/current/domains-template.csv`
- `metadata-drop/samples/fsdm_to_fpsl_mapping.md`

Expected evaluation points:

- no invented fields or domains
- explicit null, key, and domain checks
- confirmed rules separated from inferred rules
- usable SQL or rule-spec output
