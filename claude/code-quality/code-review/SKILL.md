---
name: code-review
description: Perform code reviews following engineering best practices. Use when reviewing pull requests, examining code changes, or providing feedback on code quality. Covers security, performance, testing, and design review.
---

# Code Review

Follow these guidelines when reviewing code changes.

## Change Discipline

- Write absolute minimum code required
- No sweeping changes
- No unrelated edits
- Stay focused on the specific task
- Don't break existing functionality without asking

## Investigation Approach

When reviewing code:

1. List 5-7 potential issues or concerns for each file
2. Gather evidence (check similar patterns, run tests, trace data flow)
3. Narrow to 1-2 most critical issues per file
4. Verify issues are real (not false positives or already handled)
5. Only report confirmed, actionable feedback

## Review Workflow

### 1. Gather Context

**Understanding the Changes:**
- Use `gh pr view <number>` to get PR details
- Use `git diff <base-branch>...HEAD` to see all changes
- Use `git log <base-branch>..HEAD` to see commit history
- Read the PR description carefully
- Identify which files are modified, added, or deleted

**Understanding the Codebase:**
- Use the Task tool with subagent_type=Explore to understand related code patterns
- Read files that interact with the changed code
- Look for similar patterns in the codebase
- Check for existing tests that might be affected

### 2. Perform Review

Review the changes systematically, focusing on the areas below.

### 3. Provide Feedback

Structure your feedback clearly with:
- **Critical Issues**: Must be fixed before merging (blocking)
- **Important Issues**: Should be addressed but not blocking
- **Suggestions**: Nice-to-have improvements
- **Positive Feedback**: Call out good practices

Always explain WHY something is an issue and HOW to fix it.

## Review Checklist

### Correctness & Logic

- **Runtime errors**: Check for potential exceptions, null/undefined access
- **Edge cases**: Empty arrays, null values, boundary conditions
- **Logic errors**: Off-by-one errors, incorrect conditionals, race conditions
- **Type safety**: Proper type annotations, avoiding `any` in TypeScript
- **Error handling**: Appropriate try-catch blocks, error propagation

### Performance

- **Algorithm complexity**: Avoid O(n^2) where O(n) is possible
- **Database queries**: N+1 problems, missing indexes, unbounded queries
- **Memory usage**: Unnecessary data copying, memory leaks
- **Caching**: Opportunities for caching expensive operations
- **Network calls**: Batching, unnecessary requests, missing timeouts

### Security

- **Injection vulnerabilities**: SQL injection, command injection, XSS
- **Authentication & Authorization**: Proper permission checks
- **Data exposure**: Sensitive data in logs, error messages, or API responses
- **Input validation**: Sanitize and validate all user inputs
- **Secrets management**: No hardcoded credentials, API keys, or tokens

### Design & Architecture

- **Consistency**: Follows existing patterns and conventions
- **Separation of concerns**: Clear boundaries between components
- **DRY principle**: Avoid duplicating logic
- **API design**: Clear contracts, versioning strategy, backward compatibility

### Testing

- New features MUST have tests
- Bug fixes SHOULD include regression tests
- Tests cover happy path AND edge cases
- Integration tests for component interactions
- Tests are readable and well-named
- No flaky tests

### Code Quality

- **Readability**: Clear variable/function names, appropriate comments
- **Formatting**: Follows project style guide
- **Complexity**: Functions are focused and not too long
- **Documentation**: Public APIs have docstrings/JSDoc comments
- **Dead code**: Remove commented-out code, unused imports

## Feedback Guidelines

### Tone & Communication

- **Be respectful and constructive**: Assume good intent
- **Be specific**: Point to exact lines and explain the issue clearly
- **Provide context**: Explain WHY something is a problem
- **Offer solutions**: Suggest concrete fixes or alternatives
- **Praise good work**: Call out clever solutions or good practices

### Prioritization

**Critical (Blocking):**
- Security vulnerabilities
- Data loss or corruption risks
- Breaking production functionality
- Major performance degradation

**Important (Should Fix):**
- Bugs in new functionality
- Missing test coverage
- Poor error handling
- Design issues that will cause maintenance burden

**Nice to Have (Suggestions):**
- Code style improvements
- Minor refactoring opportunities
- Additional edge case handling
- Documentation enhancements

### Approval Criteria

**Approve when:**
- No critical issues remain
- Important issues are addressed or have clear plan
- Test coverage is adequate
- Code meets quality standards

**Remember:** The goal is to reduce risk and maintain quality, not achieve perfection.

## Output Format

```
## Code Review Summary

**Overall Assessment:** [Approve/Request Changes/Comment]

**Key Changes:** [Brief summary of what the PR does]

## Critical Issues

[List blocking issues if any]

## Important Issues

[List significant issues that should be addressed]

## Suggestions

[List nice-to-have improvements]

## Positive Feedback

[Call out good practices, clever solutions, or improvements]

## Testing

[Comment on test coverage and quality]

## Recommendation

[Final recommendation with any conditions]
```
