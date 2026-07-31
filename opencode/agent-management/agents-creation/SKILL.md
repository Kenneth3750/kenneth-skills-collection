---
name: agents-creation
description: Create and maintain project subagents. Use when you need to create, modify, or validate agents. Only Build Lead.
license: MIT
compatibility: opencode
metadata:
  category: agent-management
---

# Agents Creation

Create and maintain subagents in the project, synchronized between OpenCode and Claude Code.

## What I Do

- Standard for creating and adjusting subagents
- Ensures clear prompts, minimal permissions, and appropriate tools
- Synchronizes agents between OpenCode and Claude Code

## When to Use

Use **only** when the user asks to create, modify, or validate subagents.

## Directory Structure

| Platform | Path |
|----------|------|
| Claude Code | `.claude/agents/<name>.md` |
| OpenCode | `.opencode/agent/<name>.md` |

## Claude Code Format

```yaml
---
name: agent-name
description: Clear description of role and when to use it
model: opus | sonnet | haiku
tools: Read, Glob, Grep, WebSearch, WebFetch, Write, Edit, Bash
skills: skill1, skill2
---
# Agent Name
[Prompt with role instructions]
## Responsibilities
- ...
## Restrictions
- ...
```

## OpenCode Format

```yaml
---
description: Agent description
mode: primary | subagent
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
    skill-name: allow
---
[Prompt with role instructions]
```

## Field Mapping

### Model
| OpenCode | Claude Code |
|----------|-------------|
| `openai/o3` | `opus` |
| `openai/gpt-5.2-codex` | `opus` |
| `openai/o4-mini` | `sonnet` |
| others | `sonnet` |

### Tools
| OpenCode | Claude Code |
|----------|-------------|
| `write: true` | `Write` |
| `edit: true` | `Edit` |
| `bash: true` | `Bash` |
| `webfetch: true` | `WebFetch, WebSearch` |

Always add in Claude Code: `Read, Glob, Grep`

## Mandatory Instructions

### When Creating a New Agent
1. Define clear role and responsibilities
2. Create in Claude Code (`.claude/agents/<name>.md`)
3. Sync to OpenCode (`.opencode/agent/<name>.md`)
4. Enable only necessary tools
5. Assign relevant skills

### Validations
- Name in lowercase with hyphens: `^[a-z0-9]+(-[a-z0-9]+)*$`
- Description present and clear
- Minimum necessary tools (least privilege principle)
- Prompt with clear responsibilities and limits

### Security Restrictions
Subagents should **NOT** have access to: `skills-creation`, `tools-creation`, `agents-creation`

## Output Checklist
- [ ] Agent created in `.claude/agents/<name>.md`
- [ ] Agent synced in `.opencode/agent/<name>.md`
- [ ] Valid frontmatter with required fields
- [ ] Minimum necessary tools and permissions
- [ ] Prompt with clear responsibilities and limits
