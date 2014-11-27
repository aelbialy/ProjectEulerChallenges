#project Euler #20
from math import *

x = str(factorial(100))
y = []
for i in x:
    y.append(int(i))
print(sum(y))