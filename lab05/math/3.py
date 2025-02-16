from math import *
n = int(input())
s = int(input())
area = (n*s**2)/(4*tan(pi/n))
print(f"The area of the polygon is: {area}")