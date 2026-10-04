# Reader maintenance design

The reader is currently a manual, read-only localhost spike. The following is a proposal, not implemented behavior. Project-owned source files remain read-only; network sharing and credentials stay out of scope.

## Application slice

Define a `readDocument(documentId)` operation that returns document content or a clear invalid-input, missing-document or unavailable-source result. The operation owns allowed document selection and read-only rules. A localhost request adapter parses requests and maps results; a source-file adapter reads only from the project's permitted document root. Path traversal and symlink escapes must not expand that boundary. Startup supplies the root and concrete collaborators.

Source files remain authoritative. Request data is transient; this slice needs no job system, database or durable run records. Keep caching out of the first increment so subsequent reads can observe source changes.

Verify a normal read, unknown document, escaping path, unreadable file and a file disappearing during a read. Check that the source tree is unchanged and subsequent requests still work after a failed read. These are proposed checks, not execution evidence.

## Missing service prerequisite

The project explicitly has no service guidance installed, and supplies no service-guidance route. Application-foundation requires that route for maintained service use; its application design does not establish runtime coverage. Have the project owner select/install service guidance before implementing the maintained service boundary.

That guidance must resolve loopback-only binding, startup configuration validation, process ownership, start/stop/restart behavior, graceful shutdown, readiness, failure reporting, logs and ongoing update responsibility. Until resolved, there is no complete maintained-service design or verified lifecycle contract. Do not choose a supervisor or provisioning mechanism from this application guidance alone.

The smallest next increment is to implement and verify the bounded read operation independently, then design and test the localhost lifecycle under the selected service guidance. No provisioning was performed.
