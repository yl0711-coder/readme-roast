from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .render import JsonRenderer, ReviewRenderer, RoastRenderer
from .scanner import ReadmeScanner


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="readme-roast",
        description="Roast README drift or report it strictly.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Repository path. Defaults to current directory.",
    )
    parser.add_argument(
        "--mode",
        choices=["roast", "review"],
        default="roast",
        help="Output style. Defaults to roast.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Render findings as JSON.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return exit code 1 when findings are present.",
    )
    parser.add_argument(
        "--readme",
        default="README.md",
        help="README file name to inspect. Defaults to README.md.",
    )

    args = parser.parse_args(argv)
    root = Path(args.path).resolve()

    try:
        report = ReadmeScanner(root, readme_name=args.readme).scan()
    except FileNotFoundError as error:
        print(f"readme-roast: {error}", file=sys.stderr)
        return 2

    if args.json:
        output = JsonRenderer().render(report)
    elif args.mode == "review":
        output = ReviewRenderer().render(report)
    else:
        output = RoastRenderer().render(report)

    print(output, end="")

    if args.strict and report.has_issues:
        return 1

    return 0
