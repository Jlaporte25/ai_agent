import os, subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed_process = subprocess.run(cwd=abs_working_dir, args=["python", file_path] + args, timeout=30, capture_output=True, text=True)
        if len(completed_process.stdout) == 0 and len(completed_process.stderr) == 0:
            return "No output produced"
        if not completed_process.returncode == 0:
            return f'STDOUT: {completed_process.stdout}\n STDERR: {completed_process.stderr}\n Process exited with code {completed_process.returncode}'
        return f'STDOUT: {completed_process.stdout}\n STDERR: {completed_process.stderr}\n'
    except Exception as e:
        return f"Error: executing Python file: {e}"
