import re

text = "HelloWorld PythonCode testCase ABCde Fghij JavaScript C++ TestCase Hello123 Bye"

x = re.sub("([a-z])([A-Z])", lambda x: x.group(1) + "_" + x.group(2).lower(), text)

print(x)
