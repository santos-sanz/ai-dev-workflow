# Agent Instructions

Use this repo as a workflow pack for AI-assisted software development. Keep the process simple, evidence-based, and compatible with Codex, Claude Code, OpenCode, and Cursor.

## Operating Rules

- Read the repo before asking questions that the repo can answer.
- Ask only questions that change scope, behavior, interfaces, risk, or acceptance criteria.
- Prefer the smallest applicable skill in `skills/`.
- Do not start implementation until the goal, success criteria, and constraints are clear enough to avoid rework.
- Build in vertical slices and keep a fast feedback loop running.
- Report commands run, checks passed, and checks that could not run.
- Never hide assumptions. State them in plans, handoffs, PR descriptions, or final responses.

## Skill Map

- Clarify unclear work with [`clarify-requirements`](./skills/engineering/clarify-requirements/SKILL.md).
- Produce decision-complete plans with [`plan-implementation`](./skills/engineering/plan-implementation/SKILL.md).
- Build behavior one slice at a time with [`tdd-vertical-slice`](./skills/engineering/tdd-vertical-slice/SKILL.md).
- Debug with evidence using [`diagnose-bug`](./skills/engineering/diagnose-bug/SKILL.md).
- Review branches or diffs with [`review-diff`](./skills/engineering/review-diff/SKILL.md).
- Preserve context with [`handoff`](./skills/productivity/handoff/SKILL.md).
- Commit, push, and open PRs with [`ship-pr`](./skills/engineering/ship-pr/SKILL.md).

## Documentation Discipline

- Keep [`CONTEXT.md`](./CONTEXT.md) as a glossary only.
- Keep skills small and focused on recurring behavior.
- Add new skills only when the workflow repeats often enough to justify a public interface.
