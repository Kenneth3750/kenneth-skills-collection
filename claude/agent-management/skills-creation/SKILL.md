---
name: skills-creation
description: Create and maintain project skills. Use when you need to create, modify, or validate skills. Only Build Lead.
---

# Skills Creation

Create and maintain skills in the project, synchronized between OpenCode and Claude Code.

## What I Do

- Define the standard process for creating skills
- Ensure agents use appropriate skills
- Maintain format consistency, location, and permissions
- Sync skills between OpenCode and Claude Code

## When to Use

Use **only** when the user asks to create, modify, or validate project skills.

## Directory Structure

| Platform | Path |
|----------|------|
| Claude Code | `.claude/skills/<name>/SKILL.md` |
| OpenCode | `.opencode/skill/<name>/SKILL.md` |

## Mandatory Instructions

### 1. Create the Skill in Claude Code

Location: `.claude/skills/<name>/SKILL.md`

```yaml
---
name: skill-name
description: Clear description of what it does and when to use it (max 1024 chars)
---

# Skill Name

## What I Do
[Skill scope]

## When to Use
[Triggers]

## Mandatory Instructions
[Concrete steps]
```

### 2. Sync to OpenCode

Create the equivalent in `.opencode/skill/<name>/SKILL.md` with the same content.

### 3. Validations

- `name` must match the folder name
- Valid regex: `^[a-z0-9]+(-[a-z0-9]+)*$`
- Frontmatter must include `name` and `description`
- Description between 1-1024 characters

### 4. Optional Fields (Claude Code)

```yaml
---
name: skill-name
description: ...
allowed-tools: Read, Grep, Glob  # Optional: restrict tools
model: sonnet                     # Optional: specific model
---
```

### 5. Permissions

- Claude Code: Skills load automatically
- OpenCode: Update `opencode.json` if needed to expose to other agents

## Access Restriction

> **IMPORTANT**: This skill is exclusive to the Build Lead (main session).
> Subagents should NOT use this skill. If you are a subagent, ignore this skill
> and report to the Build Lead that you need a skill created.

## Output Checklist

- [ ] Skill created in `.claude/skills/<name>/SKILL.md`
- [ ] Skill synced in `.opencode/skill/<name>/SKILL.md`
- [ ] Valid frontmatter with name and description
- [ ] Folder name matches name field
- [ ] Clear and actionable instructions
- [ ] Permissions reviewed if applicable
