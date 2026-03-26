# Implementation Packs

Use this folder for requirement-specific engineering memory.

Core rule:

- shared reusable metadata belongs in `metadata-drop/`
- requirement-specific logic belongs here
- raw source files stay local unless they are intentionally approved reference assets

## Default authoring standard

Implementation packs should be written for an average developer who needs to understand the flow quickly and maintain it safely later.

Preferred style:

- simple first
- one minimum working path before optional hardening
- description before code
- calm, low-noise wording
- inline tests when the tests live with the same class or include

Avoid by default:

- A/B/C track storytelling
- framework-heavy decomposition in the first pass
- interface-heavy design before the basic build path is clear
- restart, checkpoint, or monitoring detail in the core implementation path unless the requirement truly needs it
- operations-heavy sections before the developer can see how the feature is built

## Recommended pack structure

Use this order unless the requirement clearly needs something else:

1. Summary
2. Confirmed rules
3. Implementation rules
4. Minimum build path
5. Tests and validation
6. Optional hardening

For each major artifact, explain it before the code block:

- `Purpose`
- `What it reads`
- `What it writes`
- `Why it exists`
- `Open assumptions`

## What belongs here

- requirement summary and business intent
- confirmed metadata references used for the solution
- requirement-specific joins, filters, and transformation rules
- curated examples:
  - `zero-shot`
  - `one-shot`
  - `few-shot` when needed
- implementation notes across ABAP, AMDP, CVPM, configuration, or reconciliation
- validation, debugging, and enhancement history

## What does not belong here

- raw Excel workbooks
- raw PDFs, DOCX files, screenshots, or OCR dumps
- generic DDIC or RDL structures that are reusable across multiple requirements

## Working model

- developers may use local raw files and scratch notes outside the shared repo flow
- commit only curated information that helps future debugging or enhancement
- if a pack produces a reusable pattern across multiple requirements, a maintainer can later promote that pattern into shared metadata or a skill reference
- use GHCP to generate or refine implementation-pack content from the prompt contract when one exists, rather than manually overdesigning the pack first
