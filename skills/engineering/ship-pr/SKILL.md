---
name: ship-pr
description: Prepare completed work for a pull request with final verification, commit hygiene, push, and PR description.
---

# Ship PR

Use this skill when the implementation is complete and the user wants the work committed, pushed, and opened as a pull request.

## Native Integration

Use native git, GitHub, PR, branch, and review integrations when the active agent provides them. This skill defines the shipping checks: intended files only, final verification, concise PR story, compatibility notes, assumptions, and known risks.

## Workflow

1. **Confirm scope.**
   - Run `git status --short`.
   - Review the diff and identify intended files.
   - Do not stage unrelated user changes.

2. **Verify.**
   - Run the smallest checks that prove the work.
   - Run broader checks when the blast radius justifies them.
   - Record any checks that cannot run and why.

3. **Prepare the commit.**
   - Stage only intended files.
   - Use a concise commit message that names the user-visible change.
   - Avoid mixing unrelated cleanup into the commit.

4. **Push.**
   - Push the current branch to the remote.
   - If the branch does not exist, publish it with upstream tracking.

5. **Open the PR.**
   - Target the repo's default branch unless instructed otherwise.
   - Include summary, validation, compatibility notes, and known risks.
   - Mark as draft when the user asked for a draft or when verification is incomplete.

## PR Description Shape

```markdown
## Summary
- Main change 1
- Main change 2

## Validation
- Check or command run
- Manual review performed

## Notes
- Assumptions, limitations, or follow-up risk
```

## Done When

- Only intended files are committed.
- The branch is pushed.
- A PR URL is available.
- The user has a concise summary of changes and validation.
