# ADT Handoff Rules

Use this handoff contract when output is meant to be pasted into Eclipse ADT.

## Required Output Contract

Return one artifact block at a time in this shape:

1. `Artifact`
2. `Paste target`
3. `Action`
4. one fenced code block only
5. `Checks`

## Allowed Actions

- `create`
- `replace`
- `append`

## Paste Target Examples

- `Class definition section of <class_name>`
- `Method implementation <class_name>=> <method_name>`
- `Local test class in <class_name>`
- `CDS source <ddl_name>`
- `AMDP method body <class_name>=> <method_name>`
- `SQL Console worksheet`

## Reject These Output Shapes

- multiple unrelated artifacts in one code block
- prose mixed inside a code block
- full-class output when only one method changed
- invented object names when repo or DDIC evidence is missing
- unstructured code with no paste target
