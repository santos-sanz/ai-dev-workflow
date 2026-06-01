# AI Dev Workflow Pack

A compact workflow pack for building software with AI development agents such as Codex, Claude Code, OpenCode, and Cursor.

The goal is not to recreate features that coding agents already provide. Modern agents already read repo instructions, edit files, run commands, manage approvals, expose plan/review modes, support skills or rules, and often ship PR workflows. This pack defines the thin process layer those tools do not reliably provide by default: when to clarify, what a decision-complete plan contains, when to preserve durable specs with OpenSpec, how to keep implementation in verified vertical slices, what evidence belongs in debugging, and how to report assumptions and residual risk.

See [`NATIVE_CAPABILITIES.md`](./NATIVE_CAPABILITIES.md) for the current native-capability boundary and source links.

This pack is inspired by the small, composable skill style in [mattpocock/skills](https://github.com/mattpocock/skills), but it is intentionally adapted for this repo instead of vendored wholesale. When those upstream skills are already installed in the active agent, use the matching upstream skill first when it fits the task; otherwise use this repo's local skills.

## Workflow

Use native agent features first. Use the smallest skill only for the process discipline that the native feature does not encode.

| Phase | Native feature to prefer | Pack responsibility | Skill |
| --- | --- | --- | --- |
| Clarify | Native chat, ask/read-only mode, question tools | Decide which questions actually change scope, behavior, interfaces, risk, or acceptance criteria | [`clarify-requirements`](./skills/engineering/clarify-requirements/SKILL.md) |
| Spec | OpenSpec generated commands and skills when durable context is needed | Keep proposal, design, requirements, tasks, and archived specs reviewable in the repo | [`openspec`](./openspec) |
| Plan | Codex subagents, Claude Plan mode, OpenCode Plan agent, Cursor Ask/Plan/custom modes | Define the required shape of a decision-complete plan and visible assumptions | [`plan-implementation`](./skills/engineering/plan-implementation/SKILL.md) |
| Build | Agent file edits, terminal tools, test runners, run/verify commands | Keep implementation in one behavior-first vertical slice at a time | [`tdd-vertical-slice`](./skills/engineering/tdd-vertical-slice/SKILL.md) |
| Test | Native test runners, browser/app verification, coverage, containers, and CI | Choose tests that reduce real uncertainty and lock down behavior without brittle coverage theater | [`testing-strategy`](./skills/engineering/testing-strategy/SKILL.md) |
| Debug | Native debug skills, subagents, terminal output, browser/app tools | Require reproduction, ranked hypotheses, targeted instrumentation, and regression evidence | [`diagnose-bug`](./skills/engineering/diagnose-bug/SKILL.md) |
| Review | Native diff viewers, code-review skills, review UI, PR checks | Prioritize actionable findings against spec and repo standards | [`review-diff`](./skills/engineering/review-diff/SKILL.md) |
| Handoff | Native memory, checkpoints, conversation history, background-agent status | Create a portable summary only when work crosses sessions, tools, or agents | [`handoff`](./skills/productivity/handoff/SKILL.md) |
| Ship | Native git/PR commands, GitHub integrations, PR UI | Confirm intended scope, verification evidence, assumptions, and residual risk | [`ship-pr`](./skills/engineering/ship-pr/SKILL.md) |

## Upstream Skill Preference

Use installed `mattpocock/skills` skills opportunistically when they directly match the work, especially `grill-me` or `grill-with-docs` for alignment, `tdd` for red-green-refactor implementation, `diagnose` for debugging, `to-prd` or `to-issues` for product breakdown, `zoom-out` for broader code context, and `improve-codebase-architecture` for architecture review.

For unusually strict maintainability review, the Cursor Team Kit [`thermo-nuclear-code-quality-review`](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md) skill is a useful reference lens: look for structural simplification, abstraction quality, file growth, spaghetti branching, boundary cleanliness, and canonical ownership before accepting a diff as merely "working."

If the upstream skill is not installed or would conflict with this repo's instructions, use the local adapted skill in `skills/` instead. Do not run `npx skills@latest add mattpocock/skills`, `/setup-matt-pocock-skills`, or copy upstream skill files unless the user explicitly asks for that setup.

## Default Operating Loop

1. **Ground in the repo.** Read the files, tests, docs, and git state that can answer factual questions.
2. **Use native capabilities first.** Prefer the current agent's built-in plan mode, subagents, skills, diff review, command execution, memory, and PR integrations before creating custom workflow artifacts.
3. **Clarify only what matters.** Ask questions only when the answer changes scope, behavior, interfaces, or risk.
4. **Use OpenSpec when context must persist.** For non-trivial changes that need durable requirements, start with `/opsx:propose`, implement with `/opsx:apply`, and consolidate with `/opsx:archive`.
5. **Plan to a decision-complete level.** A different engineer or agent should be able to implement the plan without making product or architecture decisions.
6. **Implement one vertical slice at a time.** Prefer behavior-first tests and fast feedback over broad speculative edits.
7. **Choose tests by risk.** Use tests to reduce uncertainty, protect real contracts, and cover failure paths instead of chasing coverage percentages.
8. **Keep evidence close.** Run the smallest meaningful check after each important step and report what passed or could not run.
9. **Review against both spec and standards.** A change can be well-written and still solve the wrong problem.
10. **Ship with a clean story.** The PR should explain intent, main changes, validation, and remaining risk.

## Proactive Agent Workflows

Claude Code Routines move agent work from reactive prompting toward teammate-like automation: a routine can notice a schedule or event, start a remote Claude Code session, and work against configured repos and connectors without a developer keeping a local session alive.

Use that native surface before building custom proactive-agent infrastructure. Self-built runners usually add hosting, persistence, authentication, trigger plumbing, and real-time supervision problems that the workflow pack should not reimplement when the agent already owns them.

Before creating a routine, make these decisions explicit:

- **Trigger:** when the work should run, such as weekly documentation review, a GitHub issue or PR event, a webhook, or a post-deploy API call.
- **Context:** which repositories, connectors, monitoring tools, docs, or notification channels the agent needs.
- **Steerability:** how humans or review agents can inspect, pause, resume, or correct the run before changes are trusted.

Good routine candidates include weekly documentation drift checks that open PRs, deploy verifiers that inspect monitoring data after a release, and backlog triage jobs that summarize or prioritize incoming issues. Keep the same quality gates as interactive work: clear intent, scoped access, visible assumptions, repeatable verification, and reviewable output.

## Workflow Quality Gates

Use these gates to catch common blind spots before, during, and after work:

- **Intent is explicit.** The agent can state the goal, affected users or callers, success criteria, constraints, assumptions, and out-of-scope work.
- **Safety is checked.** The agent has inspected git state, protected unrelated user changes, and identified secrets, destructive commands, irreversible external side effects, and public interface changes before acting.
- **Execution is sliced.** The work uses the smallest applicable skill, proceeds in vertical slices, and keeps a repeatable feedback loop close to each change.
- **Spec context persists when needed.** OpenSpec changes are used for durable proposals, requirements, tasks, and archives when chat-local planning would not be enough.
- **Compatibility is preserved.** `AGENTS.md` remains the source of truth, while Codex, Claude Code, OpenCode, Cursor, OpenSpec generated surfaces, and plugin metadata stay synchronized with it.
- **Verification is repeatable.** The agent records commands run, OpenSpec validation when specs change, checks passed, checks skipped, and remaining risk instead of relying on manual confidence.
- **Continuity is durable.** Decisions, assumptions, residual risks, and next steps are captured in the plan, handoff, PR description, or final response.

## Agent Entrypoints

This repo includes lightweight entrypoints for common AI development tools:

- [`AGENTS.md`](./AGENTS.md) is the generic instruction file.
- [`CLAUDE.md`](./CLAUDE.md) points Claude Code at the same workflow.
- [`.cursor/rules/ai-dev-workflow.mdc`](./.cursor/rules/ai-dev-workflow.mdc) exposes the workflow to Cursor.
- [`opencode.md`](./opencode.md) gives OpenCode the same operating rules.
- [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json) lists the stable skills for Claude-compatible skill installers.
- [`.agents/skills`](./.agents/skills) exposes thin native skill adapters for agents that discover the open Agent Skills layout.
- [`openspec`](./openspec) stores OpenSpec changes, archived changes, and consolidated specs.
- [`.codex/skills`](./.codex/skills), [`.claude/commands`](./.claude/commands), [`.claude/skills`](./.claude/skills), [`.cursor/commands`](./.cursor/commands), [`.cursor/skills`](./.cursor/skills), [`.opencode/commands`](./.opencode/commands), and [`.opencode/skills`](./.opencode/skills) expose generated OpenSpec commands and skills.

## Maintenance Checks

Run these checks after changing skills, entrypoints, OpenSpec surfaces, or workflow documentation:

```bash
openspec validate --all --strict --no-interactive
python3 scripts/validate-workflow.py
git diff --check
```

[`scripts/validate-workflow.py`](./scripts/validate-workflow.py) verifies that skill front matter is valid, local Markdown links resolve, delegated entrypoints point back to `AGENTS.md`, skill references stay complete, and Claude plugin metadata matches the skill directories.

OpenSpec CLI usage requires Node.js `20.19.0` or newer. The repo validation script does not require Node; it only checks the checked-in workflow contract.

## Skill Design Rules

- Skills are small and composable.
- A skill describes behavior, not a tool-specific script.
- Repo facts are discovered from the filesystem before asking the user.
- Tests should verify public behavior rather than implementation details.
- Agent output should be concise, evidence-based, and explicit about assumptions.

## Domain Language

The shared terms for this repo live in [`CONTEXT.md`](./CONTEXT.md). Keep that file as a glossary, not a specification. Implementation decisions belong in plans, issues, PRs, or ADRs when a future reader needs the trade-off.
