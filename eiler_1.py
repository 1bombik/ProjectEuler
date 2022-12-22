# https://projecteuler.net/problem=1

answer = [a for a in range(1000) if a % 3 == 0 or a % 5 == 0]
print(sum(answer))
