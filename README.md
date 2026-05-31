# AI Dev Workflow Pack

A compact workflow pack for building software with AI development agents such as Codex, Claude Code, OpenCode, and Cursor.

The goal is not to recreate features that coding agents already provide. Modern agents already read repo instructions, edit files, run commands, manage approvals, expose plan/review modes, support skills or rules, and often ship PR workflows. This pack defines the thin process layer those tools do not reliably provide by default: when to clarify, what a decision-complete plan contains, how to keep implementation in verified vertical slices, what evidence belongs in debugging, and how to report assumptions and residual risk.

See [`NATIVE_CAPABILITIES.md`](./NATIVE_CAPABILITIES.md) for the current native-capability boundary and source links.

This pack is inspired by the small, composable skill style in [mattpocock/skills](https://github.com/mattpocock/skills), but it is intentionally adapted for this repo instead of vendored wholesale.

## Workflow

Use native agent features first. Use the smallest skill only for the process discipline that the native feature does not encode.

| Phase | Native feature to prefer | Pack responsibility | Skill |
| --- | --- | --- | --- |
| Clarify | Native chat, ask/read-only mode, question tools | Decide which questions actually change scope, behavior, interfaces, risk, or acceptance criteria | [`clarify-requirements`](./skills/engineering/clarify-requirements/SKILL.md) |
| Plan | Codex subagents, Claude Plan mode, OpenCode Plan agent, Cursor Ask/Plan/custom modes | Define the required shape of a decision-complete plan and visible assumptions | [`plan-implementation`](./skills/engineering/plan-implementation/SKILL.md) |
| Build | Agent file edits, terminal tools, test runners, run/verify commands | Keep implementation in one behavior-first vertical slice at a time | [`tdd-vertical-slice`](./skills/engineering/tdd-vertical-slice/SKILL.md) |
| Debug | Native debug skills, subagents, terminal output, browser/app tools | Require reproduction, ranked hypotheses, targeted instrumentation, and regression evidence | [`diagnose-bug`](./skills/engineering/diagnose-bug/SKILL.md) |
| Review | Native diff viewers, code-review skills, review UI, PR checks | Prioritize actionable findings against spec and repo standards | [`review-diff`](./skills/engineering/review-diff/SKILL.md) |
| Handoff | Native memory, checkpoints, conversation history, background-agent status | Create a portable summary only when work crosses sessions, tools, or agents | [`handoff`](./skills/productivity/handoff/SKILL.md) |
| Ship | Native git/PR commands, GitHub integrations, PR UI | Confirm intended scope, verification evidence, assumptions, and residual risk | [`ship-pr`](./skills/engineering/ship-pr/SKILL.md) |

## Default Operating Loop

1. **Ground in the repo.** Read the files, tests, docs, and git state that can answer factual questions.
2. **Use native capabilities first.** Prefer the current agent's built-in plan mode, subagents, skills, diff review, command execution, memory, and PR integrations before creating custom workflow artifacts.
3. **Clarify only what matters.** Ask questions only when the answer changes scope, behavior, interfaces, or risk.
4. **Plan to a decision-complete level.** A different engineer or agent should be able to implement the plan without making product or architecture decisions.
5. **Implement one vertical slice at a time.** Prefer behavior-first tests and fast feedback over broad speculative edits.
6. **Keep evidence close.** Run the smallest meaningful check after each important step and report what passed or could not run.
7. **Review against both spec and standards.** A change can be well-written and still solve the wrong problem.
8. **Ship with a clean story.** The PR should explain intent, main changes, validation, and remaining risk.

## Workflow Quality Gates

Use these gates to catch common blind spots before, during, and after work:

- **Intent is explicit.** The agent can state the goal, affected users or callers, success criteria, constraints, assumptions, and out-of-scope work.
- **Safety is checked.** The agent has inspected git state, protected unrelated user changes, and identified secrets, destructive commands, irreversible external side effects, and public interface changes before acting.
- **Execution is sliced.** The work uses the smallest applicable skill, proceeds in vertical slices, and keeps a repeatable feedback loop close to each change.
- **Compatibility is preserved.** `AGENTS.md` remains the source of truth, while Claude Code, OpenCode, Cursor, and plugin metadata stay synchronized with it.
- **Verification is repeatable.** The agent records commands run, checks passed, checks skipped, and remaining risk instead of relying on manual confidence.
- **Continuity is durable.** Decisions, assumptions, residual risks, and next steps are captured in the plan, handoff, PR description, or final response.

## Agent Entrypoints

This repo includes lightweight entrypoints for common AI development tools:

- [`AGENTS.md`](./AGENTS.md) is the generic instruction file.
- [`CLAUDE.md`](./CLAUDE.md) points Claude Code at the same workflow.
- [`.cursor/rules/ai-dev-workflow.mdc`](./.cursor/rules/ai-dev-workflow.mdc) exposes the workflow to Cursor.
- [`opencode.md`](./opencode.md) gives OpenCode the same operating rules.
- [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json) lists the stable skills for Claude-compatible skill installers.
- [`.agents/skills`](./.agents/skills) exposes thin native skill adapters for agents that discover the open Agent Skills layout.

## Maintenance Checks

Run these checks after changing skills, entrypoints, or workflow documentation:

```bash
python3 scripts/validate-workflow.py
git diff --check
```

[`scripts/validate-workflow.py`](./scripts/validate-workflow.py) verifies that skill front matter is valid, local Markdown links resolve, delegated entrypoints point back to `AGENTS.md`, skill references stay complete, and Claude plugin metadata matches the skill directories.

## Skill Design Rules

- Skills are small and composable.
- A skill describes behavior, not a tool-specific script.
- Repo facts are discovered from the filesystem before asking the user.
- Tests should verify public behavior rather than implementation details.
- Agent output should be concise, evidence-based, and explicit about assumptions.

## Domain Language

The shared terms for this repo live in [`CONTEXT.md`](./CONTEXT.md). Keep that file as a glossary, not a specification. Implementation decisions belong in plans, issues, PRs, or ADRs when a future reader needs the trade-off.
