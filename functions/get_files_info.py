import os 

def get_files_info(working_directory, directory="."):
    # First checking working directory 
    working_directory_absolute_path = os.path.abspath(working_directory)
    print(f"working_directory_absolute_path: {working_directory_absolute_path}")

    # check the inputted directory 
    directory_absolute_path = os.path.join(working_directory_absolute_path, directory)
    print(f"directory_absolute_path: {directory_absolute_path}")

    #handle directory absolute path when "../" inputs are provided. 
    directory_abs_path = os.path.abspath(directory_absolute_path)
    print(f"directory_abs_path: {directory_abs_path}")
    
    if not directory_abs_path.startswith(working_directory_absolute_path):
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
            if file == "__pycache__":
                continue 
            print(f"file: {file}")
            file_size = os.path.getsize(os.path.join(directory_absolute_path,file))
            is_dir = os.path.isdir(os.path.join(directory_absolute_path,file))
            file_name = file
            response += f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}\n"

        return response 
    except Exception as e:
        return f"ERROR: {e}"