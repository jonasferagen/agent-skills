---
name: godot-gdscript
description: "Write or review Godot GDScript, headless scene probes, resource imports and scene-geometry measurements. Use for engine implementation and technical evidence; perceptual review needs its own observer workflow."
metadata:
  version: "0.1.0"
---

# Godot and GDScript

Start with the project's engine version and existing launch/check commands. These
patterns target Godot 4; confirm version-sensitive APIs against that engine's
manual. Load only the section relevant to the change.

## Typed boundaries

Use parameter and return types and typed collections where they clarify the data
contract. Use `:=` when the expression has a known useful type; dynamic dictionary
lookups and generic node/resource APIs may need validation and an explicit type.
Check an object cast before dereferencing it: `as` can yield null. Type annotations
do not validate external data or prove a required node exists. Keep `Variant` at
boundaries that are genuinely dynamic rather than silencing a warning by accident.

## Headless probes

For an `extends SceneTree` probe, use the selected executable with
`--headless --path <project> --script res://<probe>.gd`. Prepare required imports
first using the project's workflow; a fresh copy may need an editor import pass.
Measure after the nodes and required frame/physics state are ready, and release
instantiated nodes before exiting.

Make the result explicit: finish success with `quit(0)` and failure with a nonzero
`quit(...)`. Return from the current function after requesting failure so later
code cannot continue to a success path. A helper should propagate failure to its
caller. Logging an error or relying on an assertion is not an exit-status contract.

The runner should bound execution time, preserve the engine status and diagnostics,
and require the expected completion evidence. Check a deliberately failing case as
well as a passing one on the selected engine. Keep existing log-error checks until
those checks establish the replacement covers relevant script/import failures;
`ERROR:` matching alone is not a complete failure detector. Headless success does
not establish rendered appearance or playable quality.

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

Name the measured quantity and coordinate space. Apply parent transforms and the
project's unit convention; source mesh dimensions alone do not give world size.
For world bounds, transform each contributing local AABB into the same space
(e.g. all eight corners) before combining bounds. Report this as a bounding-box
estimate, which may overestimate rotated geometry, not an exact surface measure.

Distinguish mesh bounds from collision shapes and visible geometry. Rest-pose
bounds do not establish an animated silhouette: identify animation, sample time
and the measurement method. Retain scene/resource identity, relevant transforms
and camera settings with the result. Pixels and FOV cannot supply an observer's
physical screen size or perceived distance.

If work exposes a missing case or costly workaround, surface the concrete effect
and smallest candidate improvement in existing work notes. Keep unverified fixes
explicit; ordinary success needs no extra report.

## Technical sources

Use the manual matching the selected engine; these links follow stable documentation:
[typing](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html),
[SceneTree](https://docs.godotengine.org/en/stable/classes/class_scenetree.html),
[imports](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/import_process.html),
[version control](https://docs.godotengine.org/en/stable/tutorials/best_practices/version_control_systems.html),
[visual bounds](https://docs.godotengine.org/en/stable/classes/class_visualinstance3d.html).
The [4.4 UID change](https://godotengine.org/article/uid-changes-coming-to-godot-4-4/)
explains the sidecar version boundary.
