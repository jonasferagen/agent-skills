# Environment requirement trials — 8 October 2026

## Finding and change

The materials workflow had accumulated direct-bucket access, a local mirror and
service ideas despite the eventual requirement being a shared filesystem
interface. Legacy foundation contained environment/dependency headings and
missing-mount check guidance. Current service-boundaries protected private tables
but unconditionally discouraged mounting a service's data. Its validation cases
never contrasted private storage with a published filesystem contract.

This omission should have been caught in semantic boundary review. Earlier
package checks and author-reviewed adapter cases did not establish this behavior.
The change clarifies that contract distinction, asks bootstrap to establish
external resource requirements, and supplies a native engineering convention in
project-bootstrap. It does not prescribe object storage, mounts or a service.

## Trial configuration and evidence limits

Four agents were spawned with `fork_turns=none`, without expected findings or
prior results. Three started through installed consumer AGENTS.md instructions;
one explicitly invoked service-boundaries to evaluate that skill directly. No
model override was selected. Live systems and file edits were forbidden. No
trial failed and was retried with coaching.

Fixtures lived outside either authoring repository at
`/tmp/environment-requirements-trials-20261008`. Retained fixture instructions,
README inputs and provenance are in the adjacent directory. The installed input
hash inventory identifies the exact draft evaluated: project-bootstrap bb0aad2
plus the convention/routes, and agent-skills 397b2ed plus the two edited skills.
Installation inventories still described earlier pins; these trials did not test
package integrity. Separate source checks cover the final import.

The harness supplied no extra skill bodies. The platform's available skill
metadata was not independently isolated or inventoried. File-read manifests and
word counts below are agents' reports, not independently captured read traces.
Therefore these are fresh-context behavioral trials with retained reported routes,
not proof of independent metadata discovery acceptance or reliable spontaneous
activation. No runtime readiness, data access or database behavior was exercised.

## Prompts

All consumer prompts specified read-only review, fixture-only reads, no live
systems or file edits, and requested exact reads, approximate instruction words,
unnecessary reading, unresolved obligations and results. Task portions were:

- Mount: "Review the material workflow's dependency boundary and the integration
  choices described in README.md. Give concrete recommendations and missing
  environment requirements." Entry: mount/AGENTS.md.
- Database: "Establish a concise proposed starting context for the new reporting
  repository in README.md, including what remains unknown and next verification
  needed." Entry: database/AGENTS.md.
- Output: "For the report wording change described in README.md, explain whether
  any environment or ownership documentation must change and what minimal
  verification is appropriate." Entry: output/AGENTS.md.
- Service: "use the installed service-boundaries skill
  (.guidance/engineering/skills/service-boundaries/SKILL.md) to review the choices
  in README.md." Explicit invocation, with recommendation, missing facts and read
  manifest requested; no spontaneous-discovery claim.

## Results and reported reads

Mount preserved the published filesystem interface, read-only selection and the
separate authorized indexer. It rejected the private-storage shortcut in favor
of the export operation. It requested expected-mount checks rather than directory
existence, contract/access/repair documentation, and explicit concurrency and
persistence requirements. It deferred both mirror and HTTP server absent a
requirement. Fixture evidence and live readiness stayed separate.

Reported reads: AGENTS.md, README.md, engineering/COLLECTION.md,
engineering/conventions/environment-requirements/CONVENTION.md,
engineering/skills/application-design/SKILL.md and its
references/external-integrations.md, and
engineering/conventions/environment-variables/CONVENTION.md, under `.guidance`
where applicable. Approximately 3,971 instruction words plus 87 context words.
The full environment-variable reference and much of submission/recovery guidance
were unnecessary for this review. No service-boundaries read was reported; this
motivated a separate explicit-use trial rather than attributing success to it.

Database kept provisioning and recovery with the platform team. Its proposed
README recorded the published schema/restricted role, environment-specific
endpoint, unknown credential and repair routes, optional live-mode boundary,
and future fixture strategy. It proposed stopping selected dependent work on
incompatible access and required no executable doctor for a design-only repo.

Reported reads: AGENTS.md, README.md,
.guidance/documentation/skills/project-bootstrap/SKILL.md,
.guidance/engineering/COLLECTION.md and its environment-requirements convention.
Approximately 2,142 instruction words plus 58 context words. No unnecessary files
were reported. Policy ownership, provider contracts and live readiness remained
unresolved; no database-administration guidance was loaded.

Output required no environment or ownership document change. It retained existing
temporary-output ownership and proposed only the existing focused report check
on a synthetic fixture, preserving any explicit project gate.

Reported reads: AGENTS.md, README.md, .guidance/engineering/COLLECTION.md and
.guidance/engineering/skills/verification-design/SKILL.md. Approximately 1,191
instruction words, 1,246 with context. No unnecessary reads reported. No bootstrap
or environment-requirements activation; exact wording and check command were
absent from the fixture and left unresolved.

Explicit service-boundaries use retained the published mount and separate writer,
rejected the private-storage shortcut, and requested access/layout, missing-mount,
concurrency and required persistence verification. It found no stated requirement
for a mirror or server. Reads: only the installed service-boundaries/SKILL.md
(approximately 492 words) and mount/README.md (87 words). No live implementation
or guarantee was claimed verified.

## Review and disposition

Author review of these answers found the targeted distinctions preserved in all
four cases. The original ambiguous sentence failed to distinguish the two
filesystem cases; the corrected standalone skill explicitly did so in its trial.
The database case establishes applicability beyond mounts. Owned temporary output
is the negative control. The unnecessary reads in the broad mount case remain a
routing limitation; they did not introduce a mirror, service or provisioning duty.

Keep service boundary semantics in service-boundaries, starting-context discovery
in project-bootstrap, and the resource declaration and readiness rule in the
native engineering convention. Existing tool-readiness work covers executable
workflows; this change does not replace its consumer/provider checks. No generic
manifest, background checker or additional service is introduced.

Verification: `python3 scripts/check.py` passed (five checks, zero failures) after
installing the locked TypeScript test prerequisite with `npm ci --ignore-scripts`.
`git diff --check` passed. The source and downstream import are pinned by commit;
no release tag or consumer installation is claimed by these trials.
