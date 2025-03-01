import random

with open("example5.txt", "w") as file:
    array = [random.randint(1, 100) for _ in range(random.randint(10, 30))]

    file.write(f"{array}")