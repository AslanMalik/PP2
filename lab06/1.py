import re

text_match = "Adidas boba cool abi lev dafabi"

pattern = r"ab*"

x = re.finditer(pattern, text_match)

for y in x:
    print(y)

