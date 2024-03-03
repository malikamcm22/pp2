def write_list_to_file(file_name, my_list):
    with open(file_name, 'w') as f:
        for item in my_list:
            f.write("%s\n" % item)
        print(f"The list has been written to {file_name} successfully.")

my_list = ['apple', 'banana', 'orange', 'grape']
file_name = input("Enter the file name: ")
write_list_to_file(file_name, my_list)