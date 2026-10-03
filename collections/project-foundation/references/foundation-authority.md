# Consult and preserve the foundation

Start at the local foundation, normally `project-docs/foundation.md`. Use
[foundation format and interpretation](foundation-format.md) for its declarations
and inherited values; reuse current readings. The format contains project data;
this collection owns how to interpret it. The project's adopted boundaries and
policy govern scope and engineering obligations. The overview records current
implementation choices and open options in a compact table; work queues, skill routes and evidence retain separate owners.
A glossary can own domain meanings once one is needed.

Policy is a compact table of current facts and adopted decisions. Project-policy
interprets it with boundaries; downstream requirements, repository working rules,
impact assessments and evidence retain their own document owners.

When one project spans repositories, use the declared shared owners and local
scope from [multi-repository foundations](multi-repository.md). Repository-local
text does not automatically supersede a shared decision.

Keep a short operating summary in project instructions, with each constraint
linked to its authoritative foundation document. Read that summary at task entry.
Consult policy for changes to data, access, environment, reliability or maintained
state; boundaries for responsibility or scope; and overview for application,
stack, resource or packaging decisions. Read a glossary only when relevant and
present. Routine edits within known constraints need no full foundation reread.

Revisit an affected owner when the task introduces a possible transition, such as
network access, real private data, another user or hosting. Check affected decisions
before completion. Reuse current readings; a link to a skill is not an instruction
to load every skill. Update the summary in the same change when its source changes.
Treat it as a derived copy and keep it to constraints that routinely affect work.

Apply established decisions within their stated scope. [Status, evidence and
authority](status-and-evidence.md) defines the unknown, proposed, adopted,
implemented and verified states and where authority to act comes from. Current
user decisions can change the foundation; record those changes and their
consequences so later work has the same authority. The documents do not override
the user's instructions or expand execution permissions.

When implementation and an adopted requirement disagree, identify the owner,
the requirement, the observed behavior and the affected work. Preserve the gap
until a deliberate decision or implementation change resolves it; do not edit the
policy merely to make the discrepancy disappear.

Use [project-policy](../skills/project-policy/SKILL.md) to assess changed
circumstances and requirements, including transition work and readiness evidence.
Use [source-of-truth](../skills/source-of-truth/SKILL.md) when definitions are
repeated, consumers disagree or checks must preserve alignment. Keep each decision
in its owning document and derive or check other appearances. Ordinary consultation
does not require an audit of every consumer.
