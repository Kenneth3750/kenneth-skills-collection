#!/bin/bash

# Sync skills between Claude Code and OpenCode
# Usage:
#   sync-skills.sh                    # Sync all skills
#   sync-skills.sh aws                # Sync aws category
#   sync-skills.sh aws/aws-costs      # Sync specific skill

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

FILTER="${1:-}"

echo "Syncing skills between platforms..."
echo ""

# Install for both platforms
bash "$SCRIPT_DIR/install-claude.sh" "$FILTER"
echo ""
bash "$SCRIPT_DIR/install-opencode.sh" "$FILTER"

echo ""
echo "Sync complete! Skills are now available in both Claude Code and OpenCode."
