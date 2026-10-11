# Adopt defaults without duplicating policy

Type: record
Owner: Codex
Status: Author traces and source checks passed
Date: 2026-10-11

## Basis

At `44fe9fb`, project-policy distinguished facts and requirements but did not
explain that a convention's adoption supplies its requirements without separate
local declarations. Tessera's preceding adoption produced one policy per common
engineering mechanism. Its access-boundary declaration also held a general
verification method better owned by service-boundaries.

## Findings and evidence

Project-policy 0.4.0 distinguishes project decisions from inherited defaults and
implementation selections. Service-boundaries 0.4.0 places actual listener and
access evidence alongside its existing ownership and authorization checks.
Neither selects an authentication product, exempts local services or grants
authority. Container invocation remains a separate route.

Author traces, with expected outcomes known: a policy adequacy review reads
establishment and consolidates inherited Git mechanics into their adoption;
a new recovery target remains a scoped project decision; a narrow existing-rule
question needs only the entrypoint and its owner. A listener expansion uses
service-boundaries to compare intended and observed access and the project's
decision route for changed scope; adding an HTTP adapter retains its existing
identity/handler/retry checks. A Docker argument correction stays with its
invocation guidance. These are author traces, not independent discovery evidence.

## Disposition

No descriptions, activation hooks, package layout or runtime helpers changed.
The distribution's fresh consumer adoption will independently exercise the
policy/convention distinction. `python3 scripts/check.py` passed all four checks; `git diff --check` passed.
The task reused the primary checkout's Node dependencies through a temporary
symlink, without changing dependencies. No release tag was created.
