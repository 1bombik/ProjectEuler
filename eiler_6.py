# https://projecteuler.net/problem=6

import numpy as np

a = [x for x in range(101)]
sos = sum(a)**2  # square of the sum
ss = sum(np.square(a))  # sum of the squares
print("Square of the sum =", sos)
print("Sum of the squares =", ss)
print("Answer -", sos - ss)
