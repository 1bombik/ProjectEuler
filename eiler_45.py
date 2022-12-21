answer = 0
tr_nums = [i * (i + 1) / 2 for i in range(1, 100000)]
fif_nums = [i * (3 * i - 1) / 2 for i in range(1, 100000)]
six_nums = [i * (2 * i - 1) for i in range(1, 100000)]
for tr in tr_nums:
    if tr > 40755 and tr in fif_nums and tr in six_nums:
        answer = tr
        break
print(answer)
