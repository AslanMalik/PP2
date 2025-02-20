import re

text = "HelloWorld PythonCode testCase ABCde Fghij JavaScript C++ TestCase Hello123 Bye"

x = re.sub("([a-z])([A-Z])", r"\1 \2", text) 

print(x)


