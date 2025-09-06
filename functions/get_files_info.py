import os
from google.genai import types;

def get_files_info(working_directory,directory='.'):

    try:
        full_path = os.path.join(working_directory,directory)

        abs_directory = os.path.abspath(full_path)


        if not abs_directory.startswith(os.path.abspath(working_directory)):
            return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        
        if not os.path.isdir(abs_directory):
            return(f'Error: "{directory}" is not a directory')
        

        ans=''
        for item in os.listdir(abs_directory):
            full_item= os.path.join(abs_directory,item)
            item_size = os.path.getsize(full_item)
            is_dir = os.path.isdir(full_item)
            ans = ans + f'- {item}: file_size={item_size} bytes, is_dir={is_dir} \n'

        return ans
    except Exception as e:
        return(f'Error: {e}')
    

schema_get_files_info = types.FunctionDeclaration(
name="get_files_info",
description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
        "directory": types.Schema(
            type=types.Type.STRING,
            description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
        ),
    },
),
)
