import re

text = "Hello, world. This is a test, sentence. Replace spaces, commas, and dots."


pattern = r"[ ,.]"

x = re.sub(pattern, ":", text)

print(x)

