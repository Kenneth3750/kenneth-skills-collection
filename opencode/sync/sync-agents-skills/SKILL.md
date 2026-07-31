---
name: sync-agents-skills
description: Keep agents and skills synchronized between OpenCode and Claude Code. Use when creating, modifying, or syncing configurations between both platforms.
license: MIT
compatibility: opencode
metadata:
  category: sync
---

# Sync Agents & Skills

Keep agents and skills synchronized between OpenCode and Claude Code.

## File Paths

| Type | OpenCode | Claude Code |
|------|----------|-------------|
| Agents | `.opencode/agent/*.md` | `.claude/agents/*.md` |
| Skills | `.opencode/skill/*/SKILL.md` | `.claude/skills/*/SKILL.md` |

## Agent Field Mapping

### OpenCode -> Claude Code

```yaml
# OpenCode (.opencode/agent/example.md)
---
description: Agent description
mode: primary | subagent
model: openai/gpt-5.2-codex | openai/o3 | openai/o4-mini
temperature: 0.2
tools:
  write: true
  edit: true
  bash: true
  webfetch: true
  skill: true
permission:
  skill:
    deep-research: allow
---
[prompt content]
```

Converts to:

```yaml
# Claude Code (.claude/agents/example.md)
---
name: example
description: Agent description
model: opus | sonnet | haiku
tools: Write, Edit, Bash, WebFetch, WebSearch, Read, Glob, Grep
skills: deep-research
---
[prompt content]
```

### Model Conversion Rules

| OpenCode | Claude Code |
|----------|-------------|
| `openai/o3` | `opus` |
| `openai/gpt-5.2-codex` | `opus` |
| `openai/o4-mini` | `sonnet` |
| others | `sonnet` |

### Tool Conversion Rules

| OpenCode | Claude Code |
|----------|-------------|
| `write: true` | `Write` |
| `edit: true` | `Edit` |
| `bash: true` | `Bash` |
| `webfetch: true` | `WebFetch, WebSearch` |
| `skill: true` | (implicit) |

Always add in Claude Code: `Read, Glob, Grep`

### Claude Code -> OpenCode

```yaml
# Claude Code (.claude/agents/example.md)
---
name: example
description: Agent description
model: opus
tools: Read, Glob, Grep, WebSearch, WebFetch, Write, Edit, Bash
skills: deep-research
---
[prompt content]
```

Converts to:

```yaml
# OpenCode (.opencode/agent/example.md)
---
description: Agent description
mode: subagent
model: openai/gpt-5.2-codex
temperature: 0.2
tools:
  write: true
  edit: true
  bash: true
  webfetch: true
  skill: true
permission:
  skill:
    deep-research: allow
---
[prompt content]
```

## Skills Mapping

Skills have similar format in both platforms. Just ensure:
- File is in the correct path
- Frontmatter has `name` and `description`

## Usage Instructions

### Sync All (OpenCode -> Claude Code)

1. Read all agents in `.opencode/agent/*.md`
2. For each, create equivalent in `.claude/agents/`
3. Read all skills in `.opencode/skill/*/SKILL.md`
4. For each, create equivalent in `.claude/skills/*/SKILL.md`

### Sync All (Claude Code -> OpenCode)

1. Read all agents in `.claude/agents/*.md`
2. For each, create equivalent in `.opencode/agent/`
3. Read all skills in `.claude/skills/*/SKILL.md`
4. For each, create equivalent in `.opencode/skill/*/SKILL.md`

### When Creating a New Agent

1. Create the agent in the requested platform
2. Automatically create the equivalent in the other platform
3. Inform the user of both files created

### When Modifying an Existing Agent

1. Apply changes in the platform where it was edited
2. Propagate changes to the other platform
3. Inform the user of updated files

## Important Notes

- OpenCode `mode` field has no direct equivalent in Claude Code
- OpenCode `temperature` field has no equivalent in Claude Code
- Claude Code uses `name` in frontmatter, OpenCode infers it from filename
- Claude Code `allowed-tools` has no direct equivalent in OpenCode
