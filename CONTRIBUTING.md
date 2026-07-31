# Contributing to Kenneth's Skills Collection

Thank you for your interest in contributing! This repo is a curated collection of reusable agent skills for [OpenCode](https://opencode.ai) and [Claude Code](https://code.claude.com).

## What Is a Skill?

A skill is a `SKILL.md` file that gives an AI agent instructions for a specific task. Skills are discovered automatically by both OpenCode and Claude Code when placed in the correct directories.

## Rules

### 1. Skills Must Be Completely Generic

This is the most important rule. A skill must work in **any** project, not just yours.

**Do NOT include:**
- API keys, tokens, or credentials
- Hardcoded project names, company names, or person names
- Hardcoded file paths specific to one machine or project
- Hardcoded resource IDs (AWS stack names, agent IDs, conversation IDs, etc.)
- References to specific repos or organizations

**Do include:**
- Generic code examples that work with environment variables
- Clear instructions that any developer can follow
- Error handling and common troubleshooting tips

### 2. Everything in English

All content must be in English — skill content, descriptions, commit messages, PR descriptions, and comments.

### 3. Both Platforms Required

Every skill must exist in **both** `claude/` and `opencode/` directories with the appropriate frontmatter for each platform.

### 4. Keep Category READMEs Updated

When you add, remove, or significantly change a skill, update the `claude/[category]/README.md`.

## How to Add a Skill

### Step 1: Choose or Create a Category

Categories are organized by tool/technology. Current categories:

| Category | What Goes Here |
|----------|---------------|
| `aws` | AWS CLI, services, deployments |
| `elevenlabs` | ElevenLabs API, voice AI |
| `doc-generation` | Word, Excel, Office document generation/extraction |
| `agent-management` | Creating agents, tools, and skills |
| `sync` | Claude Code ↔ OpenCode synchronization |
| `git` | Commit conventions, git workflows |
| `research` | Web research, knowledge synthesis |
| `wasmer` | Wasmer Edge deployments |
| `code-quality` | Code review, linting, best practices |
| `docs` | Project documentation (CLAUDE.md, README, etc.) |
| `session` | Work session tracking |
| `tasks` | Task delegation and tracking |

If your skill doesn't fit an existing category, create a new one.

### Step 2: Create the Skill Files

**Directory structure:**

```
[skill-name]/
├── SKILL.md              # Required: skill instructions
└── scripts/              # Optional: if the skill references scripts
    ├── calculate-costs.py
    └── other-script.sh
```

**Important:** If your skill includes scripts, they MUST go in a `scripts/` subdirectory. Never place scripts at the same level as SKILL.md.

**Claude Code format** (`claude/[category]/[skill-name]/SKILL.md`):

```yaml
---
name: skill-name
description: What this skill does and when to use it.
---

# Skill Title

## Instructions
[Clear, step-by-step guidance]

## When to Use
[Triggers and use cases]
```

**OpenCode format** (`opencode/[category]/[skill-name]/SKILL.md`):

```yaml
---
name: skill-name
description: What this skill does and when to use it.
license: MIT
compatibility: opencode
metadata:
  category: category-name
---

# Skill Title

## Instructions
[Same content as Claude Code version]

## When to Use
[Same triggers and use cases]
```

### Step 3: Update Documentation

1. Add the skill to `claude/[category]/README.md`
2. Update the skill count in the main `README.md`

### Step 4: Submit a PR

Use a descriptive commit message: `feat(category): add skill-name skill`

## Skill Name Rules

- Lowercase alphanumeric with single hyphens: `^[a-z0-9]+(-[a-z0-9]+)*$`
- 1-64 characters
- Must match the folder name
- Must be descriptive: `aws-costs` not `costs`

## Scripts in Skills

If your skill includes scripts (Python, Bash, etc.):

1. **Always place scripts in a `scripts/` subdirectory:**
   ```
   my-skill/
   ├── SKILL.md
   └── scripts/
       └── my-script.py
   ```

2. **Reference scripts in SKILL.md using platform-specific variables:**
   ```markdown
   ## Usage

   ```bash
   # For Claude Code
   python ${CLAUDE_SKILL_DIR}/scripts/my-script.py $ARGUMENTS

   # For OpenCode
   python ${SKILL_DIR}/scripts/my-script.py $ARGUMENTS
   ```
   ```

   Each platform has its own variable for the skill directory. Make sure to use the correct one in each version.

3. **Keep scripts neutral:**
   - No hardcoded paths specific to your machine
   - No project-specific names or IDs
   - Use environment variables for credentials
   - Search for `.env` file dynamically (go up directory tree)

4. **The installation scripts will automatically copy the `scripts/` directory** when users install your skill.

## Examples

### Good Skill (Generic)

```markdown
---
name: aws-costs
description: Calculate AWS costs for the last X days using Cost Explorer.
---

# Calculate AWS Costs

## Process
1. Read API key from .env
2. Query Cost Explorer API
3. Sum costs by service

```bash
export AWS_ACCESS_KEY_ID=$(grep AWS_ACCESS_KEY_ID .env | cut -d'=' -f2) && \
aws ce get-cost-and-usage \
  --time-period Start=$(date -d '30 days ago' +%Y-%m-%d),End=$(date +%Y-%m-%d) \
  --granularity MONTHLY \
  --metrics "UnblendedCost" \
  --group-by Type=DIMENSION,Key=SERVICE
```
```

### Bad Skill (Not Generic)

```markdown
---
name: aws-costs
description: Calculate AWS costs for the my-project project.
---

# Calculate AWS Costs for My Project

Deploy changes to the my-project Lambda function.
cd "C:\Users\john\my-project" && sam deploy
The stack name is my-project-stack.
Budget is $5/month.
```

## Questions?

Open an issue or check the [AGENTS.md](AGENTS.md) for detailed agent instructions.
