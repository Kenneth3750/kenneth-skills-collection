---
name: claude-md-writing
description: Create and update CLAUDE.md files for projects and subprojects. Use when you need to document context, commands, and conventions for Claude Code. Only Build Lead.
---

# CLAUDE.md Writing

Skill for creating consistent and useful CLAUDE.md files.

## What is CLAUDE.md

CLAUDE.md is the file that Claude Code reads automatically to understand:
- The context and purpose of the project
- Development commands
- Code conventions
- Project structure

## Instructions

1. Identify the scope (root or subdirectory)
2. Include the minimum required sections
3. Keep the content concise (max 1-2 screens)
4. Avoid duplicating info from parent CLAUDE.md

## Minimum Sections

### For Root CLAUDE.md
- Project description (2-3 lines)
- Monorepo/project structure
- Tech stack
- Main commands (dev, build, test, lint)
- General code rules

### For Subdirectory CLAUDE.md
- Subproject description
- Architecture/local structure
- Specific commands
- Conventions that differ from parent
- Key dependencies

## Rules

- If commands are not defined, mark as `TBD`
- Don't invent commands that don't exist
- Prioritize clarity over completeness
- Use simple Markdown format

## Access Restriction

> **IMPORTANT**: This skill is exclusive to the Build Lead (main session).
> Subagents should NOT create or modify CLAUDE.md files directly.
> If you need changes to CLAUDE.md, report to the Build Lead.

## Output Checklist

- [ ] CLAUDE.md created in the correct path
- [ ] Commands clear or marked as TBD
- [ ] No redundancies with parent CLAUDE.md
- [ ] Concise and useful content
