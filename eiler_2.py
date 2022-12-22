# https://projecteuler.net/problem=2

f1 = 1
f2 = 2
a = [f1, f2]
for i in range(35):
    f_sum = f1 + f2
    a.append(f_sum)
    f1 = f2
    f2 = f_sum
b = [j for j in a if j % 2 == 0 and j < 4_000_000]
print(sum(b))
