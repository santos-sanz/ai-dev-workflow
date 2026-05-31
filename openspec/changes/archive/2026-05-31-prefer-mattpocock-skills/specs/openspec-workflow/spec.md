## ADDED Requirements

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
