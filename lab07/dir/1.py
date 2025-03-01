import os
path = r'C:\Users\Work\Desktop\PP'

files, catagoles = [], []


for know in os.listdir(path):

    full_path = os.path.join(path, know)  

    if os.path.isfile(full_path):
        files.append(know)

    if os.path.isdir(full_path):
        catagoles.append(know)

print("Only files:", *files)
print("Only catatalog:", *catagoles)