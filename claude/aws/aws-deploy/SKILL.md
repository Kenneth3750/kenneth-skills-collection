---
name: aws-deploy
description: Deploy changes to AWS Lambda using SAM. Use when the user asks to deploy, push changes to AWS, or update the Lambda.
argument-hint: [--preview-only]
allowed-tools: Bash
---

# Deploy to AWS with SAM

Deploy project changes to AWS Lambda.

## Important - Read First

1. **SAM not in PATH** - Use full path or ensure it's installed
2. **Each Bash is a new session** - Export credentials AND run SAM in the SAME command
3. **Always preview first** before applying changes

## Build + Preview Command (use this)

```bash
export AWS_ACCESS_KEY_ID=$(grep AWS_ACCESS_KEY_ID .env | cut -d'=' -f2) && \
export AWS_SECRET_ACCESS_KEY=$(grep AWS_SECRET_ACCESS_KEY .env | cut -d'=' -f2) && \
export AWS_DEFAULT_REGION=$(grep AWS_DEFAULT_REGION .env | cut -d'=' -f2) && \
sam build && \
sam deploy --no-execute-changeset
```

## Apply Deploy Command (only if preview OK)

```bash
export AWS_ACCESS_KEY_ID=$(grep AWS_ACCESS_KEY_ID .env | cut -d'=' -f2) && \
export AWS_SECRET_ACCESS_KEY=$(grep AWS_SECRET_ACCESS_KEY .env | cut -d'=' -f2) && \
export AWS_DEFAULT_REGION=$(grep AWS_DEFAULT_REGION .env | cut -d'=' -f2) && \
sam deploy
```

## View Logs Command

```bash
export AWS_ACCESS_KEY_ID=$(grep AWS_ACCESS_KEY_ID .env | cut -d'=' -f2) && \
export AWS_SECRET_ACCESS_KEY=$(grep AWS_SECRET_ACCESS_KEY .env | cut -d'=' -f2) && \
export AWS_DEFAULT_REGION=$(grep AWS_DEFAULT_REGION .env | cut -d'=' -f2) && \
sam logs -n YourFunctionName --tail
```

## Expected Responses

**Successful build:**
```
Build Succeeded
```

**Preview with no changes (stack up to date):**
```
No changes to deploy. Stack is up to date
```
This is NORMAL if there are no pending changes.

**Preview with changes:**
```
CloudFormation stack changeset
-----------------------------------------
Operation    LogicalResourceId    ResourceType
-----------------------------------------
+ Add        NewResource          AWS::Lambda::Function
* Modify     ExistingResource     AWS::Lambda::Function
- Delete     OldResource          AWS::Lambda::Function
```

## Project Files

| File | What it does |
|------|-------------|
| `template.yaml` | Infrastructure (Lambda, API Gateway, IAM) |
| `samconfig.toml` | Deploy config (region, stack name) |
| `.env` | AWS credentials (never commit) |

## Common Errors

| Error | Solution |
|-------|----------|
| `sam: command not found` | Install SAM CLI or use full path |
| `Unable to locate credentials` | Export credentials in the same command |
| `No changes to deploy` | Not an error, stack is up to date |
| `ROLLBACK_COMPLETE` | Run `sam delete` and redeploy |
