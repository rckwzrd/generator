import os
import shutil

from copy_static import copy_files_recursive

static_path = "./static"
public_path = "./public"


def main():
    print("deleting ./public")
    if os.path.exists(public_path):
        shutil.rmtree(public_path)

    print("copying ./static to ./public")
    copy_files_recursive(static_path, public_path)


if __name__ == "__main__":
    main()
