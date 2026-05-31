## Context

The repo is a documentation-first workflow pack for AI-assisted development. It already integrates Codex, Claude Code, OpenCode, and Cursor through native instructions, skills, rules, and plugin metadata. `NATIVE_CAPABILITIES.md` explicitly says the pack should not rebuild native planning, review, command, or PR mechanics.

OpenSpec adds a complementary artifact model: changes can carry a proposal, design, requirements, tasks, and archived specs in the repository. That is useful for cross-session or cross-agent continuity, but it overlaps with the pack's existing planning and handoff language if treated as mandatory machinery.

## Goals / Non-Goals

**Goals:**

- Make OpenSpec available to the same agent surfaces already supported by the pack.
- Describe when to use OpenSpec: non-trivial changes needing durable, reviewable requirements.
- Keep `AGENTS.md` as the source of truth and align delegated entrypoints with it.
- Validate the presence of OpenSpec-generated surfaces so future changes do not silently remove them.

**Non-Goals:**

- Do not require every task to start with an OpenSpec change.
- Do not replace native plan modes, review tools, skills, or GitHub integrations.
- Do not add a Node package dependency or lockfile solely for OpenSpec.
- Do not generate upfront specs for every existing skill in this repo.

## Decisions

- Use OpenSpec-generated adapters for Codex, Claude Code, Cursor, and OpenCode.
  - Rationale: those are the repo's declared primary agent surfaces, and using the upstream generator keeps command/skill syntax aligned with OpenSpec.
  - Alternative considered: hand-write a single generic OpenSpec guide. That would be smaller, but it would not integrate with each agent's native discovery surface.

- Keep OpenSpec as optional persistent context, not a gate.
  - Rationale: the pack's core operating rule is native-first. OpenSpec is most valuable when a change needs durable specs across sessions or tools.
  - Alternative considered: require OpenSpec for all work. That adds overhead for small edits and conflicts with the pack's "smallest applicable skill" rule.

- Update existing docs instead of adding a new canonical workflow document.
  - Rationale: `AGENTS.md` is the source of truth, with README and delegated entrypoints synchronized to it.
  - Alternative considered: create `OPENSPEC.md`. That would add another entrypoint to maintain and increase drift risk.

- Extend validation for OpenSpec entrypoints.
  - Rationale: generated command/skill directories are now part of the repo contract. A deterministic repo-specific check is appropriate.
  - Alternative considered: rely on manual review. That would not catch accidental removal or drift.

## Risks / Trade-offs

- OpenSpec CLI requires Node `20.19.0+`, while the current local Node is `20.17.0` and emits an engine warning → Document the requirement and keep validation independent from running OpenSpec.
- Generated OpenSpec skills may evolve upstream → Keep generated files intact and validate presence rather than reformatting them into local style.
- Extra commands and skills increase repo surface area → Mention OpenSpec only where it changes workflow behavior and avoid duplicating generated docs.
- Optional OpenSpec use may be applied inconsistently → Add clear use criteria to `AGENTS.md`, README, and quality gates.
