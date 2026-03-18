# Inbox

Place newly received SAP or SAP Fioneer PDFs here before ingestion.

Workflow:

1. add PDF to `docs-context/inbox/`
2. create a section config JSON if you want controlled section splitting
3. run `scripts/ingest_pdf_context.py`
4. review generated markdown in `docs-context/full-source-md/`
5. curate crisp files into `docs-context/official/` or `docs-context/training/`
6. update indexes if needed
