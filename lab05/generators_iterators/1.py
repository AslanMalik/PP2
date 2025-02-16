
def square(numbers):
    for num in numbers:
        yield num**2

n = int(input())
square_n = square(range(1, n+1))
for num in square_n:
    print(num)