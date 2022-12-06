# https://projecteuler.net/problem=16

a = 2 ** 1000
b = []
a = str(a)
for i in range(len(a)):
    b.append(int(a[i]))
print(sum(b))
