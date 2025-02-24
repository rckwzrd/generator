import unittest
from generate_content import extract_title

md = """Not Title

# Title
"""

md_error = """Not Title
"""


class TestTextNode(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(extract_title(md), "Title")
        with self.assertRaises(ValueError):
            extract_title(md_error)
