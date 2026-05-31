## Why

This workflow pack already defines when to clarify, plan, build, review, hand off, and ship, but it does not provide a durable spec layer for changes that need to survive across agents or sessions. OpenSpec adds that persistent, reviewable layer while keeping native agent capabilities as the first choice for execution mechanics.

## What Changes

- Initialize OpenSpec in the repo for Codex, Claude Code, Cursor, and OpenCode.
- Document OpenSpec as the optional persistent spec-driven layer for non-trivial changes.
- Add OpenSpec usage to the default operating loop, quality gates, native capability boundary, and tool entrypoints.
- Preserve the existing pack rule that native agent modes, skills, reviews, and PR integrations remain preferred for mechanics.
- Add validation coverage so generated OpenSpec entrypoints stay present and local links remain valid.

## Capabilities

### New Capabilities

- `openspec-workflow`: Persistent proposal, design, requirement, task, and archive workflow for changes that need durable context.

### Modified Capabilities

- None. No consolidated OpenSpec specs exist yet.

## Impact

- Affected docs: `AGENTS.md`, `README.md`, `NATIVE_CAPABILITIES.md`, `CLAUDE.md`, `opencode.md`, `.cursor/rules/ai-dev-workflow.mdc`.
- Affected generated agent surfaces: `.codex/`, `.claude/`, `.cursor/commands/`, `.cursor/skills/`, `.opencode/`.
- Affected validation: `scripts/validate-workflow.py`.
- No runtime application code, public API, or package dependency is added.
