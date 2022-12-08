# https://projecteuler.net/problem=25

fib1 = 1
fib2 = 1
fib_sum = 0
fib_list = [1, 1]
while fib_sum >= 0:
    fib_sum = fib1 + fib2
    fib_list.append(fib_sum)
    fib1 = fib2
    fib2 = fib_sum
    if len(str(fib_sum)) == 1000:
        print('Number -', fib_sum)
        print('Index -', fib_list.index(fib_sum)+1)
        break
