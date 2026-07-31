---
name: wasmer-deploy
description: Deploy static apps to Wasmer Edge. Use for builds, deploys, domain configuration, and monitoring. Requires Wasmer CLI installed.
allowed-tools: Read, Write, Edit, Bash, WebFetch
---

# Wasmer Deploy

Skill for deploying static applications to Wasmer Edge.

## Quick Start

```bash
# 1. Production build
cd web && npm run build

# 2. Deploy
wasmer deploy
```

## When to Use

- Deploy the app to production
- Configure custom domains
- Check deployment status
- Monitor resource usage

## Configuration Files

The project needs two files in `web/`:

| File | Purpose |
|------|---------|
| `wasmer.toml` | Define the package (name, dependencies, files) |
| `app.yaml` | Define the app in Edge (owner, name, config) |

## Main Commands

| Command | Use |
|---------|-----|
| `wasmer deploy` | Build + publish + deploy |
| `wasmer app list` | View all apps |
| `wasmer app info <app>` | Info of one app |
| `wasmer run .` | Local test on port 8080 |

## Deployment Process

1. Pre-checks (lint, tests)
2. Production build
3. Deploy to Wasmer Edge
4. Verify deployment

## Free Tier Limits

| Resource | Limit |
|----------|-------|
| Requests | 100,000/month |
| Bandwidth | 150 GB |
| Storage | 1 GB |
| Apps | 3 max |

## Important Notes

- Always run `npm run build` before deploy
- The `dist/` directory is what gets deployed
- Deploys are immediate (no staging)
- Each deploy increments the version automatically
