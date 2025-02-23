import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_type,
    BlockType,
    markdown_to_html,
    text_to_children,
    block_to_html,
    paragraph_to_html
)

test_md = """# This is a heading

This is a paragraph.\n It has **bold** and *italic* words.

* item
* item
* item

```
code block
```

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


class TestBlockTypes(unittest.TestCase):
    def test_block_types(self):
        h = "# heading 1"
        self.assertEqual(block_to_type(h), BlockType.HEADING)
        ul_star = "* item\n* item\n* item"
        self.assertEqual(block_to_type(ul_star), BlockType.UNORDERED_LIST)
        ul_dash = "- item\n- item\n- item"
        self.assertEqual(block_to_type(ul_dash), BlockType.UNORDERED_LIST)
        li = "1. item\n2. item\n3. item"
        self.assertEqual(block_to_type(li), BlockType.ORDERED_LIST)
        code = "```\ncode block\n```"
        self.assertEqual(block_to_type(code), BlockType.CODE)
        quote = "> word quotes\n> more quotes"
        self.assertEqual(block_to_type(quote), BlockType.QUOTE)
        p = "This is a paragraph.\nWith **words**."
        self.assertEqual(block_to_type(p), BlockType.PARAGRAPH)


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        h1 = "# This is a heading"
        p = "This is a paragraph.\n It has **bold** and *italic* words."
        li = "* item\n* item\n* item"
        code = "```\ncode block\n```"
        blocks = markdown_to_blocks(test_md)
        case = [h1, p, li, code]
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


p_md = """
This is **bold** paragraph text.
In a p tag.

"""
p_html = "<div><p>This is <b>bold</b> paragraph text. In a p tag.</p></div>"

h_md = """# Head 1

Text.

## Head 2

Text.

"""
h_html = "<div><h1>Head 1</h1><p>Text.</p><h2>Head 2</h2><p>Text.</p></div>"

c_md = """```
print('hello')
```
"""
c_html = "<div><pre><code>print('hello')</code></pre></div>"

q_md = """> quote
> block

paragraph
"""
q_html = "<div><blockquote>quote block</blockquote><p>paragraph</p></div>"

l_md = """
- list
- items

1. list
2. items
"""
l_html = "<div><ul><li>list</li><li>items</li></ul><ol><li>list</li><li>items</li></ol></div>"


class TestBlockToHTML(unittest.TestCase):
    def test_markdown_to_paragraph(self):
        node = markdown_to_html(p_md)
        html = node.to_html()
        self.assertEqual(html, p_html)

    def test_markdown_to_heading(self):
        node = markdown_to_html(h_md)
        html = node.to_html()
        self.assertEqual(html, h_html)

    def test_markdown_to_code(self):
        node = markdown_to_html(c_md)
        html = node.to_html()
        self.assertEqual(html, c_html)

    def test_markdown_to_quote(self):
        node = markdown_to_html(q_md)
        html = node.to_html()
        self.assertEqual(html, q_html)

    def test_markdown_to_list(self):
        node = markdown_to_html(l_md)
        html = node.to_html()
        self.assertEqual(html, l_html)
