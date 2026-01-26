from markdown_block import markdown_to_blocks, block_to_block_type, markdown_to_html_node
from blocktype import BlockType
import unittest



class TestBlockMarkdown(unittest.TestCase):
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
            md = """
            
            
                """
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])


    def test_markdown_to_blocks_single_line(self):
            md = "This is a single line markdown without any paragraphs."
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, ["This is a single line markdown without any paragraphs."])

    def test_markdown_to_blocks_multiple_newlines(self):
            md = """
This is the first paragraph.


This is the second paragraph after multiple newlines.


This is the third paragraph.
                """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is the first paragraph.",
                    "This is the second paragraph after multiple newlines.",
                    "This is the third paragraph.",
                ],
            )

    def test_markdown_to_blocks_leading_trailing_whitespace(self):
            md = """
                
This is a paragraph with leading and trailing whitespace.    
                
                """
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, ["This is a paragraph with leading and trailing whitespace."])

    def test_markdown_to_blocks_all_text_types(self):
            md = """
This is a **bold** text, this is _italic_ text, and this is `code`.

Here is a link: [Boot.dev](https://www.boot.dev) and an image: ![Alt text](https://example.com/image.png)
                """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is a **bold** text, this is _italic_ text, and this is `code`.",
                    "Here is a link: [Boot.dev](https://www.boot.dev) and an image: ![Alt text](https://example.com/image.png)",
                ],
            )



class TestBlockTypeDetection(unittest.TestCase):
    def test_block_to_block_type(self):
            self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
            self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.CODE)
            self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
            self.assertEqual(block_to_block_type("- List item"), BlockType.UNORDERED_LIST)
            self.assertEqual(block_to_block_type("1. Ordered item"), BlockType.ORDERED_LIST)
            self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

    def test_block_to_block_type_edge_cases(self):
            self.assertEqual(block_to_block_type("## Subheading"), BlockType.HEADING)
            self.assertEqual(block_to_block_type("```\nprint('Hello, World!')\n```"), BlockType.CODE)
            self.assertEqual(block_to_block_type("> Another quote example"), BlockType.QUOTE)
            self.assertEqual(block_to_block_type("- Another list item"), BlockType.UNORDERED_LIST)
            self.assertEqual(block_to_block_type("Just some regular text."), BlockType.PARAGRAPH)

    def test_block_to_block_type_empty_and_whitespace(self):
            self.assertEqual(block_to_block_type("   "), BlockType.PARAGRAPH)
            self.assertEqual(block_to_block_type(""), BlockType.PARAGRAPH)


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_markdown_to_html_node_heading(self):
            md = "# Heading 1"
            html_node = markdown_to_html_node(md)
            self.assertEqual(html_node.tag, "h1")
            self.assertEqual(len(html_node.children), 1)
            self.assertEqual(html_node.children[0].value, "Heading 1")

    def test_markdown_to_html_node_all_other_headings(self):
            for level in range(2, 7):
                md = "#" * level + f" Heading {level}"
                html_node = markdown_to_html_node(md)
                self.assertEqual(html_node.tag, f"h{level}")
                self.assertEqual(len(html_node.children), 1)
                self.assertEqual(html_node.children[0].value, f"Heading {level}")

    def test_markdown_to_html_node_code_block(self):
            md = "```\nprint('Hello, World!')\n```"
            html_node = markdown_to_html_node(md)
            self.assertEqual(html_node.tag, "pre")
            self.assertEqual(html_node.children[0].value, "print('Hello, World!')")

    def test_markdown_to_html_node_paragraph(self):
            md = "This is a **bold** text."
            html_node = markdown_to_html_node(md)
            self.assertEqual(html_node.tag, "p")
            self.assertEqual(len(html_node.children), 3)
            self.assertEqual(html_node.children[0].value, "This is a ")
            self.assertEqual(html_node.children[1].tag, "b")
            self.assertEqual(html_node.children[1].value, "bold")
            self.assertEqual(html_node.children[2].value, " text.")



if __name__ == "__main__":
    unittest.main()