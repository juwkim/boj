while (s:= input()) != '#':
    base = int(input())
    deci = int(input())
    tmp = deci
    ans = ''
    while True:
        r, q = divmod(deci, base)
        ans = '0123456789ABCDEFGHIJ'[q] + ans
        deci = r
        if deci == 0:
            break
    print(s, tmp, ans, sep=', ')