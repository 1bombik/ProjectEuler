def foo():
    nums = []
    count = 0
    num = 0
    for tr_num in range(1, 100_000_000):
        while count <= tr_num:
            num += count
            count += 1
        nums.append(num)
    return nums


def foo1(nums):
    div_len = 0
    for number in nums:
        divs = []
        for i in range(1, number+1):
            if number % i == 0:
                divs.append(i)
        if len(divs) > div_len:
            div_len = len(divs)
            if len(divs) > 500:
                answer_num = number
                answer_dividers = divs
                break
    return (f'{answer_num}\n'
            f'{len(answer_dividers)}')


print(foo1(foo()))
