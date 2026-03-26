---
mode: agent
description: GHCP-ready requirement contract for the RDL net posting autopilot. Use this as the primary requirement input when proposing design corrections, AMDP artifacts, ABAP artifacts, or validation SQL for the netting flow.
tools:
  - read_file
  - semantic_search
  - grep_search
---

Use the `amdp` and `abap` skills.

Load implementation context from:
- `implementation/rdl-net-posting-autopilot/rdl-net-posting-implementation-pack.md`
- `implementation/rdl-net-posting-autopilot/design/netting-join-logic.md`
- `implementation/rdl-net-posting-autopilot/examples/zero-shot.md`
- `implementation/rdl-net-posting-autopilot/examples/one-shot.md`

Treat this prompt file as the primary requirement contract. If the implementation pack differs, follow this prompt file and call out the mismatch explicitly.

## Output style for GHCP

Generate the next result in a simple-first style:

- produce one simple end-to-end implementation path first
- explain each major artifact before the code block
- keep the flow linear and easy to follow for an average ABAP developer
- keep tests close to the implementation when they live in the same class or include
- move optional hardening, restart logic, monitoring detail, and CVPM extension notes after the core build path
- avoid A/B/C track storytelling
- avoid unnecessary interfaces, helper layers, or framework-style decomposition in the first pass
- prefer the smallest maintainable working design over the most theoretically modular one

## Source constraints — confirmed

- **Source**: FPSL only.
- **Excluded**: GL and GR posting blocks visible in the sample workbook are not netting source rows.
- **Driver table**: `/BA1/HFSPD`
- **Validation dim 1**: `/BA1/HKAPA`
  - Hard filter: `/BA1/CR4PFCT = '2100'`
  - Temporal: latest `/BA1/CR0KEYDAT` ≤ `/BA1/C55POSTD` where `CURRENT_FLAG = 'X'`
- **Validation dim 2**: `/BA1/HKAPD`
  - Hard filter: `/BA1/C55ACCRCT = '601'`
  - Temporal: latest `/BA1/CR0KEYDAT` ≤ `/BA1/C55POSTD` where `CURRENT_FLAG = 'X'`

## Netting model — confirmed

Use two levels:

- **Netting group**
  - used to compute the net
  - excludes contract ID
  - minimum confirmed dimensions from current evidence:
    - `/BA1/C55POSTD`
    - `/BA1/C11NODENO`
    - `/BA1/C55ACCSY`
  - preserve legal-entity and profit-center style grouping when confirmed in the target landscape

- **Per-contract result**
  - one output row per eligible contract within the netting group
  - contract ID is an output dimension, not part of the aggregation key for net calculation

## Netting and allocation logic — confirmed from sample images

The yellow "Balance aggregated" block in the sample workbook is the expected post-netting output.

**Step 1 — Compute net for the netting group**
```text
net = SUM( /BA1/K5SAMGRP ) across all eligible contracts in the netting group
```

**Step 2 — Allocate proportionally per contract**

| Condition  | Allocate across               |
|------------|-------------------------------|
| net > 0    | positive contracts only       |
| net < 0    | negative contracts only       |
| net = 0    | no allocation (zero rows out) |

```text
Allocated_Amount(i) = ( |Contract_Balance(i)| / Σ|Same-Sign Balances| ) × |net|
```

Only contracts on the same sign side as the net may receive allocation.

**Step 3 — Write output into `Z_NET_POSTING`**
- `netted-delta` = `Allocated_Amount(i)` written to the amount field
- use one anchor strategy per contract result row
- `MIN(/BA1/C55DOCNUM)` + `MIN(/BA1/C55DOCITM)` is only a candidate anchor strategy and must be revalidated in the target landscape
- source precision preserved — no rounding or truncation unless later confirmed by business or posting constraints

## Currency — confirmed

- `/BA1/K5SAMGRP` is always USD. No FX conversion step.
- Retain `/BA1/K5SAMBAL` from the chosen anchor row as-is.

## DDIC field references

| Field purpose        | DDIC field        | Status               |
|----------------------|-------------------|----------------------|
| Asset/Liability flag | `/BA1/C55ALST`    | Inferred — verify    |
| Group Category A/C/D | TBD               | Open — see below     |
| Allocation amount    | Computed in logic | Confirmed pattern    |

## Open assumption — Group Category

Values A, C, D appear in the sample output block. Safe assumption:

- A = net > 0 group
- D = net < 0 group
- C = net = 0 group

Derive from allocation outcome. Add inline comment `TODO: confirm Group Category derivation with business`. Do not hard-code a static passthrough.

## Error handling — confirmed

- Write allocation errors (division by zero, missing anchor, missing contract data) to `Z_NET_POSTING_ERR` — separate table, not inline in the output stream.
- Capture: `POSTD`, `CONTID`, `NODENO`, `ACCSY`, error text, timestamp, user.

## Inline comment anchors — keep in generated code

1. GL and GR rows are excluded from the source set.
2. Anchor row strategy must be revalidated in the landscape.
3. Pre-netting balance is not posted; only `netted-delta` goes to `Z_NET_POSTING`.
4. `/BA1/K5SAMGRP` is always USD — no FX step.
5. Group Category derivation is open — derive from outcome and confirm with business.
6. `/BA1/C55ALST` as asset/liability indicator is inferred — verify in DDIC.
7. Do not round allocation amounts unless explicitly confirmed by business or posting constraints.

## GHCP usage patterns

- Use the prompt file and propose the design correction.
- Use the prompt file and generate the next AMDP artifact.
- Use the prompt file and generate validation SQL.
- Use the prompt file and debug the implementation-pack mismatch.

Next task: ${input:task:Describe the specific artifact or delta needed (for example "correct the AMDP allocation logic", "generate validation SQL", or "prepare the ABAP write step")}
