---
name: tdd-vertical-slice
description: Build features or fixes one behavior-first vertical slice at a time using a red-green-refactor loop.
---

# TDD Vertical Slice

Use this skill when implementing behavior that can be verified with tests or another repeatable feedback loop.

## Native Integration

Use native file-editing, terminal, browser, run, verify, and test tools for the mechanics. This skill owns the implementation cadence: one observable behavior, one feedback signal, one minimal implementation, then cleanup.

## Principles

- Test public behavior, not implementation details.
- Prefer one end-to-end or integration-style behavior test over many shallow implementation tests.
- Work in vertical slices: one behavior, one failing signal, one minimal implementation, one cleanup pass.
- Do not write all tests first and all implementation second.

## Workflow

1. **Find the feedback loop.**
   - Use existing test commands when available.
   - If no test seam exists, create the smallest meaningful seam at the highest useful level.
   - For UI work, include browser or DOM verification when practical.

2. **Pick one behavior.**
   - Choose the smallest observable behavior that moves the feature forward.
   - Name the behavior in user or caller language.

3. **Red.**
   - Add one failing test or repeatable check for that behavior.
   - Run it and confirm it fails for the expected reason.

4. **Green.**
   - Add the smallest implementation that passes the check.
   - Run the focused check again.

5. **Refactor.**
   - Improve names, remove duplication, and align with local patterns.
   - Keep the feedback loop green after each meaningful cleanup.

6. **Repeat.**
   - Move to the next behavior only after the current slice is green.

## Done When

- Every implemented behavior has a meaningful feedback signal.
- All relevant checks pass.
- The final code follows local patterns and avoids speculative features.
