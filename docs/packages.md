# Skill packages

## Using a skill

Copy the complete skill directory from a selected source commit into the target
repository's `.agents/skills/<name>/` through its normal review process. Record
its provenance once, in the target's machine-readable dependency lock: the
source URL, full commit SHA, source directory, any selected release version and
each installed file's digest. A target that keeps no lock records the same
facts in the one provenance file it keeps, and never in both. The SHA is the
authoritative pin. Imported files should match that commit; keep
project-specific rules outside the imported directory, and record any necessary
local modification beside the pin.

Names, invocation examples and release tags are unchanged by source grouping.
Existing imports retain their pinned source paths; use the new path when importing
a revision after a move.

Every package keeps its required resources inside its own directory: references,
templates, scripts and their tests. Links must stay inside the package. A shipped
skill may name another skill but never links to it or depends on it: when two
packages need the same rule, each states it in full in its own words. Packages are generic: they make no
claims about a particular consuming project's process, records or conventions,
and their examples are synthetic.

A consuming project may import an explicitly self-contained reference as a file,
recording its owning skill, version, source path and full commit. This does not
install or register the whole skill. The shared-value reference at
`skills/design/single-source-of-truth/references/authoritative-values.md` supports that
use and requires no sibling resources. Keep it free of local links, so an
importer that rejects them can carry the file. Preserve the imported bytes and record
the project's own adoption and routes separately.

### Selection

Skill descriptions name the task or observed symptom that should select the
package. Keep them concise and put the main trigger first. The selected
`SKILL.md` supplies essential guidance and routes to conditional references;
open only the references needed for the current decision. Grouping this catalog
does not itself control which instructions an agent reads.

Put the source location in provenance; never bake a machine-specific path into
the skill. Reading and proposing guidance can fit a review. Writing the source
repository or adopting a new pin follows the task's actual authorization.

Test discovery with realistic requests and metadata before showing skill bodies
or expected answers. Record whether a trial used host-provided metadata, a
supplied metadata catalog, or a project hook. Check a nearby request that should
not activate the skill as well; the
[selection scenarios](../scripts/tests/selection-scenarios.md) list such pairs. A
successful package check alone says nothing about selection.

## Adding a skill

This repository owns reusable technical and authoring methods. Project setup,
process and coordination belong to the consuming project, as do its decisions,
priorities, responsibilities, requirements, local procedures and evidence. A
skill here supplies the method; the consuming project supplies its defaults.

- Keep it project-agnostic: no account details, credentials, service
  identifiers or private domain records, and no names of the projects that
  consume these skills. A skill about one project's systems
  does not belong here. Skills about Jonas himself, such as his email style,
  live in his separate local `personal-skills` repository.
- Make no claim about a consumer. A package states a need; where the consumer
  satisfies it is the installer's to decide. So a package names no path,
  filename, document home, command name or instruction wording in a consuming
  project, and ships no code a consumer imports or executes — only the interface
  contract such code is bound by. Guidance selected by a command or artifact in
  front of the reader belongs here; an outcome a project's own work must meet
  belongs to the consuming project. The consuming project states the same
  division in its own words, from its side; fix an
  overreaching package here rather than letting a consumer document the
  deviation. The retirements of `containerization` and `repository-services`
  record what this costs when it is noticed late.
- Put the manifest at `skills/<area>/<name>/SKILL.md`; choose the existing area
  whose task it serves. Keep skill names unique. Put every resource the skill
  needs inside its directory.
- Choose a short lowercase hyphenated name for the activity or subject readers
  will seek. Use familiar terms and the actual language or tool when it narrows
  the scope. Preserve an established name unless clearer discovery justifies
  changing consumer paths.
- Use the [authoring skills](releases.md#authoring-skills) while writing the package.
- Add `scenarios/README.md` when the skill has scope boundaries worth testing,
  `tests/` when it ships behavior a check can own (see
  [where a package keeps its checks](verification.md#where-a-package-keeps-its-checks)), and a
  row to the [catalog](../README.md).
