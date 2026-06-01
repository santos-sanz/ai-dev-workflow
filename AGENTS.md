# Agent Instructions

Use this repo as a workflow pack for AI-assisted software development. Keep the process simple, evidence-based, and compatible with Codex, Claude Code, OpenCode, and Cursor.

## Operating Rules

- Read the repo before asking questions that the repo can answer.
- Ask only questions that change scope, behavior, interfaces, risk, or acceptance criteria.
- Use native agent features before workflow-pack substitutes: plan modes, subagents, built-in skills, diff review, command execution, memory, checkpoints, and PR integrations.
- When an installed upstream `mattpocock/skills` skill directly matches the task, use it where the active agent can invoke it safely. Fall back to this repo's adapted skills when upstream skills are unavailable, too broad, or less aligned with these instructions.
- Prefer the smallest applicable skill in `skills/`.
- Treat skills as process guidance, not as replacements for native tools. If the active agent already has a safe native mechanism, use it and apply the skill's acceptance criteria around it.
- Use OpenSpec for non-trivial changes that need durable, reviewable requirements across sessions, agents, or PRs. For small clear edits, native planning plus the smallest applicable skill is enough.
- Do not start implementation until the goal, success criteria, and constraints are clear enough to avoid rework.
- Check the working tree before editing. Protect unrelated user changes and never mix them into commits or handoffs.
- Build in vertical slices and keep a fast feedback loop running.
- Treat destructive commands, secret exposure, irreversible external side effects, and public interface changes as scope-changing unless the user explicitly approved them.
- Report commands run, checks passed, and checks that could not run.
- Never hide assumptions. State them in plans, handoffs, PR descriptions, or final responses.

## Skill Map

- Clarify unclear work with [`clarify-requirements`](./skills/engineering/clarify-requirements/SKILL.md).
- Produce decision-complete plans with [`plan-implementation`](./skills/engineering/plan-implementation/SKILL.md).
- Build behavior one slice at a time with [`tdd-vertical-slice`](./skills/engineering/tdd-vertical-slice/SKILL.md).
- Design automated tests around real confidence with [`testing-strategy`](./skills/engineering/testing-strategy/SKILL.md).
- Debug with evidence using [`diagnose-bug`](./skills/engineering/diagnose-bug/SKILL.md).
- Review branches or diffs with [`review-diff`](./skills/engineering/review-diff/SKILL.md).
- Preserve context with [`handoff`](./skills/productivity/handoff/SKILL.md).
- Commit, push, and open PRs with [`ship-pr`](./skills/engineering/ship-pr/SKILL.md).

## Native Integration

- Check [`NATIVE_CAPABILITIES.md`](./NATIVE_CAPABILITIES.md) before adding a workflow artifact that might duplicate an agent feature.
- Codex and OpenCode can discover thin adapters in [`.agents/skills`](./.agents/skills); those adapters point back to the canonical skills in `skills/`.
- Claude Code should use `CLAUDE.md`, native skills, bundled `/debug` and `/code-review`, Plan mode, hooks, and subagents where available.
- Cursor should use native Agent/Ask/Manual modes, project rules, memories, checkpoints, diff review, and background agents where available.
- OpenSpec is available as the persistent spec layer in [`openspec`](./openspec), with generated command and skill surfaces for Codex, Claude Code, Cursor, and OpenCode. Use `/opsx:propose`, `/opsx:apply`, and `/opsx:archive` where supported, or the equivalent generated command name for the active agent.
- `mattpocock/skills` is an optional upstream skill pack, not a vendored dependency. Do not install, vendor, or configure it unless the user explicitly asks for that external setup.
- Cursor Team Kit's [`thermo-nuclear-code-quality-review`](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md) is a useful external review reference for strict maintainability checks; do not install, vendor, or configure it unless the user explicitly asks for that external setup.
- Add custom scripts, hooks, or commands only when a deterministic repo-specific check is missing.

## Documentation Discipline

- Keep [`CONTEXT.md`](./CONTEXT.md) as a glossary only.
- Keep skills small and focused on recurring behavior.
- Add new skills only when the workflow repeats often enough to justify a public interface.
- Keep tool entrypoints synchronized: `AGENTS.md` is the source of truth, while `CLAUDE.md`, `opencode.md`, Cursor rules, and Claude plugin metadata must not drift from it.
- Run `python3 scripts/validate-workflow.py` after adding, renaming, moving, or removing skills, entrypoints, or OpenSpec-generated surfaces.

## Blind Spot Review

Before changing this workflow pack, explicitly check for gaps in:

- **Intent:** goal, users, success criteria, constraints, and out-of-scope work.
- **Safety:** git state, user changes, secrets, destructive operations, and external side effects.
- **Execution:** the smallest applicable skill, vertical-slice boundaries, and feedback loop.
- **Compatibility:** Codex, Claude Code, OpenCode, Cursor, OpenSpec surfaces, and installer metadata.
- **Verification:** local links, skill front matter, entrypoint synchronization, OpenSpec validation when specs change, and commands that prove the change.
- **Continuity:** assumptions, residual risks, and handoff notes when work cannot finish in one session.
