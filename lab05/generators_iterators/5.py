
def reverse(numbers):
    for i in range(n, -1, -1):
        yield i

n = int(input())
n_reverse = reverse(n)

for num in n_reverse:
    print(num, end='')