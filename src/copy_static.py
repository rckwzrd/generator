import os
import shutil


def copy_files_recursive(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    for name in os.listdir(source_dir):
        source = os.path.join(source_dir, name)
        target = os.path.join(target_dir, name)
        if os.path.isfile(source):
            shutil.copy(source, target)
        else:
            copy_files_recursive(source, target)
