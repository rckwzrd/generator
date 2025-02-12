import unittest

from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_values(self):
        props = {"primary": "value"}
        html = HtmlNode(tag="p", value="text", children="child", props=props)
        self.assertEqual(html.tag, "p")
        self.assertEqual(html.value, "text")
        self.assertEqual(html.children, "child")
        self.assertEqual(html.props, props)

    def test_props_to_html(self):
        case = ' href="https://www.google.com" target="_blank"'
        props = {"href": "https://www.google.com", "target": "_blank"}
        html = HtmlNode(props=props)
        test_props = html.props_to_html()
        self.assertEqual(case, test_props)

    def test_no_props_to_html(self):
        case = ""
        html = HtmlNode()
        test_props = html.props_to_html()
        self.assertEqual(case, test_props)

    def test_many_props_to_html(self):
        case = ' href="https://www.google.com" target="_blank" thing="something"'
        props = {"href": "https://www.google.com", "target": "_blank", "thing": "something"}
        html = HtmlNode(props=props)
        test_props = html.props_to_html()
        self.assertEqual(case, test_props)

    def test_repr(self):
        case = "HtmlNode(p, text, None, {'class': 'primary'})"
        html = HtmlNode(tag="p", value="text", props={"class": "primary"})
        self.assertEqual(case, repr(html))
