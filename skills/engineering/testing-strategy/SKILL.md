---
name: testing-strategy
description: Design automated tests that reduce uncertainty, cover real contracts, and avoid brittle coverage theater.
---

# Testing Strategy

Use this skill when choosing what tests to add, update, or trust for a feature, fix, refactor, or AI-generated code change.

## References

- Source synthesis: [BettaTech, "¿Estamos haciendo MAL los tests de software?"](http://www.youtube.com/watch?v=PQYeWODU8Lo).
- Complementary strict review lens: [thermo-nuclear-code-quality-review](https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md), especially for spotting test suites that preserve incidental complexity, over-mock brittle internals, or bless spaghetti growth.

## Native Integration

Use the active agent's native terminal, test runner, browser, debugger, coverage, container, and CI tooling for the mechanics. This skill owns the testing decisions: what uncertainty matters, which behavioral contract should be locked down, and which test level gives the strongest useful signal with acceptable maintenance cost.

## Principles

- Tests are a safety net for future change, not just a present-tense happy-path check.
- Prefer public behavior and stable contracts over implementation details.
- Manual testing does not scale as the system grows; automate repeatable confidence checks.
- Use unit tests for isolated pure logic, integration tests for component or service contracts, and end-to-end tests for critical user journeys.
- Prefer integration tests against real empty dependencies, containers, or local services when mocks would hide contract drift.
- Use mocks sparingly and deliberately; every mock is a maintenance promise about another system's behavior.
- Treat coverage as a diagnostic signal, not a target. High coverage with weak assertions is false confidence.
- Prioritize failure paths, edge cases, boundary conditions, and regressions before adding redundant happy-path coverage.
- Treat tests as the executable contract that constrains AI-generated changes.

## Workflow

1. **Name the uncertainty.**
   - State the behavior, user path, API contract, data invariant, or regression that could break.
   - Identify who or what relies on that contract.

2. **Choose the highest useful test level.**
   - Prefer an integration or endpoint-level test when it can verify the real contract without excessive setup.
   - Use a unit test when the behavior is pure, isolated, or hard to reach through a higher-level seam.
   - Use an end-to-end test when the risk lives in real user workflow wiring, browser behavior, auth, routing, or cross-service coordination.

3. **Decide what must stay real.**
   - Keep databases, queues, filesystems, HTTP services, or time real when the contract with that dependency is the risk.
   - Use containers, test databases, fixtures, or local fakes before broad mocks when practical.
   - If a mock is necessary, document the reason in the test name, fixture, or nearby setup.

4. **Cover the risk matrix.**
   - Start with the most important error path, boundary, permission failure, invalid input, race, or regression case.
   - Add the happy path after the behavior's failure modes are constrained.
   - Avoid adding tests that only execute lines without asserting meaningful outcomes.

5. **Run the smallest meaningful loop.**
   - Run the focused test and confirm it fails for the expected reason when adding coverage.
   - Make the smallest change needed to pass.
   - Keep the focused check green while cleaning up names, fixtures, and setup.

6. **Review test quality.**
   - Check that assertions describe outcomes, not internal steps.
   - Remove brittle coupling to private helpers, incidental file layout, or arbitrary call counts.
   - Watch for structural smells from the thermo-nuclear review lens: sprawling setup, special-case branches, cast-heavy fixtures, thin wrappers, or tests that force poor production abstractions.

## Done When

- The test suite reduces a named uncertainty that matters to users, callers, or maintainers.
- The chosen test level matches the risk and avoids unnecessary brittleness.
- External contracts are verified with real dependencies where feasible, or mocks are explicit and justified.
- Error paths, edge cases, and regressions are covered before shallow coverage targets.
- The final checks pass and the remaining testing gaps are stated plainly.
