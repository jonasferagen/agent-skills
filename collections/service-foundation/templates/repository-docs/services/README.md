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

<!-- Copy the dispatcher as executable services/control. Each defined service
provides executable services/<name>/control accepting an action and --root.
Link the selected service/runtime guidance; remove this prompt. -->
