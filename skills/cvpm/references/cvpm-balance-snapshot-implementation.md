# CVPM Balance-Snapshot Implementation Pattern (Image-Derived)

Classification: extracted-customer-demo-evidence
Source basis: OCR from `metadata-drop/OtherDocs/CVPM/*.jpg` (25 images)
Trust usage: implementation flow structure, IMG navigation pattern, monitor workflow, and operational metrics examples
Do not use for: direct reuse of `Z*` names, class names, or any sample IDs in productive landscapes

---

## Intent

Use this reference when the user asks for a practical, sequence-first CVPM setup pattern that includes:

- class and data-source build order
- analytical process and step-sequence setup
- run execution and monitor checks

Route code-writing artifacts to `abap`/`amdp` and SQL verification to `reconciliation`.

---

## Observed Build Order (Evidence-Based)

The image set repeatedly shows this implementation order:

1. Create server/worklist class (sample shown: `Z_CL_CM_BS_SOLUTION_WL`)
2. Create CVPM step-execution class (sample shown: `Z_CL_CM_BS_SOLUTION`)
3. Create server entry for primary data source
4. Create primary data source (PDS)
5. Create analytical process (sample shown: `Z_CM_BS_SOLUTION`)
6. Create custom step sequence for that process
7. Execute and monitor the run

Keep all names as placeholders unless repository/customer metadata confirms exact objects.

---

## IMG Nodes to Verify During Setup

Under CVPM custom-process settings, the OCR evidence includes these nodes:

- Application Log: Edit Subobject for CVPM
- Edit Analytical Processes
- Define Process-Specific Pushbuttons
- Edit Custom Step Sequences for Analytical Processes
- Edit Fixed Step Sequences for Analytical Processes
- Define Package Size Per Legal Entity, Accounting System, and Source System

Use this as a navigation checklist when guiding configuration sessions.

---

## Analytical Process Design Fields (Observed)

Sample process screens show configuration of:

- report title
- step controller class
- process category / leading-process attributes
- dynamic selection behavior
- application-log subobject and authorization category

Treat all sample values as illustrative only.

---

## Process Parameter and DRG Pattern

OCR evidence shows a compact parameter set on the process:

- `/BA1/C11SRCSY`
- `/BA1/C55LGENT`
- `/BA1/C55POSTD`
- `/BA1/CROTSTMP`

Observed parameter type usage:

- single value
- value range

Observed data reading group:

- DRG `0001` for source-data style selection

When information is missing, keep placeholders and ask for confirmed parameter governance.

---

## Step Sequence Pattern (Balance-Snapshot Style)

For a sequence shown as `10`, the evidence indicates:

- Step 15: `Enrich Parameters` (type: parameter enrichment)
- Step 20: `Worklist` (type: worklist creation)
- Step 30: `Enrich Data` (type: data enrichment)

Use this as a pattern when designing custom step chains that separate parameter prep, worklist creation, and enrichment logic.

---

## Operational Monitoring Pattern

Monitor entry captured in the images:

- `/BAL/PW_PROCMON` (start CVPM process monitor)

Log evidence captured includes:

- run start/end messages
- step-sequence identifier
- source-data timestamp
- package count and records processed

Sample metric from screenshots:

- 161 packages
- 3,204,009 records processed

Treat these as a scale example to discuss threading/package tuning, not a target baseline.

---

## Navigation Map by Implementation Step

Use this matrix when the user asks where each CVPM setup step is performed.

1. Create server class
- Observed screen: Class Builder (server/worklist class screen)
- Navigation evidence: Class Builder UI is visible in screenshots
- Note: transaction code is not clearly readable in OCR; use local Class Builder entry point

2. Create CVPM class
- Observed screen: Class Builder (CVPM class screen)
- Navigation evidence: Class Builder UI with CVPM interfaces/methods is visible
- Note: transaction code is not clearly readable in OCR; use local Class Builder entry point

3. Create server entry for primary data source
- Observed area: data source maintenance for worklists
- IMG path evidence:
	Financial Products Subledger -> Data Loading Process -> Data Sources for Worklists

4. Create primary data source (PDS)
- Observed screen: Display Primary Data Sources / technical view for worklist data source
- IMG path evidence:
	Financial Products Subledger -> Data Loading Process -> Data Sources for Worklists

5. Create analytical process
- Observed screen: Change View "Analytical Processes": Details
- IMG path evidence:
	Financial Products Subledger -> Calculation and Valuation Process Manager (CVPM) -> General Settings for Custom Processes -> Edit Analytical Processes
- Dialog subareas visible:
	Process Parameter, Data Reading Groups, Technical Settings, Status Management

6. Create custom step sequence
- Observed screens: Change View "Step Sequences": Details and "Steps": Overview/Details
- IMG path evidence:
	Financial Products Subledger -> Calculation and Valuation Process Manager (CVPM) -> General Settings for Custom Processes -> Edit Custom Step Sequences for Analytical Processes
- Adjacent node shown:
	Edit Fixed Step Sequences for Analytical Processes

7. Execute and monitor run
- Execution entry: SE38 is explicitly referenced in screenshot text
- Monitor menu path evidence:
	Financial Products Subledger -> Calculation and Valuation Process Manager (CVPM) -> /BAL/PW_PROCMON (Start CVPM Process Monitor)
- Monitor log evidence:
	step sequence, source-data timestamp, package count, record count, start/end timestamps

---

## Navigation Confidence Notes

- High confidence: IMG nodes and monitor entry /BAL/PW_PROCMON are directly readable in OCR.
- Medium confidence: class creation location is clearly Class Builder, but OCR does not reliably expose the transaction code string.

---

## Minimal Validation Checklist

Before sign-off, validate:

- process created and active
- step sequence attached to process
- worklist creation step executes without package errors
- monitor shows completed run with package and record statistics
- application log is readable and tied to process/subobject

If runtime diagnostics are needed, route detailed SQL/data checks to `reconciliation`.
