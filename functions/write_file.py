import os

def write_file(working_dir, file_path, content):
    abs_working_dir = os.path.abspath(working_dir)
    target_file = os.path.abspath(os.path.join(working_dir, file_path))
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
