# Godot and GDScript scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Expected behavior |
| --- | --- |
| A headless probe logs a failure and then exits zero | Flagged: the probe finishes failure with a nonzero `quit(...)` and returns after requesting it; logging or an assertion is not an exit-status contract. |
| A log-scanning check is replaced by exit-status handling | The replacement is first shown on the project's engine against a passing probe, a deliberate `quit(1)`, a syntax or missing-resource failure and a never-quitting probe; `ERROR:` matching stays until all four give nonzero status. |
| A probe is run on a fresh checkout with no `.godot/` cache | A headless import pass runs before the probe, and the run is bounded with a timeout whose status is kept apart from the engine's. |
| The project documents no engine version or unit convention | The version is inferred from `project.godot`, CI or tool-version files; 1 unit = 1 metre is assumed; both assumptions are stated in the report. |
| Source-side `.import` or `.uid` metadata is confused with the generated cache | Adjacent `.import` settings and 4.4+ `.uid` sidecars are committed with their source and preserved on moves; `.godot/` is excluded; identities are not regenerated to quiet a warning. |
| A world measurement is taken under transformed parents or during animation | Parent transforms, the unit convention and all eight AABB corners are applied in one space; the result is a bounding-box estimate with scene identity, transforms, animation sample time and method retained. |
| A question needs a perceptual judgement, such as whether a scene looks right at a given distance | Technical measurements are reported and a human review is requested from the user; pixels and FOV do not supply an observer's screen size or distance. |
| Rename a screenshot file | No Godot implementation review is needed. |

## Limits

- These cases are not verified against a running engine. Before relying on an
  exit-status replacement for log scanning, demonstrate it on the project's
  engine, including a fresh import and a transformed-geometry fixture.
