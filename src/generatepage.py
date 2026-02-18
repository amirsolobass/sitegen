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
    final_html = temp.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    # replace BasePath placeholder first (permanent basepath support)
    final_html = final_html.replace("{{ BasePath }}", basepath)
    # replace legacy absolute href/src paths that start with "/" to use basepath
    # but avoid double-prefixing links that already include the basepath or point to `docs/`.
    try:
        import re
        # when basepath is '/', no change required
        if basepath != "/":
            # strip leading slash for lookahead pattern
            bp = basepath.lstrip('/')
            # pattern: match href="/ not followed by basepath or docs/
            href_pattern = r'href="/(?!' + re.escape(bp) + r'|docs/)'
            src_pattern = r'src="/(?!' + re.escape(bp) + r'|docs/)'
            final_html = re.sub(href_pattern, 'href="' + basepath, final_html)
            final_html = re.sub(src_pattern, 'src="' + basepath, final_html)
        else:
            # basepath is root, no changes necessary for absolute paths
            pass
    except Exception:
        # fallback to simple replace if regex fails for any reason
        final_html = final_html.replace('href="/', 'href="' + basepath)
        final_html = final_html.replace('src="/', 'src="' + basepath)
    # Normalize any accidental /docs/ prefixes in links (some markdown had /docs/ references)
    final_html = final_html.replace('href="/docs/', 'href="' + basepath)
    final_html = final_html.replace('src="/docs/', 'src="' + basepath)
    final_html = final_html.replace('href="' + basepath + 'docs/', 'href="' + basepath)
    final_html = final_html.replace('src="' + basepath + 'docs/', 'src="' + basepath)

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
                generate_page(from_path, template_path, dest_path, basepath)