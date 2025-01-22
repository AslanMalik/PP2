a = 200
b = 33
if b > a:
  print("b is greater than a")  # works if b > a
elif a == b:
  print("a and b are equal")  # works if a == b
else:
  print("a is greater than b")  # if and elif wont work

print()

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")  # multipluy two conditions 

print()

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")  # combine two conditions 

print()

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")  # not make reverse False or True
