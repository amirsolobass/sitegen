import os
import shutil

def copy_from_dir(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory '{src_dir}' does not exist.")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.makedirs(dest_dir)
    for filename in os.listdir(src_dir):
        src_file = os.path.join(src_dir, filename)
        dest_file = os.path.join(dest_dir, filename)
        if os.path.isdir(src_file): # if directory
            # ensure destination directory exists
            if not os.path.exists(dest_file):
                os.makedirs(dest_file)
            # recursively copy directories
            copy_from_dir(src_file, dest_file)
        else: # if file
            # ensure parent directory exists
            parent_dir = os.path.dirname(dest_file)
            if not os.path.exists(parent_dir):
                os.makedirs(parent_dir)
            shutil.copy(src_file, dest_file)

        