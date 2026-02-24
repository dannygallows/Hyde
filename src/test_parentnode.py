import unittest

from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_no_children(self):
        parent_node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><span>child</span></div>")

    def test_to_html_no_nested_children(self):
        parent_node = ParentNode("div", [])
        parent_node_other = ParentNode("div", [parent_node])
        with self.assertRaises(ValueError):
            parent_node_other.to_html()

    def test_div_soup(self):
        node = LeafNode("b", "div")
        
        for _ in range(500):
            node = ParentNode("div", [node])

        html = node.to_html()

        self.assertTrue(html.startswith("<div>" * 500))
        self.assertTrue(html.endswith("</div>" * 500))

if __name__ == "__main__":
    unittest.main()
