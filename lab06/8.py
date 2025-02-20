import re

text = "Hello world Python Code testCase ABCde Fghij JavaScript C++ Test_case Hello123 Bye"

x = re.findall("[A-Z]\w*", text)

print(x)

