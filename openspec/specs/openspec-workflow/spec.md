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
