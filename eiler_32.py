numbers = []
for i in range(1, 10000):
    for k in range(1, 10000):
        number = i * k
        check = str(i) + str(k) + str(number)
        check1 = set(check)
        if "0" not in check and 9 == len(check) == len(check1):
            print(i, k, number)
            numbers.append(number)
numbers = list(set(numbers))
print(sum(numbers))
