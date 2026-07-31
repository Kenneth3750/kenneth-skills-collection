---
name: create-session
description: Create work sessions to document progress. Use when finishing a workday or important milestone.
---

# Create Session

Skill for creating and maintaining work sessions that document project progress.

## What I Do

- Create session files that document completed and pending work
- Maintain maximum 10 sessions per subproject (delete oldest if exceeded)
- Provide context to resume work in new workdays

## When to Use

Use this skill when:
- You finish a significant workday
- You complete an important milestone or feature
- You need to document the current state before pausing
- You want to leave context for the next session

## Session Location

Each subproject has its sessions folder:
- `web/sessions/` - Web subproject sessions
- `app/sessions/` - App subproject sessions (when exists)
- `backend/sessions/` - Backend sessions (when exists)

## Filename Format

```
session_XXX_short_description.md
```

- `XXX`: 3-digit sequential number (001, 002, ..., 999)
- `short_description`: snake_case, maximum 3-4 words

Examples:
- `session_001_realtime_transcription.md`
- `session_002_mobile_optimization.md`
- `session_003_file_upload.md`

## File Structure

```markdown
# Session XXX: Descriptive Title

**Date**: YYYY-MM-DD
**Approximate duration**: ~X hours
**Status**: Completed | In progress

---

## Summary

Brief paragraph (2-3 sentences) describing the objective and result.

---

## Completed

### Category 1
- [x] Completed task
- [x] Another completed task

### Category 2
- [x] More tasks...

---

## Pending

### Category
- [ ] Pending task
- [ ] Another pending task

---

## Key modified files

```
path/file1.ts  # Brief description
path/file2.tsx # Brief description
```

---

## Technical notes

Important observations, metrics, known limitations.

---

## Suggested next session

Numbered list of 2-4 priority items for the next session.
```

## Important Rules

### 10 Session Limit
- NEVER more than 10 sessions in a folder
- Before creating session_011, delete session_001
- Always check how many sessions exist before creating

### Maximum Length
- Maximum 200 lines per file
- Be concise but informative
- Prioritize that it's useful for resuming work

### Numbering
- Always use 3 digits (001, 002, etc.)
- Continue from highest existing number + 1
- If an old session is deleted, DO NOT reuse its number

## Process to Create Session

1. List existing sessions in the subproject folder
2. If there are 10 or more, delete the lowest numbered one
3. Determine next number (max existing + 1)
4. Create file following the structure
5. Verify it doesn't exceed 200 lines

## Usage Example

```bash
# View existing sessions
ls web/sessions/

# If there are 10, delete the oldest
rm web/sessions/session_001_*.md

# Create new session
# (use Write tool with the defined structure)
```
