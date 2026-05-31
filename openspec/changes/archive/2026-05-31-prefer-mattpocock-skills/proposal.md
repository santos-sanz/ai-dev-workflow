## Why

The workflow pack is inspired by `mattpocock/skills`, but current instructions do not tell agents what to do when those upstream skills are installed and available. Making the preference explicit lets agents benefit from upstream skills without vendoring or duplicating them in this repo.

## What Changes

- Document that agents should use an installed `mattpocock/skills` skill when it directly matches the task and the active agent can invoke it safely.
- Keep local skills in `skills/` as the portable fallback and adaptation layer.
- Clarify that upstream skills should not be installed, vendored, or configured unless the user asks for that external side effect.
- Reflect the preference in `AGENTS.md`, README, delegated entrypoints, and native capability boundaries.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `openspec-workflow`: Extend the workflow compatibility contract to include external skill-pack preference for `mattpocock/skills`.

## Impact

- Affected docs: `AGENTS.md`, `README.md`, `NATIVE_CAPABILITIES.md`, `CLAUDE.md`, `opencode.md`, `.cursor/rules/ai-dev-workflow.mdc`.
- Affected OpenSpec spec: `openspec/specs/openspec-workflow/spec.md`.
- No upstream skill files are copied into this repo.
- No package dependency, lockfile, hook, or generated command is added.
