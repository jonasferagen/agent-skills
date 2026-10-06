# Consumer controller trial — 2026-10-07

Fresh-context trial for revision 0.6.0's import contract. The evaluator defined a
new `queue` service in a consumer fixture that holds no installation and resolves
a `primary` route to one, entering from the fixture's own `AGENTS.md` with no
expected route supplied. Nothing was installed, started or enabled.

## Result

The changed route was reached without prompting. Actual order:
`AGENTS.md` → `project.md` → `project-docs/foundation.md` → the stub service index
→ `COLLECTION.md` → `references/repository-services.md` → `references/extension.md`
→ `references/runtime-helpers.md` → `references/service-definition.md` → the three
templates → `skills/runtime-operations/SKILL.md` → `scripts/runtimeApi.py` →
`templates/repository-docs/tools/service_runtime.py` → `scripts/serviceControl.py`
→ `skills/service-boundaries/SKILL.md` → `scripts/validate-services.py` →
`scripts/service_format.py`.

The contract was applied as written: the loader and dispatcher were copied
verbatim, the offered interface was named rather than assumed, discovery was kept
in its own function, and no controller appended the installed path itself. The
evaluator correctly skipped `installation.md`, the installation checker,
provenance, the credential and backup helpers and every test directory, which
ordinary consumption does not need. It declined to invent the worker's command,
recorded it as an open fact owned elsewhere, and reported the structural check's
stated limits instead of claiming readiness. It identified the absent
implementation-conventions owner the convention requires and recorded the
conventions in the instruction owner that does exist.

## Findings

- **Resolved a declared relative route against the wrong directory**, caught it
  with its own test and fixed it. Two of three existing consumers had made the
  same choice independently, one surviving only because the declared target is
  absolute. Addressed in `references/runtime-helpers.md` in the same revision.
- **`references/extension.md` read as largely restating the repository
  convention** for a consumer whose project had already declared adoption. It was
  classified useful rather than required. The overlap between adoption and
  convention is not yet resolved; no change was made on one trial.
- **The binding surface was learned by reading `serviceControl.py`**, 687 words of
  source, to decide `command`, `port` and `health_service`. No reference documents
  which fields a project binding supplies and what omitting one selects. This is
  the largest unnecessary read in the trial and remains open.
- **`service-boundaries` applied only in part.** The collection routes a service
  transition to both members; the evaluator found the member HTTP/MCP-centric and
  took one sentence from it for a transport-free worker. Consistent with the
  review that prompted this revision; not addressed here.

## Limits

One trial, one fixture, one task shape. Cold entry and deeper-guidance cases were
exercised; nearby-work and source-authoring cases were not, and are unexercised
limitations. The fixture's placeholder service carried a non-functioning
controller, which the structural checker accepts and the evaluator correctly
identified as something the convention forbids shipping — a reminder that the
check admits a stub. No runtime state was changed, so no control action,
readiness success or recovery path is evidenced.
