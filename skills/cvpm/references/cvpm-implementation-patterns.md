# CVPM Implementation Patterns

- describe the intended process-step sequence before suggesting implementation structure
- identify where calculation methods, target values, or analytical decisions influence the run design
- use worklist discussion only when the requirement clearly depends on carried-forward positions or analytical decisions
- use thread or parallelism guidance only when the user provides runtime, volume, or operational evidence
- route ABAP wrapper design to `abap` and pushdown-heavy implementation to `amdp`
- route source-to-target logic to `mapping` instead of embedding mapping detail into CVPM design
