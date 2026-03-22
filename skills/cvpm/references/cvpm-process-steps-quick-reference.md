# CVPM Process Steps Quick Reference

Purpose: provide a low-context, implementation-focused summary of standard FPSL CVPM process steps before opening the full reference.

Use this file first for:
- job structure sketches
- method-selection discussions
- quick troubleshooting orientation

Escalate to `fpsl-process-steps-reference.md` only when detailed semantics or edge-case step behavior is required.

## Core Step Set (At a Glance)

| Step Family | Typical Objective | Typical Output |
|---|---|---|
| Register | Bring source positions into CVPM scope | Registered positions and control counts |
| Accrue / Defer | Time-based recognition and deferral logic | Periodized accounting measures |
| Value / Value FX | Revaluation and FX effects by method rules | Valuation deltas and FX postings |
| Classify | Assign accounting treatment class | Classification-aligned result buckets |
| Post / Transfer | Hand off validated results to downstream posting path | Posting-ready aggregates and logs |

## Minimal Design Checklist

1. Confirm accounting goal and period granularity.
2. Confirm required step families (do not include unused steps by default).
3. Define method dependencies step by step.
4. Define control totals and expected checkpoint outputs per step.
5. Confirm rerun behavior and operational monitor expectations.

## Fast Troubleshooting Lens

- Step did not execute: verify sequence dependency and prerequisite outputs.
- Step executed with low volume: compare expected versus actual worklist scope.
- Totals drift across steps: validate control totals and key integrity after each handoff.
- Run succeeds but results look wrong: verify method assignment and classification path.

## When To Open Full Reference

Open `fpsl-process-steps-reference.md` when you need:
- complete process-step semantics
- less common step variants
- deeper operational context for monitor and periodic tasks

## Output Standard

When this quick reference is used, return:
- selected step sequence
- method dependency notes
- control totals per checkpoint
- explicit confirmed versus inferred assumptions
