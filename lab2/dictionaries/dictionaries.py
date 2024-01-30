thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) #ford
print(thisdict["year"]) #year
print(thisdict["model"]) #mustang


thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1999",
    "year" : "2020"
}
print(thisdict) #{'brand' : 'Ford', 'model' : 'Mustang', 'year' : '2020'}
print(len(thisdict)) #3
print(type(thisdict)) #<class 'dict'>
x = thisdict.keys()
print(x) #dict_keys(['brand', 'model', 'year'])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
# before dict_keys(['brand', 'model', 'year'])
#after dict_keys(['brand', 'model', 'year','color'])

x = thisdict.values() #dict_values(['Ford', 'Mustang',1964])


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


"""
clear()	     Removes all the elements from the dictionary
copy()	     Returns a copy of the dictionary
fromkeys()	 Returns a dictionary with the specified keys and value
get()	      Returns the value of the specified key
items()	      Returns a list containing a tuple for each key value pair
keys()	      Returns a list containing the dictionary's keys
pop()	      Removes the element with the specified key
popitem()	  Removes the last inserted key-value pair
setdefault()  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	  Updates the dictionary with the specified key-value pairs
values()	  Returns a list of all the values in the dictionary
"""
