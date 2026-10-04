# Versioned process format — 4 October 2026

Project-foundation 1.5.0 adds an opt-in `project-process/v1` Markdown contract,
shared parser and document-check integration. The process template defaults to
this structure. Existing unversioned flat pages and named process entries remain
valid; installing the collection does not migrate them. Project-docs is 6.3.0.
This is an unreleased source revision; no release tag or remote push is implied.

The format fixes five facts, identifies semantic roles without renaming headings,
and supplies stable step/handoff keys independent of diagram labels. Explicit
handoffs distinguish transfer, feedback and specialization. The generic parser
contains no Forge metadata, repository names, UI or execution behavior. Consumers
must resolve links and retain parser provenance and scoped statuses.

## Verification

The complete `python3 scripts/check.py` run passed all six package/helper checks,
with no failed or skipped tests. Package checks cover all declared installations;
the complete project-foundation inventory has 91 files and nine members. Twelve new
parser tests cover source locations, legacy/fenced/commented examples, unsupported
versions, exact facts, missing/duplicate/unattached roles, keys, incomplete rows,
Detail links, relation kinds, explicit unknown/no-handoff cases and duplicate
tables. Further negative controls reject malformed extra role markers and
None/Unknown declarations that would otherwise hide a handoff table. A document-check regression confirms selected-format rejection reaches
the public managed-home check. Existing layout tests remain passing.

The first full run found two unresolved Markdown template placeholder links;
the template now uses fillable link-cell placeholders, with the final single-link
rule supplied by the format reference. A test initially used invalid nested HTML
comments; its fixture was corrected to a valid commented declaration. Node 24 and
the repository's pinned TypeScript dependency were used for the source checks.

## Fresh consumer routing trials

Two fresh agent contexts used an installed complete copy outside this source repo
and a realistic synthetic AGENTS hook, without expected routes or prior reports.
No live systems were accessed.

The deliberate migration read 3,343 whitespace words of guidance once each, with
no displayed truncation or repeated guidance. Its direct collection route reached
the process format, authoring rules and template. The agent preserved the old
headings and proposed scope, exposed three existing reviewer steps and one
feedback handoff, and left unsupported roles absent. The installed parser and
managed-home checker passed; a duplicate-key negative control failed. A separate
check confirmed retained headings, status and four resolving Detail links.
The owner remained scoped to the coordinator's ownership of the explanation;
the trial did not invent overall process or acceptance authority.

The nearby introduction edit read only the fixture AGENTS (33 words) and source
README (19 words). It preserved the proposed synthetic status and activated no
process-format, installation or source-authoring guidance. This case demonstrates
that a narrow prose edit can stay outside migration work.

These cases cover cold entry, deeper migration guidance and a nearby out-of-scope
edit. Source-authoring entry routes were unchanged and no new authoring-entry
trial was selected. They establish scoped route reachability, not automatic host
discovery, whole-collection efficiency or rendered browser behavior. Forge's
separate consumer adoption and browser verification own downstream evidence.
