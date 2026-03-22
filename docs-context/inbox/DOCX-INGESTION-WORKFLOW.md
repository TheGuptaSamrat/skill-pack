# SAP FPSL .docx Ingestion Workflow

**Status:** Ready to consume new Word documentation on SAP FPSL  
**Last updated:** 2026-03-22  
**Source:** Workflow template for autonomous ingestion

---

## Quick Start

When you provide the `.docx` file:

### Step 1: Prepare the Document
```bash
# Option A: Convert Word → PDF (preserves formatting)
# Use Word's "Save as PDF" or:
# pandoc source.docx -t pdf -o source.pdf

# Option B: Convert Word → Markdown (text-friendly)
# pandoc source.docx -t markdown -o source.md
```

### Step 2: Place in Staging
```bash
# For PDF (recommended)
cp source.pdf metadata-drop/pdf-resources/

# For Markdown
cp source.md docs-context/inbox/review-drafts/
```

### Step 3: Ingest via Script
Edit `docs-context/inbox/config-fpsl-admin.json` to add a new source section:

```json
{
  "source": "FPSL_NEW_REFERENCE.pdf",
  "sections": [
    {
      "title": "<SECTION_TITLE>",
      "page_range": [1, 5],
      "topics": ["fpsl-config", "cvpm"],
      "trust_level": "official-product",
      "do_not_use_for": ["synthetic examples", "non-SAP platforms"]
    }
  ]
}
```

Then run:
```bash
python3 scripts/ingest_pdf_context.py \
  --config docs-context/inbox/config-fpsl-admin.json \
  --source metadata-drop/pdf-resources/FPSL_NEW_REFERENCE.pdf \
  --output-dir docs-context/inbox/review-drafts/
```

### Step 4: Review & Route
- Extracted sections land in `docs-context/inbox/review-drafts/`
- I'll review for accuracy and skill alignment
- Update `docs-context/shared/official-sources-router.md` with new reference
- Integrate into relevant SKILL.md Load Orders (typically steps 2–5)

### Step 5: Validate & Commit
```bash
python3 scripts/validate_file_naming.py && \
python3 scripts/validate_skill_pack_links.py && \
bash scripts/smoke-check.sh

git add . && \
git commit -m "docs(fpsl): add official <topic> reference to <skills>" && \
git push origin main
```

---

## Expected Integration Points

Based on your input (1–10 page official SAP FPSL reference):

| Skill | Integration | Priority | Reason |
|-------|-------------|----------|--------|
| **config** | Add to Load Order step 3–4 | High | Strengthens configuration workflow |
| **cvpm** | Add to Load Order step 2–3 | High | Supports CVPM process guidance |
| **quality** | Add to Load Order step 2 if quality topics present | Medium | May enhance DDIC-driven rules |
| **reconciliation** | Add to Load Order step 3 if reconciliation topics present | Medium | May reinforce verification patterns |

---

## Document Assessment Checklist

When the document arrives, I'll evaluate:

- [ ] Official SAP/Fioneer source verified
- [ ] No proprietary client data
- [ ] Scope clearly defined (CVPM, config, reconciliation, etc.)
- [ ] No duplicate coverage with existing references
- [ ] Quality of technical content (actionable, precise, non-conflicting)
- [ ] Page count < 100 (quick reference status)
- [ ] Extractable sections (clear sections, no embedded visuals-only content)

---

## Skills Ready to Integrate

**Current state (before new doc):** 10 active skills, all validators passing  
**New doc impact:** Expected to strengthen 2–3 skills (config, cvpm priority)  
**Risk:** Low (pdf-based ingestion is deterministic; easy rollback if needed)

---

## Handoff

**Next action:** Provide the `.docx` file path/upload.  
**Timeline:** Quick (1–2 commits for 1–10 page reference).  
**Output:** Updated skill pack with new reference material integrated and committed to main.

