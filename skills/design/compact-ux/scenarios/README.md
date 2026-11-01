# Compact UX scenarios

Synthetic requests and expected behavior. Ordinary use does not read these
cases. Record observed evaluations with the change that ran them.

## Familiar equipment comparison

Request: make the equipment grid less verbose; experienced players know the
rules. Remove repeated information circles too. Cards currently show names,
selection, damage, timing, parry and several lines of reach instructions.

Expected: preserve comparison values and selection, shorten repeated copy and
attach explanations to the name and relevant stat areas. Preserve negative
signs and fixed versus rolled amounts. Provide keyboard and touch access without
making inspection equip an item unexpectedly. Check a narrow layout and the
ordinary selection path. Do not replace every removed line with a new icon.

## Familiar editor with repeated help controls

Request: simplify a material inspector used daily by its author. Every field
has a sentence explaining it and an information circle. Several fields can be
unavailable for the selected material.

Expected: keep labels, current values and availability visible. Put explanation
on the field label or value, remove redundant help controls and retain reasons
that affect the current edit. Preserve edit behavior and saved values. Use the
existing visual language and test keyboard and touch details.

## Consequential first use

Request: simplify a new user's account deletion dialog by hiding its explanation
in a tooltip. The dialog explains which shared records will be removed.

Expected: do not assume familiarity or hide the consequence needed to decide.
Keep deletion meaning and confirmation explicit. A compact-UX trigger should
not select this package for first-use onboarding or a visual-only change.

## Nearby implementation task

Request: fix the material loader's duplicate network requests; keep the inspector
interface unchanged.

Expected: do not activate this skill or redesign the inspector. Work on request
ownership and preserve the requested UI boundary.
