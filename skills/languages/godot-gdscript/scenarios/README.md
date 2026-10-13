# Godot and GDScript scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| A headless probe logs a failure and then exits zero | Flagged: the probe finishes failure with a nonzero `quit(...)` and returns after requesting it; logging or an assertion is not an exit-status contract. |
| A log-scanning check is replaced by exit-status handling | The replacement first demonstrates success, explicit failure, script or load failure and timeout on the selected engine; `ERROR:` matching stays until then. |
| Source-side `.import` or `.uid` metadata is confused with the generated cache | Adjacent `.import` settings and 4.4+ `.uid` sidecars are committed with their source and preserved on moves; `.godot/` is excluded; identities are not regenerated to quiet a warning. |
| A world measurement is taken under transformed parents or during animation | Parent transforms, the unit convention and all eight AABB corners are applied in one space; the result is a bounding-box estimate with scene identity, transforms, animation sample time and method retained. |
| A question needs a perceptual judgement, such as whether a room feels large | Technical evidence cannot answer it; the perceptual review belongs to an observer workflow, and pixels and FOV do not supply an observer's screen size or distance. |
| Rename a screenshot file | No Godot implementation review is needed. |

## Limits

- The selected engine was unavailable when the skill was drafted, so no
  engine-level probe, import or geometry execution backs these cases; one
  supplied-metadata draft trial preserved the exit-status, sidecar and
  transformed-geometry distinctions.
- Before relying on an exit-status replacement for log scanning, demonstrate it
  on the project's engine; verify fresh import and a transformed geometry
  fixture when those paths are implemented.
