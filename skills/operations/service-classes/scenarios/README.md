# Service classes scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| Decide whether a command, job or editor should become a service | Classify it here; a process manager, transport or container choice is not made here. |
| Decide whether a service is running or scheduled and what it must prove | Running owes live readiness of one named instance; scheduled owes the last run's durable outcome. |
| Decide what a scheduled service's status must report | Schedule, last run and last success together; it never reports `ready`, because readiness is not a property it has. It exits 0 only when the schedule is active and the last run succeeded; a failed last run reports `failed` with the last success as an attention and exits nonzero. |
| An operator wants a nightly database dump, and the dump is only safe inside a maintenance window people agree on | Schedule the dump only inside a window that is fixed in advance; name the window as an attended precondition the unattended run cannot check, and record what the run may read, write and delete. |
| A scheduled service writes its own schedule units | Expected, not a departure to defend: `start` is what installs the schedule. |
| A project already has its own status words | Keep them and map each onto the default meanings; do not rename them to this skill's words. |
| Read a project-wide status whose rows look like failures | Read the state and lifecycle vocabularies; several distinct situations report `absent`, a deliberately stopped service exits nonzero without a fault, and a row's lifecycle says what a bulk start may start. Change no runtime state. |
| A status row carries a lifecycle value the reader does not recognise, or has none | Read as unclassified; nothing acts on a class it cannot name, and the row is not dropped. |
| Choose where service documents live or how guides are shaped | The project's own choice; this skill names no home. |
| Decide service ownership or add a transport to an operation | The service-design skill, which covers service interfaces and storage ownership, or the project's own decision where it is not installed; this skill classifies rather than designs the boundary. |
| Choose credentials, lifecycle controls or helper imports for a controller | The project's own choice; this skill states only what a status must report. |
| Correct a spelling error in an operating guide | Nothing from this skill. |

Installing the skill starts nothing and adopts no layout. A local service is
still a service, and a scheduled service is still a service: having no listener
removes readiness, not lifecycle or ownership.

## Limits

- The nearest neighbour to separate in routing is service-design, the skill that
  covers service interfaces and storage ownership.
