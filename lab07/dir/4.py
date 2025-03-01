text = "task4.txt"

with open(text) as file:
    count = 0
    for line in file:
        count += 1
    
    print(count)