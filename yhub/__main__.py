"""Console entry point for the yhub name-reservation release."""

from __future__ import annotations

import sys

from . import __version__

_NAME = "yhub"
_TAGLINE = "an always-on local hub for your own machines, services and pipelines"


def _text() -> str:
    return (
        f"{_NAME} {__version__} — name-reservation release\n"
        "\n"
        "This release reserves the distribution name on PyPI and does nothing else.\n"
        f"The real package ({_TAGLINE}) is planned for 2027: CLI + web dashboard + MCP\n"
        "server, installed from a single wheel.\n"
        "\n"
        f"Until then, `{_NAME} --version` is all this package does.\n"
    )


def main(argv: list[str] | None = None) -> int:
    """Print the reservation notice. `--version` / `--help` are the only recognised flags."""
    args = list(sys.argv[1:] if argv is None else argv)
    if args and args[0] in ("-V", "--version"):
        print(f"{_NAME} {__version__}")
        return 0
    if args and args[0] in ("-h", "--help"):
        print(_text())
        print(f"usage: {_NAME} [--version | --help]")
        return 0
    print(_text())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
