import re
from textnode import TextNode, TextType


def extract_images(text):
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches


def extract_links(text):
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue
        split_nodes = []
        split = old.text.split(delimiter)
        if len(split) % 2 == 0:
            raise ValueError("Invalid markdown: delimiter not closed")
        for i in range(len(split)):
            if split[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(split[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
