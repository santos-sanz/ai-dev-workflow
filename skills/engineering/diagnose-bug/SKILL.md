---
name: diagnose-bug
description: Diagnose bugs, flakes, and regressions through reproduce, minimize, hypothesize, instrument, fix, and regression-test.
---

# Diagnose Bug

Use this skill when something is broken, failing, flaky, slow, or otherwise not understood.

## Native Integration

Use native debug skills, subagents, terminal output, browser tools, traces, and logs when they exist. This skill defines the evidence standard: reproduce the real symptom, minimize it, test ranked hypotheses, instrument deliberately, and lock down the fix.

## Workflow

1. **Build a feedback loop.**
   - Prefer a failing test.
   - Otherwise use a CLI command, HTTP script, browser script, captured trace, replay fixture, or minimal harness.
   - For flaky bugs, raise the reproduction rate with repetition, stress, seeds, or narrowed timing.

2. **Reproduce the reported symptom.**
   - Confirm the loop shows the same failure the user described.
   - Capture the exact error, wrong output, timing, or visible symptom.
   - Do not fix a nearby but different issue.

3. **Minimize.**
   - Reduce the input, scenario, or code path until the signal is as small and fast as practical.
   - Keep the minimized repro connected to the real failure mode.

4. **Hypothesize.**
   - Write three to five ranked, falsifiable hypotheses.
   - Each hypothesis must predict what evidence would confirm or reject it.

5. **Instrument deliberately.**
   - Change one variable at a time.
   - Prefer debugger or targeted probes over broad logging.
   - Tag temporary logs or probes so they are easy to remove.

6. **Fix and lock down.**
   - Convert the repro into a regression test when a correct seam exists.
   - Apply the smallest correct fix.
   - Re-run the minimized repro, the original repro, and relevant broader checks.

7. **Clean up.**
   - Remove temporary instrumentation.
   - Delete throwaway harnesses unless they became useful tests.
   - State the root cause in the final response or PR.

## Done When

- The original symptom no longer reproduces.
- A regression check exists or the lack of a correct seam is documented.
- Temporary debugging artifacts are removed.
- The root cause and verification evidence are clear.
