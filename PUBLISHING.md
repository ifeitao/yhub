# Publishing `yhub` 0.0.1 (name reservation)

Everything here is prepared; the only steps left need your PyPI/GitHub credentials.

## 0. Check what will be uploaded

```bash
cd ~/Projects/yhub
uv build --no-sources        # -> dist/yhub-0.0.1-py3-none-any.whl + dist/yhub-0.0.1.tar.gz
uv run --no-project --with ./dist/yhub-0.0.1-py3-none-any.whl yhub --version
```

## Option A — fastest one-off (API token)

The project does not exist yet, so you need an **account-scoped** token
(PyPI → Account settings → API tokens → "Add API token", scope = *entire account*).

```bash
cd ~/Projects/yhub
uv build --no-sources
UV_PUBLISH_TOKEN=pypi-... uv publish
```

After the project exists you can (and should) switch to a project-scoped token, or to Option B.

## Option B — recommended, no secrets (trusted publishing)

1. Create the GitHub repo `ifeitao/yhub` and push these files.
2. On PyPI: **Account → Publishing → Add a pending publisher**
   - PyPI project name: `yhub`
   - Owner: `ifeitao`
   - Repository name: `yhub`
   - Workflow name: `publish.yml`
   - Environment name: `pypi`
3. Create a GitHub Release (or run the `publish` workflow manually). `.github/workflows/publish.yml`
   builds and uploads with OIDC — no token anywhere.

## Rehearse on TestPyPI first (recommended)

Add this to `pyproject.toml`:

```toml
[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true
```

Then:

```bash
uv build --no-sources
uv publish --index testpypi            # needs a TestPyPI token (separate account)
uv run --no-project --index-url https://test.pypi.org/simple/ --with yhub yhub --version
```

## After publishing

```bash
uv tool install yhub --refresh
yhub --version         # -> yhub 0.0.1
```

## Notes and pitfalls

- **The license is baked into 0.0.1 permanently.** `license = "MIT"` is what this version will
  carry forever; changing it later only affects new releases. Confirm MIT (simplest, most
  permissive) vs Apache-2.0 (adds an explicit patent grant, common for dev tools) *before*
  uploading.
- **PEP 639 needs hatchling >= 1.27** for `license = "MIT"` + `license-files`; the pin in
  `pyproject.toml` says so.
- **`uv build --no-sources`** is the documented build for publishing (builds resolve without
  `tool.uv.sources`).
- PyPI rejects new names that are **too similar to an existing project** (`-`, `_`, `.` count as
  the same character). Reserving `yhub` therefore also blocks look-alikes such as `y-hub`.
- Do **not** publish empty metadata-only releases: a name claimed with no intent to use can be
  reclaimed by PyPI. This package has a real, runnable entry point and a README explaining the
  reservation, which is the intended shape.
- PyPI no longer accepts username/password uploads — token or trusted publishing only.
