# https://projecteuler.net/problem=14

sub_len = 0
answer = 0
for a in range(1, 1_000_000):
    subseq = []
    num = a
    while num != 1:
        subseq.append(num)
        if num % 2 == 0:
            num /= 2
        else:
            num = (3 * num) + 1
    if len(subseq) > sub_len:
        sub_len = len(subseq)
        answer = a
print(f"The longest subsequence goes with the number - {answer}\n"
      f"It's length - {sub_len+1}")
