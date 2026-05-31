# AI Dev Workflow Pack

A compact workflow pack for building software with AI development agents such as Codex, Claude Code, OpenCode, and Cursor.

The goal is not to make agents autonomous by hiding the engineering process. The goal is to give agents a simple, repeatable way to do normal software engineering work: clarify the request, plan the change, build in small verified slices, diagnose failures with evidence, review the diff, hand off context, and ship a pull request.

This pack is inspired by the small, composable skill style in [mattpocock/skills](https://github.com/mattpocock/skills), but it is intentionally adapted for this repo instead of vendored wholesale.

## Workflow

Use the smallest skill that fits the current job. Skills can be used by a human as prompts, by an agent as operating instructions, or by a tool that supports skill installation.

| Phase | Use when | Skill |
| --- | --- | --- |
| Clarify | The request is underspecified, high-risk, or product-heavy | [`clarify-requirements`](./skills/engineering/clarify-requirements/SKILL.md) |
| Plan | The work needs implementation decisions before editing code | [`plan-implementation`](./skills/engineering/plan-implementation/SKILL.md) |
| Build | You are adding behavior or fixing a bug with tests | [`tdd-vertical-slice`](./skills/engineering/tdd-vertical-slice/SKILL.md) |
| Debug | Something is broken, flaky, slow, or hard to explain | [`diagnose-bug`](./skills/engineering/diagnose-bug/SKILL.md) |
| Review | A branch, PR, or working tree needs technical review | [`review-diff`](./skills/engineering/review-diff/SKILL.md) |
| Handoff | Another agent or future session must continue the work | [`handoff`](./skills/productivity/handoff/SKILL.md) |
| Ship | The work is ready to commit, push, and open a PR | [`ship-pr`](./skills/engineering/ship-pr/SKILL.md) |

## Default Operating Loop

1. **Ground in the repo.** Read the files, tests, docs, and git state that can answer factual questions.
2. **Clarify only what matters.** Ask questions only when the answer changes scope, behavior, interfaces, or risk.
3. **Plan to a decision-complete level.** A different engineer or agent should be able to implement the plan without making product or architecture decisions.
4. **Implement one vertical slice at a time.** Prefer behavior-first tests and fast feedback over broad speculative edits.
5. **Keep evidence close.** Run the smallest meaningful check after each important step and report what passed or could not run.
6. **Review against both spec and standards.** A change can be well-written and still solve the wrong problem.
7. **Ship with a clean story.** The PR should explain intent, main changes, validation, and remaining risk.

## Agent Entrypoints

This repo includes lightweight entrypoints for common AI development tools:

- [`AGENTS.md`](./AGENTS.md) is the generic instruction file.
- [`CLAUDE.md`](./CLAUDE.md) points Claude Code at the same workflow.
- [`.cursor/rules/ai-dev-workflow.mdc`](./.cursor/rules/ai-dev-workflow.mdc) exposes the workflow to Cursor.
- [`opencode.md`](./opencode.md) gives OpenCode the same operating rules.
- [`.claude-plugin/plugin.json`](./.claude-plugin/plugin.json) lists the stable skills for Claude-compatible skill installers.

## Skill Design Rules

- Skills are small and composable.
- A skill describes behavior, not a tool-specific script.
- Repo facts are discovered from the filesystem before asking the user.
- Tests should verify public behavior rather than implementation details.
- Agent output should be concise, evidence-based, and explicit about assumptions.

## Domain Language

The shared terms for this repo live in [`CONTEXT.md`](./CONTEXT.md). Keep that file as a glossary, not a specification. Implementation decisions belong in plans, issues, PRs, or ADRs when a future reader needs the trade-off.
