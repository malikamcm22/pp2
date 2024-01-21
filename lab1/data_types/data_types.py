x = 5
print(type(x)) #<class 'int'>



x = "Hello World"
#display x:
print(x) #"Hello World"
#display the data type of x:
print(type(x)) #<class 'str'>


x = 20
print(x)
print(type(x)) 
#<class 'int'>

x = 20.5
print(x)
print(type(x)) 
#<class 'float'>

x = range(6)
print(x)
print(type(x)) 
"""
range(0, 6)
<class 'range'>
"""


x = {"name" : "John", "age" : 36}
print(x)
print(type(x)) 
"""
{'name': 'John', 'age': 36}
<class 'dict'>
"""


x = {"apple", "banana", "cherry"}
print(x)
print(type(x)) 
#{"apple", "banana", "cherry"}
#<class 'set'>

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) 
"""
frozenset({'apple', 'banana', 'cherry'})
<class 'frozenset'>
"""


x = True
print(x)
print(type(x)) 
#true
# #<class 'bool'>

x = b"Hello"
print(x)
print(type(x)) 
#<class 'bytes'>

x = bytearray(5)
print(x)
print(type(x)) 
#<class 'bytearray'>

x = memoryview(bytes(5))
print(x)
print(type(x))
#<class 'memoryview'>

x = None
print(x)
print(type(x)) 
#<class 'NoneType'>
