# Maintained catalog reader: design and verification plan

This is a proposed design, not a deployed service. Keep the recorded operating choice: an installed user service starting with the user session, loopback only, with no boot-without-login requirement. No provisioning or live verification was performed.

## Boundary and ownership

The project owns the note source files, snapshot extraction, read-only browser contract and service lifecycle. The service reads only its configured project source root and owns an in-memory snapshot; it neither changes the source nor introduces a database. Run under the selected user-session identity, without credentials or elevation. Do not claim that sharing this OS user creates a separate filesystem security boundary.

Retain the existing browser transport. Route catalog reads through one application handler that validates bounded inputs and maps allowed note identifiers to the configured source root; reject traversal, unsupported methods and invalid inputs. Keep extraction and catalog rules out of the transport adapter. Bind explicitly to loopback, validate request Host/origin where applicable, and reject unexpected browser origins. Localhost is a network boundary, not authentication against other local processes. Add no MCP transport, remote sharing, outbound jobs or writes.

Preserve snapshot behavior: validate sources and build one snapshot before readiness; restarting refreshes it. If extraction fails, report a bounded diagnostic and fail startup rather than serve an unmarked stale snapshot. Document that source edits are not visible until restart.

## Lifecycle and promotion

Promotion changes reliance from an operator's foreground spike to a session-managed reader with repeatable startup, identifiable readiness, recovery and support controls. Provide named `start`, `stop`, `restart`, `status` and `logs` commands. The process manager owns the entire unit process group; commands affect only that unit. An occupied port fails startup and never authorizes killing its owner.

Use an installed user unit as already selected. This is a scoped exception to the runtime member's transient-viewer default: the reader is maintained, not a disposable preview. Session startup is enabled during a separately authorized installation step; ordinary controls neither install, enable nor upgrade it. No lingering or system-level boot service is needed. Pin the selected checkout/release and non-secret settings across restarts; status reports that selection and the unit identity. Use bounded restart-on-failure with a restart-rate limit, and make intentional stop persistent until an explicit start or a subsequent session start.

Expose readiness only after successful snapshot creation and binding. A health response carrying the process PID, checked against the intended unit's process group, plus the selected release in status, prevents an unrelated listener from proving readiness. Record start/stop timeouts and useful startup/failure logs. If control tooling launches subprocesses, use argument vectors, closed unused stdin, a filtered child environment and timeouts. Logs should avoid note contents.

When implementation is authorized, record reliance, installed-session lifecycle and the scoped transient-default exception in `project.md`. Put exact unit/release settings, controls, snapshot refresh semantics, readiness and recovery procedures in `docs/service.md`. Those existing owners remain authoritative; this proposal does not silently replace them or correct unrelated text.

## Verification plan and acceptance evidence

- Trace every existing browser operation through transport input, identity assumptions, validation, the application handler and response mapping. Exercise valid reads, invalid identifiers, traversal, unsupported writes/methods and unexpected Host/origin requests. Confirm the source files remain unchanged and no additional transport or outbound work appears.
- In an isolated implementation test, verify explicit loopback binding and inability to reach the service through a non-loopback address. Confirm edits remain absent until restart and the refreshed snapshot appears afterward.
- Exercise login/session startup, explicit start/stop/restart, bounded crash recovery and restart-rate exhaustion. Confirm complete process-group cleanup after normal stop and failed startup; preserve an unrelated process holding the port.
- Verify health cannot pass before extraction completes, missing/unreadable sources fail startup, and a different listener returning success cannot satisfy readiness. Confirm status identifies the intended unit and checkout/release.
- Check that ordinary controls retain release/settings, cannot provision or upgrade the service, and reject unknown arguments. No credential/database/backup scenarios apply to this credential-free, file-backed reader.
- Record the exact public paths, lifecycle scenarios and checks run, their nonzero counts, results and unresolved failures. Acceptance requires evidence for these boundaries; documentation review alone is not runtime evidence. No executable reader or project test guidance is supplied here, so endpoint names, implementation mechanics and actual test results remain unverified.

## Evaluator appendix

Instruction/source files read in full once each (approximately whitespace-delimited words):

| File | Words | Classification and reason |
| --- | ---: | --- |
| `AGENTS.md` | 42 | Required: local ownership and route selection. |
| `project.md` | 54 | Required: authoritative constraints and installed-session choice. |
| `.agents/collections/service-foundation/COLLECTION.md` | 275 | Required: promotion explicitly routes to both members and preserves project choices. |
| `.agents/collections/service-foundation/skills/service-boundaries/SKILL.md` | 377 | Required: service ownership, handler/adapter separation and public-path evidence. |
| `.agents/collections/service-foundation/skills/runtime-operations/SKILL.md` | 1,577 | Required: lifecycle, readiness, process identity, controls and verification. Credential, database and backup detail is irrelevant to this scope, but was included in the member read. |
| `docs/service.md` | 38 | Required and useful: existing snapshot/manual-start behavior and missing lifecycle support. |

Total: approximately 2,363 words. No content was truncated; no content-reading repeats. A separate word-count pass read these same six files mechanically without redisplaying their contents. No other trial directory or authoring repository was inspected. Installation guidance and helper scripts were intentionally not read: no collection installation, tooling implementation or provisioning is requested. No applicable routed guidance is known to have been missed. There is no supplied implementation or separate test-policy owner; work depending on those is deferred to implementation, not inferred from external guidance.

Preserved constraints: local read-only source ownership, loopback-only access, installed user service at session start, no boot-without-login need, no credentials/database/outgoing jobs/remote sharing, no provisioning, and no unrelated file changes. The supplied synthetic directory has no Git repository; work was performed directly within it.
