# Validation — Service classes

Scope boundaries worth testing for
[service-classes](../skills/operations/service-classes/SKILL.md), created on
9 October 2026 from the judgment half of the retired `repository-services`
package. Its inherited evidence is on the
[repository-services page](repository-services.md), the
[service foundation page](service-foundation.md) and under
[its trials](service-foundation-trials/); the layout, dispatcher, validator and
structured format those trials also exercised are no longer in this repository.
This page records intended behaviour and actual results; it establishes no
consumer adoption.

## Intended selection

| Request | Should select | Should not select |
| --- | --- | --- |
| Decide whether a command, job or editor should become a service | service-classes | A process manager, transport or container choice |
| Decide whether a service is running or scheduled and what it must prove | service-classes | The distribution's service convention, which assumes the class is known |
| Decide what a scheduled service's status must report | service-classes | A live readiness probe, which this class does not have |
| Read a project-wide status whose rows look like failures | service-classes, the status-reports reference | Any mutation of runtime state |
| Adopt a `services/` home, its guide shape or its checks | The installing distribution's service convention | service-classes, which names no home |
| Decide service ownership or add a transport to an operation | service-boundaries | service-classes, which classifies rather than designs the boundary |
| Choose credentials, lifecycle controls or helper imports for a controller | runtime-operations | service-classes beyond naming that owner |
| Correct a spelling error in an operating guide | Nothing from this skill | Service review or classification |

Installing the skill starts nothing and adopts no layout. A local service is
still a service, and a scheduled service is still a service: having no listener
removes readiness, not lifecycle or ownership.

## Bundled checks

The package ships none. Nothing in it is structurally checkable: it states which
class a service belongs to and what that class owes, and no validator can
establish that a project's answer is right. The four suites that covered the
format parser, structural validator, dispatcher and dispatcher template left
with those artifacts, and the shared-contract comparison that checked the state
and class tables against a producer's declarations was removed from this
repository when the producer left it.

The two vocabularies in
[status reports](../skills/operations/service-classes/references/status-reports.md)
are therefore unchecked here. They were byte-equal to `ServiceReport`'s
declarations at `4170d2b`, verified at the split, and the comparison is worth
re-establishing in the distribution that will hold the code and the installed
guidance together.

## Limits

No routing trial has been run. The package is new, carries the `(draft)` marker,
and its rename was justified by a trial finding against the old catalog row
rather than by evidence that requests now reach the new one. Three
near-neighbours must be separated — this package, `service-boundaries` and
`runtime-operations` — and so must this package against the distribution's
service convention, which is where a layout question should land. Both catalogs
present the same set, so that trial belongs with the distribution's, as the
Docker split's did.

The carried passages were kept close to verbatim rather than rewritten, and no
independent passage-by-passage comparison against `4170d2b` was made.
