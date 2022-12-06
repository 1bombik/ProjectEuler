# https://projecteuler.net/problem=13

a = []
with open('eiler_13.txt', 'r') as file:
    for line in file:
        a.append(int(line))
print(str(sum(a))[0:10])
