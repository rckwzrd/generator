import unittest
from block_markdown import markdown_to_blocks

test_md = """# This is a heading

This is a paragraph.\n It has **bold** and *italic* words.

* item
* item
* item

"""

test_md_multi_new_line = """# Heading 1


# Heading 2



# Heading 3
"""

test_md_white_space = """   # Heading 1

This is a paragraph 1.   

   # Heading 2   

This is paragraph 2.
"""


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        h1 = "# This is a heading"
        p = "This is a paragraph. It has **bold** and *italic* words."
        li = "* item\n* item\n* item"
        blocks = markdown_to_blocks(test_md)
        case = [h1, p, li]
        self.assertListEqual(blocks, case)

    def test_multi_newline(self):
        h1 = "# Heading 1"
        h2 = "# Heading 2"
        h3 = "# Heading 3"
        blocks = markdown_to_blocks(test_md_multi_new_line)
        case = [h1, h2, h3]
        self.assertListEqual(blocks, case)

    def test_white_space(self):
        h1 = "# Heading 1"
        p1 = "This is a paragraph 1."
        h2 = "# Heading 2"
        p2 = "This is paragraph 2."
        blocks = markdown_to_blocks(test_md_white_space)
        case = [h1, p1, h2, p2]
        self.assertListEqual(blocks, case)
