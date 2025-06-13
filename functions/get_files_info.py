import os
from os.path import isdir

def get_files_info(working_directory, directory=None):
    path = os.path.abspath(directory)
    if directory not in working_directory:
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if os.path.isdir(path):
        raise Exception(f'Error: "{directory}" is not a directory')
