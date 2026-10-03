# Source maintenance

This is a synthetic authoring repository. Use an isolated task worktree under
`.worktrees/` for edits; inspect Git state and base first. Preserve unrelated work.
The complete collection is `collections/project-foundation/`.

When source maintenance is authorized, make the smallest demonstrated correction,
run `python3 scripts/validate-packages.py` and `git diff --check`, and record
actual verification and limits in `validation/notes.md`. For changed routes,
exercise the original case, a nearby task and a case requiring deeper guidance
as appropriate. Keep source repair and consumer pin adoption separate.
