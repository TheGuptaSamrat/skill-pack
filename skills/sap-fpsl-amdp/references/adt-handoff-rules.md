# ADT Handoff Rules

Use this handoff contract when output is meant to be pasted into Eclipse ADT or Eclipse SQL Console.

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

- `AMDP method body <class_name>=> <method_name>`
- `Method implementation <class_name>=> <method_name>`
- `Local test class in <class_name>`
- `CDS source <ddl_name>`
- `SQL Console worksheet`

## Reject These Output Shapes

- multiple unrelated artifacts in one code block
- prose mixed inside a code block
- full-class output when only one method or SQL block changed
- invented object names when repo or DDIC evidence is missing
