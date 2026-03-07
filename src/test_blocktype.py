import unittest
from blocktype import block_to_block_type, BlockType

class TestBlocktype(unittest.TestCase):
    def test_block_to_blocktype_head(self):
        test = block_to_block_type("### This is a level 3 heading")
        self.assertEqual(test, BlockType.HEADING)
    def test_block_to_blocktype_code(self):
        input = """```
print('hello world')
```"""
        test = block_to_block_type(input)
        self.assertEqual(test, BlockType.CODE)
    def test_block_to_blocktype_quote(self):
        test = block_to_block_type(
"""> This is a quote
> This is a quote"""
        )
        self.assertEqual(test, BlockType.QUOTE)
    def test_block_to_blocktype_unordered(self):
        test = block_to_block_type(
"""- This is a quote
- This is a quote"""
        )
        self.assertEqual(test, BlockType.UNORDERED_LIST)
    def test_block_to_blocktype_quote(self):
        test = block_to_block_type(
"""1. This is a quote
2. This is a quote
3. something else"""
        )
        self.assertEqual(test, BlockType.ORDERED_LIST)