import os
from block_markdown import markdown_to_html_node
from pathlib import Path

def extract_title(markdown):
    """
    Grab the text of the h1 header from the markdown file (The line that starts with a single #) and return it. 
    If there is no h1 header, raise an exception. All pages need a single h1 header.
    """
    headers = []
    with open(markdown, 'r') as f:
        for line in f:
            if line.startswith("# "):
              headers.append(line)
    if len(headers) > 1:
        raise Exception(f"Multiple headers are found in the markdown file {markdown}")
    elif not headers:
        raise Exception(f"No header detected in {markdown}")
    elif len(headers) == 1:
        return headers[0].lstrip("# ")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown_content = f.read()
    with open(template_path, "r") as f:
        template_content = f.read()
    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(from_path)
    full_html_page = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    dest_dir_path = os.path.dirname(dest_path)
    os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path := dest_path.split(".")[0]+ ".html", "w") as f:
        f.write(full_html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    for fname in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, fname)
        dest_path = os.path.join(dest_dir_path, fname)
        print(f"* {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            path = Path(from_path)
            if path.suffix != ".md":
                print(f"{path} is not a markdown file")
            elif path.suffix == ".md":
                generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)
