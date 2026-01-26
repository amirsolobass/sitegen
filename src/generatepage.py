from markdown_block import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from extracttitle import extract_title
import os



def generate_page(from_path, template_path, dest_path, basepath="/"):
    if not os.path.exists(from_path):
        raise FileNotFoundError(f"Source markdown file '{from_path}' does not exist.")
    if not os.path.isfile(from_path):
        raise ValueError(f"Source path '{from_path}' is not a file.")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file '{template_path}' does not exist.")
    if not os.path.exists(dest_path):
        # ensure parent directory exists
        parent_dir = os.path.dirname(dest_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Read the markdown content
    content = open(from_path).read()
    temp = open(template_path).read()
    # convert to html string
    html_content = markdown_to_html_node(content).to_html()
    # extract title
    title = extract_title(content)
    # replace {{content}} and {{title}} in template
    final_html = temp.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    # replace href and src paths to be relative
    final_html = final_html.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    # write to dest_path

    open(dest_path, "w").write(final_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    root = os.path.abspath(dir_path_content)
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith(".md"):
                from_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(from_path, root)
                dest_path = os.path.join(dest_dir_path, relative_path[:-3] + ".html")  # change .md to .html
                generate_page(from_path, template_path, dest_path)
    print("ROOT:", root)
    for dirpath, dirnames, filenames in os.walk(root):
        print("DIR:", dirpath)
        for filename in filenames:
            print("FILE:", filename)