# Prompt Library

Use these as short starting prompts in VS Code with GitHub Copilot.

Working rule:

- start from the implementation pack when one exists
- keep the prompt to the task delta
- rely on repo metadata instead of prompt bloat
- name the skill explicitly only when the task is ambiguous or you want to override routing
- ask for one simple working path before optional hardening
- ask for descriptions before code when you want output that an average developer can follow quickly

## Pack-First Prompts

### Build from an implementation pack

```text
Build from this implementation pack. Use approved metadata first, keep placeholders explicit where object names are not confirmed, and return one simple working path with the smallest useful next artifact.
```

### Enhance an existing implementation

```text
Enhance this existing implementation pack. Reuse the confirmed metadata and example patterns already captured here, keep new assumptions explicit, and propose only the delta needed for the enhancement. Keep the solution easy to understand and maintain.
```

### Debug an implementation

```text
Debug this implementation using the pack evidence first. Compare the current behavior against the documented logic and examples, call out confirmed versus inferred causes, and suggest the smallest useful fix path. Keep the explanation linear and practical.
```

### Generate checks from approved metadata and the pack

```text
Generate validation checks from the approved metadata and this implementation pack. Keep counts, totals, key checks, and evidence gaps explicit.
```

### Generate a cleaner implementation pack draft

```text
Generate a cleaner implementation-pack draft from this requirement and prompt context. Use one minimum working path, explain each artifact before the code, keep tests near the implementation when appropriate, and move optional hardening after the core build path.
```

## Core Skills

### `abap`

```text
Use the abap skill in this repo. Generate the smallest clean ABAP artifact for this FPSL task. Keep placeholders explicit where object names are not confirmed. Explain the artifact before the code and keep tests and validation close to the implementation.
```

### `amdp`

```text
Use the amdp skill in this repo. Design the smallest AMDP plus ABAP wrapper for this FPSL or FSDM transformation. Keep SQL staged, explain why AMDP is justified, and avoid extra abstraction unless it clearly helps maintainability.
```

### `config`

```text
Use the config skill in this repo. Give me an evidence-first FPSL configuration walkthrough with prerequisites, impact notes, and validation steps. Keep assumptions explicit.
```

### `integration`

```text
Use the integration skill in this repo. Propose the smallest useful FSDM-to-FPSL data-loading design note with extract, stage, validate, and load checkpoints, restart logic, and technical control checks.
```

### `projections`

```text
Use the projections skill in this repo. Estimate monthly and yearly FPSL or FSDM volume growth from the given assumptions. Show the storage impact and label uncertainty clearly.
```

## Focused Skills

### `quality`

```text
Use the quality skill in this repo. Generate DDIC-driven quality checks for the provided layer. Separate confirmed rules from inferred rules and return SQL or a rule-spec note.
```

### `reconciliation`

```text
Use the reconciliation skill in this repo. Generate the smallest DDIC-aware query set to validate counts, totals, keys, and data flow for this FPSL or FSDM step.
```

### `mapping`

```text
Use the mapping skill in this repo. Build a source-to-target mapping specification from the provided metadata. Keep confirmed, inferred, and unresolved sections separate.
```

### `test-data`

```text
Use the test-data skill in this repo. Generate meaningful synthetic data and insert scripts for this FPSL scenario. Keep synthetic assumptions explicit and populate all required attributes.
```

### `cvpm`

```text
Use the cvpm skill in this repo. Propose the smallest useful CVPM design note for this requirement. Include process-step sequence, method guidance, worklist or thread placeholders where needed, and validation follow-up actions.
```

### `partitioning`

```text
Use the partitioning skill in this repo. Review whether partitioning is justified for the given FPSL-relevant table. Base the answer on volume, growth, access pattern, and operational implications.
```

## Prompt Extensions

Add one line if needed:

- `Use normalized metadata first.`
- `Return one ADT-ready artifact block at a time.`
- `Lead with one minimum working path before optional hardening.`
- `Explain each artifact before presenting code.`
- `Keep tests close to the implementation when they live in the same class or include.`
- `Do not invent object names; keep placeholders explicit.`
- `Separate confirmed setup from inferred setup.`
- `Route any follow-up coding to abap or amdp.`
- `Route field-level mapping to mapping and posted-result balancing to reconciliation.`

Repository hygiene note:

- keep prompts and outputs anchored to implementation packs, skill-owned references, and indexed metadata
- avoid relying on root-level session or review summary files for active guidance
