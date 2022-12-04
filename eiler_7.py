# https://projecteuler.net/problem=7

number = int(input("What number do you need? - "))
y = []
x = 2  # lowest prime number
for b in range(1, 100000000, 2):
    c = (x**(b-1))-1  # Fermat's little theorem
    if c % b == 0:
        y.append(b)
    if len(y) == number:
        break
print(y[number-1])
