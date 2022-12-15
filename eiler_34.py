import numpy as np

numbers = []

for number in range(3, 50000):
    a = []
    for digit in (str(number)):
        for i in digit:
            a.append(np.math.factorial(int(i)))
            if number == sum(a):
                numbers.append(number)

print(f'Numbers - {numbers}')
print(f'Sum of numbers - {sum(numbers)}')
