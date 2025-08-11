import os

def run_python_file(working_directoy, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directoy)
    abs_file_path = os.path.abspath(os.path.join(working_directoy, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
