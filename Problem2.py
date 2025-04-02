import os

def list_directory_contents(path=''):
    try:
        # List all files and directories in the specified path
        contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")

# Example usage
directory = input("Enter the directory path (or press Enter for current directory): ") or '.'
list_directory_contents(directory)
