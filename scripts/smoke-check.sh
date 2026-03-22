#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"

required_files=(
  "$repo_root/README.md"
  "$repo_root/prompt-library.md"
  "$repo_root/metadata-normalization.md"
  "$repo_root/.github/copilot-instructions.md"
  "$repo_root/.github/instructions/amdp.instructions.md"
  "$repo_root/.github/instructions/abap.instructions.md"
  "$repo_root/.github/instructions/config.instructions.md"
  "$repo_root/.github/instructions/quality.instructions.md"
  "$repo_root/.github/instructions/projections.instructions.md"
  "$repo_root/.github/instructions/reconciliation.instructions.md"
  "$repo_root/.github/instructions/mapping.instructions.md"
  "$repo_root/.github/instructions/test-data.instructions.md"
  "$repo_root/.github/instructions/cvpm.instructions.md"
  "$repo_root/.github/instructions/partitioning.instructions.md"
  "$repo_root/scripts/normalize_excel.py"
  "$repo_root/scripts/audit_skill_pack_redundancy.py"
  "$repo_root/scripts/validate_skill_pack_links.py"
  "$repo_root/scripts/validate_file_naming.py"
  "$repo_root/scripts/run-context-optimization.sh"
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
  "$repo_root/skills/amdp/SKILL.md"
  "$repo_root/skills/amdp/agents/openai.yaml"
  "$repo_root/skills/abap/SKILL.md"
  "$repo_root/skills/abap/agents/openai.yaml"
  "$repo_root/skills/config/SKILL.md"
  "$repo_root/skills/config/agents/openai.yaml"
  "$repo_root/skills/quality/SKILL.md"
  "$repo_root/skills/quality/agents/openai.yaml"
  "$repo_root/skills/projections/SKILL.md"
  "$repo_root/skills/projections/agents/openai.yaml"
  "$repo_root/skills/reconciliation/SKILL.md"
  "$repo_root/skills/reconciliation/agents/openai.yaml"
  "$repo_root/skills/mapping/SKILL.md"
  "$repo_root/skills/mapping/agents/openai.yaml"
  "$repo_root/skills/test-data/SKILL.md"
  "$repo_root/skills/test-data/agents/openai.yaml"
  "$repo_root/skills/cvpm/SKILL.md"
  "$repo_root/skills/cvpm/agents/openai.yaml"
  "$repo_root/skills/partitioning/SKILL.md"
  "$repo_root/skills/partitioning/agents/openai.yaml"
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
  "$repo_root/metadata-drop/change-log.md"
  "$repo_root/test-cases/README.md"
  "$repo_root/test-cases/feedback-template.md"
  "$repo_root/test-cases/test-case-05-guided-configuration.md"
  "$repo_root/test-cases/test-case-06-reconciliation-query.md"
  "$repo_root/test-cases/test-case-07-mapping-spec.md"
  "$repo_root/test-cases/test-case-08-test-data.md"
  "$repo_root/test-cases/test-case-09-projections.md"
  "$repo_root/test-cases/test-case-10-reconciliation-focused.md"
  "$repo_root/test-cases/test-case-11-mapping-focused.md"
  "$repo_root/test-cases/test-case-12-test-data-focused.md"
  "$repo_root/test-cases/test-case-13-quality-focused.md"
  "$repo_root/test-cases/test-case-14-cvpm-focused.md"
  "$repo_root/test-cases/test-case-15-partitioning-focused.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

python3 "$repo_root/scripts/validate_skill_pack_links.py" \
  --repo-root "$repo_root" \
  --out-json "docs-context/indexes/validation-skill-pack.json"

python3 "$repo_root/scripts/validate_file_naming.py" \
  --repo-root "$repo_root"

echo "Smoke check passed."
