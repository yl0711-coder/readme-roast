import unittest
import tempfile
from pathlib import Path

from readme_roast.cli import main


class CliTest(unittest.TestCase):
    def test_missing_readme_returns_2(self) -> None:
        self.assertEqual(2, main(["/definitely/not/here"]))

    def test_custom_readme_argument_works(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.zh-CN.md").write_text("`missing/path.md`\n", encoding="utf-8")

            self.assertEqual(1, main([str(root), "--readme", "README.zh-CN.md", "--strict"]))


if __name__ == "__main__":
    unittest.main()
