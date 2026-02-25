import unittest

from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code(self):
        test_input = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, test_input)

    def test_bold(self):
        test_input = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, test_input)

    def test_italic(self):
        test_input = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, test_input)

    def test_multiple_inlines(self):
        test_input = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("some more code", TextType.CODE),
        ]
        node = TextNode("This is text with `code` and `some more code`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, test_input)

    def test_multiple_old_nodes(self):
        test_input = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        node_other = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node_other], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, test_input)
