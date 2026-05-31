---
name: plan-implementation
description: Produce a decision-complete implementation plan before code changes, including interfaces, data flow, verification, assumptions, and rollout notes.
---

# Plan Implementation

Use this skill when a change is too large, risky, or ambiguous to implement directly.

## Native Integration

Use the active agent's native planning mechanism first, such as Codex subagents, Claude Plan mode, OpenCode Plan agent, or Cursor Ask/Plan/custom modes. This skill defines the content and acceptance criteria for the plan; it is not a replacement for native read-only planning controls.

## Workflow

1. **Inspect the system.**
   - Read the relevant source, tests, docs, config, and existing patterns.
   - Identify public interfaces, ownership boundaries, and feedback loops.
   - Check `CONTEXT.md` and any ADRs when they exist.

2. **Define the target behavior.**
   - State the current behavior and desired behavior.
   - List in-scope and out-of-scope changes.
   - Name affected users, callers, commands, APIs, files, or workflows only when needed for implementation clarity.

3. **Choose the approach.**
   - Prefer existing patterns over new abstractions.
   - Keep changes as small as the goal allows.
   - Define any public API, schema, CLI, UI, or file format changes precisely.
   - Record assumptions where the repo or user did not provide a fact.

4. **Plan verification.**
   - Identify the highest useful test seam.
   - Include manual checks only when automation cannot cover the behavior.
   - Include regression coverage for bugs.

5. **Produce the plan.**
   - Keep it concise but decision-complete.
   - Another engineer or agent should be able to implement without making product or architecture decisions.

## Plan Shape

```markdown
# Title

## Summary
- What will change and why.

## Implementation
- Behavior-level edits grouped by subsystem.
- Public interfaces or contracts that change.

## Test Plan
- Automated checks.
- Manual checks, if needed.

## Assumptions
- Defaults chosen because the repo or user did not specify them.
```

## Done When

- The plan can be implemented without unresolved decisions.
- The plan names verification commands or scenarios.
- Assumptions and risks are visible.
