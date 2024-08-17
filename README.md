# cscienv_nbgrader_exchange

Changes nbgrader's submission/collect folder from
`<exchange-root>/<course-id>/inbound/<submission-folder>/...` to
`<exchange-root>/<course-id>/inbound/<NB_USER>/<submission-folder>/...`.
This allows for more easily preventing student access to other student's
submissions.

To see the main changes run `git diff compare~1 compare`

## Requirements

- JupyterLab >= 3.0

## Install

To install the extension, execute:

```bash
pip install git+https://github.com/csci-env/nbgrader_exchange.git
```

---

## Notes

This JupyterLab extension modifies how nbgrader interacts with its
exchange directories to isolate student submissions from each other. This
is necessary because the JupyterLab instances use the default 'jovyan'
user regardless of which student/instructor is logged in. Not isolating
submissions would allow students to modify submissions from other students.
This isolation is accomplished by nesting student submissions under an
additional folder named after their nbgrader student ID (their student
email). This allows mounting solely the folder for the current student
into the Jupyterlab container.

The extension setup is twofold:
1. Install the extension via the Dockerfile for the base container.
2. add a `c.ExchangeFactory.xxxx = "cscienv_nbgrader_exchange.xxxx.xxx"` line to
   the base container's nbgrader configuration to override which classes are
   used as the implementation of the various nbgrader commands.

The above changes and supporting code in the deploy script are already present.
Full integration of nbgrader itself needs to be enabled by uncommenting the
lines in the Dockerfile of the base container under the `nbgrader` heading and
uncommenting the lines in the start-notebook-hook.sh script (also for the base
container)

The extension's
code inherits from nbgrader's default implementations. For example, the
`cscienv_nbgrader_exchange.collect.ExchangeCollect` class extends nbgrader's
`nbgrader.exchange.default.collect.ExchangeCollect` class and overrides
the minimum number of methods needed to implement the custom behaviour.

The overridden methods in the extension are based on version 0.8.3 (at the time
of writing this documentation) of the nbgrader extension. The source of the
overridden methods is virtually the same with just a few changes to implement
the custom behaviour. Version 0.8.3 was used because it is the newest version
that works on the version of JupyterLab used by the CSCI environment.

