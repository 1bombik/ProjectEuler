# https://projecteuler.net/problem=3

from sympy import *

a = 600851475143
y = [2]
for b in range(3, a+1, 2):
    if isprime(b) and a % b == 0:
        y.append(b)
print(f"Max prime factor of {a} is {max(y)}")
