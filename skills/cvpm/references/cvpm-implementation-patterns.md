# CVPM Implementation Patterns

- describe the intended process-step sequence before suggesting implementation structure
- when users ask for practical setup flow, use the evidence-backed build order: server/worklist class -> CVPM class -> primary data source -> analytical process -> custom step sequence -> run + monitor
- keep screenshot-derived `Z*` class/process names as sample-only evidence, never as defaults
- identify where calculation methods, target values, or analytical decisions influence the run design
- use worklist discussion only when the requirement clearly depends on carried-forward positions or analytical decisions
- use thread or parallelism guidance only when the user provides runtime, volume, or operational evidence
- for monitor-first troubleshooting, anchor guidance in CVPM monitor workflow and package/record metrics instead of class-level speculation
- route ABAP wrapper design to `abap` and pushdown-heavy implementation to `amdp`
- route source-to-target logic to `mapping` instead of embedding mapping detail into CVPM design

See `cvpm-balance-snapshot-implementation.md` for the image-derived runbook pattern and observed monitor evidence.
