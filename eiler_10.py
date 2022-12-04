# https://projecteuler.net/problem=10

from sympy import *

b = [2]
for i in range(3, 2_000_000, 2):
    if isprime(i):
        b.append(i)
print(sum(b))
