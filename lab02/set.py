thisset = {"apple", "banana", "cherry", False, True}
print(thisset)  # Outputs: {False, True, 'banana', 'cherry', 'apple'} 

print()

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)  # Outputs each element in the set (order is not guaranteed)

print()

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)  # Outputs: {'orange', 'banana', 'cherry', 'apple'} (order is not guaranteed)

print()

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)  # Outputs: {'cherry', 'apple'}

print()

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)  # Outputs each element in the set (order is not guaranteed)

print()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)  # Outputs a union of all sets: {'John', 1, 2, 3, 'cherry', 'Elena', 'bananas', 'apple', 'b', 'a', 'c'} (order is not guaranteed)

print()

# Set Methods
# add()                        Adds an element to the set
# clear()                      Removes all the elements from the set
# copy()                       Returns a copy of the set
# difference()          (-)    Returns a set containing the difference between two or more sets
# difference_update()   (-=)   Removes the items in this set that are also included in another, specified set
# discard()                    Removes the specified item
# intersection()        (&)    Returns a set, that is the intersection of two other sets
# intersection_update() (&=)   Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()                 Returns whether two sets have no intersection or not
# issubset()            (<=)   Returns whether another set contains this set or not
# <                            Returns whether all items in this set are present in another, specified set(s)
# issuperset()          (>=)   Returns whether this set contains another set or not
# >                            Returns whether all items in another, specified set(s) are present in this set
# pop()                        Removes an element from the set
# remove()                     Removes the specified element
# symmetric_difference() (^)   Returns a set with the symmetric differences of two sets
# symmetric_difference_update()(^=) Inserts the symmetric differences from this set and another
# union()               (|)    Return a set containing the union of sets
# update()             (|=)    Update the set with the union of this set and others
