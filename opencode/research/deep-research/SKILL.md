---
name: deep-research
description: Research topics on the web rigorously and generate structured reports. Use when you need to investigate technologies, compare options, analyze costs, or synthesize information from multiple sources.
license: MIT
compatibility: opencode
metadata:
  category: research
---

# Deep Research

Skill for iterative web research with structured report delivery.

## Instructions

1. Use WebSearch and WebFetch to research from multiple sources
2. Iterate until you have enough information for a well-founded recommendation
3. Create the report in `docs/research/research-<topic>.md`

## Report Format

The report must include:

### Executive Summary
- 5-8 bullets with main findings

### Thematic Sections
- Comparisons and tradeoffs between options
- Metrics when relevant (cost, latency, quality)

### Comparison Tables
- When there's numerical data or comparable features

### Recommendation
- Recommended option with justification
- Identified risks
- Suggested next steps

### References
- Numbered list of consulted sources
- Format: `[Name](URL)` with author/date if available

## Citation Format

Use inline citations like: `[Source](URL)`.

At the end, add a **References** section with a numbered list.

## Usage Example

```
Research state management solutions for React applications. 
Include comparisons of Redux, Zustand, and Jotai. 
Compare bundle size, learning curve, performance, and ecosystem.
```
