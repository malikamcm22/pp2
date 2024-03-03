import string

for letter in string.ascii_uppercase:
    file_name = letter + ".txt"
    with open(file_name, 'w') as f:
        f.write(f"This is file {file_name}")
        print(f"{file_name} has been created successfully.")