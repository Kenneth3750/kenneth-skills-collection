---
name: follow-todo
description: Follow the TODO assigned by the Build Lead. For all subagents.
license: MIT
compatibility: opencode
metadata:
  category: tasks
---

# Follow TODO

Skill for subagents to follow tasks delegated by the Build Lead.

## What I Do

- Read and follow the TODO assigned in my folder
- Complete only the specified tasks
- Respect the indicated restrictions
- Don't deviate from the defined scope

## When to Use

Use **always** when the Build Lead indicates you have an assigned TODO.

## TODO Location

Your TODO will be in: `agents/<your-role>/todo/<file>.md`

## Mandatory Instructions

### 1. Read the TODO

Before doing anything:

```
Read agents/<your-role>/todo/<file>.md
```

### 2. Understand the Scope

The TODO has important sections:

| Section | What to do |
|---------|-----------|
| Context | Understand the problem |
| Objective | This is what you must achieve |
| Tasks | Specific list of what to do |
| Relevant files | Read them first |
| Restrictions | **DO NOT violate these rules** |
| Completion criteria | How to know you're done |

### 3. Strict Rules

1. **Only do what the TODO says**
   - Don't add extra features
   - Don't refactor unrelated code
   - Don't "improve" things outside the scope

2. **Respect the restrictions**
   - If it says "don't modify X", don't touch it
   - If it says "only files in Y/", don't go outside

3. **One thing at a time**
   - Complete each task before moving to the next
   - If you find something that needs fixing but isn't in the TODO, report it at the end

4. **Don't extend**
   - If the TODO has 3 tasks, do 3 tasks
   - Don't add task 4 "because it makes sense"

### 4. During Implementation

For each task:

1. Read the mentioned relevant files
2. Implement only what's necessary
3. Verify it works
4. Mentally mark the task as completed

### 5. When Finished

Report to the Build Lead:

```
## TODO Completed: <TODO name>

### Tasks performed
- [x] Task 1 - Description of what I did
- [x] Task 2 - Description of what I did

### Files created/modified
- `path/to/file.ts` - What changed

### Notes
- Relevant observations
- Things I found but weren't in scope (if applicable)
```

## What NOT to Do

| DON'T | Reason |
|-------|--------|
| Add extra features | Goes outside scope, can break things |
| Refactor existing code | Wasn't in the TODO |
| "Improve" things along the way | Introduces unreviewed changes |
| Ignore restrictions | The Build Lead put them for a reason |
| Do more than requested | Saves tokens, avoids errors |

## Output Checklist

- [ ] Read the complete TODO before starting
- [ ] Completed ONLY the listed tasks
- [ ] Respected ALL restrictions
- [ ] Didn't add anything outside scope
- [ ] Reported the result to the Build Lead
