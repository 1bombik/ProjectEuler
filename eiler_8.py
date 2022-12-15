from functools import reduce

with open('eiler_8.txt', 'r') as a:
    a = ''.join(a).replace('\n', '')

n1 = 0
n2 = 13
answer = 0
answer_numbers = []
while n2 <= 1000:
    list_1 = []
    for i in range(n1, n2):
        list_1.append(int(a[i]))
        c = reduce(lambda k, j: k * j, list_1)
        if c > answer:
            answer = c
            answer_numbers.append(list_1)
    n1 += 1
    n2 += 1
print(f'Max answer - {answer}')
print(f'Numbers for the max answer - {answer_numbers[-1]}')
