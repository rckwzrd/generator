from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_nodes
from textnode import text_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def block_to_type(block):
    lines = block.split("\n")
    if block.startswith(("#", "##", "###", "####", "#####", "######")):
        return BlockType.HEADING
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    return [block.strip() for block in markdown.split("\n\n") if block != ""]


def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html(block))
    return ParentNode("div", children, None)


def block_to_html(block):
    block_type = block_to_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html(block)
    if block_type == BlockType.HEADING:
        return heading_to_html(block)
    if block_type == BlockType.CODE:
        return code_to_html(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html(block)
    if block_type == BlockType.UNORDERED_LIST:
        return ul_to_html(block)
    if block_type == BlockType.ORDERED_LIST:
        return ol_to_html(block)
    raise ValueError("invalid block type")


def text_to_children(text):
    text_nodes = text_to_nodes(text)  # turn text into nodes
    children = []
    for node in text_nodes:
        html_node = text_to_html_node(node)  # turn nodes to html
        children.append(html_node)
    return children


def paragraph_to_html(block):
    paragraph = " ".join(block.split("\n"))
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    children = text_to_children(block[level+1:])
    return ParentNode(f"h{level}", children)


def code_to_html(block):
    if not block.startswith("```") and not block.endswidth("```"):
        raise ValueError("invalid code block")
    children = text_to_children(block[4:-4])
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def quote_to_html(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    children = text_to_children(" ".join(new_lines))
    return ParentNode("blockquote", children)


def ul_to_html(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def ol_to_html(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)
