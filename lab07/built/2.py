string = "Hello World!Python is FUN.123 ABC abc"

small = sum(map(str.islower, string))
big = sum(map(str.isupper, string))

print("Small count:", small)
print("Big count:", big)