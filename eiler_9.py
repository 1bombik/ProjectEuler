# https://projecteuler.net/problem=9

k = 1000
for a in range(1, k):
    for b in range(a, k):
        for c in range(b, k):
            if (a ** 2 + b ** 2 == c ** 2
                    and a < b < c
                    and a + b + c == 1000):
                print(a, b, c)
                print(a * b * c)
