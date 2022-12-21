d = []
answer = []
numbers = [i * (3 * i - 1) / 2 for i in range(1, 10000)]
for j in numbers:
    for k in numbers:
        summ = j + k
        diff = k - j
        if summ in numbers and diff in numbers:
            d = [j, k, abs(diff)]
            answer.append(d)
print(answer)
