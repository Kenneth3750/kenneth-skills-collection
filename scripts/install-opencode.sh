#!/bin/bash

# Install skills for OpenCode
# Usage:
#   install-opencode.sh                    # Install all skills
#   install-opencode.sh aws                # Install all skills from aws category
#   install-opencode.sh aws/aws-costs      # Install specific skill

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
SOURCE_DIR="$REPO_DIR/opencode"
TARGET_DIR=".opencode/skills"

FILTER="${1:-}"

install_skill() {
    local skill_path="$1"
    local skill_name=$(basename "$skill_path")
    local target="$TARGET_DIR/$skill_name"
    
    if [ -f "$skill_path/SKILL.md" ]; then
        mkdir -p "$target"
        cp "$skill_path/SKILL.md" "$target/SKILL.md"
        echo "  ✓ Installed: $skill_name"
        
        # Copy any additional files (scripts, etc.) in the skill directory
        for file in "$skill_path"/*; do
            if [ -f "$file" ] && [ "$(basename "$file")" != "SKILL.md" ]; then
                cp "$file" "$target/"
                echo "    ✓ Copied: $(basename "$file")"
            fi
        done
        
        return 0
    fi
    return 1
}

echo "Installing skills for OpenCode..."
mkdir -p "$TARGET_DIR"

if [ -z "$FILTER" ]; then
    # Install all skills
    echo "Installing all skills..."
    for category in "$SOURCE_DIR"/*/; do
        for skill in "$category"*/; do
            install_skill "$skill" || true
        done
    done
elif [ -d "$SOURCE_DIR/$FILTER" ]; then
    # Install category
    echo "Installing category: $FILTER"
    for skill in "$SOURCE_DIR/$FILTER"/*/; do
        install_skill "$skill" || true
    done
elif [ -d "$SOURCE_DIR/$(dirname "$FILTER")/$(basename "$FILTER")" ]; then
    # Install specific skill
    echo "Installing skill: $FILTER"
    install_skill "$SOURCE_DIR/$FILTER"
else
    echo "Error: '$FILTER' not found in opencode/"
    echo ""
    echo "Available categories:"
    ls -1 "$SOURCE_DIR"
    exit 1
fi

echo ""
echo "Installation complete! Skills are now available in OpenCode."
echo "Restart OpenCode to load the new skills."
