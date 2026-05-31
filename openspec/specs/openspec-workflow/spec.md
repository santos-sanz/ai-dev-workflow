# openspec-workflow Specification

## Purpose
Define how OpenSpec fits into this workflow pack as a durable specification layer for changes that need reviewable requirements, cross-session continuity, or cross-agent handoff.
## Requirements
### Requirement: OpenSpec is available on supported agent surfaces
The workflow pack SHALL expose OpenSpec change workflows for Codex, Claude Code, Cursor, and OpenCode.

#### Scenario: Supported agent uses OpenSpec commands
- **WHEN** a supported agent loads this repository
- **THEN** the repository provides OpenSpec command or skill files for that agent

#### Scenario: Workflow validation checks OpenSpec surfaces
- **WHEN** maintainers run the workflow validation script
- **THEN** the script verifies that required OpenSpec directories are present

### Requirement: OpenSpec complements native capabilities
The workflow pack SHALL describe OpenSpec as a persistent specification layer that complements, rather than replaces, native agent capabilities.

#### Scenario: Small change can skip OpenSpec
- **WHEN** a requested change is small, clear, and low-risk
- **THEN** the workflow allows the agent to use native capabilities and the smallest applicable pack skill without creating an OpenSpec change

#### Scenario: Durable context uses OpenSpec
- **WHEN** a requested change needs reviewable requirements, cross-session continuity, or cross-agent handoff
- **THEN** the workflow directs the agent to use OpenSpec proposal, design, specs, tasks, and archive artifacts

### Requirement: Source of truth remains synchronized
The workflow pack SHALL keep `AGENTS.md` as the source of truth while documenting OpenSpec consistently across delegated entrypoints.

#### Scenario: Entrypoints point to the canonical workflow
- **WHEN** an agent reads `CLAUDE.md`, `opencode.md`, or Cursor rules
- **THEN** the entrypoint points back to `AGENTS.md` and describes OpenSpec in a way that does not conflict with the canonical workflow

#### Scenario: Maintenance guidance includes OpenSpec
- **WHEN** maintainers change OpenSpec-generated commands, skills, specs, or workflow entrypoints
- **THEN** the workflow instructs them to run the repo validation checks

### Requirement: Upstream Matt Pocock skills are preferred when available
The workflow pack SHALL instruct agents to use an installed `mattpocock/skills` skill when it directly matches the task and can be invoked safely by the active agent.

#### Scenario: Matching upstream skill is available
- **WHEN** a task maps directly to an installed upstream `mattpocock/skills` skill
- **THEN** the agent uses that skill before falling back to the local adapted workflow skill

#### Scenario: Upstream skill is unavailable
- **WHEN** the active agent cannot invoke a matching upstream `mattpocock/skills` skill
- **THEN** the agent uses the local skill in `skills/` or the native agent capability that best fits the task

### Requirement: Upstream skills are not hidden dependencies
The workflow pack SHALL avoid installing, vendoring, or configuring `mattpocock/skills` unless the user explicitly asks for that external side effect.

#### Scenario: Task only needs workflow guidance
- **WHEN** the user asks for ordinary implementation, review, debugging, or shipping work
- **THEN** the agent does not install or vendor upstream skill files without explicit approval

#### Scenario: User asks to install upstream skills
- **WHEN** the user explicitly asks to install or configure `mattpocock/skills`
- **THEN** the agent treats that as an external setup task and reports the files, commands, and assumptions involved
