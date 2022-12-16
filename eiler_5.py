# https://projecteuler.net/problem=5

import numpy as np

first = int(input("Enter the first number of the range: "))
last = int(input("Enter the last number of the range: "))
a = np.array([1])
x = first
for x in range(first, last+1):
    a = np.append(a, x)
y = np.lcm.reduce(a)
print(y)
