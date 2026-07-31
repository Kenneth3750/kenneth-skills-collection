#!/usr/bin/env python3
"""
Calculate ElevenLabs conversation costs for a range of days.

Usage:
    python calculate-costs.py <days>
    python calculate-costs.py <days> --detail
    python calculate-costs.py <days> --agent <agent_id>

Examples:
    python calculate-costs.py 7           # Last 7 days
    python calculate-costs.py 30 --detail # Last 30 days with detail
    python calculate-costs.py 7 --agent agent_xyz123  # Single agent only
"""

import sys
import json
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict

# Find project root (where .env is located)
script_dir = Path(__file__).resolve().parent

# Try to find .env by going up the directory tree
env_path = None
current = script_dir
for _ in range(10):  # Max 10 levels up
    test_path = current / ".env"
    if test_path.exists():
        env_path = test_path
        break
    current = current.parent

if not env_path:
    print("Error: .env file not found. Please create it with ELEVENLABS_API_KEY.")
    sys.exit(1)

# Read API key from .env
api_key = None

with open(env_path, "r") as f:
    for line in f:
        if line.startswith("ELEVENLABS_API_KEY="):
            api_key = line.strip().split("=", 1)[1]
            break

if not api_key:
    print("Error: ELEVENLABS_API_KEY not found in .env")
    sys.exit(1)

# Parse arguments
if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

try:
    days = int(sys.argv[1])
except ValueError:
    print(f"Error: '{sys.argv[1]}' is not a valid number of days")
    sys.exit(1)

show_detail = "--detail" in sys.argv
agent_filter = None
if "--agent" in sys.argv:
    idx = sys.argv.index("--agent")
    if idx + 1 < len(sys.argv):
        agent_filter = sys.argv[idx + 1]

# Calculate date range (Unix timestamps)
now = datetime.now()
end_date = now
start_date = now - timedelta(days=days)

ts_min = int(start_date.timestamp())
ts_max = int(end_date.timestamp())

print(f"=== ElevenLabs Costs - Last {days} days ===")
print(f"From: {start_date.strftime('%Y-%m-%d %H:%M')}")
print(f"To: {end_date.strftime('%Y-%m-%d %H:%M')}")
if agent_filter:
    print(f"Agent: {agent_filter}")
print()

def api_get(endpoint):
    """Make GET request to ElevenLabs API."""
    url = f"https://api.elevenlabs.io/v1{endpoint}"
    req = urllib.request.Request(url, headers={"xi-api-key": api_key})
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except urllib.error.HTTPError as e:
        print(f"API Error {e.code}: {e.reason}")
        return None

# Step 1: List all conversations in the range
print("Getting conversation list...")
conversations = []
cursor = None
page = 0

while True:
    page += 1
    url = f"/convai/conversations?page_size=100&start_time_unix_secs_min={ts_min}&start_time_unix_secs_max={ts_max}"
    if agent_filter:
        url += f"&agent_id={agent_filter}"
    if cursor:
        url += f"&cursor={cursor}"

    data = api_get(url)
    if not data:
        break

    conversations.extend(data.get("conversations", []))
    print(f"  Page {page}: {len(data.get('conversations', []))} conversations")

    if not data.get("has_more"):
        break
    cursor = data.get("next_cursor")

print(f"\nTotal conversations found: {len(conversations)}")

if not conversations:
    print("No conversations in this period.")
    sys.exit(0)

# Step 2: Get costs for each conversation
print("\nGetting detailed costs...")

totals = {
    "credits": 0,
    "voice_credits": 0,
    "llm_credits": 0,
    "llm_usd": 0.0,
    "duration_secs": 0,
    "successful": 0,
    "failed": 0
}

by_agent = defaultdict(lambda: {
    "name": "",
    "credits": 0,
    "duration_secs": 0,
    "conversations": 0
})

details = []

for i, conv in enumerate(conversations):
    conv_id = conv["conversation_id"]

    # Get detail with costs
    detail = api_get(f"/convai/conversations/{conv_id}")
    if not detail:
        continue

    metadata = detail.get("metadata", {})
    charging = metadata.get("charging", {})

    cost = metadata.get("cost", 0)
    voice = charging.get("call_charge", 0)
    llm = charging.get("llm_charge", 0)
    llm_usd = charging.get("llm_price", 0)
    duration = metadata.get("call_duration_secs", 0)

    # Accumulate totals
    totals["credits"] += cost
    totals["voice_credits"] += voice
    totals["llm_credits"] += llm
    totals["llm_usd"] += llm_usd
    totals["duration_secs"] += duration

    if conv.get("call_successful") == "success":
        totals["successful"] += 1
    else:
        totals["failed"] += 1

    # Accumulate by agent
    agent_id = conv["agent_id"]
    by_agent[agent_id]["name"] = conv.get("agent_name", agent_id)
    by_agent[agent_id]["credits"] += cost
    by_agent[agent_id]["duration_secs"] += duration
    by_agent[agent_id]["conversations"] += 1

    # Save detail if requested
    if show_detail:
        date = datetime.fromtimestamp(conv["start_time_unix_secs"])
        details.append({
            "date": date.strftime("%Y-%m-%d %H:%M"),
            "agent": conv.get("agent_name", "")[:30],
            "duration": duration,
            "credits": cost,
            "status": conv.get("call_successful", "?")
        })

    # Show progress
    if (i + 1) % 10 == 0:
        print(f"  Processed: {i + 1}/{len(conversations)}")

print(f"  Processed: {len(conversations)}/{len(conversations)}")

# Show results
print("\n" + "=" * 50)
print("COST SUMMARY")
print("=" * 50)

duration_min = totals["duration_secs"] / 60
print(f"\nConversations: {len(conversations)} ({totals['successful']} successful, {totals['failed']} failed)")
print(f"Total duration: {duration_min:.1f} minutes ({totals['duration_secs']} seconds)")

print(f"\n--- Credits ---")
print(f"Voice: {totals['voice_credits']:,} credits")
print(f"LLM:   {totals['llm_credits']:,} credits (${totals['llm_usd']:.4f} USD)")
print(f"TOTAL: {totals['credits']:,} credits")

# Average cost per minute
if duration_min > 0:
    cred_per_min = totals["credits"] / duration_min
    print(f"\nAverage cost: {cred_per_min:.0f} credits/minute")

# By agent
if len(by_agent) > 1:
    print(f"\n--- By Agent ---")
    for agent_id, stats in sorted(by_agent.items(), key=lambda x: -x[1]["credits"]):
        mins = stats["duration_secs"] / 60
        print(f"{stats['name'][:40]}")
        print(f"  {stats['conversations']} conv, {mins:.1f} min, {stats['credits']:,} cred")

# Detail if requested
if show_detail and details:
    print(f"\n--- Conversation Details ---")
    print(f"{'Date':<16} {'Agent':<32} {'Dur':>5} {'Cred':>7} {'Status':<8}")
    print("-" * 75)
    for d in details:
        print(f"{d['date']:<16} {d['agent']:<32} {d['duration']:>5} {d['credits']:>7} {d['status']:<8}")

print()
