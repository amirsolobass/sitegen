from inline_markdown import extract_markdown_images, extract_markdown_links
import unittest

class TestExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.boot.dev) inside"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_extract_multiple_markdown_links_and_images(self):
        text = """
        Here is an ![image1](https://example.com/image1.png) and a [link1](https://example.com/link1).
        Also, check out this ![image2](https://example.com/image2.png) and [link2](https://example.com/link2).
        """
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)

        self.assertListEqual(
            [
                ("image1", "https://example.com/image1.png"),
                ("image2", "https://example.com/image2.png"),
            ],
            image_matches,
        )

        self.assertListEqual(
            [
                ("link1", "https://example.com/link1"),
                ("link2", "https://example.com/link2"),
            ],
            link_matches,
        )

    def test_no_matches(self):
        text = "This is a simple text without any markdown images or links."
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)

        self.assertListEqual([], image_matches)
        self.assertListEqual([], link_matches)



if __name__ == "__main__":
    unittest.main()