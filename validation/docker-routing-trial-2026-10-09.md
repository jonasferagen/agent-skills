# Docker routing trial — 9 October 2026

Acceptance evidence for the containerization split: `docker-cli`,
`docker-compose-cli` and `docker-cleanup` against each other and against the
consuming framework's `local-containers` convention, which now owns the
outcomes the retired skill carried.

## Method and its limits

Four cases, one fresh agent each, no shared history and no expected route
supplied. Each worked in its own copy of a consumer fixture outside both
authoring repositories: a small service repository with a Python API, a
PostgreSQL database and a Godot previewer, holding an `AGENTS.md` that adopts
the installed engineering collection and names its entrypoint, an
`UPSTREAM.md` pin, a `compose.yaml`, a leaking test harness and a
`compose run` script that borrows the previewer definition. Entry was the
project-instruction hook in every case.

**This is an entrypoint-routing trial, not independent discovery acceptance.**
The agents reached guidance by reading project instructions and the collection
entrypoint, not from host-supplied skill metadata. Per the
[trial method](discovery.md#routing-trial-method), fresh conversation context
does not establish fresh metadata, so nothing here establishes that a skill
activates spontaneously. It establishes that the catalog routes a realistic
request to the right member.

Container commands were withheld from every case: the fixture has no daemon, and
each agent was told to reason from the files. Defects they identified in the
fixture are therefore read from code, not observed.

## Cases and results

| Case | Task | Route reached | Verdict |
| --- | --- | --- | --- |
| 1 | A harness leaks containers when a run dies, and its fixed port has twice clobbered a local database | `docker-cli` + `local-containers` | Correct |
| 2 | A `compose run` export keeps destroying a developer's open previewer state | `local-containers` + `docker-compose-cli/references/project-isolation.md` | Correct |
| 3 | The build box is at 96% disk and nobody knows what is eating it | `docker-cleanup` + `references/inventory.md`, then both CLI packages for the repair | Correct |
| 4 | Declare what a new GPU previewer variant needs before anyone writes it | `local-containers` and its cross-referenced conventions | Correct |

No case selected the wrong Docker package, and no case was misrouted by the word
"container" alone — the risk recorded against `docker-compose-cli` before the
trial.

Each boundary was declined for a stated reason rather than missed:

- Case 1 did not follow the `docker-compose-cli` or `docker-cleanup` rows,
  citing `docker-cli`'s own statement that a single container is its scope.
- Case 3 reached the two CLI packages only through `docker-cleanup`'s "Do not
  select this skill for" section, and read just the passages it named.
- Case 4 considered all three skills and skipped them, because the convention
  says they own invocation mechanics and the task stopped before any command.

Case 2 exercised the one seam the split does not separate cleanly. It read the
outcome in `local-containers` and the mechanic in `project-isolation.md`, and
reported that the anchor link between them is how it knew the two passages were
meant to be read together. The required-argument rule survived: it made the run
root a required second argument and quoted the reason, that a default is what
the next call site omits silently.

The guidance also found real defects unaided. Three cases independently
identified the fixture's `compose run` inheriting the service-owned
`previewer-home`, and three identified its teardown selecting by the
`harbour-test-` name pattern. Case 3 found the anonymous-volume leak the fixture
was built around and ranked it the prime suspect for the right reason: the
largest consumer was also the least attributable, which is what "nobody knows
what is eating it" means. It classified that group review-first rather than
safe, because the owner was unknown.

## Findings repaired

Both were defects in text added by the split.

**`docker-compose-cli` stated an unfollowable rule.** "Pass `--project-name`,
`--file` and `--env-file` on every invocation" cannot be followed by a project
with no env file: compose rejects a `--env-file` path that does not exist, and
omitting the flag is what lets a `.env` beside the compose file be picked up.
Case 2 worked around it with `--env-file /dev/null` and reported the gap. The
rule now covers the no-env-file case.

**`docker-cleanup` offered no way to find unlabelled resources.** Case 3's prime
suspect was a population of anonymous volumes, and `inventory.md` had neither a
way to select resources carrying no label nor a way to total a group of
hash-named ones. The agent declined to invent a command, which was correct, and
left the plan weaker for it. `inventory.md` gains "Find what carries no label at
all": subtracting each owner's claimed listing from the full one, since Docker
has no filter for a label's absence, plus summing per-volume sizes from
`docker system df -v` and reporting count beside total. The subtraction was run
against a live daemon holding 12 volumes and correctly isolated the one carrying
no compose project label — an editor's volume, not any project's, which is the
case the tiering must not treat as safe.

## Findings raised, not repaired

These concern the consuming framework's conventions or its catalog rather than
the three skills, and two of them are a single pattern. They are recorded for a
decision rather than patched here.

**A convention requires a declaration without naming its home.** Case 2 could
not find where a repository's writable-roots declaration lives when it has none;
case 4 could not find where a composed-set declaration lives. Both left the
question open rather than guessing, which is the right behaviour and the reason
the gap is visible. Two independent cases reaching the same shape suggests one
rule about declaration homes rather than two local repairs.

**`local-containers` is read by every container task and mostly does not
apply.** All four cases read its 2,439 words. Case 3 called it the session's
highest-cost read for the least return: it paid out two sentences, both already
stated by `docker-cleanup`. Case 1 needed five of its sections and not the rest.
The convention may want conditional references rather than one page, which is a
decision for its owner.

**A project's label scheme has no findable home.** Cases 1 and 3 both needed it
— cleanup makes label attribution authoritative, and case 1 had to invent a
namespace. The convention says to record it with the containers' owner, which is
not a location a reader can open.

**The `repository-services` catalog row invites a wrong read.** Case 4 opened it
on "adding a service" and found it was about a `services/` home the fixture does
not have. The read prevented inventing that layout, so it was not wasted, but
the row's wording is what pulled it.

**`compose run` builds implicitly, against the convention.** `local-containers`
says a run never pulls or builds an image implicitly, but a `build:` service
with no declared build command gives a reader nothing to point a failure at.
Case 2 declined to add `--no-build` and left it unresolved.

**GPU guidance is one sentence.** Case 4 derived device nodes, container
runtimes and driver policy from the generic environment-requirements fields,
since the convention offers only that hardware access is a declared prerequisite
with its own preflight check.

## Remaining gaps

One run per case demonstrates each route, not its reliability. Independent
discovery acceptance still requires host-supplied metadata, which this host
could not establish. No case exercised source authoring, and no case exercised
`docker-cli` and `docker-compose-cli` in conflict — a task touching one
container inside an existing project, where both could reasonably be selected.
