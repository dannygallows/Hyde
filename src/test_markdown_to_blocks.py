import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty(self):
        md = "          "
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

        md_none = ""
        blocks_none = markdown_to_blocks(md_none)
        self.assertEqual(blocks_none, [])

    def test_markdown_to_blocks_whitespace(self):
        md = """
# This is a heading


This is a paragraph with trailing spaces.          

* This is a list
* item 2


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph with trailing spaces.",
                "* This is a list\n* item 2",
            ],
    )