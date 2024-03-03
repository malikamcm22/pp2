from functools import reduce
list2=[2,3,4,5]

def my_func(numbers):
    multiply=1
    for i in numbers:
        return reduce(lambda a,b:a*b, numbers)

# list1=[]
# list1.append(int(input()))

print(my_func(list2))
