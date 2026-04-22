from __future__ import annotations

import json

from .models import Finding, Report


ROAST_LINES = [
    "this README believes in folders that no longer exist",
    "the documentation has entered a creative writing phase",
    "confidence level is high, filesystem support is low",
    "this repo is explaining a life it no longer lives",
    "the README and the repository are no longer on speaking terms",
]

MAINTENANCE_AURAS = [
    "optimistic chaos",
    "unfinished genius",
    "heroic improvisation",
    "post-release denial",
    "high-confidence drift",
]


class RoastRenderer:
    def render(self, report: Report) -> str:
        if not report.findings:
            return (
                "README Roast\n\n"
                "Status: surprisingly honest\n"
                "This README appears to describe reality.\n"
            )

        drama = min(100, 35 + len(report.findings) * 11)
        confidence = max(12, 92 - len(report.findings) * 9)
        aura = MAINTENANCE_AURAS[len(report.findings) % len(MAINTENANCE_AURAS)]

        lines = [
            "README Roast",
            "",
            f"Repository: {report.root}",
            f"README: {report.readme}",
            "",
            "Verdict:",
            f"- {ROAST_LINES[len(report.findings) % len(ROAST_LINES)]}",
            f"- findings: {len(report.findings)}",
            f"- confidence without evidence: {confidence}%",
            f"- documentation drama: {drama}%",
            f"- maintenance aura: {aura}",
            "",
            "Highlights:",
        ]

        for finding in report.findings[:8]:
            lines.append(f'- line {finding.line}: {finding.message}')

        if len(report.findings) > 8:
            lines.append(f"- plus {len(report.findings) - 8} more reality issues")

        lines.extend(
            [
                "",
                "Advice:",
                "- open the README and the repository side by side",
                "- remove claims that no longer exist",
                "- make the docs slightly less ambitious than the code",
            ]
        )

        return "\n".join(lines).rstrip() + "\n"


class ReviewRenderer:
    def render(self, report: Report) -> str:
        lines = [
            "README Review",
            "",
            f"Repository: {report.root}",
            f"README: {report.readme}",
            "",
            "Findings:",
        ]

        if not report.findings:
            lines.append("- none")
            lines.append("")
            lines.append("Result: clean")
            return "\n".join(lines) + "\n"

        for finding in report.findings:
            lines.append(f'- line {finding.line} [{finding.kind}] {finding.message}')

        lines.append("")
        lines.append("Result: failed")
        return "\n".join(lines) + "\n"


class JsonRenderer:
    def render(self, report: Report) -> str:
        payload = {
            "repository": report.root,
            "readme": report.readme,
            "has_issues": report.has_issues,
            "findings": [self._finding(finding) for finding in report.findings],
        }
        return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"

    @staticmethod
    def _finding(finding: Finding) -> dict[str, str | int]:
        return {
            "kind": finding.kind,
            "line": finding.line,
            "value": finding.value,
            "message": finding.message,
        }
