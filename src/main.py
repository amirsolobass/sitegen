from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from copystatic import copy_from_dir
from generatepage import generate_pages_recursive
import sys


def main():
    basepath = "/"
    if sys.argv and len(sys.argv) > 1:
        basepath = sys.argv[1]




    copy_from_dir("static", "docs")
    print("Copied static files from 'static' to 'docs' directory.")
    print(f"Basepath for links set to: {basepath}")
    generate_pages_recursive("content", "template.html", "docs", basepath)
    print("Generated pages recursively from 'content' using 'template.html'.")
    

if __name__ == "__main__":
    main()