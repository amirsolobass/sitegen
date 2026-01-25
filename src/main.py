from textnode import TextNode, TextType
from htmlnode import LeafNode
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
import re

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise ValueError("Link TextNode must have a URL")
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise ValueError("Image TextNode must have a URL")
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Unsupported TextType: {text_node.text_type}")
    




def main():
    node = TextNode("Hello, World!", TextType.TEXT, None)
    print("Created TextNode:")
    print(node)

    html_node = text_node_to_html_node(node)
    print("Converted to HTMLNode:")
    print(html_node)

    
main()