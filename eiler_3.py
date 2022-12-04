# https://projecteuler.net/problem=3

a = 600851475143
x = 2  # lowest prime number
b = 0
y = []
for b in range(1, a+1):
    c = (x**(b-1))-1  # Fermat's little theorem
    if c % b == 0 and a % b == 0:
        y.append(b)
print("The prime factors of", a, "-", y)
print("Max prime factor of", a, "-", max(y))
