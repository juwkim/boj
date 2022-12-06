while n:=int(input()):
    num, k = 0, 1
    while n:
        num += n%10 * (2**k - 1)
        n, k = n // 10, k + 1
    print(num)