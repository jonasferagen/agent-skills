# Establish or review policy

Start with existing instructions, policy, the requested outcome and the relevant
design and operating owners. Keep adequate policy and stronger commitments. Find
the missing decisions by tracing actual users, state and actions; do not invent
rules to fill a document template.

## Discover consequential facts

Use these axes as prompts during establishment or a substantive adequacy review.
They are not a required table or a questionnaire to repeat for every task.

| Axis | Facts that affect requirements |
| --- | --- |
| Phase and scope | Current outcome, included capabilities and deliberately deferred scope |
| Intended lifetime | Disposable experiment, evolving system or maintained service; disposal and handoff expectations |
| Users and reliance | Who uses it, what they depend on and who supports them |
| Data | Synthetic or real, sensitivity, ownership, replaceability and retention |
| Exposure and authority | Local or public access, identities, external writes, spending and unattended actions |
| Compatibility | Existing consumers, interfaces, retained state and upgrade commitments |
| Recovery | Accepted loss and downtime, recovery responsibility and required evidence |

Separate the current phase and useful outcome from possible future capabilities.
Keep deferred implementation in the project's planning home, with a revisit
condition when useful. Do not make every uncertainty an immediate work item.
An early phase does not waive obligations for real data, external actions or
existing consumers. Local use does not imply disposable state.

Scope facts to the relevant repository, service or environment when they differ.
Trace requirements across boundaries: an isolated test environment and a shared
maintained environment can have different data and recovery guarantees. Do not
inspect live accounts or systems merely to fill a profile; use available evidence
and identify the decisions the authorized task actually needs.

## Derive requirements

Connect each consequential fact or adopted decision to the required outcome and
the owner that supplies it. Consider failure cases the axes do not expose. Record
what is known, decided or unresolved and identify affected work. Assumptions need
an explicit scope; a label such as "prototype" establishes no blanket exemption.

A rule states its scope, required outcome and reason. Name the deciding owner
and how compliance is judged: a command, a reader or both. Link existing checks
and their limits. Keep mechanisms in their design or operating owner unless the
mechanism itself is the adopted constraint.

An exception identifies the rule and affected scope, reason, deciding owner and
review condition. It takes effect through the project's existing authority;
preserve standing authorization and stronger commitments. A proposed exception
does not erase a requirement.

Separate missing policy decisions from missing proof of an established rule.
For each material unknown, identify who can decide, what depends on the answer
and the evidence needed. Preserve established requirements while those questions
remain open. Use [changes](changes.md) when the review reveals changed facts or
obligations; assess their consequences before claiming readiness.
