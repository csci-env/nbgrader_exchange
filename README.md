# cscienv_nbgrader_exchange

Changes nbgrader's submission/collect folder from
`<exchange-root>/<course-id>/inbound/<submission-folder>/...` to
`<exchange-root>/<course-id>/inbound/<NB_USER>/<submission-folder>/...`.
This allows for more easily preventing student access to other student's
submissions.

## Requirements

- JupyterLab >= 3.0

## Install

To install the extension, execute:

```bash
pip install cscienv_nbgrader_exchange
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall cscienv_nbgrader_exchange
```

## Troubleshoot

If you are seeing the frontend extension, but it is not working, check
that the server extension is enabled:

```bash
jupyter server extension list
```

If the server extension is installed and enabled, but you are not seeing
the frontend extension, check the frontend extension is installed:

```bash
jupyter labextension list
```

