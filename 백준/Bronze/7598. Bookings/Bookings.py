while True:
    air, n = input().split()
    n = int(n)
    if air == '#':
        break
    while True:
        change, num = input().split()
        num = int(num)
        if change == 'X':
            break
        if change == 'B' and num <= 68 - n:
            n += num
        if change == 'C' and num <= n:
            n -= num
    print(air, n)