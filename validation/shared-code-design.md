# Validation — Shared code design

## Behavioral scenarios

These scenarios were reviewed against the instructions. No independent agent
trial or package extraction has been run for this new skill.

| Request and context | Expected decision |
| --- | --- |
| Two services carry an identical utility and drift check, but it rarely changes | Keep checked copies unless another concrete cost justifies a dependency. |
| A copied kit changes in both services every week and has stable public behavior | Compare coordination cost with a versioned package or generated copies, including publishing and consumer upgrades. |
| A proposed shared package imports a sibling checkout at build time | Reject that shape when independent builds are promised; require a declared obtainable dependency. |
| Similar handlers implement different domain rules | Keep domain ownership separate even if syntax looks alike. |
| Tests duplicate fixture creation while runtime code is independent | Consider shared test setup without imposing a runtime dependency. |
| A copy check passes today | Treat it as agreement today, then inspect change history for maintenance cost. |
| A versioned package is introduced | Test consumers independently and verify whether one can retain an older declared version. |
| One rule appears in SQL, application code and documentation | Identify its authoritative definition and consistency mechanism; file-level kit synchronization alone cannot settle it. |

## Source and limits

Derived from inspection of a two-service copied kit whose files and tests are
checked for exact agreement while each service builds on its own. The review did
not measure long-term change cost or try a package extraction. The skill records
the decision criteria, not a conclusion that this kit should move.

On 2026-09-30, the current tree passed the package validator (15 packages),
the system skill validator for `shared-code-design`, and `git diff --check`.
