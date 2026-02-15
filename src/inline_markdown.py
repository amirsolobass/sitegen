from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not delimiter:
        return old_nodes
    new_nodes = []
    if not old_nodes:
        return []
    
    if delimiter == "":
        new_nodes.extend(old_nodes)
        return new_nodes
    count = 0
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        # how many times does `delimiter` appear in this node?
        delimiter_count = node.text.count(delimiter)
        if delimiter_count % 2 != 0:
            # For backticks and underscores, if unmatched, just skip processing and return as-is
            # This handles cases where they're part of code block markers or filenames
            if delimiter in ["`", "_"]:
                new_nodes.append(node)
                continue
            else:
                raise ValueError(f"Unmatched delimiter '{delimiter}' in text node: {node.text}")
        # Split the text by the delimiter
        parts = node.text.split(delimiter)
        for i, part in enumerate(parts):
            if not part:
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def split_nodes_image(old_node):
    if not old_node:
        return [old_node]
    new_nodes = []
    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text is None or node.text == "":
            continue
        matches = extract_markdown_images(node.text)
        if not matches: 
            new_nodes.append(node) 
            continue
        last_index = 0
        for alt_text, url in matches: 
            start_index = node.text.find(f"![{alt_text}]({url})", last_index) 
            if start_index > last_index: 
                new_nodes.append(TextNode(node.text[last_index:start_index], TextType.TEXT)) 
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, href=url)) 
            last_index = start_index + len(f"![{alt_text}]({url})") 
        if last_index < len(node.text): 
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))
    return new_nodes

def split_nodes_link(old_node):
    if not old_node:
        return [old_node]
    new_nodes = []
    for node in old_node:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if node.text is None or node.text == "":
            continue
        matches = extract_markdown_links(node.text)
        if not matches: 
            new_nodes.append(node) 
            continue
        last_index = 0
        for link_text, url in matches: 
            start_index = node.text.find(f"[{link_text}]({url})", last_index) 
            if start_index > last_index: 
                new_nodes.append(TextNode(node.text[last_index:start_index], TextType.TEXT)) 
            new_nodes.append(TextNode(link_text, TextType.LINK, href=url)) 
            last_index = start_index + len(f"[{link_text}]({url})") 
        if last_index < len(node.text): 
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches



def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
