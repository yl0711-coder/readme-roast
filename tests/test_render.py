import json
import unittest

from readme_roast.models import Finding, Report
from readme_roast.render import JsonRenderer, ReviewRenderer, RoastRenderer


def _report(findings=None):
    if findings is None:
        findings = [
            Finding("link", 3, "docs/guide.md", 'local link target "docs/guide.md" does not exist'),
        ]
    return Report(root="/work/app", readme="/work/app/README.md", findings=findings)


class RoastRendererTest(unittest.TestCase):
    def test_clean_report_is_honest(self):
        output = RoastRenderer().render(_report(findings=[]))

        self.assertIn("surprisingly honest", output)

    def test_findings_are_summarized(self):
        output = RoastRenderer().render(_report())

        self.assertIn("findings: 1", output)
        self.assertIn("line 3", output)


class ReviewRendererTest(unittest.TestCase):
    def test_failed_result_lists_findings(self):
        output = ReviewRenderer().render(_report())

        self.assertIn("line 3 [link]", output)
        self.assertIn("Result: failed", output)

    def test_clean_result(self):
        output = ReviewRenderer().render(_report(findings=[]))

        self.assertIn("Result: clean", output)


class JsonRendererTest(unittest.TestCase):
    def test_json_is_valid(self):
        payload = json.loads(JsonRenderer().render(_report()))

        self.assertTrue(payload["has_issues"])
        self.assertEqual("link", payload["findings"][0]["kind"])
        self.assertEqual(3, payload["findings"][0]["line"])


if __name__ == "__main__":
    unittest.main()
