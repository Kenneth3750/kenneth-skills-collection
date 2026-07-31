---
name: aws-costs
description: Calculate AWS costs for the last X days. Use when the user asks about costs, expenses, or AWS budget.
license: MIT
compatibility: opencode
metadata:
  category: aws
---

# Calculate AWS Costs

Calculate AWS costs for the last `$ARGUMENTS` days.

## Main Command

```bash
python ${CLAUDE_SKILL_DIR}/scripts/calculate-costs.py $ARGUMENTS
```

**Examples:**
```bash
python ${CLAUDE_SKILL_DIR}/scripts/calculate-costs.py 7         # Last 7 days
python ${CLAUDE_SKILL_DIR}/scripts/calculate-costs.py 30        # Last 30 days
python ${CLAUDE_SKILL_DIR}/scripts/calculate-costs.py 7 --daily # With daily breakdown
python ${CLAUDE_SKILL_DIR}/scripts/calculate-costs.py 30 --budget 10.0  # Custom budget alert
```

## What It Shows

- Costs by service (Lambda, API Gateway, S3, etc.)
- Total spent in the period
- Monthly projection (if less than 30 days)
- Budget percentage used
- Alerts if approaching limit

## Manual Command (if script fails)

```bash
export AWS_ACCESS_KEY_ID=$(grep AWS_ACCESS_KEY_ID .env | cut -d'=' -f2) && \
export AWS_SECRET_ACCESS_KEY=$(grep AWS_SECRET_ACCESS_KEY .env | cut -d'=' -f2) && \
export AWS_DEFAULT_REGION=us-east-1 && \
aws ce get-cost-and-usage \
  --time-period Start=$(date -d '30 days ago' +%Y-%m-%d),End=$(date +%Y-%m-%d) \
  --granularity MONTHLY \
  --metrics "UnblendedCost" \
  --group-by Type=DIMENSION,Key=SERVICE
```

## Notes

- The script reads credentials automatically from `.env`
- AWS Cost Explorer may have 24h delay in data
- Set your budget limit in the script configuration
