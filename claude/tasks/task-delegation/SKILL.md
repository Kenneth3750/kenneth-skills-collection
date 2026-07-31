---
name: task-delegation
description: Delegate tasks to subagents using structured TODO files. Only Build Lead.
---

# Task Delegation

Skill for delegating tasks to subagents in a structured and scoped way.

## What I Do

- Create specific TODO files for each delegated task
- Keep tasks small and focused
- Prevent subagents from deviating or doing too much
- Clean up completed TODOs

## When to Use

Use **always** when you're going to delegate a task to a subagent.

## Directory Structure

```
agents/
├── web-engineer/
│   └── todo/
│       └── 001-implement-audio-capture.md
├── app-engineer/
│   └── todo/
├── backend-engineer/
│   └── todo/
└── ...
```

## Mandatory Instructions

### 1. Before Delegating

1. Identify the correct subagent for the task
2. Divide the task into small and specific modules
3. Create the TODO file before launching the subagent

### 2. Create the TODO File

Location: `agents/<agent-name>/todo/<number>-<short-description>.md`

Format:
```markdown
# TODO: <Descriptive Title>

## Context
<2-3 lines of relevant context>

## Objective
<What it must achieve specifically>

## Tasks
- [ ] Specific task 1
- [ ] Specific task 2
- [ ] Specific task 3

## Relevant files
- `path/to/file1.ts` - Description
- `path/to/file2.ts` - Description

## Restrictions
- Don't modify X
- Maintain compatibility with Y
- Only touch files in Z/

## Completion criteria
<How to know it's ready>
```

### 3. Rules for TODOs

| Rule | Reason |
|------|--------|
| Max 3-5 tasks per TODO | Keeps scope limited |
| Specific tasks, not vague | "Create hook useX" not "Implement feature" |
| Include relevant files | The agent knows where to look |
| Include restrictions | Prevents touching what it shouldn't |
| One module at a time | Not "design the whole app" |

### 4. Delegate to the Subagent

When launching the subagent, indicate to follow its TODO:

```
You have an assigned TODO in agents/<agent>/todo/<file>.md
Read the TODO and complete the specified tasks.
Use the follow-todo skill to guide you.
```

### 5. After Completion

1. Verify that the tasks are fulfilled
2. **Delete the TODO file** to not accumulate
3. If there's more work, create a new TODO for the next iteration

## Example

To implement audio capture:

**BAD** (too broad):
```markdown
## Tasks
- [ ] Implement the entire audio recording system
- [ ] Make the UI
- [ ] Connect with Whisper
```

**GOOD** (scoped):
```markdown
# TODO: Create hook useAudioCapture

## Context
We need to capture audio from the microphone for real-time transcription.
We already have ONNX Runtime working with WebGPU/WASM.

## Objective
Create a hook that captures audio from the microphone using Web Audio API.

## Tasks
- [ ] Create `web/src/hooks/useAudioCapture.ts`
- [ ] Implement `startCapture()` that requests permissions and opens stream
- [ ] Implement `stopCapture()` that closes the stream
- [ ] Expose state: `isCapturing`, `error`, `audioContext`

## Relevant files
- `web/src/hooks/useOnnxRuntime.ts` - Existing hook pattern
- `web/src/App.tsx` - Where the hook will be used

## Restrictions
- Don't modify useOnnxRuntime.ts
- Don't integrate with VAD yet (will be another TODO)
- Only capture, no processing

## Completion criteria
- Hook exported and correctly typed
- Works in Chrome/Firefox/Edge
- Handles permission errors
```

## Access Restriction

> **IMPORTANT**: This skill is exclusive to the Build Lead (main session).
> Subagents do NOT use this skill - they use `follow-todo`.

## Output Checklist

- [ ] TODO created in `agents/<agent>/todo/`
- [ ] Specific and scoped tasks (max 3-5)
- [ ] Relevant files listed
- [ ] Clear restrictions
- [ ] Subagent launched with reference to the TODO
