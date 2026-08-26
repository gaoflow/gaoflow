import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "update_merged_pr_count.py"
START = "<!-- merged-pr-count:start -->"
END = "<!-- merged-pr-count:end -->"
SAMPLE = f"""before
{START}
[**609 merged pull requests**](https://example.test) across public projects.
{END}
after
"""


def load_updater():
    spec = importlib.util.spec_from_file_location("update_merged_pr_count", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class MergedPrCountTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.updater = load_updater()

    def test_replaces_only_the_count(self):
        updated = self.updater.replace_count(SAMPLE, 610)

        self.assertEqual(updated, SAMPLE.replace("**609 merged", "**610 merged"))
        self.assertTrue(updated.startswith("before\n"))
        self.assertTrue(updated.endswith("after\n"))

    def test_reapplying_the_same_count_is_idempotent(self):
        self.assertEqual(self.updater.replace_count(SAMPLE, 609), SAMPLE)

    def test_invalid_marker_layouts_are_rejected(self):
        cases = {
            "missing start": SAMPLE.replace(START, ""),
            "missing end": SAMPLE.replace(END, ""),
            "duplicate start": SAMPLE.replace(START, f"{START}\n{START}"),
            "duplicate end": SAMPLE.replace(END, f"{END}\n{END}"),
            "reversed": SAMPLE.replace(START, "TEMP")
            .replace(END, START)
            .replace("TEMP", END),
        }
        for name, readme in cases.items():
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.updater.replace_count(readme, 610)

    def test_missing_or_duplicate_count_phrase_is_rejected(self):
        missing = SAMPLE.replace("**609 merged pull requests**", "merged pull requests")
        duplicate = SAMPLE.replace(
            "across public projects.", "and **608 merged pull requests**."
        )

        for readme in (missing, duplicate):
            with self.assertRaises(ValueError):
                self.updater.replace_count(readme, 610)

    def test_invalid_counts_are_rejected(self):
        for count in (-1, 1.5, True, "610"):
            with self.subTest(count=count), self.assertRaises(ValueError):
                self.updater.replace_count(SAMPLE, count)

    def test_write_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "README.md"

            self.assertTrue(self.updater.write_if_changed(output, SAMPLE))
            self.assertFalse(self.updater.write_if_changed(output, SAMPLE))
            self.assertEqual(output.read_text(encoding="utf-8"), SAMPLE)

    def test_validation_failure_does_not_touch_existing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "README.md"
            output.write_text(SAMPLE, encoding="utf-8")

            with self.assertRaises(ValueError):
                invalid = SAMPLE.replace(START, "")
                updated = self.updater.replace_count(invalid, 610)
                self.updater.write_if_changed(output, updated)

            self.assertEqual(output.read_text(encoding="utf-8"), SAMPLE)


if __name__ == "__main__":
    unittest.main()
