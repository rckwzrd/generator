import re
from textnode import TextNode, TextType


def split_nodes_link(old_nodes):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue
        links = extract_links(old.text)
        if len(links) == 0:
            new_nodes.append(TextNode(old.text, TextType.TEXT))
            continue
        original_text = old.text
        for link in links:
            delim = f"[{link[0]}]({link[1]})"
            split = original_text.split(f"{delim}", 1)
            if len(split) != 2:
                raise ValueError("invalid markdown, link not closed")
            if split != "":
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(f"{link[0]}", TextType.LINKS, link[1]))
            original_text = split[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old in old_nodes:
        if old.text_type != TextType.TEXT:
            new_nodes.append(old)
            continue
        images = extract_images(old.text)
        if len(images) == 0:
            new_nodes.append(TextNode(old.text, TextType.TEXT))
            continue
        original_text = old.text
        for image in images:
            delim = f"![{image[0]}]({image[1]})"
            split = original_text.split(f"{delim}", 1)
            if len(split) != 2:
                raise ValueError("invalid markdown, image not closed")
            if split != "":
                new_nodes.append(TextNode(split[0], TextType.TEXT))
            new_nodes.append(TextNode(f"{image[0]}", TextType.IMAGES, image[1]))
            original_text = split[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


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
