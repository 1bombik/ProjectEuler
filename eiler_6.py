# https://projecteuler.net/problem=6

import numpy as n

first = int(input("Enter the first number of the range: "))
last = int(input("Enter the last number of the range: "))
a = []
for x in range(first, last+1):
    a.append(x)
sos = sum(a)**2  # square of the sum
ss = n.square(a)  # sum of the squares
ss = sum(ss)
print("Square of the sum =", sos)
print("Sum of the squares =", ss)
print("Answer -", sos - ss)
