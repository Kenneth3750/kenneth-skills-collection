---
name: commit
description: Create consistent commits with structured title scheme. Separate changes by monorepo section (web, backend, app). Use for all project commits.
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
style(web): improve mobile responsiveness for transcription
docs: add session notes for VAD implementation
chore(web): update @huggingface/transformers to 3.5
test(backend): add unit tests for auth middleware
perf(web): optimize audio chunking for large files
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

If there are changes in `web/` and `docs/`:
```bash
# First web
git add web/
git commit -m "feat(web): add metadata display to recording"

# Then docs
git add docs/
git commit -m "docs: update session with recording improvements"
```

### 4. Atomic Commits

Within the same area, if there are very different changes, separate them:

```bash
# Change 1: new component
git add web/src/components/RecordingResult.*
git commit -m "feat(web): add RecordingResult component"

# Change 2: update hook
git add web/src/hooks/useVADTranscription.ts
git commit -m "refactor(web): expose metadata in useVADTranscription"
```

### 5. Commit Description (body)

Only if the title is not enough. Format:

```
feat(web): add pause/resume controls to recording

- Add pause() and resume() methods to useVADTranscription
- Update UI with pause button that toggles state
- Show visual indicator when paused

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

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

## Typical Flow

```bash
# 1. Check status
git status

# 2. Check changes by file
git diff --stat

# 3. Mentally group by area and type

# 4. Commit in order
git add web/src/hooks/useVADTranscription.ts
git commit -m "refactor(web): add metadata tracking to VAD hook"

git add web/src/components/RecordingResult.tsx web/src/components/RecordingResult.css
git commit -m "feat(web): add RecordingResult component with download"

git add web/src/App.tsx
git commit -m "feat(web): integrate RecordingResult in main app"

git add docs/
git commit -m "docs: update web architecture in CLAUDE.md"
```

## Output Checklist

- [ ] Changes grouped by monorepo area
- [ ] Title follows `type(area): description` format
- [ ] Title in imperative and English
- [ ] Title <= 72 characters
- [ ] No area mixing in a commit
- [ ] Commits in logical dependency order
