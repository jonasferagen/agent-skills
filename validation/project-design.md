# Project design extraction — 2026-10-08

## Scope

Standalone project-design 0.1.0 extracts the task workflow from
project-foundation `bb95633f4e94c00053b6d43a7a92c493a4698636`, whose native
skill was 5.0.0. Responsibilities, conceptual models, workflow design and
integration choices remain. Legacy foundation tables, document trees, browsing
formats and mandatory companion routes are removed. The consuming project owns
document shape, location and adopted engineering capabilities.

## Informed author walkthroughs

The author already knew the legacy skill and expected behavior. These are
informed route and artifact reviews, not independent discovery trials. They make
no spontaneous-selection or total-context claim.

| Request | Route reviewed | Preserved outcome |
| --- | --- | --- |
| Shape a repository whose output is design decisions | Entry point → workflows | A manual document process is a valid mechanism; no service, runtime or deployment is inferred. |
| Distinguish a lending title, physical copy and loan | Entry point → conceptual-models | Independent lifecycles explain identity; a returned damaged copy need not be available. No database schema is selected. |
| Separate runtime code from authored content | Entry point, concrete normal/change cases | Trace content-only and runtime changes, preparation writes and compatibility before choosing another repository or container. |
| Compare ways to execute a selected operation | Entry point → integrations | Compare manual/local options, authority, effects and evidence; no provider guarantee or execution permission follows from a proposal. |
| Interpret one existing handoff term | Existing agreement or project-contracts | No architecture redesign or full integration pass. |
| Correct a label in a current guide | Existing document and writing guidance | No design reconstruction or format migration. |

The real consumer being established is tessera-design: a local design-process
and system-design owner that inherits Tessera's shared policy. Its manual process
belongs in current documentation; unimplemented target-system designs have a
separate root-level home. Its existence supplies no product architecture.

A representative process trace follows a scoped question, evidence gathering,
draft design, a normal/exception walkthrough, decision under existing authority
and handoff to a separate implementation owner. If evidence is missing, only the
dependent choice waits; if a design changes an adopted obligation, the policy
owner is consulted. Document adoption does not establish implementation.

## Validation and limits

The package and skill-creator validators pass. All three references remain
reachable from the entry point and contain no distribution-relative links.
The full source check passed: five checks, four suites, 157 tests and no skips.
`git diff --check` passed. No release tag was created.
Current provider behavior was not investigated because no provider selection is
part of this extraction. No implementation, service or document parser is added.
Independent cold-entry and nearby-negative activation remain unverified.

The reusable boundary is responsibility versus packaging: a design owner can
produce decisions and artifacts without acquiring a runtime. The optional
distribution collection owns templates; the standalone skill owns reasoning.
