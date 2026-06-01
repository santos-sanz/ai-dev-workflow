# Native Capability Boundary

Research snapshot: 2026-06-01.

Use this file to avoid rebuilding capabilities that the target coding agent already provides. The workflow pack should supply process criteria and portable handoff language, not duplicate editor or agent features.

## Native Capabilities by Agent

| Agent | Native capabilities to use first | Source |
| --- | --- | --- |
| Codex | `AGENTS.md` project instructions, native skills, plugins, hooks, subagents, sandbox and approval settings, MCP, app/IDE/CLI surfaces, review, automations, worktrees, local environments, in-app browser, computer use, non-interactive mode, GitHub Action | [Codex configuration](https://developers.openai.com/codex/config-basic), [Codex skills](https://developers.openai.com/codex/skills), [Codex hooks](https://developers.openai.com/codex/hooks), [Codex subagents](https://developers.openai.com/codex/subagents) |
| Claude Code | `CLAUDE.md` and auto memory, Plan mode, native skills and bundled skills such as `/debug`, `/code-review`, `/run`, and `/verify`, hooks, subagents, IDE diff review, commits and PRs, routines and scheduled tasks, MCP | [Claude overview](https://code.claude.com/docs/en/overview), [Claude memory](https://code.claude.com/docs/en/memory), [Claude skills](https://code.claude.com/docs/en/skills), [Claude subagents](https://code.claude.com/docs/en/sub-agents), [Claude hooks](https://code.claude.com/docs/en/hooks), [Claude routines](https://code.claude.com/docs/en/routines) |
| OpenCode | `AGENTS.md` rules, Build and Plan primary agents, General/Explore/Scout subagents, native `skill` tool, permissions, built-in file/search/bash/LSP/web tools, custom commands, MCP servers, CLI automation | [OpenCode rules](https://opencode.ai/docs/rules), [OpenCode agents](https://opencode.ai/docs/agents/), [OpenCode skills](https://opencode.ai/docs/skills), [OpenCode tools](https://opencode.ai/docs/tools), [OpenCode permissions](https://opencode.ai/docs/permissions), [OpenCode CLI](https://opencode.ai/docs/cli/) |
| Cursor | Agent, Ask, Manual, and Custom modes; project rules; `AGENTS.md`; memories; codebase indexing; MCP; terminal integration; checkpoints; chat history/export; diff review; background agents | [Cursor concepts](https://docs.cursor.com/get-started/concepts), [Cursor modes](https://docs.cursor.com/agent), [Cursor rules](https://docs.cursor.com/en/context), [Cursor memories](https://docs.cursor.com/en/context/memories), [Cursor diff review](https://docs.cursor.com/agent/review), [Cursor background agents](https://docs.cursor.com/background-agent) |

## Do Not Rebuild

- Generic file editing, patch application, terminal execution, code search, or LSP lookup.
- Approval systems, sandbox profiles, permission prompts, or tool access control.
- Diff viewers, checkpoints, review UI, or change acceptance controls.
- Generic plan/read-only modes, background-agent runners, or subagent orchestration.
- Generic memory, conversation history, or chat export.
- Generic PR creation when the current agent already integrates with GitHub or `gh`.
- Generic proactive-agent hosting, cron wrappers, webhook runners, or remote session persistence when Claude Code Routines can run the work on Anthropic-managed infrastructure with schedule, API, or GitHub triggers.
- Generic custom-command frameworks when the agent already has slash commands or command files.
- OpenSpec proposal, design, spec, task, command, or archive mechanics when the OpenSpec CLI and generated agent surfaces already provide them.
- Installed upstream skill-pack behavior, including `mattpocock/skills`, when the active agent can already discover and invoke those skills.

## What This Pack Owns

- Clarification criteria: ask only questions that change scope, behavior, interfaces, risk, constraints, or acceptance criteria.
- Decision-complete plans: document target behavior, affected contracts, verification, assumptions, and rollout notes.
- Vertical-slice discipline: one observable behavior, one feedback signal, one minimal implementation, then cleanup.
- Testing strategy: choose unit, integration, and end-to-end tests by risk; avoid mock-heavy false confidence and coverage theater.
- Evidence-based debugging: reproduce, minimize, rank hypotheses, instrument deliberately, fix, and lock down regression coverage.
- Review standards: findings first, severity, file/line evidence, spec coverage, missing tests, and residual risk.
- Portable handoffs: concise state that survives crossing tools, agents, branches, or sessions.
- Shipping hygiene: intended files only, final verification, clear PR story, assumptions, and known risk.
- OpenSpec use criteria: when durable proposal/design/spec/task/archive context is worth the overhead, and how that context fits the native-first workflow.
- External skill-pack boundaries: when to prefer an available upstream skill or external reference such as Cursor Team Kit's `thermo-nuclear-code-quality-review`, when to fall back to local adapted skills, and when installation would require explicit user approval.

## Proactive Automation Boundary

Claude Code Routines are the native choice for proactive work when a saved agent task can run from a configured prompt, repositories, connectors, and triggers. They are most useful when the important design problem is not how to host the agent, but when it should run, what context it can access, and how a human or reviewing agent can steer or inspect the result.

Use a routine before adding repo-specific automation when the workflow is recurring or event-driven, such as documentation maintenance, deploy verification, or backlog triage. Add repo scripts or external runners only when the native routine surface cannot express a required trigger, integration, verification step, or compliance boundary.

## Integration Rule

When a native feature covers the mechanics, use it and apply the relevant skill only as acceptance criteria. Use an installed `mattpocock/skills` skill when it directly fits the task and is available through the active agent; otherwise use this repo's adapted skills. Use OpenSpec when requirements and decisions need durable repo context beyond a single chat or native plan. Create new scripts, commands, hooks, or agent configs only for deterministic repo-specific checks or missing native surfaces.
