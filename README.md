# Kenneth's Skills Collection

A curated collection of reusable agent skills for **OpenCode** and **Claude Code**. Each skill is neutral, project-agnostic, and available in both platform formats.

## Skills Index

| Category | Description | Skills |
|----------|-------------|--------|
| [AWS](claude/aws/README.md) | AWS CLI, Cost Explorer, SAM deployments | 2 |
| [ElevenLabs](claude/elevenlabs/README.md) | ElevenLabs API, costs, conversation transcripts | 2 |
| [Document Generation](claude/doc-generation/README.md) | Generate and extract Word, Excel, and Office documents | 3 |
| [Agent Management](claude/agent-management/README.md) | Create and maintain agents, tools, and skills | 3 |
| [Sync](claude/sync/README.md) | Keep Claude Code and OpenCode configurations in sync | 1 |
| [Git](claude/git/README.md) | Commit conventions and git workflows | 1 |
| [Research](claude/research/README.md) | Web research with structured reports | 1 |
| [Wasmer](claude/wasmer/README.md) | Deploy static apps to Wasmer Edge | 1 |
| [Code Quality](claude/code-quality/README.md) | Code review guidelines and best practices | 1 |
| [Documentation](claude/docs/README.md) | Create and maintain project documentation | 1 |
| [Session Management](claude/session/README.md) | Document work progress in sessions | 1 |
| [Task Management](claude/tasks/README.md) | Structured task delegation and tracking | 2 |

**Total: 19 skills** across 12 categories.

## Installation

### Using npx (Recommended)

```bash
# Install all skills for Claude Code
npx kenneth-skills-collection install:claude

# Install all skills for OpenCode
npx kenneth-skills-collection install:opencode

# Install all skills for both platforms
npx kenneth-skills-collection install:all

# Install specific category
npx kenneth-skills-collection install:claude aws
npx kenneth-skills-collection install:opencode elevenlabs

# Install specific skill
npx kenneth-skills-collection install:claude aws/aws-costs
npx kenneth-skills-collection install:opencode elevenlabs/elevenlabs-conversation
npx kenneth-skills-collection install:all doc-generation/docx-generation
```

### Manual Installation

```bash
git clone https://github.com/Kenneth3750/kenneth-skills-collection.git
cd kenneth-skills-collection

# Install all skills
bash scripts/install-claude.sh
bash scripts/install-opencode.sh

# Install specific category
bash scripts/install-claude.sh aws
bash scripts/install-opencode.sh aws

# Install specific skill
bash scripts/install-claude.sh aws/aws-costs
bash scripts/install-opencode.sh aws/aws-costs

# Sync both platforms
bash scripts/sync-skills.sh                    # All skills
bash scripts/sync-skills.sh aws                # AWS category
bash scripts/sync-skills.sh aws/aws-costs      # Specific skill
```

## How It Works

Skills are organized by **tool/technology first**, then by action type:

```
claude/[category]/[skill-name]/SKILL.md
opencode/[category]/[skill-name]/SKILL.md
```

After installation, skills are copied to the correct platform paths:
- **Claude Code**: `.claude/skills/<skill-name>/SKILL.md`
- **OpenCode**: `.opencode/skills/<skill-name>/SKILL.md`

**Note**: Category READMEs are for documentation only and are not installed.

## Contributing

1. Create the skill in both `claude/<category>/<skill-name>/SKILL.md` and `opencode/<category>/<skill-name>/SKILL.md`
2. Follow the SKILL.md format with proper frontmatter
3. Keep skills generic and reusable (no project-specific references, no secrets)
4. Update the category README with the new skill
5. Submit a pull request

## License

MIT
