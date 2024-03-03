def copy_file(source_file, dest_file):
    with open(source_file, 'r') as f1:
        with open(dest_file, 'w') as f2:
            f2.write(f1.read())
            print(f"Contents of {source_file} have been copied to {dest_file} successfully.")

source_file = input("Enter the source file name: ")
dest_file = input("Enter the destination file name: ")
copy_file(source_file, dest_file)