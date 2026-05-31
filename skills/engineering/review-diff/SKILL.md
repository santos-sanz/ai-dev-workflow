---
name: review-diff
description: Review a branch, PR, or working tree against the intended spec and the repo's documented standards.
---

# Review Diff

Use this skill when reviewing changes before merge or before handing work back to a user.

## Workflow

1. **Choose the comparison point.**
   - Use the commit, branch, tag, or PR base provided by the user.
   - If none is provided, default to the merge base with the main branch when that is obvious.

2. **Collect review inputs.**
   - Diff and commit list.
   - Original plan, issue, PRD, user request, or acceptance criteria.
   - Repo standards such as `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, ADRs, contributing docs, and formatter or test config.

3. **Review against the spec.**
   - Find required behavior that is missing or partial.
   - Find behavior that was not requested and increases scope or risk.
   - Check edge cases and failure modes called out by the spec.

4. **Review against standards.**
   - Find violations of documented project rules.
   - Prefer concrete bugs, regressions, maintainability risks, and missing tests over style commentary.
   - Do not repeat issues already enforced by tooling unless the tooling is failing.

5. **Report findings first.**
   - Order by severity.
   - Cite file and line when possible.
   - Include open questions and residual test gaps after findings.

## Finding Shape

```markdown
- [P1] Short title
  File and line. Explain the bug or risk, why it matters, and what would fix it.
```

Use `P0` for release blockers, `P1` for serious defects, `P2` for normal issues, and `P3` for minor improvements.

## Done When

- The review clearly says whether blocking issues were found.
- Findings are actionable and grounded in the diff.
- Missing spec or missing verification is explicitly called out.
