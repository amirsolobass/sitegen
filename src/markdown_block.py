import re

from numpy import block
from blocktype import BlockType
from inline_markdown import text_to_textnodes
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_html import text_node_to_html_node


def markdown_to_blocks(markdown):
    if not markdown or markdown.strip() == "":
        return []
    split_lines = re.split(r'\n\s*\n', markdown.strip())
    blocks = []
    for line in split_lines:
        cleaned_line = line.strip()
        blocks.append(cleaned_line)
    # Remove empty blocks
    blocks = [block for block in blocks if block]
    return blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith("#"):
        if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
            return BlockType.HEADING
        else:
            return BlockType.PARAGRAPH
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">") or block.startswith("> "):
        for line in lines:
            if not line.startswith(">") and not line.startswith("> "):
                return BlockType.PARAGRAPH              
        return BlockType.QUOTE
    if block.startswith(("- ", "* ", "+ ")):
        for line in lines:
            if not line.startswith("- ") and not line.startswith("* ") and not line.startswith("+ "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def block_to_html_node(block):
    lines = block.split("\n")
    block_type = block_to_block_type(block)

    if block_type == BlockType.HEADING:
        level = len(re.match(r"^(#+)", lines[0]).group(1))
        content = lines[0][level+1:].strip()
        text_nodes = text_to_textnodes(content)
        html_children = [text_node_to_html_node(node) for node in text_nodes]
        return ParentNode(f"h{level}", html_children)

    elif block_type == BlockType.CODE:
        code_content = "\n".join(lines[1:-1])
        content = LeafNode("code", code_content)
        return ParentNode("pre", [content])

    elif block_type == BlockType.QUOTE:
        quote_lines = [line[1:].strip() for line in lines]
        quote_content = " ".join(quote_lines)
        text_nodes = text_to_textnodes(quote_content)
        html_children = [text_node_to_html_node(node) for node in text_nodes]
        return ParentNode("blockquote", html_children)

    elif block_type == BlockType.UNORDERED_LIST:
        list_items = []
        for line in lines:
            item_content = line[2:].strip()
            # Skip inline parsing if this line contains code block delimiters
            if "```" in item_content:
                html_children = [LeafNode("", item_content)]
            else:
                text_nodes = text_to_textnodes(item_content)
                html_children = [text_node_to_html_node(node) for node in text_nodes]
            list_items.append(ParentNode("li", html_children))
        return ParentNode("ul", list_items)

    elif block_type == BlockType.ORDERED_LIST:
        list_items = []
        for line in lines:
            item_content = re.sub(r"^\d+\. ", "", line).strip()
            # Skip inline parsing if this line contains code block delimiters
            if "```" in item_content:
                html_children = [LeafNode("", item_content)]
            else:
                text_nodes = text_to_textnodes(item_content)
                html_children = [text_node_to_html_node(node) for node in text_nodes]
            list_items.append(ParentNode("li", html_children))
        return ParentNode("ol", list_items)

    else:  # Paragraph
        paragraph_content = " ".join([line.strip() for line in lines])
        text_nodes = text_to_textnodes(paragraph_content)
        html_children = [text_node_to_html_node(node) for node in text_nodes]
        return ParentNode("p", html_children)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(block) for block in blocks]
    if len(children) == 1:
        return children[0]
    parent_node = ParentNode("div", children)
    return parent_node
    

    
    