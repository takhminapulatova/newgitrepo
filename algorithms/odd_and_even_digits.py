def odd_and_even_dig(n: int):
    even_d = 0
    odd_d = 0
    while n != 0:
        a = n % 10
        if a % 2 == 0:
            even_d += 1
        else:
            odd_d += 1
        n = n // 10

    print(even_d)
    print(odd_d)


odd_and_even_dig(3455)
