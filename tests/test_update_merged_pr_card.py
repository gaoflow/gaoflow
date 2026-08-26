import importlib.util
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "update_merged_pr_card.py"


def load_generator():
    spec = importlib.util.spec_from_file_location("update_merged_pr_card", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class MergedPrCardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.generator = load_generator()

    def test_rendered_svg_contains_exact_count_and_no_remote_content(self):
        svg = self.generator.render_svg(609, "gaoflow")
        root = ET.fromstring(svg)

        self.assertEqual(root.attrib["viewBox"], "0 0 680 150")
        self.assertIn(">609<", svg)
        self.assertIn("609 merged pull requests", svg)
        self.assertNotIn("<script", svg)
        self.assertNotIn('href="http', svg)
        self.assertNotIn("url(http", svg)

    def test_negative_count_is_rejected(self):
        with self.assertRaises(ValueError):
            self.generator.render_svg(-1, "gaoflow")

    def test_write_is_idempotent(self):
        svg = self.generator.render_svg(609, "gaoflow")
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "merged-prs.svg"

            self.assertTrue(self.generator.write_if_changed(output, svg))
            self.assertFalse(self.generator.write_if_changed(output, svg))
            self.assertEqual(output.read_text(encoding="utf-8"), svg)


if __name__ == "__main__":
    unittest.main()
