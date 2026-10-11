# Establish or review policy

Start with existing instructions, principles, policy, the requested outcome and the relevant
design and operating owners. Keep adequate policy and stronger commitments. Find
the missing decisions by tracing actual users, state and actions; do not invent
rules to fill a document template.

## Discover consequential facts

Use these axes as prompts during establishment or a substantive adequacy review.
They are not a required table or a questionnaire to repeat for every task.
Record the facts they surface with the project's operating-facts owner: its
environment declaration when it keeps one, otherwise the policy. Policy states
the constraints adopted because of those facts.

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

Check adopted defaults before drafting local statements. Use their requirements
by reference and record only what the project decides in addition or differently.
Group related decisions by the outcome a reader needs; one Git adoption decision
need not become separate policies for branches, verification, pushing and cleanup.
A recovery target or deliberate access exemption remains a project decision even
when conventions supply its implementation method. Removing a duplicate statement
does not relax the rule supplied by the adopted convention.

Establish the project's governing choices before deriving requirements. A new
project can adopt a principle from an explicit owner decision; it need not wait
for an implementation to exist. Record the tradeoff, scope, cost and conditions
that would require reconsideration. Examples such as accepting breaking changes
to accelerate exploration illustrate choices; they adopt nothing for a consumer.

Connect each applicable principle and consequential fact or adopted decision to the required outcome and
the owner that supplies it. Consider failure cases the axes do not expose. Record
what is known, decided or unresolved and identify affected work. Assumptions need
an explicit scope; a label such as "prototype" establishes no blanket exemption.

A rule states its scope, required outcome and reason. Name the deciding owner
and how compliance is judged: a command, a reader or both. Link existing checks
and their limits. State what could change its applicability. "No application
login required" is a scoped policy choice, not a deduction from "one user";
"simple backups" needs an agreed retained-data scope and acceptable loss before
an implementation can be judged. Do not invent numerical targets. Keep mechanisms in their design or operating owner unless the
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
