# https://projecteuler.net/problem=4

b = []
k = []
for i in range(100, 1000):
    for n in range(100, 1000):
        a = i * n
        b.append(a)
for j in b:
    if str(j) == str(j)[::-1]:
        k.append(j)
print(max(k))
