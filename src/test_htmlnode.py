import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "This is a test", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        with self.subTest():
            self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
        with self.subTest():
            self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        with self.subTest():
            node = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

        with self.subTest():
            node2 = ParentNode(
                "p",
                [
                    ParentNode(
                                "a",
                                [
                                    LeafNode("b", "Bold text"),
                                    LeafNode(None, "Normal text"),
                                    LeafNode("i", "italic text"),
                                    LeafNode(None, "Normal text"),
                                ],
                    ),
                ],
            )
            self.assertEqual(node2.to_html(), '<p><a><b>Bold text</b>Normal text<i>italic text</i>Normal text</a></p>')

        with self.subTest():
            node = ParentNode(
                "h2",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            self.assertEqual(
                node.to_html(),
                "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
            )
        
        with self.subTest():
            child_node = LeafNode("span", "child")
            parent_node = ParentNode("div", [child_node])
            self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

if __name__ == "__main__":
    unittest.main()