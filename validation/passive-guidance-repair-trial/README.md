# Passive guidance repair trials — 3 October 2026

Fresh evaluators worked in separate synthetic consumer fixtures with the complete
draft collection based on `b55f4647fc7228e61e04827d54b3d365b0388dc1`. Each started
at consumer AGENTS, completed its request and recorded actual reads and checks.
No expected answer, suspected defect or missing-guidance report was supplied.
All actions were limited to fixture files and local synthetic Git repositories.

- [Ordinary read](capture-only/answer.md): the status-reference defect was not
  traversed; no source maintenance was activated.
- [Authorized read](authorized/answer.md): the status-reference defect was
  encountered and repaired at source; see [the source patch](authorized/source.patch).
- [Missing project term](project-gap/answer.md): retry permission remained unknown;
  no skill defect was inferred.
- [Capture-only review](capture-review/answer.md): the broken review route was
  recorded as a source candidate; see [work notes](capture-review/workspace/work-notes.md).
- [Authorized review](authorized-review/answer.md): the review route was repaired
  at source; see [the source patch](authorized-review/source.patch).

Each directory retains the request, setup identity, read log, relevant project
and source instructions, original agreement, answer, work notes and any source
patch. Instruction files are renamed to avoid presenting archived AGENTS hooks
as active repository instructions. Complete installations and temporary Git
repositories are omitted. Paths and synthetic pins in logs describe the original
fixtures, not current installation routes.

The trials preceded the final wording correction that allows separate capture of
a distinct defect in the capture workflow. That correction received independent
meaning comparison; self-defect behavior was not exercised. The copied full
validator in repair fixtures lacked its standalone-package tree; direct collection
checks passed, and the full validator passed in the actual authoring repository.
See [the validation record](../passive-guidance-repair.md) for results and limits.
