

numbers = [int(x) for x in input().split()] 

print(sorted(list(filter(lambda x : x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1)), numbers))))