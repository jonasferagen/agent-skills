# Verification design scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| A schema example parses, but a claim says two writers cannot both win | Require independent-session evidence for the race; keep the schema check for its own claim. |
| Unit and integration suites assert the same domain decision | Keep the decision assertion at the cheaper domain layer; use integration to show the public path reaches it. Confirm a retained check fails for a representative defect before removing another. |
| Two suites each build the same image and then use separate mutable databases | Consider reusing the built artifact while preserving isolated state; measure setup cost first. |
| A developer ran a focused test during implementation | Name it as focused feedback; do not report the milestone gate as complete. |
| Docker is unavailable for a required image check | Report that check as outstanding, not passed or silently skipped. |
| A project already defines a milestone gate | Preserve the gate unless the user asks to change it; offer a costed alternative without silently weakening the gate (the checks a change must pass before it is accepted). |
| A settled suite has mock drift and weak assertions | Treat it as a separate review of the suite; this skill selects evidence for active changes. |
| A wrapper command is proposed solely because many commands exist | Require a concrete reduction in omission or setup cost; keep each command's coverage and result visible. |
| The pre-acceptance check runs the full service suite for a documentation-only change, and the project keeps a path-to-suite map (changed paths to suites) | Select suites from the affected inputs of the change as it will be merged: Markdown-only work selects the documentation checks; a code change includes its document dependency; a shared structured contract selects both suites. |
| A changed path is one the path-to-suite map cannot place: unknown, executable, a symlink, empty, or part of the check configuration | Full checks run; unclear dependencies keep broad checks. |
| A selected check fails | The change is reported as not verified and is not accepted on that run. |
| A path-to-suite map is invalid or a named check command is missing | Refused rather than skipped. |
| A repository has a small cheap suite and no path-to-suite map | No selector is required; full verification is preserved. |
