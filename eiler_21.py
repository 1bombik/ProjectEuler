answer = []
for num in range(1, 10000):
    friend_num = num
    da = 0
    db = 0
    for div in range(1, friend_num):
        if friend_num % div == 0:
            da += div
    for divs in range(1, da):
        if da % divs == 0:
            db += divs
    if friend_num == db and da != db:
        answer.append(db)
print(sum(answer))
