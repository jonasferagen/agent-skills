---
name: godot-gdscript
description: "Write or review Godot GDScript, headless scene probes, resource imports and scene-geometry measurements. Use for engine implementation and technical checks; whether a scene looks or plays right is a human judgement outside this skill."
metadata:
  version: "0.2.0"
---

# Godot and GDScript

Start with the project's engine version and existing launch/check commands. If
none are documented, infer the version from `project.godot` (`config/features`
lists the engine version a project was last opened with), CI configuration or a
tool-version file, state the assumption in your report, and ask the user when
nothing settles it. These patterns target Godot 4; confirm version-sensitive
APIs against that engine's manual. Read only the heading relevant to the change.

The engine executable is whatever the project's scripts name; otherwise use
`godot` or `godot4` on `PATH`, or a `GODOT` environment variable when the
project sets one. Record which executable and version a check ran against.

## Typed boundaries

Use parameter and return types and typed collections where they clarify the data
contract. Use `:=` when the expression has a known useful type; dynamic dictionary
lookups and generic node/resource APIs may need validation and an explicit type.
Check an object cast before dereferencing it: `as` can yield null. Type annotations
do not validate external data or prove a required node exists. Keep `Variant` at
boundaries that are genuinely dynamic rather than silencing a warning by accident.

## Headless probes

A probe is a script that loads a scene without a window, inspects it and exits
with a status. Write it as `extends SceneTree` (the `--script` entry point that
owns the main loop; an `extends Node` script needs a scene to host it) and run the
chosen executable with `--headless --path <project> --script res://<probe>.gd`.
Import resources first:
a fresh checkout has no `.godot/` cache, so run
`godot --headless --path <project> --import` (or the project's own import step)
before the probe. Measure after the nodes and required frame/physics state are
ready, and release instantiated nodes before exiting.

Make the result explicit: finish success with `quit(0)` and failure with a nonzero
`quit(...)`. Return from the current function after requesting failure so later
code cannot continue to a success path. A helper should propagate failure to its
caller. Logging an error or relying on an assertion is not an exit-status contract.

The runner should bound execution time, preserve the engine status and
diagnostics, and require a completion marker: a fixed sentinel line the probe
prints just before `quit(0)` (for example `PROBE OK`), so a run that died early
with status 0 is still a failure. For example:

```bash
timeout 120 godot --headless --path . --script res://tools/probe.gd >probe.log 2>&1
status=$?   # 124 means the timeout fired
grep -qx 'PROBE OK' probe.log || status=1
```

Before an exit-status check replaces a log-scanning one, show it on the chosen
engine against four cases: a passing probe; a deliberate failure (a probe that
calls `quit(1)` on an assertion you know is false); a script or load failure (a
probe with a syntax error, or one that loads a missing `res://` path); and a
timeout (a probe that never calls `quit`). Keep the existing `ERROR:` matching
until all four give the expected nonzero status; `ERROR:` matching alone is not a
complete failure detector either. Headless success does not establish rendered
appearance or playable quality.

## Imports and source identity

For Godot 4, keep authored assets and adjacent `<asset>.import` settings in source
control; exclude the generated `.godot/` cache. For versions that generate script
or shader `.uid` sidecars (introduced in 4.4), commit them with their source and
preserve them on moves. Do not confuse adjacent `.import` metadata with an import
cache directory or regenerate identities merely to quiet a warning.

Treat import options as inputs: retain settings that affect scale, materials,
filtering, compression or animation. Reimport and inspect the resulting resource
when changing them. Keep game-owned adaptations outside importer-generated output
that the next import can replace. Use a disposable copy when a probe/import must
leave authored source unchanged; compare the relevant source files afterward.

## Measure the instantiated scene

When the task involves scene geometry, name the measured quantity and
coordinate space. Apply parent transforms and the project's unit convention;
source mesh dimensions alone do not give world size. If the project states no
unit convention, assume Godot's usual one (1 unit = 1 metre) and say so in the
result. For world bounds, transform each contributing local AABB into the same
space (e.g. all eight corners) before combining bounds. Report this as a
bounding-box estimate, which may overestimate rotated geometry, not an exact
surface measure.

Distinguish mesh bounds from collision shapes and visible geometry. Rest-pose
bounds do not establish an animated silhouette: identify animation, sample time
and the measurement method. State scene/resource identity, relevant transforms
and camera settings in the report. Pixels and FOV cannot supply an observer's
physical screen size or perceived distance. Whether something looks or plays
right is a perceptual judgement this skill cannot make: give the user the
measurements, the scene and camera used, and any screenshots or a launch command
to see it, and ask for a human review.

## Technical sources

Use the manual matching the chosen engine; these links follow stable documentation:
[typing](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html),
[SceneTree](https://docs.godotengine.org/en/stable/classes/class_scenetree.html),
[command line](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html),
[imports](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html),
[version control](https://docs.godotengine.org/en/stable/tutorials/best_practices/version_control_systems.html),
[visual bounds](https://docs.godotengine.org/en/stable/classes/class_visualinstance3d.html).
The [4.4 UID change](https://godotengine.org/article/uid-changes-coming-to-godot-4-4/)
explains the sidecar version boundary.
