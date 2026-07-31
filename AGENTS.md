# AGENTS.md - Kenneth's Skills Collection

This file tells AI agents how this repository works and what rules to follow when making changes.

## What This Repo Is

A public, curated collection of **reusable agent skills** for [OpenCode](https://opencode.ai) and [Claude Code](https://code.claude.com). Each skill is a `SKILL.md` file that gives an AI agent instructions for a specific task.

Skills in this repo must be **completely generic** — no API keys, no project-specific IDs, no company names, no secrets. They must work in any codebase where the skill is relevant.

## Repository Structure

```
kenneth-skills-collection/
├── README.md                    # Main index with links to each category
├── AGENTS.md                    # This file — rules for AI agents
├── CONTRIBUTING.md              # Rules for human contributors
├── package.json                 # npm/npx entry point for installation
├── index.js                     # CLI for installing skills
├── scripts/                     # Installation scripts
│   ├── install-claude.sh
│   ├── install-opencode.sh
│   └── sync-skills.sh
├── claude/                      # Skills in Claude Code format
│   └── [category]/
│       ├── README.md            # Category documentation (NOT installed)
│       └── [skill-name]/
│           ├── SKILL.md         # The actual skill
│           └── scripts/         # Optional: scripts referenced by the skill
│               └── *.py, *.sh, etc.
└── opencode/                    # Skills in OpenCode format
    └── [category]/
        └── [skill-name]/
            ├── SKILL.md         # The actual skill (OpenCode frontmatter)
            └── scripts/         # Optional: scripts referenced by the skill
                └── *.py, *.sh, etc.
```

### Skill Directory Structure

Each skill must follow this structure:

```
[skill-name]/
├── SKILL.md              # Required: skill instructions
└── scripts/              # Optional: if the skill references scripts
    ├── calculate-costs.py
    └── other-script.sh
```

**Important rules for scripts:**
- Scripts MUST be placed in a `scripts/` subdirectory inside the skill folder
- Reference scripts in SKILL.md using platform-specific variables:
  - Claude Code: `${CLAUDE_SKILL_DIR}/scripts/script-name.py`
  - OpenCode: `${SKILL_DIR}/scripts/script-name.py`
- The installation scripts will automatically copy the `scripts/` directory
- Keep scripts generic and neutral (no hardcoded paths, no secrets)

## Categories

Skills are organized by **tool or technology first**, then by action type. Each category is a folder inside `claude/` and `opencode/`.

Current categories: `aws`, `elevenlabs`, `doc-generation`, `agent-management`, `sync`, `git`, `research`, `wasmer`, `code-quality`, `docs`, `session`, `tasks`.

Each category has a `README.md` inside `claude/[category]/` that lists and describes every skill in that category. **Category READMEs are documentation only — they are NOT installed into user projects.**

## Rules for AI Agents

### 1. Every Skill Must Exist in Both Platforms

When you create, modify, or delete a skill, you **must** do it in **both** `claude/` and `opencode/`:

```
claude/[category]/[skill-name]/SKILL.md      ← Claude Code format
opencode/[category]/[skill-name]/SKILL.md    ← OpenCode format
```

The content is the same. Only the YAML frontmatter differs:

**Claude Code frontmatter:**
```yaml
---
name: skill-name
description: What this skill does and when to use it.
---
```

**OpenCode frontmatter:**
```yaml
---
name: skill-name
description: What this skill does and when to use it.
license: MIT
compatibility: opencode
metadata:
  category: category-name
---
```

### 2. Everything Must Be in English

All content in this repo must be written in **English** — skill content, descriptions, commit messages, PR descriptions, comments, everything. The only exception is if the user explicitly asks for another language.

### 3. Every Skill Must Be Completely Generic

This is the most important rule. A skill must work in **any** project, not just a specific one.

**NOT generic (bad):**
```markdown
# Deploy to AWS
Deploy changes to the my-project Lambda function.
cd "C:\Users\john\my-project" && sam deploy
The stack name is my-project-voice-agent.
```

**Generic (good):**
```markdown
# Deploy to AWS with SAM
Deploy project changes to AWS Lambda.
export AWS_ACCESS_KEY_ID=$(grep AWS_ACCESS_KEY_ID .env | cut -d'=' -f2) && \
sam build && sam deploy --no-execute-changeset
```

**NOT generic (bad):**
```markdown
# Get ElevenLabs Conversation
Get the transcript of conversation conv_xyz789 from the my-agent agent.
Use the script at agents/elevenlabs/scripts/get-conversation.py
```

**Generic (good):**
```markdown
# Get ElevenLabs Conversation
Get the full transcript of an ElevenLabs conversation by its ID.
curl -s "https://api.elevenlabs.io/v1/convai/conversations/$ARGUMENTS" \
  -H "xi-api-key: $(grep ELEVENLABS_API_KEY .env | cut -d'=' -f2)"
```

**NOT generic (bad):**
```markdown
# Commit
Separate changes by monorepo section: web/, backend/, app/.
Use the my-project commit conventions.
```

**Generic (good):**
```markdown
# Commit
Separate changes by monorepo section (web, backend, app, etc.).
Format: <type>(<area>): <imperative description>
```

**Checklist for generic skills:**
- [ ] No API keys, tokens, or credentials
- [ ] No hardcoded project names, company names, or person names
- [ ] No hardcoded file paths specific to one machine or project
- [ ] No hardcoded resource IDs (AWS stack names, agent IDs, etc.)
- [ ] No references to specific repos or organizations
- [ ] Works in any codebase where the skill is relevant

### 4. Always Update the Category README

When you add, remove, or significantly change a skill, you **must** update the `claude/[category]/README.md` to keep the skill listing accurate.

The category README has this format:

```markdown
# [Category Name] Skills

[Brief description of the category]

## Available Skills

| Skill | Description |
|-------|-------------|
| [skill-name](skill-name/SKILL.md) | One-line description of what the skill does. |
```

### 5. Update the Main README Count

If you add or remove a skill, update the skill count in the main `README.md` table.

### 6. Commit Messages

Use the format: `type(category): description`

Examples:
```
feat(aws): add s3-bucket-management skill
fix(elevenlabs): remove hardcoded agent ID from conversation skill
docs(agent-management): update agents-creation with new model mappings
refactor(doc-generation): simplify docx-generation examples
```

## Workflow: Adding a New Skill

1. Decide which category the skill belongs to (or create a new one)
2. Create `claude/[category]/[skill-name]/SKILL.md` with Claude Code frontmatter
3. Create `opencode/[category]/[skill-name]/SKILL.md` with OpenCode frontmatter
4. Make sure the skill is completely generic (check the checklist above)
5. Write everything in English
6. Update `claude/[category]/README.md` with the new skill entry
7. Update the skill count in the main `README.md`
8. Commit with a descriptive message

## Workflow: Modifying a Skill

1. Edit the skill in **both** `claude/` and `opencode/`
2. Ensure it remains completely generic
3. If the skill's purpose or description changed, update `claude/[category]/README.md`
4. Commit with a descriptive message

## Workflow: Deleting a Skill

1. Delete the skill folder from **both** `claude/` and `opencode/`
2. Remove the skill entry from `claude/[category]/README.md`
3. Update the skill count in the main `README.md`
4. Commit with a descriptive message

## Workflow: Creating a New Category

1. Create the folder in both `claude/[category]/` and `opencode/[category]/`
2. Create `claude/[category]/README.md` with the category description and skill table
3. Add the category to the main `README.md` index table
4. Add skills to the new category following the standard workflow
