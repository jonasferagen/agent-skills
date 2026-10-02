# Notes for a retrieval plan

These are supplied planning assumptions, not measured results. Current requirement:
read-only retrieval of synthetic local data, no UI. Production suitability and
performance remain unverified. Database model decisions remain open.

Three ways to exercise retrieval after those decisions are settled:
- Saved SQL queries: direct visibility into joins; requires a SQL-capable caller;
  query definitions must be maintained with the schema.
- A command-line application: repeatable named operations; requires application
  language and packaging choices; query code must be maintained with the schema.
- An HTTP endpoint: supports separate callers; introduces transport, access and
  hosting decisions plus operational work; request contracts and query code must
  be maintained. No present requirement calls for separate callers.

Write docs/database/retrieval-options.md so a reader can compare what each exposes,
what it requires, and what needs maintenance. Preserve uncertainty and make a
bounded recommendation for the next experiment, without adopting a stack or
creating implementation. Link the existing model for unresolved domain decisions.
