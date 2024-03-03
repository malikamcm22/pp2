def count_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        num_lines = len(lines)
        print(f"The number of lines in {file_name} is: {num_lines}")

file_name = input("Enter the file name: ")
count_lines(file_name)
