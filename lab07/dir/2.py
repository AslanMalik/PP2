import os
file = r"C:\Users\Work\Desktop\PP2\my_project\lab07\dir\1.py"

print(os.access(file, os.F_OK))
print(os.access(file, os.R_OK))
print(os.access(file, os.W_OK))
print(os.access(file, os.X_OK))