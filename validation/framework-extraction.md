# Project foundation extraction

The framework moves to https://github.com/jonasferagen/project-foundation.
Clear-writing, diagrams-and-tables and source-of-truth remain standalone source
packages here. Their new versions remove hard-coded framework dependencies;
the framework imports their complete directories at an explicit source commit.

The selected source baseline is `9093cfca4ffa93df1be35b1bb7ebffaef0baac65`, including
the landed 1.5.0 process format and its declaration hardening. Framework-specific
validation and native source history follow the new repository. Generic validation
stays here. Links to removed historical artifacts identify that original revision.

## Verification — 2026-10-04

The dependency source commit is `666d57d5004f78948ce69dcf93db102538a10f81`.
`python3 scripts/check.py` passed: 21 skill entries, five collections and all
61 helper tests across three suites; no skips. The new framework's independent
source comparison verified complete imported bytes and modes at that Git commit,
including the shared installation checker and reciprocal paired-rule records.

The fresh-context [standalone routing trial](generic-standalone-routing.md) reached
all three generic skills without a framework installation. One shared context
covered prose uncertainty, a repeated definition and diagram meaning; it read
11 files, approximately 3,781 whitespace words. No required guidance was missed
and no output constraint was violated. This establishes those bounded document
cases, not runtime behavior, historical ownership or native client discovery.
The framework's separate trial and release review are owned by its migration
record. The independent private repository is published with filtered native history,
the dependency lock and its own source checks. Agent-skills source retirement
landed after that publication. The first annotated release is
`project-foundation/v1.6.0` at new-repository commit
`a3b74c317a5d421c0a8aa1c8a4e77e56fb368288`. Forge's complete source cutover
landed locally at `3a0cf038b7c8e090714fec510a259215d28c1b68`, with shared
main-access verification at `3b09e9ee3a540638ee30ddb05d3434bb17cd158d`.
The canonical [migration record](https://github.com/jonasferagen/project-foundation/blob/main/validation/repository-migration.md)
owns framework release and consumer evidence; this repository retains generic
source and its standalone trial. Source-cutover and release CI both passed.
