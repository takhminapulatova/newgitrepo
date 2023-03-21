def digit_sum(n: int):
    sum_n = 0
    while n > 0:
        sum_n = sum_n + n
        n = n - 1
    print(sum_n)


digit_sum(6)
