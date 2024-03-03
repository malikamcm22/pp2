import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.R_OK | os.W_OK):
            os.remove(path)
            print(f"{path} has been deleted successfully.")
        else:
            print(f"You don't have permission to delete {path}.")
    else:
        print(f"{path} does not exist.")

path = input("Enter the path of the file to be deleted: ")
delete_file(path)