def my_func(tuplee):
    return all(tuplee)

my_tuple=(True, True, True)
my_tuple2=(False, True, False)

print(my_func(my_tuple))#true
print(my_func(my_tuple2))#false

