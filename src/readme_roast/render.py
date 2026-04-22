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


class RoastRenderer:
    def render(self, report: Report) -> str:
        if not report.findings:
            return (
                "README Roast\n\n"
                "Status: surprisingly honest\n"
                "This README appears to describe reality.\n"
            )

        lines = [
            "README Roast",
            "",
            f"Repository: {report.root}",
            f"README: {report.readme}",
            "",
            "Verdict:",
            f"- {ROAST_LINES[len(report.findings) % len(ROAST_LINES)]}",
            f"- findings: {len(report.findings)}",
            "",
            "Highlights:",
        ]

        for finding in report.findings[:8]:
            lines.append(f'- line {finding.line}: {finding.message}')

        if len(report.findings) > 8:
            lines.append(f"- plus {len(report.findings) - 8} more reality issues")

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

