# Claude Code Instructions

Follow [`AGENTS.md`](./AGENTS.md) as the source of truth for this repo.

This repo is intentionally documentation-first. Prefer editing Markdown workflow artifacts over adding scripts or dependencies unless a specific verification gap requires automation.

Use Claude Code's native capabilities before adding workflow-pack machinery: Plan mode for read-only planning, bundled `/debug` and `/code-review` for those workflows, `/run` and `/verify` for app validation, hooks for deterministic lifecycle checks, subagents for isolated exploration, and built-in git/PR support for shipping.

If upstream `mattpocock/skills` skills are installed in Claude Code, use the matching skill when it directly fits the task. Do not install or configure that upstream pack unless the user asks for setup.

Use the generated OpenSpec commands in `.claude/commands/opsx/` when a change needs durable proposal, design, spec, task, or archive artifacts. Keep OpenSpec complementary to Claude Code's native Plan mode and review tools.

Stable Claude-compatible skills are listed in [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json).
