import re

text = "abb abbb c abb d x abbb yz a ab abbbb xyz babbb"

pattern = r"ab{2,3}"

x = re.findall(pattern, text)

print(x)