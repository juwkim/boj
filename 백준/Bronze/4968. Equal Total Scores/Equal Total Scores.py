while (s:= input()) != '0 0':
    n, m = map(int, s.split())
    
    p = [int(input()) for _ in range(n)]
    q = [int(input()) for _ in range(m)]
    
    a = set(p)
    b = set(q)
    
    s, t = sum(p), sum(q)
    
    switch = False
    if s > t:
        a, b = b, a
        s, t = t, s
        switch = True
    if (t - s) & 1:
        print(-1)
        continue
    diff = (t - s) // 2

    ans = 1
    flag = False
    while ans + diff <= 100:
        if ans in a and ans + diff in b:
            flag = True
            break
        ans += 1
    if flag:
        if switch:
            print(ans + diff, ans)
        else:
            print(ans, ans + diff)
    else:
        print(-1)