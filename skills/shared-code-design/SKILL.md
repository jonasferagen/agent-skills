---
name: shared-code-design
description: "Decide whether repeated code across independently buildable components should stay copied with a drift check, be generated, or become a versioned dependency. Use when a shared kit or utility appears in several services and its maintenance cost or coupling is under review."
metadata:
  version: "0.1.0"
---

# Shared code design

Decide where repeated implementation belongs while preserving the components'
actual ownership and build promises. Start with the existing package boundaries,
dependency graph and recent changes. Similar code alone does not establish that
the components need a shared package.

## Separate the questions

Identify whether the repetition is a rule, an implementation, or test setup. A
rule needs an authoritative owner and derived or checked copies. Repeated code
may be a stable abstraction, or it may only look alike while the components
change for different reasons. Test setup may be shared without sharing runtime
code. Keep domain decisions in the component that owns them.

If each component promises to build from its own directory, check that promise
directly. A sibling source import or undeclared host package breaks it. A shared
dependency can preserve independent builds when each component declares and pins
its version and can obtain it without the sibling checkout.

## Compare maintenance costs

Use recent changes to count the edits, coordination and failures caused by the
copy. Consider the costs of the alternatives:

- **Checked copies:** simple independent builds; each change requires coordinated
  edits and a check that compares the live file set and contents. Name who owns
  updates and how a consumer adopts them.
- **Generated copies:** one authoring home while components still carry their
  own build inputs; generation and review must keep outputs current and preserve
  local adaptations.
- **Versioned package:** one implementation with explicit consumer versions;
  publishing, compatibility, dependency acquisition and upgrade testing become
  part of the work.

Choose a new shared dependency when a stable, independently testable abstraction
and repeated change cost justify those new obligations. Avoid extracting domain
rules or widening a dependency simply because files are identical. A passing
copy check proves agreement today; it does not measure the effort to keep the
copies current.

## Verify the chosen boundary

Build and test each consumer on its own. Exercise a representative shared change
through every affected consumer and check the public behavior it supports. If
copies remain, make drift fail in the normal gate and test that the check fails
when one copy changes. If a package or generator replaces them, verify that an
older consumer can retain its declared version or state why simultaneous upgrades
are required. Record the adoption path and the remaining structural copies.

This skill concerns implementation distribution. A rule appearing in code,
schema, configuration and docs also needs its own authoritative definition;
identical files are only one form of that broader problem.
