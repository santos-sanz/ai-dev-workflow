# AI Dev Workflow Pack

Shared language for this repo. This file is a glossary only.

## Language

**Workflow Pack**:
A lightweight collection of documentation, agent entrypoints, and skills that define how AI development agents should work in a software repo.
_Avoid_: framework, platform, methodology

**Skill**:
A focused Markdown instruction that tells an agent how to handle one recurring workflow.
_Avoid_: script, automation, macro

**Agent**:
An AI development assistant operating in a codebase, such as Codex, Claude Code, OpenCode, or Cursor.
_Avoid_: bot, worker

**Clarification Loop**:
The conversation phase where the agent resolves goal, scope, constraints, success criteria, and trade-offs before planning or implementation.
_Avoid_: requirements gathering when referring to the iterative agent conversation

**Implementation Plan**:
A decision-complete description of what will be built, how it will be verified, and which assumptions are being used.
_Avoid_: outline, notes

**Vertical Slice**:
A narrow change that delivers one observable behavior end to end, including tests or another meaningful feedback signal.
_Avoid_: layer task, horizontal slice

**Feedback Loop**:
A fast, repeatable command, test, script, browser check, or manual procedure that proves whether the current behavior is correct.
_Avoid_: validation vibes, sanity check when the signal is not repeatable

**Compatibility Contract**:
The agreement that every tool entrypoint exposes the same workflow intent and skill set, with `AGENTS.md` as the source of truth.
_Avoid_: tool-specific fork, copied prompt

**Safety Check**:
A pre-action review of git state, user changes, secrets, destructive commands, irreversible external side effects, and public interface changes.
_Avoid_: permission check when the risk is broader than tool access

**Quality Gate**:
A concrete criterion that must be satisfied before work moves to the next phase, such as explicit success criteria or a repeatable verification command.
_Avoid_: best practice when the criterion is required for this workflow

**Native Capability Boundary**:
The line between what an agent or editor already provides as a built-in feature and what this workflow pack should define as process guidance.
_Avoid_: reimplementation plan, custom framework

**Handoff**:
A compact summary that lets another agent or future session continue the work without replaying the whole conversation.
_Avoid_: transcript, dump

## Relationships

- A **Workflow Pack** contains many **Skills**.
- An **Agent** uses a **Skill** during a specific phase of work.
- A **Clarification Loop** produces enough information for an **Implementation Plan**.
- An **Implementation Plan** is executed through one or more **Vertical Slices**.
- A **Feedback Loop** verifies each **Vertical Slice**.
- A **Quality Gate** catches a blind spot before the workflow advances.
- A **Compatibility Contract** keeps tool entrypoints aligned around the same **Skills**.
- A **Safety Check** protects the user and repo before an **Agent** acts.
- A **Native Capability Boundary** prevents the **Workflow Pack** from duplicating agent or editor features.
- A **Handoff** preserves unresolved context when the work cannot finish in one session.
