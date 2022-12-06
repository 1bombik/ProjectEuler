import numpy as np

a = np.math.factorial(100)
b = []
a = str(a)
for i in range(len(a)):
    b.append(int(a[i]))
print(sum(b))
