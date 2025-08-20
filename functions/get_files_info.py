import os 

def get_files_info(working_directory, directory="."):
    
    working_directory_absolute_path = os.path.abspath(working_directory)
    print(f"working_directory_absolute_path: {working_directory_absolute_path}")

    directory_absolute_path = os.path.join(working_directory_absolute_path,directory)
    print(f"directory_absolute_path: {directory_absolute_path}")
    
    if not directory_absolute_path.startswith(working_directory_absolute_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory_absolute_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        response = ""
        if directory == ".":
            response += "Result for current directory:\n"
        else:
            response += f"Result for '{directory}' directory:\n"
        files = os.listdir(directory_absolute_path)

        for file in files:
            print(f"file: {file}")
            file_size = os.path.getsize(os.path.join(directory_absolute_path,file))
            is_dir = os.path.isdir(os.path.join(directory_absolute_path,file))
            file_name = file
            response += f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}\n"

        return response 
    except Exception as e:
        return f"ERROR: {e}"