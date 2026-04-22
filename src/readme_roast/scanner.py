from __future__ import annotations

import re
from pathlib import Path

from .models import Finding, Report

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
TREE_LINE_RE = re.compile(r"^[\s│├└─]+([A-Za-z0-9._/-]+/?)(\s+#.*)?$")


class ReadmeScanner:
    def __init__(self, root: Path, readme_name: str = "README.md") -> None:
        self.root = root
        self.readme = self.root / readme_name

    def scan(self) -> Report:
        if not self.readme.exists():
            raise FileNotFoundError(f"{self.readme.name} not found in {self.root}")

        findings: list[Finding] = []
        lines = self.readme.read_text(encoding="utf-8", errors="ignore").splitlines()

        for index, line in enumerate(lines, start=1):
            findings.extend(self._markdown_links(line, index))
            findings.extend(self._inline_paths(line, index))
            findings.extend(self._tree_paths(line, index))

        return Report(
            root=str(self.root),
            readme=str(self.readme),
            findings=self._unique(findings),
        )

    def _markdown_links(self, line: str, line_number: int) -> list[Finding]:
        findings: list[Finding] = []

        for target in MARKDOWN_LINK_RE.findall(line):
            if self._skip_target(target):
                continue

            if not self._exists(target):
                findings.append(
                    Finding(
                        kind="link",
                        line=line_number,
                        value=target,
                        message=f'local link target "{target}" does not exist',
                    )
                )

        return findings

    def _inline_paths(self, line: str, line_number: int) -> list[Finding]:
        findings: list[Finding] = []

        for value in INLINE_CODE_RE.findall(line):
            candidate = value.strip()

            if not self._looks_like_path(candidate) or self._skip_target(candidate):
                continue

            if not self._exists(candidate):
                findings.append(
                    Finding(
                        kind="path",
                        line=line_number,
                        value=candidate,
                        message=f'referenced path "{candidate}" does not exist',
                    )
                )

        return findings

    def _tree_paths(self, line: str, line_number: int) -> list[Finding]:
        match = TREE_LINE_RE.match(line)

        if not match:
            return []

        value = match.group(1).strip()

        if self._skip_target(value) or self._exists(value):
            return []

        return [
            Finding(
                kind="tree",
                line=line_number,
                value=value,
                message=f'project tree entry "{value}" does not exist',
            )
        ]

    def _exists(self, target: str) -> bool:
        candidate = (self.root / target).resolve()

        try:
            candidate.relative_to(self.root.resolve())
        except ValueError:
            return False

        return candidate.exists()

    @staticmethod
    def _skip_target(target: str) -> bool:
        return (
            target.startswith("http://")
            or target.startswith("https://")
            or target.startswith("#")
            or "://" in target
        )

    @staticmethod
    def _looks_like_path(value: str) -> bool:
        if "[" in value or "]" in value or "(" in value or ")" in value:
            return False

        return (
            "/" in value
            or value.endswith(".md")
            or value.endswith(".json")
            or value.endswith(".php")
            or value.endswith(".py")
            or value.endswith(".js")
            or value.endswith(".ts")
            or value.endswith(".yml")
            or value.endswith(".yaml")
        )

    @staticmethod
    def _unique(findings: list[Finding]) -> list[Finding]:
        seen: set[tuple[str, int, str]] = set()
        unique: list[Finding] = []

        for finding in findings:
            key = (finding.kind, finding.line, finding.value)
            if key in seen:
                continue

            unique.append(finding)
            seen.add(key)

        return unique
