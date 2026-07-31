#!/usr/bin/env python3
"""
Calculate AWS costs for a range of days.

Usage:
    python calculate-costs.py <days>
    python calculate-costs.py <days> --daily
    python calculate-costs.py <days> --budget <amount>

Examples:
    python calculate-costs.py 7        # Last 7 days (summary)
    python calculate-costs.py 30       # Last 30 days
    python calculate-costs.py 7 --daily # With daily breakdown
    python calculate-costs.py 30 --budget 10.0  # Custom budget alert
"""

import sys
import json
import subprocess
import os
from pathlib import Path
from datetime import datetime, timedelta

# Find project root (where .env is located)
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent.parent  # Start from scripts/.. and go up

# Try to find .env by going up the directory tree
env_path = None
current = script_dir
for _ in range(10):  # Max 10 levels up
    test_path = current / ".env"
    if test_path.exists():
        env_path = test_path
        project_root = current
        break
    current = current.parent

if not env_path:
    print("Error: .env file not found. Please create it with AWS credentials.")
    sys.exit(1)

# Read credentials from .env
credentials = {}

with open(env_path, "r") as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            credentials[key] = value

# Set environment variables for AWS CLI
os.environ["AWS_ACCESS_KEY_ID"] = credentials.get("AWS_ACCESS_KEY_ID", "")
os.environ["AWS_SECRET_ACCESS_KEY"] = credentials.get("AWS_SECRET_ACCESS_KEY", "")
os.environ["AWS_DEFAULT_REGION"] = credentials.get("AWS_DEFAULT_REGION", "us-east-1")

# Parse arguments
if len(sys.argv) < 2:
    print(__doc__)
    sys.exit(1)

try:
    days = int(sys.argv[1])
except ValueError:
    print(f"Error: '{sys.argv[1]}' is not a valid number")
    sys.exit(1)

show_daily = "--daily" in sys.argv

# Parse budget argument
budget = 5.0  # Default budget
if "--budget" in sys.argv:
    idx = sys.argv.index("--budget")
    if idx + 1 < len(sys.argv):
        try:
            budget = float(sys.argv[idx + 1])
        except ValueError:
            print(f"Error: Invalid budget value '{sys.argv[idx + 1]}'")
            sys.exit(1)

# Calculate dates
today = datetime.now()
end_date = today + timedelta(days=1)  # AWS CE needs next day
start_date = today - timedelta(days=days)

start_str = start_date.strftime("%Y-%m-%d")
end_str = end_date.strftime("%Y-%m-%d")

print(f"=== AWS Costs - Last {days} days ===")
print(f"Period: {start_str} to {today.strftime('%Y-%m-%d')}")
print(f"Maximum budget: ${budget:.2f} USD/month")
print()

def run_aws_command(granularity):
    """Execute aws ce get-cost-and-usage."""
    cmd = [
        "aws", "ce", "get-cost-and-usage",
        "--time-period", f"Start={start_str},End={end_str}",
        "--granularity", granularity,
        "--metrics", "UnblendedCost",
        "--group-by", "Type=DIMENSION,Key=SERVICE"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)

    return json.loads(result.stdout)

# Get costs
print("Querying AWS Cost Explorer...")
granularity = "DAILY" if show_daily else "MONTHLY"
data = run_aws_command(granularity)

# Process results
total_cost = 0.0
services = {}

for period in data.get("ResultsByTime", []):
    period_start = period["TimePeriod"]["Start"]
    period_end = period["TimePeriod"]["End"]

    if show_daily:
        print(f"\n--- {period_start} ---")

    for group in period.get("Groups", []):
        service = group["Keys"][0]
        cost = float(group["Metrics"]["UnblendedCost"]["Amount"])

        if cost != 0:
            total_cost += cost
            services[service] = services.get(service, 0) + cost

            if show_daily and cost > 0.0001:
                print(f"  {service}: ${cost:.6f}")

# Show summary
print("\n" + "=" * 50)
print("SERVICE SUMMARY")
print("=" * 50)

if services:
    # Sort by cost descending
    sorted_services = sorted(services.items(), key=lambda x: -x[1])

    for service, cost in sorted_services:
        if abs(cost) > 0.0000001:
            print(f"{service:40} ${cost:.6f}")
else:
    print("No costs registered (Free Tier)")

print("-" * 50)
print(f"{'TOTAL':40} ${total_cost:.6f}")
print()

# Calculate monthly projection
if days < 30 and total_cost > 0:
    projection = (total_cost / days) * 30
    print(f"Monthly projection: ${projection:.4f}")

# Budget alert
if total_cost > budget * 0.8:
    print(f"\n⚠️  WARNING: Close to ${budget}/month limit")
elif total_cost > budget:
    print(f"\n🚨 CRITICAL: Exceeded ${budget}/month limit")
else:
    percentage = (total_cost / budget) * 100 if budget > 0 else 0
    print(f"\nBudget used: {percentage:.2f}% of ${budget}/month")

print()
