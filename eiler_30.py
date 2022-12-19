# https://projecteuler.net/problem=30

summ = 0
for number in range(2, 1000000):
    nums = [int(i) ** 5 for i in str(number)]
    if number == sum(nums):
        summ += number
print(summ)
