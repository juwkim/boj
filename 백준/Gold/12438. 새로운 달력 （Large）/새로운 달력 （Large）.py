for case in range(1, 1 + int(input())):
    n, m, w = map(int, input().split())
    
    s, u = {}, {}
    d, t, f, i = 0, 0, None, 0
    while i < n:
        t += (m + d - 1) // w + 1
        d = (m + d) % w
        if d not in s:
            s[d] = i
            u[d] = t
        else:
            f = i - s[d]
            g = t - u[d]
            break
        i += 1
            
    if f != None:
        r = n - i - 1
        t += g * (r//f)
        for i in range(r % f):
            t += (m + d - 1) // w + 1
            d = (m + d) % w
    ans = t

    print(f"Case #{case}: {ans}")