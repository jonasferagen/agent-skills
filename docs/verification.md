# Source verification

## Maintenance checks

For source maintenance, install Node 24 and Python 3.11 or later, then run
`python3 scripts/check.py`. It runs every `test_*.py`
suite under `scripts/` and `skills/`, including each package's own `tests/`.
Empty, failed, skipped and incomplete suites fail it, and missing prerequisites
fail explicitly. CI runs the same command. These local checks do not establish
live service or database acceptance.

### Where a package keeps its checks

| Directory | Holds |
| --- | --- |
| `references/` | Guidance applied while using the skill |
| `scripts/` | Tools the skill uses |
| `tests/` | Executable checks of behavior the package owns, as `test_*.py` suites `check.py` discovers; each suite declares its prerequisites in its docstring and runs from an independent copy of the package with `python3 -m unittest discover -s tests` |
| `scenarios/README.md` | Maintained requests, context and expected behavior, with current limits beside the behavior they qualify; case directories with synthetic inputs only when a case needs them |

Create none of these empty, and require no uniform section template beyond
useful case meaning. Scenarios hold inputs and expectations, not observed
outputs, timestamps or run reports. Source-wide package checks, cross-skill
consistency checks and the [selection scenarios](../scripts/tests/selection-scenarios.md)
stay in `scripts/tests/`.

### Evaluating a skill against its scenarios

Give a fresh agent the case's request and context with the installed package,
not the expected behavior, under the isolation rules in
[routing quality](#routing-quality). Judge the artifacts against the expected
behavior; note missed obligations and unnecessary reading as well as wrong
answers. Record the observed results, the commit evaluated and the context
configuration with the change that ran them — its commit message, review or the
project's work record — not in the package. A run that shows a failure worth
keeping adds a regression case; one that shows a limit states it beside the
behavior it qualifies. One passing run demonstrates a route, not its reliability.

## Discovery and routing

### Routing quality

A consumer must be able to find the relevant guidance without reading this
authoring repository's maintenance material. Additional reading must follow a
concrete task need, and required deeper guidance must remain reachable. Apply this
standard to our own catalog and instructions as well as their output.

Routing is an acceptance requirement when changing triggers, entrypoints, shared
guidance or packaging, and before releasing a skill. Run proportionate practical
trials by the method below. Preserve task constraints and check missed obligations
as well as unnecessary reading. Package validation alone cannot establish routing
quality.

#### Routing trial method

Select realistic cases for the changed routes:

| Case | Observe |
| --- | --- |
| Cold entry into ordinary consumer work | Reads before useful work and irrelevant activation |
| Work requiring deeper guidance | Whether required references are reached and obligations preserved |
| Nearby work outside the changed skill's scope | Whether the agent avoids unrelated guidance |
| Source authoring when consumption or authoring routes change | Whether relevant maintenance rules still apply |

Start a new agent for each case with no forked conversation history, prior case
results, expected findings or preloaded skill bodies. Record the context
configuration and the exact skill metadata supplied at startup, including stale
or absent entries; fresh conversation context does not establish fresh metadata.
If the host cannot provide this isolation, record the run as an informed review
or walkthrough, which cannot pass independent acceptance.

Place the consumer fixture outside this repository with an installed copy, a
realistic project instruction hook and provenance. Start from that hook or from
normal discovery metadata; do not supply the expected route, and record whether
entry was explicit invocation, supplied metadata or project instructions. A
source-authoring trial starts in an isolated copy of this repository. Keep live
systems outside the trial. Reused agents can implement fixes and review known
findings; their results stay separate from independent acceptance.

Have the evaluator record the files actually read, approximate words, repeated
reads, truncation and reused context, distinguishing instruction reads from
catalogs, generated-output review and mechanical checks. Classify each material
read as required, useful or irrelevant with a reason, and report required
guidance missed and output constraints preserved or violated. An unexercised
case is a limitation.

A consumer reaching source maintenance material without a task reason is a
finding; so is missing necessary deeper guidance, even when reading falls.
Compare equivalent tasks across revisions and record the smallest supported fix
and remaining gaps. A single successful run demonstrates a route, not its
reliability. Capture a demonstrated problem in the owning package's scenarios;
do not turn every observation into another mandatory instruction.

Do not set a universal word budget. Compare equivalent tasks and explain which
reads were unnecessary. Record remaining gaps; do not claim the requirement is
verified from word-count reductions alone. Ordinary prose edits need no new trial
unless they change routing or reveal concrete friction.

When authoring here, use the catalog and maintenance guides relevant to the
change. When consuming an installed skill, use its entrypoint and project
routes. Do not follow provenance back to the source repository unless the task needs source
maintenance, upgrade information or investigation of a concrete source issue.
