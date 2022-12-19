# https://projecteuler.net/problem=40

a = '0.'
for i in range(1, 200000):
    i = str(i)
    a += i
    if len(a) > 1000002:
        break
answer = int(a[0 + 2]) * \
         int(a[9 + 2]) * \
         int(a[99 + 2]) * \
         int(a[999 + 2]) * \
         int(a[9999 + 2]) * \
         int(a[99999 + 2]) * \
         int(a[999999 + 2])
print(answer)
