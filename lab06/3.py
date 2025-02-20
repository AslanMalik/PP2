import re 

text = "hello_world python_code test_case Test_Case hello123_world hello world some_var another_example_ok"

pattern = r"[a-z]+_[a-z]+"

x = re.findall(pattern, text)

print(x)