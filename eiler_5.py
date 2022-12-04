# https://projecteuler.net/problem=5

import numpy as n

first = int(input("Enter the first number of the range: "))
last = int(input("Enter the last number of the range: "))
a = n.array([1])
x = first
for x in range(first, last+1):
    a = n.append(a, x)
y = n.lcm.reduce(a)
print(y)
