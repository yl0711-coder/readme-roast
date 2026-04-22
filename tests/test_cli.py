import unittest

from readme_roast.cli import main


class CliTest(unittest.TestCase):
    def test_missing_readme_returns_2(self) -> None:
        self.assertEqual(2, main(["/definitely/not/here"]))


if __name__ == "__main__":
    unittest.main()

