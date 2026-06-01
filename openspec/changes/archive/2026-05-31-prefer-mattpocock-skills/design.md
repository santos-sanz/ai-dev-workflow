## Context

This repo already carries local, adapted skills for clarification, planning, vertical slices, debugging, review, handoff, and shipping. The README credits `mattpocock/skills` as inspiration, but the repo deliberately avoids vendoring that upstream pack.

The upstream pack contains skills such as `grill-me`, `grill-with-docs`, `tdd`, `diagnose`, `to-prd`, `to-issues`, `zoom-out`, and `improve-codebase-architecture`. Its quickstart uses `pnpx skills@latest add mattpocock/skills` and a setup skill, which is an external install/configuration action.

## Goals / Non-Goals

**Goals:**

- Prefer upstream `mattpocock/skills` when they are already installed and clearly match the task.
- Keep the local workflow pack functional without upstream skills.
- Prevent accidental vendoring or installing external skills as a hidden side effect.
- Preserve `AGENTS.md` as the source of truth and keep delegated entrypoints synchronized.

**Non-Goals:**

- Do not install `mattpocock/skills` in this repo.
- Do not copy upstream `SKILL.md` files into local `skills/`.
- Do not add validation that depends on network access or the external skills registry.
- Do not replace local skills with upstream names.

## Decisions

- Document upstream skills as a preference, not a dependency.
  - Rationale: the user asked to try using them when possible, which implies opportunistic use rather than hard requirement.
  - Alternative considered: install the upstream pack. That would add external side effects and potentially agent-specific files outside the repo's compact workflow contract.

- Keep local skills as fallback.
  - Rationale: this repo must stay compatible across Codex, Claude Code, OpenCode, and Cursor even when upstream skills are unavailable.
  - Alternative considered: remove local equivalents. That would make the pack less portable.

- Add a source link and installation note to README only.
  - Rationale: maintainers need to know how upstream skills are obtained, but agents should not install them without user approval.
  - Alternative considered: add installer commands to every entrypoint. That would encourage hidden dependency changes.

## Risks / Trade-offs

- Upstream skill behavior may change over time -> Treat upstream skills as optional and use local skills when precise repo behavior matters.
- Agents may overuse external skills for simple work -> Keep the "smallest applicable skill" rule and native-first boundary.
- Some agents may not expose upstream skills -> Document a clear fallback to local `skills/`.
