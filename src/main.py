from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link
from copystatic import copy_from_dir
from generatepage import generate_pages_recursive


    



def main():
    copy_from_dir("static", "public")
    print("Copied static files from 'static' to 'public' directory.")
    generate_pages_recursive("content", "template.html", "public")
    print("Generated pages recursively from 'content' using 'template.html'.")
    

if __name__ == "__main__":
    main()