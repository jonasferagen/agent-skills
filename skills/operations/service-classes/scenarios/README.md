# Service classes scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| Decide whether a command, job or editor should become a service | Classify it here; a process manager, transport or container choice is another owner's decision. |
| Decide whether a service is running or scheduled and what it must prove | Running owes live readiness of one named instance; scheduled owes the last run's durable outcome. The consuming project's service convention assumes the class is already known. |
| Decide what a scheduled service's status must report | Schedule, last run and last success together, exiting nonzero with a named reason; it never reports `ready`, because readiness is not a property it has. |
| An operator wants a daily paid shipment of finished exports, and the export build takes a lock an author may hold | Schedule only the shipping; name the lock as an attended precondition nobody can promise for an unattended window. Bound the spend the policy chose rather than avoid cost as such. |
| A scheduled service writes its own schedule units | Expected, not a departure to defend: `start` is what installs the schedule. |
| Read a project-wide status whose rows look like failures | Read the state and class vocabularies; several distinct situations report `absent`, and a row's class says what a project-wide launch may start. Mutate no runtime state. |
| A status row carries a class value the reader does not recognise, or predates the class key | Read as unclassified; nothing acts on a class it cannot name, and the row is not dropped. |
| Adopt a `services/` home, its guide shape or its checks | The consuming project's own decision; this skill names no home. |
| Decide service ownership or add a transport to an operation | service-design; this skill classifies rather than designs the boundary. |
| Choose credentials, lifecycle controls or helper imports for a controller | runtime-operations, beyond naming that owner here. |
| Correct a spelling error in an operating guide | Nothing from this skill. |

Installing the skill starts nothing and adopts no layout. A local service is
still a service, and a scheduled service is still a service: having no listener
removes readiness, not lifecycle or ownership.

## Limits

- No routing trial has run against this package under its current name; the
  rename rests on a trial finding against the previous catalog row. The
  near-neighbours to separate are service-design, runtime-operations and
  the consuming project's service convention.
- The two vocabularies in `references/status-reports.md` are copies of a report
  producer's declarations that live with the consuming project's deployed code.
  They matched at the split and are unchecked here; re-establishing that
  comparison belongs where the code and the installed guidance live together.
