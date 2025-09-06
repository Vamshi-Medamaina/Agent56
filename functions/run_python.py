import os
import subprocess
from google.genai import types


def run_python_file(working_directory,file_path,args=[]):
    try:
        full_path= os.path.join(working_directory,file_path)

        abs_file_path = os.path.abspath(full_path)

        if not abs_file_path.startswith(os.path.abspath(working_directory)):
            return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        
        if not os.path.exists(abs_file_path):
            return(f'Error: File "{file_path}" not found.')
        
        if not abs_file_path.endswith(".py"):
            print(abs_file_path)
            return(f'Error: "{file_path}" is not a Python file.')

        cmd=['python3',abs_file_path] + args

        completed_process= subprocess.run(args=cmd,cwd=working_directory,timeout=30,capture_output=True,text=True)

        if not completed_process.stdout and not completed_process.stderr:
            return("No output produced")

        str=''

        str=str+f'STDOUT:\n{completed_process.stdout}\nSTDERR:{completed_process.stderr}\n'

        if not completed_process.returncode == 0:
            str =str+f'Process exited with code {completed_process.returncode}"'

        return str
    
    except Exception as e:
        return(f"Error: executing Python file: {e}")




schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
