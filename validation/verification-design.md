# Validation — Verification design

## Behavioral scenarios

These scenarios were reviewed against the instructions. These initial scenarios were author traces; they do not establish independent
activation.

| Request and context | Expected decision |
| --- | --- |
| A schema example parses, but a claim says two writers cannot both win | Require independent-session evidence for the race; keep the schema check for its own claim. |
| Unit and integration suites assert the same domain decision | Keep the decision assertion at the cheaper domain layer; use integration to show the public path reaches it. Confirm a retained check fails for a representative defect before removing another. |
| Two suites each build the same image and then use separate mutable databases | Consider reusing the built artifact while preserving isolated state; measure setup cost first. |
| A developer ran a focused test during implementation | Name it as focused feedback; do not report the milestone gate as complete. |
| Docker is unavailable for a required image check | Report that check as outstanding, not passed or silently skipped. |
| A project already defines a milestone gate | Preserve the gate until the project owner changes it; offer a costed alternative without silently weakening the commitment. |
| A settled suite has mock drift and weak assertions | Route the review to a test audit; this skill selects evidence for active changes. |
| A wrapper command is proposed solely because many commands exist | Require a concrete reduction in omission or setup cost; keep each command's coverage and result visible. |

## Source and limits

Derived from inspection of a local two-service project with contract examples,
embedded and native database tests, transport tests and image-backed integration
suites. The review found repeated build requests but did not measure their cost
or replace the test workflow. The skill therefore makes measurement and preserved
failure signals prerequisites for consolidation rather than claiming a speedup.

On 2026-09-30, the current tree passed the package validator (15 packages),
the system skill validator for `verification-design`, and `git diff --check`.

## Change-selected suites — 2026-10-11

Version 0.3.0 adds repository-owned input scopes and dependencies, selected from
the result after integration preparation. Tessera's existing landing command
ran the full game hook for documentation changes; that hook included Python
checks and Godot import/startup. No elapsed-cost claim is made.

Author fixture tests use real temporary Git repositories and observe the base
ref as well as commands: Markdown-only work selects docs; a code change includes
its document dependency after a concurrent base commit; a shared structured
contract selects both suites; renames classify both paths; unknown, executable,
symlink, empty and check-configuration changes use full checks. Failed selected
checks leave the base unchanged. Invalid maps and missing hooks refuse.
The retained project record identifies exact commands and results.

The second case is tessera-policy's optional docs hook without a suite map;
repositories without that hook preserve full verification. A nearby small cheap
suite need not gain a selector, and unclear dependencies retain broad checks.
These are author implementation evidence and routing traces, not spontaneous
skill activation or a measured maintenance-cost improvement. Jonas grants
full-gate amnesty for this pass; only affected tests and document/package checks
run. Full suites and Godot checks remain unrun.
