# Structured service definition

`service-definition/v1` is an optional format inside the service's existing
`README.md`. It gives readers comparable facts without duplicating the operating
guide. Adopt it per service; unversioned guides remain valid. Project policy
chooses whether and when structured definitions are required.

Declare `Service format: service-definition/v1` once before `## Service definition`.
That section contains only one `Field` / `Value` Markdown table, with each field
below exactly once. Other sections retain repository-defined headings and rules.
Declarations inside fenced examples or HTML comments do not select the format.
Unknown versions, duplicate declarations, missing or empty fields fail validation.

| Field | Meaning |
| --- | --- |
| Identity | Stable project-qualified identity, such as `example.reader`; lowercase letters and digits separated by dots or hyphens, beginning with a letter. Unique across a browser's selected services. |
| Owner | Repository and responsible capability; ownership is a documented fact. |
| Purpose | Capability the service provides. |
| Status | Scoped implementation/adoption statement; never inferred live health. |
| Lifetime | Maintained or explicitly launched lifetime and startup decision. |
| Exposure | Transport and allowed audience. |
| Dependencies | Route to selected dependencies and prerequisites. |
| State | Route to configuration, reads, writes and retained state. |
| Operations | Route to setup and start, stop, restart, status and logs commands. |
| Readiness | Route to what readiness checks prove and do not prove. |
| Recovery | Route to failure, shutdown, recovery and preservation guarantees. |
| Evidence | Route to exercised acceptance evidence and its limits. |

Every value is nonempty. The last six fields require an inline Markdown link or
exactly `Unknown` or `None`; do not invent evidence to fill a field. Local relative
Markdown paths, same-document anchors and project symbolic references are allowed.
Absolute paths, external URLs and backslash paths are excluded from these facts.
Link to the existing detail owner instead of copying commands or changing facts.
Escape literal table pipes. Supporting documents retain their own authority.

[The parser](../scripts/service_format.py) owns format recognition and bounded
home discovery. It preserves fact values and source line numbers; it neither runs
services nor resolves links. [The checker](../scripts/validate-services.py) checks
the declared format alongside the service-home structure. It does not check link
targets, the truth of the claims, health or operational compliance.

A browser explicitly selects adopted homes, includes their index and immediate
service guides, and rejects missing or symlinked sources. It uses this parser,
validates selected Markdown routes and preserves source provenance. It must label
unversioned guides distinctly, preserve `Unknown` / `None`, and keep documented
status separate from live readiness. Browser selection is an adapter concern;
service-foundation does not require a browser or project-foundation installation.
