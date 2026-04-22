from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Finding:
    kind: str
    line: int
    value: str
    message: str


@dataclass(frozen=True)
class Report:
    root: str
    readme: str
    findings: list[Finding] = field(default_factory=list)

    @property
    def has_issues(self) -> bool:
        return bool(self.findings)

