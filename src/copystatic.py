import shutil
import os

def copy_files_recursive(source_dir_path, dest_dir_path):
    """
     shutil.copytree can be used instead of this function
    """
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    for fname in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, fname)
        dest_path = os.path.join(dest_dir_path, fname)
        print(f"* {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)
