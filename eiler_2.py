# https://projecteuler.net/problem=2

f1 = 1
f2 = 2
a = [f1, f2]
b = []
i = 0
for i in range(35):
    f_sum = f1 + f2
    a.append(f_sum)
    f1 = f2
    f2 = f_sum
    i += 1
for j in a:
    if j % 2 == 0 and j < 4000000:
        b.append(j)
print(sum(b))
