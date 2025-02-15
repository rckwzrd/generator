import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode 


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
        case = ' href="https://www" target="_blank" thing="some"'
        props = {"href": "https://www", "target": "_blank", "thing": "some"}
        html = HtmlNode(props=props)
        test_props = html.props_to_html()
        self.assertEqual(case, test_props)

    def test_repr(self):
        case = "HtmlNode(p, text, None, {'class': 'primary'})"
        html = HtmlNode(tag="p", value="text", props={"class": "primary"})
        self.assertEqual(case, repr(html))


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf = LeafNode(tag="a", value="Click me!", props={"href": "https://"})
        case = '<a href="https://">Click me!</a>'
        self.assertEqual(case, leaf.to_html())

    def test_no_value(self):
        leaf = LeafNode(tag="a", value=None, props={"href": "https:/"})
        with self.assertRaises(ValueError):
            leaf.to_html()

    def test_no_tag(self):
        leaf = LeafNode(value="raw text")
        case = "raw text"
        self.assertEqual(case, leaf.to_html())

    def test_repr(self):
        leaf = LeafNode(tag="a", value="Click me!", props={"href": "https://"})
        case = "LeafNode(a, Click me!, {'href': 'https://'})"
        self.assertEqual(case, repr(leaf))


class TestParentNode(unittest.TestCase):
    def test_children_html(self):
        child = LeafNode(tag="div", value="child")
        parent = ParentNode(tag="span", children=[child])
        case = "<span><div>child</div></span>"
        self.assertEqual(case, parent.to_html())

    def test_empty_children_html(self):
        parent = ParentNode(tag="span", children=[])
        case = "<span></span>"
        self.assertEqual(case, parent.to_html())

    def test_grandchildren_html(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("div", [grandchild])
        parent = ParentNode("span", [child])
        case = "<span><div><b>grandchild</b></div></span>"
        self.assertEqual(case, parent.to_html())

    def test_many_children_html(self):
        children = [
            LeafNode("b", "bold"),
            LeafNode(None, "normal"),
            LeafNode("i", "italic"),
            LeafNode(None, "normal")
        ]
        parent = ParentNode("p", children)
        case = "<p><b>bold</b>normal<i>italic</i>normal</p>"
        self.assertEqual(case, parent.to_html())

    def test_value_error(self):
        parent_no_children = ParentNode("p", children=None)
        parent_no_tag = ParentNode(tag=None, children=[])
        with self.assertRaises(ValueError):
            parent_no_children.to_html()
        with self.assertRaises(ValueError):
            parent_no_tag.to_html()

    def test_repr(self):
        children = [LeafNode("b", "bold")]
        props = {"class": "primary"}
        parent = ParentNode("p", children=children, props=props)
        case = "ParentNode(p, [LeafNode(b, bold, None)], {'class': 'primary'})"
        self.assertEqual(case, repr(parent))
