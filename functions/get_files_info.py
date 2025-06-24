import os
from os.path import isdir, isfile

def get_files_info(working_directory, directory=None):
    path = os.path.abspath(directory)
    if directory not in working_directory:
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if os.path.isdir(path):
        raise Exception(f'Error: "{directory}" is not a directory')
    dir_contents = os.listdir(path)
    final_str = []
    for content in dir_contents:
        if os.path.isfile(content):
            file_size = os.path.getsize(content)
            file_str = f"- {content}: file_size={file_size} bytes, is_dir=False"
            final_str.append(file_str)
        elif os.path.isdir(content):
            dir_size = os.path.getsize(content)
            dir_str = f"- {content}: file_size={dir_size} bytes, is_dir=True"
            new_path = os.path.abspath(content)
            get_files_info(content, new_path)
    joined_str = final_str.join("\n")
    return joined_str

