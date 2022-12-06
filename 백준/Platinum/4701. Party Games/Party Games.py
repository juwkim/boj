while n:= int(input()):
    names = sorted(input() for _ in range(n))
    n >>= 1
    
    ans = ''
    a, b = names[n-1], names[n]
    for i, j in zip(a, b):
        if i == j:
            ans += i
        else:
            break
    while True:
        if a <= ans < b:
            print(ans)
            break
        tmp1 = ans + a[len(ans)]
        if a <= tmp1 < b:
            print(tmp1)
            break
        if a[len(ans)] != 'Z':
            tmp2 = ans + chr(ord(a[len(ans)]) + 1)
            if a <= tmp2 < b:
                print(tmp2)
                break
        ans = tmp1