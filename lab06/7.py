import re

text = "hello_world convert_snake_to_camel this_is_a_test python_code_example make_snake_case_great_again"

x = re.sub("_([a-z])", lambda x: x.group(1).upper() , text)

print(x)
