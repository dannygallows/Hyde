from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from textnode_tohtml_convertor import text_node_to_html_node
from textnode import TextNode, TextType
from parentnode import ParentNode
from text_to_textnodes import text_to_textnodes


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    child_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        htmlnode = block_to_htmlnode(block, block_type)
        child_nodes.append(htmlnode)
    return ParentNode("div", child_nodes)


def block_to_htmlnode(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        lines = block.split('\n')
        text = " ".join(lines)
        return ParentNode("p", text_to_children(text))
    if block_type == BlockType.HEADING:
        hashes, value = block.split(" ", 1)
        return ParentNode(f"h{len(hashes)}", text_to_children(value))
    if block_type == BlockType.CODE:
        child_node = text_node_to_html_node(TextNode(block[4:-3], TextType.CODE))
        return ParentNode("pre", [child_node])
    if block_type == BlockType.QUOTE:
        lines = block.split('\n')
        cleaned_lines = "\n".join([line.lstrip("> ").strip() for line in lines])
        return ParentNode("blockquote", text_to_children(cleaned_lines))
    if block_type == BlockType.UNORDERED_LIST:
        children_list = []
        lines = block.split('\n')
        for line in lines:
            text = line[2:]
            children_list.append(ParentNode("li", text_to_children(text)))
        return ParentNode("ul", children_list)
    if block_type == BlockType.ORDERED_LIST:
        children_list = []
        lines = block.split('\n')
        for line in lines:
            parts = line.split(". ", 1)
            text = parts[1]
            children_list.append(ParentNode("li", text_to_children(text)))
        return ParentNode("ol", children_list)


def text_to_children(text):
    children = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        children.append(text_node_to_html_node(textnode))
    return children
