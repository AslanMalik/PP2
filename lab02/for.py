for x in "banana":
  print(x)  # Prints each letter in the string "banana"

print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)  # Prints each fruit in the list
  if x == "banana":
    break  # Stops the loop when x = "banana" 

print()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue  # Skips the iteration when x = "banana" 
  print(x)  # Prints all fruits except "banana"

print()

for x in range(2, 30, 3):
  print(x)  # Prints numbers from 2 to 29, step by 3

print()

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)  # Prints all combinations of adjectives and fruits
