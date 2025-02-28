import os
import shutil
import sys

from copy_static import copy_files_recursive
from generate_content import generate_page_recursive

static_path = "./static"
public_path = "./docs"
content_path = "./content"
template = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("deleting ./public")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print("copying ./static to ./public")
    copy_files_recursive(static_path, public_path)

    print("generating page")
    print(content_path, template, public_path)
    generate_page_recursive(content_path, template, public_path, basepath)


if __name__ == "__main__":
    main()
