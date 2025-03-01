
with open("example5.txt") as file:
    info = file.read()
    with open("example5_copy.txt", "w") as file1:
        file1.write(info)

