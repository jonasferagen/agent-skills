---
name: python-design
description: "Design or review the structure of Python programs: module responsibilities, phase contracts, state ownership, shared interfaces and naming. Use for architectural decisions and scoped refactoring; language correctness belongs to python-patterns."
metadata:
  version: "1.0.0"
---

# Python design

Make responsibilities and contracts visible as a Python program grows. Choose
functions, modules, values and classes by the responsibility they express;
neither classes nor a particular architectural pattern are required.

<!-- Package-boundary copy: python-patterns/SKILL.md carries the same repository authority rule. Keep both aligned. -->
The repository owns product contracts, framework choices, tooling and test
policy. When its instructions conflict with this package, report both passages
rather than silently changing either owner. Follow the user's explicit decision.

## Workflow

1. Establish the requested scope: review, conversion plan or implementation.
   Read the product contracts and trace one representative call through its
   data transformations, dependencies and effects before proposing boundaries.
2. Name the concrete responsibility, invariant or lifecycle that is unclear.
   Read the narrowest matching reference below and inspect callers as well as
   callees. Distinguish a demonstrated defect from a design preference.
3. Choose the smallest change that clarifies the contract. Preserve public
   behaviour unless the task authorizes a change; keep small fixes scoped.
   A review or plan does not authorize implementing its recommendations.
4. For implementation, update affected callers and run relevant checks. For a
   plan, identify migration steps, compatibility obligations and evidence needed
   to switch. Explain tradeoffs and what remains untested.

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

Python-patterns is a suitable companion for runtime validation, numerical
correctness, mutation mechanics and failure handling. This skill addresses who
owns those contracts and how callers use them. Repository contracts still own
domain semantics, tool choices and acceptance criteria.
