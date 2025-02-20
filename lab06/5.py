import re

text = "acb a123b aXYZb a_b a-b aabb ab aac abbb abc xyzab bbb"


goal = r"a.*b$"

x = re.findall(goal, text)

print(x)



