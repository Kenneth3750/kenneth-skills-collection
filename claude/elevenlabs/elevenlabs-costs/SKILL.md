---
name: elevenlabs-costs
description: Calculate ElevenLabs costs for the last X days. Use when the user asks about costs, expenses, credits consumed, or spending on ElevenLabs.
argument-hint: [days] [--detail] [--agent agent_id]
allowed-tools: Bash(python:*), Bash(curl:*), Read
---

# Calculate ElevenLabs Costs

Calculate ElevenLabs conversation costs for the last `$ARGUMENTS` days.

## Recommended Method: Use the Script

```bash
python ${CLAUDE_SKILL_DIR}/scripts/calculate-costs.py $ARGUMENTS
```

**Examples:**
```bash
python ${CLAUDE_SKILL_DIR}/scripts/calculate-costs.py 7              # Last 7 days
python ${CLAUDE_SKILL_DIR}/scripts/calculate-costs.py 30 --detail    # With per-conversation detail
python ${CLAUDE_SKILL_DIR}/scripts/calculate-costs.py 7 --agent agent_XXX  # Single agent only
```

## Manual Process (if script fails)

### Step 1: Calculate Unix timestamps

```python
from datetime import datetime, timedelta
days = 7  # Change as needed
now = datetime.now()
ts_max = int(now.timestamp())
ts_min = int((now - timedelta(days=days)).timestamp())
print(f"Min: {ts_min}, Max: {ts_max}")
```

### Step 2: List conversations in range

```bash
ELEVENLABS_API_KEY=$(grep ELEVENLABS_API_KEY .env | cut -d'=' -f2)

curl -s "https://api.elevenlabs.io/v1/convai/conversations?page_size=100&start_time_unix_secs_min={ts_min}&start_time_unix_secs_max={ts_max}" \
  -H "xi-api-key: $ELEVENLABS_API_KEY"
```

**Endpoint parameters:**
| Parameter | Description |
|-----------|-------------|
| `page_size` | Max 100 |
| `start_time_unix_secs_min` | Minimum Unix timestamp |
| `start_time_unix_secs_max` | Maximum Unix timestamp |
| `agent_id` | Filter by agent (optional) |
| `cursor` | For pagination |

**Response:** List of conversations WITHOUT costs (only basic metadata)

### Step 3: Get costs for each conversation

For EACH conversation_id from the list:

```bash
curl -s "https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}" \
  -H "xi-api-key: $ELEVENLABS_API_KEY"
```

**Cost fields in response:**
```json
{
  "metadata": {
    "cost": 1654,                    // Total in credits
    "call_duration_secs": 338,
    "charging": {
      "call_charge": 1567,           // Voice credits
      "llm_charge": 87,              // LLM credits
      "llm_price": 0.014298          // USD spent on LLM
    }
  }
}
```

### Step 4: Sum totals

Accumulate for each conversation:
- `metadata.cost` → Total credits
- `metadata.charging.call_charge` → Voice credits
- `metadata.charging.llm_charge` → LLM credits
- `metadata.charging.llm_price` → USD spent on LLM
- `metadata.call_duration_secs` → Total duration

## Important Notes

- Conversation listing does NOT include costs, only basic metadata
- You MUST get details for each conversation to see costs
- API is ordered by date descending (most recent first)
- Handle pagination if `has_more: true`
- Voice credits are calculated: ~750 credits/minute
- LLM cost varies by model used
