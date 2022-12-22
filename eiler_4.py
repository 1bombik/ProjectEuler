# https://projecteuler.net/problem=4

b = []
for i in range(100, 1000):
    for n in range(100, 1000):
        a = i * n
        b.append(a)
k = [j for j in b if str(j) == str(j)[::-1]]
print(max(k))
