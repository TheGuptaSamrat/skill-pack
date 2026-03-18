#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"

required_files=(
  "$repo_root/README.md"
  "$repo_root/.github/copilot-instructions.md"
  "$repo_root/skills/sap-fpsl-amdp/SKILL.md"
  "$repo_root/skills/sap-fpsl-amdp/agents/openai.yaml"
  "$repo_root/skills/sap-fpsl-abap/SKILL.md"
  "$repo_root/skills/sap-fpsl-abap/agents/openai.yaml"
  "$repo_root/skills/sap-fpsl-configuration/SKILL.md"
  "$repo_root/skills/sap-fpsl-configuration/agents/openai.yaml"
  "$repo_root/skills/sap-fpsl-tech-docs/SKILL.md"
  "$repo_root/skills/sap-fpsl-tech-docs/agents/openai.yaml"
  "$repo_root/metadata-drop/README.md"
  "$repo_root/metadata-drop/ddic/README.md"
  "$repo_root/metadata-drop/cds/README.md"
  "$repo_root/metadata-drop/fpsl/README.md"
  "$repo_root/metadata-drop/fsdm/README.md"
  "$repo_root/metadata-drop/configuration/README.md"
  "$repo_root/metadata-drop/samples/README.md"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

echo "Smoke check passed."
