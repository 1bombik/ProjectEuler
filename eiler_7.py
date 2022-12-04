# https://projecteuler.net/problem=7

from sympy import *

number = int(input("What number do you need? - "))
y = [2]
for b in range(3, 1000000, 2):
    if isprime(b):
        y.append(b)
    if len(y) == number:
        break
print(y[number-1])
