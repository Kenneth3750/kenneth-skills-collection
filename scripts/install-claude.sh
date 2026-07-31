#!/bin/bash

# Install skills for Claude Code
# Usage:
#   install-claude.sh                    # Install all skills
#   install-claude.sh aws                # Install all skills from aws category
#   install-claude.sh aws/aws-costs      # Install specific skill

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
SOURCE_DIR="$REPO_DIR/claude"
TARGET_DIR=".claude/skills"

FILTER="${1:-}"

install_skill() {
    local skill_path="$1"
    local skill_name=$(basename "$skill_path")
    local target="$TARGET_DIR/$skill_name"
    
    if [ -f "$skill_path/SKILL.md" ]; then
        mkdir -p "$target"
        cp "$skill_path/SKILL.md" "$target/SKILL.md"
        echo "  ✓ Installed: $skill_name"
        
        # Copy scripts/ directory if it exists
        if [ -d "$skill_path/scripts" ]; then
            mkdir -p "$target/scripts"
            cp -r "$skill_path/scripts/"* "$target/scripts/"
            echo "    ✓ Copied: scripts/"
        fi
        
        return 0
    fi
    return 1
}

echo "Installing skills for Claude Code..."
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
    echo "Error: '$FILTER' not found in claude/"
    echo ""
    echo "Available categories:"
    ls -1 "$SOURCE_DIR" | grep -v README.md
    exit 1
fi

echo ""
echo "Installation complete! Skills are now available in Claude Code."
echo "Restart Claude Code to load the new skills."
