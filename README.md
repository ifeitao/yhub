# yhub

**This is a name-reservation release (`0.0.1`).** It reserves the distribution name `yhub` on
PyPI and does nothing else.

The real package — **an always-on local hub for your own machines, services and pipelines**
(CLI + web dashboard + MCP server, installed from a single wheel) — is planned for **2027**.

Nothing in this repository is a working product yet. Please don't build on it.

## What the real release will be

- **Information surface**: a wall of status cells (services, sync pipelines, scheduled jobs,
  mounts) you keep on screen, each cell a three-state reading — fresh / stale / failing.
- **Action surface**: buttons, toggles and inputs on those same cells, so a cell can *do*
  something, not just report.
- **Three faces from one declaration**: every capability is declared once and generated into a
  CLI command, an HTTP route and an MCP tool.
- **Local by default**: binds `127.0.0.1` only; reads the machine it runs on (local daemons,
  mounts, files), not a cloud account.

## Verify the install

```bash
uv tool install yhub
yhub --version          # -> yhub 0.0.1
```

or without installing anything:

```bash
uv run --no-project --with yhub python -m yhub --version
```

## License

MIT — see [LICENSE](LICENSE).
