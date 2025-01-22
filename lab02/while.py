i = 1
while i < 6:
  print(i)  # Outputs numbers from 1 to 5 (inclusive)
  i += 1

print()

i = 1
while i < 6:
  print(i)  # Outputs numbers starting from 1
  if i == 3:
    break  # Stops the loop when i equals 3
  i += 1

print()

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue  # Skips the iteration when i equals 3
  print(i)  # Outputs all numbers from 1 to 6 except 3
