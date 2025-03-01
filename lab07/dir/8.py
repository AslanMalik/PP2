import os

file = r"C:\Users\Work\Desktop\PP2\my_project\lab07\dir\1.py"

if os.path.exists(file):
    os.remove("1.py")
else:
    print("Empty")
