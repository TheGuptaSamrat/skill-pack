# CVPM Core Rules

- treat CVPM as FPSL process design, not as generic configuration or coding work
- start from the accounting objective, process cadence, and affected process steps
- use process-step framing such as register, accrue, defer, value, classify, and related valuation steps where the evidence supports it
- keep customer-specific job structure, class names, worklists, and thread settings as placeholders until confirmed
- separate standard FPSL method concepts from customer implementation choices
- do not turn generic training concepts into proof of local setup

## Minimum Evidence Checklist (Before Production-Level Guidance)

- accounting objective and run cadence (periodic, event-driven, rerun)
- target process-step sequence with dependencies
- method mapping and required inputs/outputs per step
- source-data and staging evidence (including parameter governance)
- threading and performance assumptions based on real volume/runtime evidence
- posting and reconciliation checkpoints for run sign-off
