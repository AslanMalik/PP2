import time
import math

number = int(input())
wait = int(input())

time.sleep(wait/1000)
root = math.sqrt(number)

print(f"Square root of {number} after 2123 miliseconds is {root}")