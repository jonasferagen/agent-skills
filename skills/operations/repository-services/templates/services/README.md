# Services

<!-- List implemented service definitions and link their operating guides.
Keep candidate status and next work in the existing design/planning owner.
Delete this prompt before adopting the template. -->

| Service | Lifecycle | Operating guide |
| --- | --- | --- |

<!-- Link the project's service convention and candidate review when present. -->

Use `./services/control <name> start|stop|restart|status|logs`.
`./services/control --help` lists services with executable controllers. Options
after the action pass through to that service's controller.
`./services/control status` reports every service in the project: this checkout and
each member checkout it was given, by repeated `--checkout` or once in
`SERVICE_CHECKOUTS`. Add `--scope checkout` to narrow it to one. It reports the installed checkout even when
run from a task worktree, and exits nonzero only when a controller will not run.

<!-- Copy the dispatcher as executable services/control. Each defined service
provides executable services/<name>/control accepting an action and --root.
Link the selected service/runtime guidance; remove this prompt. -->
