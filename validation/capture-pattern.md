# Validation — Capture Pattern

## Expected behavior

- A consolidation review reveals repeated image builds: inspect the relevant
  existing skill, keep the unmeasured optimization conditional, and avoid
  duplicating guidance already present.
- A user corrects a project-specific port: update the local fact when authorized;
  do not create a reusable port rule.
- A reproduced failure reveals a general transaction invariant: identify its
  conditions and owning database guidance without requiring a second incident.
- A read-only review reveals useful guidance: identify its home and a precise
  proposed addition; do not mutate the source repository.
- A skill maintenance task authorizes changes: update the existing owner first,
  validate and record the evidence; do not rewrite installed copies silently.
- An ordinary typo fix: do not load this skill merely because files changed.
- No source repository is configured: report the missing location and proposed
  home; do not assume a private filesystem path.
- A lesson is already covered: report the existing home and stop.
- An explicit `/capture-pattern` request names a small, speculative idea: assess
  it even without an opportunistic trigger; preserve uncertainty and scope.
- A rule has growing exceptions: reconsider its scope or abstraction, while
  keeping distinctions needed to protect required behavior.

## Discovery trial

The planned trial gives a fresh subagent the original Atlas/Work scan request
without conversation history or an explicit skill invocation. Record the actual
catalog supplied, any project routing instruction, the skill files opened and
the result. Installation, discovery, selection and correct use are separate
claims. A prompt listing the desired skill as an instruction cannot establish
implicit selection. A project hook can test configured routing but cannot
establish metadata-only selection.

This trial may inspect the repository and propose guidance, but must not edit
the project or skill source. Skill bodies and expected findings are withheld.
After the answer, ask which skill metadata was available and which files were
read. Run a nearby negative case to check unnecessary activation.

## Trials on the original installed name — 2026-09-30

The initial package was installed as `lesson-capture` in Atlas/Work at source
pin `ed10f8f100774b2d4195f8f08d344690afefa066`, with a conditional project
AGENTS.md link. The project HEAD was `dd91849`. Each trial used a fresh agent
without this conversation, expected findings or skill bodies. The scan was
restricted to read-only inspection and cheap checks. After each answer, a
follow-up asked which skill files the agent had opened; that part of the evidence
is the agent's retrospective account, not an exported tool trace.

- **Original scan, first trial: failed selection.** The review found five
  consolidation candidates and ran inexpensive checks, but did not open
  lesson-capture or inspect a reusable lesson's source home. The agent reported
  that the new skill was absent from initial metadata, encountered only as the
  AGENTS.md link. It opened only the imported source-of-truth skill.
- **First lookup control:** answered the native-test command without opening any
  SKILL.md. It reported seeing the lesson-capture link in AGENTS.md and leaving
  it unopened.
- **Repair:** replaced the broad "when a meaningful lesson emerges" reminder
  with a checkpoint before finishing an architecture or consolidation review
  with concrete findings. It asks for the strongest candidate's home or a reason
  to keep it local, and explicitly excludes routine lookups and literal edits.
- **Lookup after repair:** again answered the command without opening a skill.
  It did not report encountering the hook, so this establishes no unnecessary
  activation in that run, not rejection after reading the revised instruction.
- **Original scan after repair: passed configured routing.** The agent opened
  the installed lesson-capture and source-of-truth instructions, followed import
  provenance to the source catalog, then read only verification-design and
  shared-code-design there. It identified the strongest lesson as already
  covered by verification-design and made no source change. Its review reported
  four consolidation candidates and 29 passing Docker-free integration checks,
  plus contract and kit checks. This exercised the project checkpoint, not
  selection from refreshed host metadata.
- **Separate metadata-only trial:** given only the live name/description catalog,
  another fresh agent chose the expected smallest set in seven cases: none for
  command lookup, verification-design for active milestone checks, test-audit
  for a permissive mock, shared-code-design for copied kit extraction,
  source-of-truth for conflicting URL definitions, lesson-capture for an
  unmeasured reusable optimization, and none for a literal spelling correction.
  The sixth request explicitly asked about keeping a lesson for future projects;
  this trial does not establish spontaneous selection from the original prompt.

The native subagents inherited the session's initial skill metadata. Installing
this package during the turn did not add it to that inherited list. Consequently,
the original-request experiment tests the installed project hook, while the
separate catalog experiment tests description matching. Neither proves future
host refresh behavior or reliable activation across repeated runs.
