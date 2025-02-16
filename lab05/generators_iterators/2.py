
def define_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

n = int(input())
even_n = define_even(range(n))

for num in even_n:
    print(num, end=', ')