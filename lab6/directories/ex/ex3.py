import os

def check_path(path):
    if os.path.exists(path):
        print(f"{path} exists.")
        dirname, filename = os.path.split(path)
        print(f"Directory: {dirname}")
        print(f"Filename: {filename}")
    else:
        print(f"{path} does not exist.")

path = input("Enter a path: ")
check_path(path)
