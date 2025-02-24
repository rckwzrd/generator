import os

from pathlib import Path
from block_markdown import markdown_to_html


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("#"):
            return line[2:]
    raise ValueError("No title found")


def generate_page(source_path, template_path, target_html):
    print(f"* {source_path} {template_path} -> {target_html}")
    source_file = open(source_path, "r")
    markdown = source_file.read()
    source_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    html = markdown_to_html(markdown).to_html()

    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # get dirs for html file
    target_dir = os.path.dirname(target_html)
    # if target_dir is just html file makedir will FileNotFoundError
    if target_dir != "":
        # make dirs for html if they don't exist
        os.makedirs(target_dir, exist_ok=True)
    to_file = open(target_html, "w")
    to_file.write(template)
    to_file.close()


def generate_page_recursive(source, template, target):
    for name in os.listdir(source):
        print("in listdir loop", name)
        source_path = os.path.join(source, name)
        target_path = os.path.join(target, name)
        if os.path.isfile(source_path):
            print("is md file, generating html")
            target_html = Path(target_path).with_suffix(".html")
            generate_page(source_path, template, target_html)
        else:
            print("is dir, calling again")
            generate_page_recursive(source_path, template, target_path)
