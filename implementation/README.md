# Implementation Packs

Use this folder for requirement-specific engineering memory.

Core rule:

- shared reusable metadata belongs in `metadata-drop/`
- requirement-specific logic belongs here
- raw source files stay local unless they are intentionally approved reference assets

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
