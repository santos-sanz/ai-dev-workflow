---
name: handoff
description: Summarize active work so another agent or future session can continue without replaying the full conversation.
---

# Handoff

Use this skill when work will continue in another session, another agent, or after a long pause.

## Native Integration

Use native memory, checkpoints, conversation history, chat export, background-agent status, and PR/session links when they are enough. Create a handoff only when context must survive crossing tools, agents, branches, or sessions where native continuity is not reliable.

## Workflow

1. **Summarize the goal.**
   - State the user's objective and current status.
   - Link to the relevant branch, PR, issue, plan, or files when available.

2. **Capture decisions.**
   - List decisions already made.
   - Include assumptions that still matter.
   - Do not duplicate full specs or diffs when a link or path is enough.

3. **Capture current state.**
   - Note what changed.
   - Note what has been verified.
   - Note what failed, is blocked, or remains unverified.

4. **Give the next agent an entry point.**
   - Name the next recommended skill.
   - Provide the next concrete command or file to inspect.
   - Warn about user changes or repo state that must not be overwritten.

## Handoff Shape

```markdown
# Handoff

## Goal

## Current State

## Decisions and Assumptions

## Verification

## Next Steps
```

## Done When

- A fresh agent can continue without reading the full conversation.
- The handoff is compact and references durable artifacts instead of copying them.
- Sensitive information is omitted.
