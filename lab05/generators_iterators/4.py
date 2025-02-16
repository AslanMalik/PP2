
def square(a, b):
    for i in range(a, b+1):
        yield i**2

a, b = int(input()), int(input())

square_numbers = square(a, b)

for num in square_numbers:
    print(num, end=' ')