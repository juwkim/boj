g = lambda: [*map(int, input().split())]

for step in range(1, 1 + int(input())):
    N, T = g()
    buf = [[] for i in range(N)]
    for _ in range(int(input())):
        H, P = g()
        if H != T:
            buf[H-1].append(P)
    cnt = []
    flag = True
    for i in range(N):
        buf[i].sort(reverse=True)
        num = 0
        l = len(buf[i])
        idx = 0
        while num < l and idx < l:
            num += buf[i][idx]
            idx += 1
        if num < l:
            flag = False
            break
        else:
            cnt.append(idx)
    if flag:
        print(f'Case #{step}:', *cnt)
    else:
        print(f'Case #{step}: IMPOSSIBLE')