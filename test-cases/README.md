# Developer Test Cases

Use this folder to hand trial scenarios to a small group of developers and collect structured feedback.

Goals:

- verify prompt reduction
- verify output quality
- verify Eclipse ADT handoff quality
- identify missing metadata or weak guidance
- compare broad core skills versus narrower focused skills
- verify the 6 use cases map cleanly to one primary skill each
- verify added engineering-focused skills stay modular and do not blur into neighboring skills
- verify integration-focused prompts route to `integration` instead of `mapping`, `reconciliation`, or `config`
- verify boundary prompts still keep field-spec work in `mapping` and balancing work in `reconciliation`

How to run:

1. assign one test case to one developer
2. ask them to use the named skill only
3. ask them to keep the prompt short
4. ask them to record the outcome in `feedback-template.md`
5. capture the new scoring fields for context efficiency, output accuracy, factual correction count, and usability so test-case reviews can be compared against `docs-context/indexes/skill-efficiency-report.md`
