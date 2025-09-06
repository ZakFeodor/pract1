from math import *
a = float(input())
z1 = (sin(2*a)+sin(5*a)+-sin(3*a))/(cos(a)+1-2*sin(2*a)**2)
z2 = 2*sin(a)
print(round(z1, 3), round(z2, 3))