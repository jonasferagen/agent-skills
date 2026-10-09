# Validation — Repository services

Retired on 9 October 2026 at 0.3.1, replaced by
[service-classes](service-classes.md). This page preserves historical evidence,
and its links to the former package's own files are history rather than live
routes. The classification and status judgment moved to service-classes, which
cites the trials below as its inherited evidence; the `services/` home, document
shapes, reserved actions, dispatcher, validator, `service-definition/v1` and the
adoption declaration left this repository for the installing distribution's
convention. See the [decision log](../DECISIONS.md) for the split and the
remaining owners.

The skill was assembled on 7 October 2026 from the service convention, structured
definition, templates, validator, parser and dispatcher that the
service-foundation collection had carried at collection level. Their trials and
decisions are recorded on the [service foundation page](service-foundation.md)
and under [its trials](service-foundation-trials/); this page is the standalone
skill's own record from that date. It records intended behaviour and actual
results; it establishes no consumer adoption.

## Intended selection — as of 0.3.1

Rows 1 and 4 moved to the distribution's convention with the layout and the
structured format; the rest carry over to service-classes, which restates them
without naming a home.


| Request | Should select | Should not select |
| --- | --- | --- |
| Adopt a `services/` home and its checks in a project | repository-services, then the service extension | service-boundaries or runtime-operations, unless the task also designs a service |
| Decide whether a capability is a running or scheduled service and write its guide | repository-services, then the convention | A process manager, transport or container choice |
| Report one line per instance across a project's checkouts | repository-services, the report section of the convention | Any mutation of runtime state; a project-wide start or stop is composed elsewhere |
| Opt an existing guide into `service-definition/v1` | repository-services, then the structured definition | Migration of guides that did not opt in |
| Decide service ownership or add a transport to an operation | service-boundaries | repository-services, which documents and checks what was decided |
| Choose credentials, lifecycle controls or helper imports for a controller | runtime-operations | repository-services beyond naming that owner |
| Correct a spelling error in an operating guide | Nothing from this skill | Service review, template adoption or the validator |

Installing the skill starts nothing. A local or scheduled service is still a
service; the templates ship no service-specific controller, and a stub that
appears operational is the defect the skill names.

## Bundled checks

The package shipped these checks until its retirement; `service-classes` ships
none, because nothing in the residue is structurally checkable. The four suites
and the dispatcher left with the layout, and the shared contract check described
below was removed from this repository when the artifacts it compared left it.

`python3 scripts/check.py` discovered the package's suite under `tests/`: 44
tests across the service format parser, the structural validator, the
dispatcher and the dispatcher template. They cover opt-in parsing and version
guards, unselected guides being skipped rather than failed, explicit member
selection for the project-wide report, rejection of `--checkout` with a named
service, and the template's option pass-through. The source gate's shared
contract check compares the dispatcher's report schema and state vocabulary
with their owner in runtime-operations and the convention's tables.

These are structural checks. They do not establish that a consuming project's
services run, that a guide's claims are true, or that a project-wide launch
behaves as the convention describes.

## History

| Date | Record |
| --- | --- |
| 2026-10-04 | Service document extension and structured definitions, moved from the project framework: [service foundation](service-foundation.md#optional-service-document-extension--2026-10-04) |
| 2026-10-07 | Scheduled service class and the `lifecycle` vocabulary: [scheduled service trial](service-foundation-trials/scheduled-service.md) and the [launch decision](service-foundation.md#2026-10-07--what-a-project-wide-launch-may-touch) |
| 2026-10-09 | Members named explicitly, 0.3.0: [service foundation](service-foundation.md#2026-10-09--members-are-named-not-read-out-of-a-document) |
| 2026-10-09 | Checked package copies, 0.3.1: [reference-sharing sweep](reference-sharing-sweep.md) |
| 2026-10-09 | Retired at 0.3.1; judgment kept as [service-classes](service-classes.md), layout and tooling to the distribution: [decision log](../DECISIONS.md) |

## Limits

No fresh-context routing trial has been run against the standalone package
since the flattening; the trials above exercised the same resources as
collection members entered through a collection entrypoint. The selection
table is intended behaviour, not measured discovery. The trial records describe
the dispatcher before 0.3.0 and are left as the observations they were.
