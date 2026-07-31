---
name: commit
description: Create consistent commits with structured title scheme. Separate changes by monorepo section (web, backend, app). Use for all project commits.
license: MIT
compatibility: opencode
metadata:
  category: git
---

# Commit

Skill for creating consistent, navigable commits separated by monorepo section.

## What I Do

- Define title and description scheme for commits
- Separate changes by monorepo section (never mix web + backend)
- Create atomic and focused commits
- Facilitate git history navigation

## When to Use

Use **always** when the user asks to commit changes.

## Commit Scheme

### Title Format

```
<type>(<area>): <imperative description>
```

**Maximum 72 characters** in the title.

### Allowed Types

| Type | Use |
|------|-----|
| `feat` | New functionality |
| `fix` | Bug fix |
| `refactor` | Code change without changing behavior |
| `style` | Format changes, CSS, visual styles |
| `docs` | Documentation |
| `chore` | Maintenance, configs, dependencies |
| `test` | Tests |
| `perf` | Performance improvements |

### Monorepo Areas

| Area | Folder | Description |
|------|---------|-------------|
| `web` | `web/` | PWA React + Vite |
| `app` | `app/` | Mobile app |
| `backend` | `backend/` | APIs and services |
| `docs` | `docs/` | Project documentation |
| `infra` | `scripts/`, `.github/` | CI/CD, scripts, infra |
| `root` | Root | Global configs (root package.json, CLAUDE.md) |

### Title Examples

```
feat(web): add file transcription with drag-and-drop
fix(web): resolve model loading state not updating
refactor(web): extract download utilities to separate module
docs: add session notes for VAD implementation
chore(web): update @huggingface/transformers to 3.5
```

## Mandatory Instructions

### 1. Analyze Pending Changes

```bash
git status
git diff --stat
```

### 2. Group by Area

Identify which files belong to each area:
- `web/*` → area `web`
- `backend/*` → area `backend`
- `docs/*` → area `docs`
- Root files → area `root`

### 3. Create Separate Commits by Area

**CRITICAL RULE**: Never combine changes from different areas in the same commit.

### 4. Atomic Commits

Within the same area, if there are very different changes, separate them.

### 5. Commit Description (body)

Only if the title is not enough.

### 6. Commit Order

When there are multiple commits, order by logical dependency:
1. Infrastructure/config changes first
2. Then base code changes (hooks, utils)
3. Then components that use those changes
4. Documentation last

## Strict Rules

| Rule | Reason |
|------|--------|
| Don't mix areas | Facilitates revert and cherry-pick |
| Imperative title | "add" not "added" or "adding" |
| Title in English | Consistency with git conventions |
| Max 72 chars in title | Readability in git log |
| One commit = one logical change | Atomic commits |
| No empty commits | If no real changes, don't commit |

## Output Checklist

- [ ] Changes grouped by monorepo area
- [ ] Title follows `type(area): description` format
- [ ] Title in imperative and English
- [ ] Title <= 72 characters
- [ ] No area mixing in a commit
- [ ] Commits in logical dependency order
