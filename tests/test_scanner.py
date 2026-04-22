import tempfile
import unittest
from pathlib import Path

from readme_roast.scanner import ReadmeScanner


class ReadmeScannerTest(unittest.TestCase):
    def test_detects_missing_markdown_link_and_inline_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "[Guide](docs/setup.md)\n"
                "Run `scripts/dev.py`\n",
                encoding="utf-8",
            )

            report = ReadmeScanner(root).scan()

            self.assertEqual(2, len(report.findings))
            self.assertEqual({"docs/setup.md", "scripts/dev.py"}, {item.value for item in report.findings})

    def test_detects_missing_tree_entry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "```text\n"
                "project/\n"
                "├── src/\n"
                "└── docs/\n"
                "```\n",
                encoding="utf-8",
            )
            (root / "src").mkdir()

            report = ReadmeScanner(root).scan()

            self.assertEqual(1, len(report.findings))
            self.assertEqual("docs/", report.findings[0].value)

    def test_ignores_remote_links_and_existing_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "setup.md").write_text("# setup\n", encoding="utf-8")
            (root / "README.md").write_text(
                "[Docs](docs/setup.md)\n"
                "[Website](https://example.com)\n"
                "See `docs/setup.md`\n",
                encoding="utf-8",
            )

            report = ReadmeScanner(root).scan()

            self.assertEqual([], report.findings)

    def test_supports_custom_readme_name(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.zh-CN.md").write_text("`missing/path.md`\n", encoding="utf-8")

            report = ReadmeScanner(root, readme_name="README.zh-CN.md").scan()

            self.assertEqual(1, len(report.findings))
            self.assertEqual("missing/path.md", report.findings[0].value)


if __name__ == "__main__":
    unittest.main()
