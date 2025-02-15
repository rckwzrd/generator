import unittest

from textnode import TextNode, TextType, text_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is different", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("Text", TextType.LINKS, "https://")
        node2 = TextNode("Text", TextType.LINKS, "https://")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("Text", TextType.CODE)
        self.assertEqual("TextNode(Text, code, None)", repr(node))


class TestTextToHtmlNode(unittest.TestCase):
    def test_text_to_html_error(self):
        node = TextNode("Text that raises ValueError", text_type=None)
        with self.assertRaises(Exception):
            text_to_html_node(node)

    def test_text_to_html(self):
        text = TextNode("I am text", TextType.TEXT)
        html = text_to_html_node(text)
        self.assertEqual(html.tag, None)
        self.assertEqual(html.value, "I am text")

        code = TextNode("I am code", TextType.CODE)
        html = text_to_html_node(code)
        self.assertEqual(html.tag, "code")
        self.assertEqual(html.value, "I am code")

        link = TextNode("I am link", TextType.LINKS, "https://")
        html = text_to_html_node(link)
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.value, "I am link")
        self.assertEqual(html.props, {"href": "https://"})

        link = TextNode("I am image", TextType.IMAGES, "https://")
        html = text_to_html_node(link)
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")
        self.assertEqual(html.props, {"src": "https://", "alt": "I am image"})


if __name__ == "__main__":
    unittest.main()
