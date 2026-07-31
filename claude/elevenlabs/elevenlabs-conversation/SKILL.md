---
name: elevenlabs-conversation
description: Get the full transcript of an ElevenLabs conversation by its ID. Use when the user asks to view a conversation, transcript, or analyze an ElevenLabs call.
argument-hint: [conversation_id]
allowed-tools: Bash(python:*), Bash(curl:*), Read
---

# Get ElevenLabs Conversation

Get the transcript and details of conversation `$ARGUMENTS`.

## Process (follow exactly)

1. **Read API key from .env** (NEVER check if it exists, always read directly):
   ```bash
   ELEVENLABS_API_KEY=$(grep ELEVENLABS_API_KEY .env | cut -d'=' -f2)
   ```

2. **Make GET to endpoint**:
   ```
   GET https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}
   Header: xi-api-key: {API_KEY}
   ```

3. **Full curl command**:
   ```bash
   curl -s "https://api.elevenlabs.io/v1/convai/conversations/$ARGUMENTS" \
     -H "xi-api-key: $(grep ELEVENLABS_API_KEY .env | cut -d'=' -f2)"
   ```

## Response Structure

```json
{
  "conversation_id": "conv_...",
  "agent_id": "agent_...",
  "status": "done",
  "transcript": [
    {
      "role": "agent" | "user",
      "message": "Message text",
      "time_in_call_secs": 0,
      "tool_calls": [],
      "tool_results": []
    }
  ],
  "metadata": {
    "call_duration_secs": 338,
    "cost": 1654,
    "charging": {
      "call_charge": 1567,
      "llm_charge": 87
    }
  },
  "analysis": {
    "call_successful": "success",
    "transcript_summary": "..."
  }
}
```

## Important Transcript Fields

| Field | Description |
|-------|-------------|
| `role` | "agent" or "user" |
| `message` | Message text (null if tool call) |
| `time_in_call_secs` | Seconds from call start |
| `tool_calls` | Invoked tools |
| `tool_results` | Tool results |

## Common Errors

- **404**: conversation_id doesn't exist or is misspelled
- **401**: Incorrect API key or not included
- **NEVER** check if the environment variable is set - always read from .env directly
