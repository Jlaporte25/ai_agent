import os

def write_file(working_dir, file_path, content):
    abs_working_dir = os.path.abspath(working_dir)
    if os.path.exists(abs_working_dir):
        pass

import os

def write_file(working_directory, file_path, content):
    """
    Writes content to a file within a permitted working directory.

    Args:
        working_directory: The allowed base directory.
        file_path: The path to the file to write to (relative or absolute).
        content: The string content to write to the file.

    Returns:
        A string indicating success or failure, with an error message if the write fails.
    """

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path)) #Join and then absolutize.  Crucial to security checks.


    if not abs_file_path.startswith(abs_working_dir + os.sep): #Security check!  OS.sep handles windows vs linux
        return f'Error: Cannot write to {file_path} as it is outside the permitted working directory'

    try:
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)  # Ensure directory exists
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return f'Successfully wrote to {file_path} ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {str(e)}'

