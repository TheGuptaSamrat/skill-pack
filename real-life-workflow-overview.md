# Real Life Workflow Overview

This repository helps SAP FPSL and FSDM developers use AI in a controlled and practical way.

It is not a generic chatbot setup.
It is a structured skill pack that gives AI the right SAP context before code or documentation is generated.

## What Problem It Solves

Today, AI output quality often depends on how well each individual developer writes prompts.

This repository improves that by giving the team:

- reusable skill-specific guidance
- trusted metadata inputs
- consistent output expectations
- test cases for trial and feedback

## What A Developer Does

In day-to-day work, the developer uses:

- Eclipse ADT for the actual SAP development
- VS Code with GitHub Copilot for AI interaction
- this repository as the context layer

## Step-By-Step Workflow

### 1. Choose the right skill

The developer chooses one of the core or focused skills:

- `amdp`
- `abap`
- `config`
- `quality`
- `docs`
- `projections`
- `reconciliation`
- `mapping`
- `test-data`

Use core skills for general work. Use focused skills for narrower jobs.

Use `quality` for DDIC-driven data quality rules. Use `projections` for sizing and estimation. Use `docs` for documentation and general technical interpretation. Use `mapping` for source-to-target mapping work.

### 2. Give a short prompt

The developer does not need to write a long prompt.

GHCP may often infer the right route from the task wording, but the most reliable pilot pattern is to name the skill explicitly in the prompt.

Example:

```text
Use amdp from this repo. Build the smallest ABAP wrapper and AMDP method for FSDM cashflow to FPSL posting input. Include tests and validation.
```

### 3. AI reads the repository context

The AI uses:

- the selected skill instructions
- relevant references
- normalized metadata if available

This reduces repeated prompting and improves consistency.

### 4. AI generates output

The expected output is:

- smaller and more focused
- easier to paste into Eclipse ADT
- more likely to include tests and validation
- less likely to invent SAP objects or fields

### 5. Developer validates and continues

The developer pastes only the needed output into Eclipse ADT and validates it.

This keeps human review and SAP validation in place.

## How Metadata Fits In

If trusted Excel metadata is available:

1. it is uploaded into `metadata-drop/raw-excel/`
2. the repo normalizes it into smaller working files
3. the normalized files become the default context for later AI use

This makes future prompts shorter and more accurate.

One thing to watch in pilot use is whether developers normalize new metadata before prompting, because that is what keeps the context lightweight and reusable.

## Why This Is Useful

Expected benefits:

- less time spent writing prompts
- better first drafts
- more consistent code generation
- better technical documentation
- easier onboarding of developers

## What This Is Not

This does not:

- replace SAP design review
- replace functional validation
- make autonomous production changes
- remove the need for developer judgment

It is a delivery accelerator, not a replacement for engineering ownership.

## How We Can Trial It

The repository already includes developer test cases.

A simple pilot can be:

1. give 3-4 developers one test case each
2. ask them to use the repo with GitHub Copilot
3. collect feedback on speed, quality, and usability

## Simple Summary

In real life, this works as a reusable SAP AI context layer:

- developer chooses a skill
- gives a short prompt
- AI uses repository context and metadata
- developer gets a better first draft
- developer validates in Eclipse ADT

That is the intended operating model.
