---
name: elevenlabs-costs
description: Calculate ElevenLabs costs for the last X days. Use when the user asks about costs, expenses, credits consumed, or spending on ElevenLabs.
license: MIT
compatibility: opencode
metadata:
  category: elevenlabs
---

# Calculate ElevenLabs Costs

Calculate ElevenLabs conversation costs for the last `$ARGUMENTS` days.

## Recommended Method: Use the Script

```bash
python scripts/calculate-elevenlabs-costs.py $ARGUMENTS
```

**Examples:**
```bash
python scripts/calculate-elevenlabs-costs.py 7              # Last 7 days
python scripts/calculate-elevenlabs-costs.py 30 --detail    # With per-conversation detail
python scripts/calculate-elevenlabs-costs.py 7 --agent agent_XXX  # Single agent only
```

## Manual Process (if script fails)

### Step 1: Calculate Unix timestamps

```python
from datetime import datetime, timedelta
days = 7
now = datetime.now()
ts_max = int(now.timestamp())
ts_min = int((now - timedelta(days=days)).timestamp())
```

### Step 2: List conversations in range

```bash
ELEVENLABS_API_KEY=$(grep ELEVENLABS_API_KEY .env | cut -d'=' -f2)

curl -s "https://api.elevenlabs.io/v1/convai/conversations?page_size=100&start_time_unix_secs_min={ts_min}&start_time_unix_secs_max={ts_max}" \
  -H "xi-api-key: $ELEVENLABS_API_KEY"
```

### Step 3: Get costs for each conversation

```bash
curl -s "https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}" \
  -H "xi-api-key: $ELEVENLABS_API_KEY"
```

### Step 4: Sum totals

Accumulate: `metadata.cost`, `metadata.charging.call_charge`, `metadata.charging.llm_charge`, `metadata.charging.llm_price`, `metadata.call_duration_secs`

## Important Notes

- Conversation listing does NOT include costs, only basic metadata
- You MUST get details for each conversation to see costs
- Handle pagination if `has_more: true`
- Voice credits: ~750 credits/minute
