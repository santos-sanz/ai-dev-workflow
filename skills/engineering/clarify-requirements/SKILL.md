---
name: clarify-requirements
description: Interview the user until goal, scope, constraints, success criteria, and trade-offs are clear enough to plan or implement.
---

# Clarify Requirements

Use this skill when the request is underspecified, high-risk, product-heavy, or likely to be misimplemented without more context.

## Native Integration

Use the active agent's native chat, Ask/read-only mode, question tool, or planning surface to gather context. This skill only defines which questions are worth asking and what a usable brief must contain.

## Workflow

1. **Ground first.**
   - Read relevant repo files, docs, tests, issue text, current branch, and git status.
   - Do not ask questions that local context can answer.

2. **State the current understanding.**
   - Summarize the goal in one or two sentences.
   - Call out known constraints and likely success criteria.
   - Separate facts from assumptions.

3. **Ask only decision-changing questions.**
   - Ask about scope boundaries, user-visible behavior, compatibility, data contracts, rollout, risk, and acceptance criteria.
   - Prefer one question at a time when the answer changes the next question.
   - Include a recommended answer when there is a sensible default.

4. **Resolve ambiguity into a usable brief.**
   - Capture the final goal, in-scope work, out-of-scope work, constraints, assumptions, and acceptance criteria.
   - If the work is now implementable, hand off to `plan-implementation` or `tdd-vertical-slice`.

## Done When

- The agent can explain what must change and what must not change.
- The user-visible success criteria are explicit.
- Major trade-offs have a chosen direction or a documented assumption.
- No remaining question would materially change the implementation plan.
