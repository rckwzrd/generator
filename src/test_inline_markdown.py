import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_images, extract_links


class TestInlineMarkdown(unittest.TestCase):
    def test_invalid_delim(self):
        node = TextNode("This is **BOLD text", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_delim_bold(self):
        node = TextNode("This is **BOLD** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("BOLD", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_multi_bold(self):
        node = TextNode("This is **BOLD BOLD BOLD** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("BOLD BOLD BOLD", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            new_nodes,
        )


    def test_delim_many_bold(self):
        node = TextNode("This is **BOLD** and **BOLD** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("BOLD", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("BOLD", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is `CODE` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("CODE", TextType.CODE),
                TextNode(" text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_italic(self):
        node = TextNode("This is **BOLD** and *ITALIC* text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("BOLD", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("ITALIC", TextType.ITALIC),
                TextNode(" text", TextType.TEXT)
            ],
            new_nodes,
        )


class TestExtractText(unittest.TestCase):
    def test_extract_images(self):
        text = "Text with ![rick roll](link/) and ![obi wan](link/)"
        images = extract_images(text)
        case = [("rick roll", "link/"), ("obi wan", "link/")]
        self.assertListEqual(images, case)

    def test_no_images(self):
        text = "text images for rick roll and obi wan"
        images = extract_images(text)
        case = []
        self.assertListEqual(images, case)

    def test_extract_links(self):
        text = "text links for [boot dev](https://) and [youtube](https://)"
        links = extract_links(text)
        case = [("boot dev", "https://"), ("youtube", "https://")]
        self.assertListEqual(links, case)

    def test_no_links(self):
        text = "text links for boot dev and youtube"
        links = extract_links(text)
        case = []
        self.assertListEqual(links, case)
