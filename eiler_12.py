# https://projecteuler.net/problem=12

def foo():
    nums = []
    count = 0
    num = 0
    for tr_num in range(1, 12500):
        while count <= tr_num:
            num += count
            count += 1
        nums.append(num)
    return nums


def foo1(nums):
    for number in nums:
        divs = [i for i in range(1, number+1) if number % i == 0]
        if len(divs) > 500:
            answer_num = number
            answer_dividers = divs
            break
    return (f'Answer - {answer_num}\n'
            f'Quantity of dividers - {len(answer_dividers)}')


print(foo1(foo()))
