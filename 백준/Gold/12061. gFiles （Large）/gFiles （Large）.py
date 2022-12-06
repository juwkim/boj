for step in range(1, 1 + int(input())):
    l, r = 0, 10 ** 15
    flag = False
    for _ in range(int(input())):
        p, k = map(int, input().split())
        if flag:
            continue
        if p == 100:
            ans = k
            flag = True
            continue           
        l = max(l, 100 * k // (p + 1) + 1)
        if p:
            r = min(r, 100 * k // p)
    if not flag:
        if l == r:
            ans = l
        else:
            ans = -1
    print(f'Case #{step}: {ans}')