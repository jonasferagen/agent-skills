# What counts as merge evidence

Read this while verifying, and again before merging when time has passed since
the checks ran. [`change-workflow`](../SKILL.md) owns the boundary this evidence
is owed at: what merges is green, verified on the tree that will actually merge.

## Three things that look like merge evidence

- **A conflict-free merge is not a test result.** Git resolving the texts says
  nothing about the resulting behavior. If the base advanced or the tree changed,
  the resulting tree is what needs checking.
- **Focused branch verification does not verify the merged result.** It finds
  authoring defects early, which is why it runs while authoring; the merged tree
  still owes its own run.
- **A check that rewrites tracked content does not verify its input.** Its result
  describes the post-rewrite worktree, not the committed candidate that will
  merge, and the first run has already made its own failure irreproducible.
  Inspect and commit the repair through the normal lane, then run again on the
  committed tree. A project hook or check found rewriting a tracked file is a
  defect to report there, not a quirk to work around.

Report each check's command, exit status and useful result line. **A verdict
names what it measured:** a run that covered a subset of the suite says which
subset, and a check that could not run at all is a refusal rather than a silent
pass. Report an absent or un-runnable project check as friction to fix in that
project — never guess at a substitute, skip verification quietly, or invent a
scanner for the occasion.

## Freshness is two object IDs, not a second run

A verification result describes one tree at one moment. When the candidate or the
integration branch moves between the checks and the merge, the answer is to
synchronize and check again — never to run something different for reassurance.

Record both identities immediately after the final synchronization and before
running the project's canonical full check run:

```bash
gate_candidate=$(git rev-parse HEAD)
gate_integration=$(git rev-parse <integration-remote>/<integration-branch>)
git merge-base --is-ancestor "$gate_integration" "$gate_candidate"
```

The ancestry assertion is what makes the pair meaningful: it confirms the tree
about to be checked actually contains the integration point it claims.

Compare both immediately before merging:

```bash
git fetch <integration-remote>
test "$(git rev-parse HEAD)" = "$gate_candidate"
test "$(git rev-parse <integration-remote>/<integration-branch>)" = "$gate_integration"
```

Either comparison failing means the evidence is stale: synchronize and check the
resulting tree again. Re-running the checks without re-synchronizing establishes
nothing. The comparison only detects invalidation — it never substitutes for the
checks, authorizes a merge, or proves that a remote advance was harmless.

**The window is real even when no push is rejected.** Two lanes of one repository
share one merge target, so a second landing that merges there while these checks
run pushes first; this push then fast-forwards cleanly and publishes a
combination nothing verified. No push is rejected and nothing notices. Merge the
commit that was checked rather than a branch tip that moved during its own run,
and leave the rest for the next attempt.

## Why the check has to be nameable

A project with one composite check command makes freshness legible: the thing is
nameable, and everything else is explicitly not it. A project whose "full check"
is really one lane of a larger set will merge on partial evidence without anyone
deciding to.

Where a project narrows the run from the changed paths, the narrowing is that
project's to prove, not this lane's to assume: a path its selector cannot
classify takes the full run, a narrowed run names the lane it selected and what
it measured, and a selection that measured nothing is refused rather than
reported green.

## Markdown links and anchors

Where a project checks Markdown link integrity, use
[`remark-validate-links`](https://github.com/remarkjs/remark-validate-links)
through `remark-cli` with `--frail` rather than writing a link walker or a
heading-slug implementation of its own:

```text
<package-runner> remark --use remark-validate-links --frail <markdown-scope>
```

`--frail` makes warnings fail. Use the CLI rather than the Node API: the CLI also
validates heading anchors in other Markdown files. The plugin covers local files
and anchors; external URL availability and undefined reference definitions are
separate checks. Keep the stage reading the whole documentation scope rather than
only the changed paths, because a link breaks from a path appearing or
disappearing anywhere in the tree.
