import re

text = "Hello world Python Code testCase ABCde Fghij JavaScript C++ Test_case Hello123 Bye"

pattern = r"[A-Z][a-z]+"

x = re.findall(pattern, text)

print(x)