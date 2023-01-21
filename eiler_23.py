abunts = []
answer = 0
for i in range(1, 28124):
    divs = []
    for number in range(1, i):
        if i % number == 0:
            divs.append(number)
    if sum(divs) > i:
        abunts.append(i)
for j in range(28124):
    for k in range(28124):
        num = j + k
        if num not in abunts:
            answer += num
print(answer)
