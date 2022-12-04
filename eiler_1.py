# https://projecteuler.net/problem=1

a = int(0)
b = int(0)
for a in range(1000):
    if a % 3 == 0 or a % 5 == 0:
        b = a + b
print(b)
