thistuple = ("apple", "banana", "cherry")
print(thistuple)  # Outputs: ('apple', 'banana', 'cherry')

print()

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  # Outputs: 'cherry' 

print()

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)  # Outputs: ('apple', 'banana', 'cherry', 'orange')

print()

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)  # Outputs: 'apple'
print(yellow)  # Outputs: 'banana'
print(red)  # Outputs: 'cherry'

print()

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])  # Outputs each element in the tuple: 'apple', 'banana', 'cherry'

print()

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  # Outputs: ('a', 'b', 'c', 1, 2, 3)

print()

# Tuple Methods
# count()  Returns the number of times a specified value occurs in a tuple
# index()  Searches the tuple for a specified value and returns the position of where it was found
