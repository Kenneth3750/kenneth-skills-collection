---
name: tools-creation
description: Create and maintain custom tools for the project. Use when you need to create, modify, or validate custom tools. Only Build Lead.
---

# Tools Creation

Create and maintain custom tools in the project.

## What I Do

- Standard for creating custom tools with per-agent logic
- Define how to create scripts and wrappers
- Ensure compatibility, correct names, and permissions
- Document differences between OpenCode and Claude Code

## When to Use

Use **only** when the user asks to create, modify, or validate custom tools.

## Directory Structure

### OpenCode
```
agents/<agent>/tools/        # Real logic (Python/bash)
.opencode/tool/              # JS/TS wrapper
```

### Claude Code
```
scripts/                     # Executable scripts
.claude/hooks/               # Hooks for validation (optional)
```

## Instructions for OpenCode

1. The **real logic** of the tool must live in `agents/<agent>/tools/` (Python or bash)
2. The **wrapper** is defined in JS/TS inside `.opencode/tool/` using `tool()`
3. The wrapper filename is the tool name
4. The wrapper must invoke the script and pass JSON payload via stdin
5. Document arguments with `tool.schema`

## Instructions for Claude Code

Claude Code doesn't have custom tools like OpenCode, but you can achieve similar effects with:

### 1. Executable Scripts

Create scripts in `scripts/` that Claude can invoke via Bash:

```bash
#!/bin/bash
# scripts/my-tool.sh
# Description: What this script does

INPUT="$1"
# logic here
echo "result"
```

### 2. Hooks (for validation)

Use hooks in settings.json or in agent frontmatter:

```yaml
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate.sh"
```

### 3. Skills as Alternative

For complex logic, create a skill that documents how to use scripts:

```yaml
---
name: my-tool
description: Execute my custom tool
---

To use this tool, run:
bash scripts/my-tool.sh <arguments>
```

## Access Restriction

> **IMPORTANT**: This skill is exclusive to the Build Lead (main session).
> Subagents should NOT use this skill. If you are a subagent, ignore this skill
> and report to the Build Lead that you need a tool created.

## Output Checklist

- [ ] Tool/script implemented in correct location
- [ ] Clear usage documentation
- [ ] Error handling implemented
- [ ] Execution permissions configured (chmod +x)
- [ ] Synchronized between platforms if applicable
