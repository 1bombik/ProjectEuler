a = []
for i in range(1, 1001):
    a.append(i ** i)

print(str(sum(a))[-10:])
