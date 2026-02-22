import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        test_dictionary = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("p", "This is a text node", props=test_dictionary)
        node2 = HTMLNode("p", "This is a text node", props=test_dictionary)
        self.assertEqual(node, node2)
    
    def test_neq_tag(self):
        node = HTMLNode("a","This is a text node")
        node2 = HTMLNode("h1","This is a text node")
        self.assertNotEqual(node, node2)

    def test_neq_props(self):
        test_dictionary = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        test_dictionary2 = {
            "href": "https://www.google.com",
            "target": "_dank",
        }
        node = HTMLNode("h1","This is a text node", props=test_dictionary)
        node2 = HTMLNode("h1","This is a text node", props=test_dictionary2)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
