---
name: python-design
description: "Design or review the structure of Python programs: module responsibilities, phase contracts, state ownership, shared interfaces and naming. Use for architectural decisions and scoped refactoring, not for language-level correctness such as validation, numerics or failure handling."
metadata:
  version: "1.1.0"
---

# Python design

Make responsibilities and contracts visible as a Python program grows. Choose
functions, modules, values and classes by the responsibility they express;
neither classes nor a particular architectural pattern are required.

The project's own instructions decide product contracts, framework choices,
tooling and testing. Read them first; if nothing is documented, infer the
supported Python version and tools from `pyproject.toml`, CI configuration and
tool-version files, and state the assumption. When those instructions conflict
with this skill, report the conflict to the user, quoting both passages, and
ask which to follow. Follow the user's explicit decision.

## Workflow

1. Establish the requested scope: a review, a replacement plan (how to migrate
   from one implementation to another while keeping its public behaviour) or
   an implementation.
   Read the product contracts and trace one representative call through its
   data transformations, dependencies and effects before proposing boundaries.
2. Name the concrete responsibility, invariant or lifecycle that is unclear.
   Read the narrowest matching reference below and inspect callers as well as
   callees. Distinguish a demonstrated defect from a design preference.
3. Choose the smallest change that clarifies the contract. Preserve public
   behaviour unless the task authorizes a change; keep small fixes scoped.
   A review or plan does not authorize implementing its recommendations.
4. For implementation, update affected callers and run relevant checks. For a
   plan, identify migration steps, compatibility obligations and the checks
   that must pass before switching. Explain tradeoffs and what remains untested.

A review or plan is reported to the user as: findings, each tied to the code or
call trace that shows it; a recommendation with the smallest change; and what
remains untested or undecided.

## Start by symptom

| Symptom or decision | Read |
| --- | --- |
| Names, module responsibilities or version dispatch are unclear | [Names and modules](references/names-and-modules.md) |
| Stages share partially populated state or a new implementation must preserve behaviour | [Phase contracts](references/phase-contracts.md) |
| An operation needs a home, state lifetime or configurable policy | [Operations and state](references/operations-and-state.md) |
| A data record gains invariants, or arguments travel together | [Values and call sites](references/values-and-call-sites.md) |
| Modules share private helpers, diagnostic strings or large clients | [Dependency boundaries](references/dependency-boundaries.md) |

## Scope

Start with existing strengths, then tie each proposed boundary to a concrete
caller need, invariant, independent change or lifecycle. More files, interfaces
or immutable records are not evidence of better design. Avoid turning a known
sequence of calls into a framework or unifying different semantics merely
because their records look similar.

How to validate a value, compare numbers, mutate safely or report a failure
is a language-level concern outside this skill. The references mention
validation and failure only to place them: this skill addresses which stage or
object owns such a guarantee and how callers rely on it. The project still
decides domain semantics, tool choices and acceptance criteria.
