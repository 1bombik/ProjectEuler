answer = []
for a in range(2, 101):
    for b in range(2, 101):
        number = a ** b
        answer.append(number)
answer = sorted(list(set(answer)))
print(len(answer))
