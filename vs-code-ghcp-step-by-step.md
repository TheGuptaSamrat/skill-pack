# VS Code With GitHub Copilot: Step By Step

This guide shows how a developer can use this skill pack with VS Code and the GitHub Copilot extension while still developing in Eclipse ADT.

## 1. Open The Right Tools

Keep two work surfaces open:

- Eclipse ADT for the real SAP artifact work
- VS Code for GitHub Copilot and this repository

Recommended setup:

- open the ABAP project in Eclipse ADT
- open this repository in VS Code
- keep the target class, CDS artifact, or design note visible in Eclipse
- if metadata was uploaded, keep the workbook in `metadata-drop/raw-excel/`

## 2. Pick The Right Skill

Choose only one skill first.

- `sap-fpsl-amdp`
  - AMDP, SQLScript, CDS table functions, pushdown-heavy logic
- `sap-fpsl-abap`
  - ABAP OO, orchestration, validation, exceptions, ABAP Unit
- `sap-fpsl-configuration`
  - configuration guidance, derivative rules, setup validation, upload checks
- `sap-fpsl-tech-docs`
  - technical specs, mapping docs, metadata interpretation, handoff docs
- `sap-fpsl-projections`
  - sizing estimates, volume trends, DB growth assumptions, sensitivity views

Use `sap-fpsl-projections` for estimation and sizing outputs. Use `sap-fpsl-tech-docs` for documentation, mapping, and metadata interpretation.

Do not load all skills at once unless the task genuinely spans them.

## 3. Load Only The Required Context

In VS Code, point Copilot to:

- the relevant `skills/<skill-name>/SKILL.md`
- one or two reference files from the same skill if needed
- relevant files from `metadata-drop/normalized/` first
- raw uploads only when normalization is missing or under review

Keep context lean.

Good example:

- `skills/sap-fpsl-amdp/SKILL.md`
- `skills/sap-fpsl-amdp/references/sql-and-performance-rules.md`
- `metadata-drop/ddic/current/fields-template.csv`
- `metadata-drop/samples/fsdm_to_fpsl_mapping.md`

If a new workbook was uploaded, first run normalization from VS Code:

1. `Terminal: Run Task`
2. choose `Metadata: Normalize latest workbook`
3. then use files under `metadata-drop/normalized/`

## 4. Write A Short Prompt

The prompt should contain only the task delta.

GHCP should often route correctly from the task wording, but the most reliable pilot pattern is still to name the intended skill explicitly.

Example for ABAP:

```text
Use sap-fpsl-abap from this repo. Generate a modular class for validating and preparing FPSL posting input from FSDM cashflow rows. Include ABAP Unit and validation steps.
```

Example for AMDP:

```text
Use sap-fpsl-amdp from this repo. Design the smallest ABAP wrapper and AMDP method for transforming FSDM cashflow rows into FPSL posting input. Use repository metadata only and keep placeholders where names are not confirmed.
```

Example for configuration:

```text
Use sap-fpsl-configuration from this repo. Review this derivative-rule change request and produce a configuration checklist, validation sequence, and risks. Use sample navigation only as guidance, not as confirmed setup.
```

## 5. Ask For The Smallest Useful Output

Do not ask for everything at once unless needed.

Good first requests:

- class definition only
- method implementation only
- ABAP Unit scaffold only
- AMDP method only
- validation checklist only
- technical mapping note only

This keeps the output easier to review and paste into ADT.

## 6. Paste Into Eclipse ADT

Take only the required block from VS Code and paste it into the correct Eclipse artifact.

Typical flow:

1. generate a class skeleton
2. paste into ADT
3. generate one method body
4. paste into ADT
5. generate the unit test
6. paste into ADT
7. activate and validate

## 7. Validate Immediately

Do not wait until the end.

Validate after each meaningful paste:

- syntax and activation
- object dependencies
- unit test behavior
- counts, totals, and grain
- logs or traces where relevant

Common transactions:

- `SE24`
- `SE80`
- `SE11`
- `SE16N`
- `ST05`
- `SAT`
- `SM37`
- `SLG1`

## 8. Improve Quality With Metadata

If output is too generic, add better evidence instead of writing a much longer prompt.

Best upgrades:

- DDIC exports
- CDS definitions
- existing class signatures
- configuration screenshots or extracts
- sample source rows
- confirmed target fields

The repo is designed so better metadata improves output quality.

If a new raw Excel was uploaded recently, check:

- `metadata-drop/manifest.csv`
- `metadata-drop/change-review.md`

If status says `reverify-required`, do not trust older generated mappings without rechecking them.

In pilot use, watch whether developers normalize new metadata before prompting. The repo is designed to work best when normalized files, not raw uploads, are used as the default context.

## 9. Keep The Team Consistent

If the team likes a pattern:

- add it to `metadata-drop/` if it is evidence
- add it to `references/` if it is reusable guidance
- do not hide important working knowledge inside personal prompts

## 10. Practical Daily Pattern

Daily working sequence:

1. open Eclipse ADT and VS Code
2. choose one skill
3. load only the needed context
4. give a short prompt
5. request the smallest useful artifact
6. paste into ADT
7. validate immediately
8. refine with metadata, not prompt bloat

## Example Outcome

Instead of a long custom prompt, a developer should be able to say:

```text
Use sap-fpsl-tech-docs from this repo. Build a technical mapping note from the attached DDIC and CDS evidence for FSDM cashflow to FPSL posting input. Separate confirmed metadata from assumptions and include code-generation guidance.
```

That is the intended working model.
