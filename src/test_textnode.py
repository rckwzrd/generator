import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is different", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("Text", TextType.CODE)
        self.assertEqual(node.url, None)

    def test_repr(self):
        node = TextNode("Text", TextType.CODE)
        self.assertEqual("TextNode(Text, code, None)", repr(node))


if __name__ == "__main__":
    unittest.main()
