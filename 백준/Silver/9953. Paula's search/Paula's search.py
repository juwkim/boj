while n:= int(input()):
    ans = n&1
    n = (n-1)//2
    
    l, r = 0, 49
    while True:
        ans += 1
        m = (l + r) // 2
        if m == n:
            print(ans)
            break
        elif m > n:
            r = m - 1
        else:
            l = m + 1