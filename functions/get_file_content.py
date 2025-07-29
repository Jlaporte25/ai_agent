import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    if file_path:
        target_dir = os.path.abspath(os.path.join(working_directory, file_path))
        if not target_dir.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path):
            return f'Error: File is not found or is not a regular file: "{file_path}"'

    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)

