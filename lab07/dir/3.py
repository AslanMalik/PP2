import os

file = r"C:\Users\Work\Desktop\PP2\my_project\lab07\dir\1.py"

if os.path.exists(file):
    print(os.path.basename(file))
    print(os.path.dirname(file))
else:
    print("Dont exist")