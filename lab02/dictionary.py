thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)  # Outputs dictionary: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x)  # Before the change: dict_values(['Ford', 'Mustang', 1964])
car["year"] = 2020
print(x)  # After the change: dict_values(['Ford', 'Mustang', 2020])

print()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)  # Outputs the updated dictionary: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

print()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)  # Adds a new key-value pair: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

print()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)  # Removes 'model': {'brand': 'Ford', 'year': 1964}

print()

for x, y in thisdict.items():
  print(x, y)  # Outputs key-value pairs: 'brand Ford', 'year 1964'

print()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)  # Outputs dictionary: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print()

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"])  # Outputs the name of child2: 'Tobias'

print()

# Dictionary Methods
# clear()       Removes all the elements from the dictionary
# copy()        Returns a copy of the dictionary
# fromkeys()    Returns a dictionary with the specified keys and value
# get()         Returns the value of the specified key
# items()       Returns a list containing a tuple for each key value pair
# keys()        Returns a list containing the dictionary's keys
# pop()         Removes the element with the specified key
# popitem()     Removes the last inserted key-value pair
# setdefault()  Returns the value of the specified key. If the key does not exist: inserts the key with the specified value
# update()      Updates the dictionary with the specified key-value pairs
# values()      Returns a list of all the values in the dictionary
