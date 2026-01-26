import unittest
from extracttitle import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_valid(self):
        markdown = "# My Title\n\nSome content here."
        title = extract_title(markdown)
        self.assertEqual(title, "My Title")

    def test_extract_title_with_whitespace(self):
        markdown = "#    My Title with Spaces   \n\nSome content here."
        title = extract_title(markdown)
        self.assertEqual(title, "My Title with Spaces")

    def test_extract_titile_other_headings(self):
        markdown = "## Subtitle\n\nSome content here."
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_extract_title_more_headings(self):
        markdown = "### Another Subtitle\n\nSome content here."
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_extract_title_no_title(self):
        markdown = "Some content here without a title."
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_extract_title_empty(self):
        markdown = ""
        with self.assertRaises(ValueError):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()