
def four_three(numbers):
    for num in range(0, numbers+1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input())
numbers = four_three(n)

for num in numbers:
    print(num, end = ' ')