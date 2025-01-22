thislist = ["apple", 1, True]
print(thislist)  # Outputs: ['apple', 1, True]

print()

thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # Outputs: 'banana'
print(thislist[-1])  # Outputs: 'cherry'

print()

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  # Outputs: ['apple', 'blackcurrant', 'cherry']

print()

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # Outputs: ['apple', 'banana', 'cherry', 'orange']

print()

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")  # Removes 'banana'
thislist.pop(1)  # Removes the element at index 1 ('cherry')
print(thislist)  # Outputs: ['apple']

print()

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)  # Outputs each element in the list: 'apple', 'banana', 'cherry'

print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  # Outputs: ['apple', 'banana', 'mango']

print()

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)  # Outputs: ['Kiwi', 'Orange', 'banana', 'cherry']

print()

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)  # Outputs: ['apple', 'banana', 'cherry']

print()

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)  # Outputs: ['a', 'b', 'c', 1, 2, 3]

print()

# List Methods
# append()  Adds an element at the end of the list
# clear()   Removes all the elements from the list
# copy()    Returns a copy of the list
# count()   Returns the number of elements with the specified value
# extend()  Add the elements of a list (or any iterable) to the end of the current list
# index()   Returns the index of the first element with the specified value
# insert()  Adds an element at the specified position
# pop()     Removes the element at the specified position
# remove()  Removes the item with the specified value
# reverse() Reverses the order of the list
# sort()    Sorts the list
