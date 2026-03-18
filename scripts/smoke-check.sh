#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"

required_files=(
  "$repo_root/README.md"
  "$repo_root/metadata-normalization.md"
  "$repo_root/.github/copilot-instructions.md"
  "$repo_root/.github/instructions/amdp.instructions.md"
  "$repo_root/.github/instructions/abap.instructions.md"
  "$repo_root/.github/instructions/configuration.instructions.md"
  "$repo_root/.github/instructions/tech-docs.instructions.md"
  "$repo_root/.github/instructions/projections.instructions.md"
  "$repo_root/scripts/normalize_excel.py"
  "$repo_root/scripts/run-normalization.sh"
  "$repo_root/scripts/ingest_pdf_context.py"
  "$repo_root/.vscode/tasks.json"
  "$repo_root/docs-context/README.md"
  "$repo_root/docs-context/indexes/source-catalog.md"
  "$repo_root/docs-context/indexes/topic-map.md"
  "$repo_root/docs-context/indexes/ingestion-manifest.csv"
  "$repo_root/docs-context/indexes/update-policy.md"
  "$repo_root/docs-context/indexes/versioning-convention.md"
  "$repo_root/docs-context/inbox/README.md"
  "$repo_root/docs-context/inbox/section-config.template.json"
  "$repo_root/skills/sap-fpsl-amdp/SKILL.md"
  "$repo_root/skills/sap-fpsl-amdp/agents/openai.yaml"
  "$repo_root/skills/sap-fpsl-abap/SKILL.md"
  "$repo_root/skills/sap-fpsl-abap/agents/openai.yaml"
  "$repo_root/skills/sap-fpsl-configuration/SKILL.md"
  "$repo_root/skills/sap-fpsl-configuration/agents/openai.yaml"
  "$repo_root/skills/sap-fpsl-tech-docs/SKILL.md"
  "$repo_root/skills/sap-fpsl-tech-docs/agents/openai.yaml"
  "$repo_root/skills/sap-fpsl-projections/SKILL.md"
  "$repo_root/skills/sap-fpsl-projections/agents/openai.yaml"
  "$repo_root/metadata-drop/README.md"
  "$repo_root/metadata-drop/ddic/README.md"
  "$repo_root/metadata-drop/cds/README.md"
  "$repo_root/metadata-drop/fpsl/README.md"
  "$repo_root/metadata-drop/fsdm/README.md"
  "$repo_root/metadata-drop/configuration/README.md"
  "$repo_root/metadata-drop/samples/README.md"
  "$repo_root/metadata-drop/raw-excel/README.md"
  "$repo_root/metadata-drop/normalized/README.md"
  "$repo_root/metadata-drop/manifest.csv"
  "$repo_root/metadata-drop/change-review.md"
  "$repo_root/test-cases/README.md"
  "$repo_root/test-cases/feedback-template.md"
  "$repo_root/test-cases/test-case-05-guided-configuration.md"
  "$repo_root/test-cases/test-case-06-reconciliation-query.md"
  "$repo_root/test-cases/test-case-07-mapping-spec.md"
  "$repo_root/test-cases/test-case-08-test-data.md"
  "$repo_root/test-cases/test-case-09-projections.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

echo "Smoke check passed."
