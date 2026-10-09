# Project bootstrap validation

## Extraction and scope — 2026-10-08

The standalone 0.1.0 package extracts the workflow from project-foundation's
`collections/documents/skills/project-bootstrap/` at
`bb95633f4e94c00053b6d43a7a92c493a4698636` (legacy skill 7.0.0). It begins a
new standalone version line. No legacy foundation tables, reserved document tree,
validator, mandatory companion installation or distribution-specific routes are
carried forward. Project document conventions own shape and placement.

The motivating gap was Tessera adopting a policy skill without establishing its
operating context. Its later policy records the user's local solo-development
posture and explicit open decisions. Bootstrap now checks for actual context,
not just an installation link. This task also adds the complementary planning
workflow; neither requires the other to be installed.

## Author walkthrough

This is an informed author review, not an independent discovery or activation
trial. Skill bodies and legacy behavior were already known. The paths below are
the reviewed routes, not a fresh agent's measured read trace. No context-saving
or spontaneous-selection claim is made.

| Request and input | Route reviewed | Result and boundary |
| --- | --- | --- |
| Set up a small local project; product direction is unknown | SKILL.md, selected project policy and document guidance | Overview can state actual responsibility; policy records known posture and explicit unknowns. No invented stack, releases or work queue. |
| Existing project has installed guidance but no project policy | SKILL.md, existing README/instructions and policy workflow | Establish facts and decisions with a real owner; a skill link alone fails the completion review. Preserve existing commands and commitments. |
| Add a member to an existing shared project | SKILL.md and the shared policy/instructions | Member records local responsibility and reachable common owners; no duplicate policy. Missing shared input blocks only dependent decisions. |
| Update an installed dependency pin | Existing installation procedure | Description and body exclude a fresh bootstrap pass; context is unchanged unless the task actually exposes a relevant gap. |
| Correct a sentence in an existing README | Existing document and writing guidance | No bootstrap, policy reconstruction or empty scaffold. |
| Author this standalone extraction | Repository AGENTS, README maintenance sections and selected writing guidance | Upstream package is self-contained; distribution owns templates and consumer adoption. |

### Small output specimen

Synthetic input: a new repository stores local design notes; the user works alone,
has no external users or release commitment, and has not chosen a product or stack.
The task authorizes repository instructions and document setup.

The reviewed output is a README explaining the notes repository and linking its
policy and instructions; the policy records that known posture and leaves product
scope, future data and recovery objectives open. Instructions route to those
owners, the selected guidance and actual checks if any exist. No application,
remote, dependency, service or active plan is implied. A next decision depends on
the next requested outcome; an undecided stack does not block recording context.

Compare with the legacy failure mode: a README linking only installed skills
would leave the project's facts unstated. The new "Establish actual context" and
completion review explicitly reject that output. In a dependency-only upgrade,
that review is not a reason to recreate established project documents.

## Evidence and limits

Both new skill packages pass the skill-creator validator and the repository
package validator. The full source check passed: five checks, four helper suites,
157 tests and no skips; `git diff --check` passed. Behavioral conclusions above are manual review of the stated
routes and specimen. There are no new runtime helpers or automated behavior tests.
Independent cold-entry, shared-owner and negative discovery trials remain
unverified; package checks cannot establish them. No release tag is created.

The reusable finding belongs in this bootstrap workflow: installing instructions
and establishing the facts those instructions govern are separate outcomes.
Policy prompts and document shape remain with their existing owners.

## Environment requirements — 8 October 2026

Bootstrap now establishes the consumer contract for a selected external runtime
resource and keeps provisioning with its providing owner. The standalone skill
states the minimum outcome and uses project-supplied environment guidance when
available; it requires no companion package or particular manifest.

See [environment requirement trials](environment-requirements-2026-10-08.md) for
the fresh-context database setup case and the nearby owned-output control.

## Provided resources — 9 October 2026

Version 0.3.0. Establishing actual context now covers both sides of an external
resource: a providing repository publishes one contract per resource it provides,
and a consumer's environment requirements cite that contract with its selector,
access, relied-on layout and missing-dependency behavior. A missing contract is
reported to the provider as its bootstrap gap rather than written by the consumer.
Author review only; an independent downstream adoption trial is recorded by the
distribution that imports this revision.

## Provider selector — 9 October 2026

Version 0.4.0. An independent downstream adoption of 0.3.0 published a provider
contract whose interface was a host path naming the storage vendor, and whose
text told consumers what the provider did not check behind it. The skill now
names the provider-set selector as the contract's binding, keeps the host path
and mechanism out of the contract, and keeps unchecked guarantees as the
provider's open work rather than a consumer-facing caveat. Author review; the
downstream re-trial is recorded by the importing distribution.
