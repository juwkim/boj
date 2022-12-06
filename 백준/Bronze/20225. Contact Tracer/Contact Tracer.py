g = lambda: [*map(int, input().split())]

while (s:= input()) != '0 0 0':    
    m, n, p = map(int, s.split())
    cnt = 1
    res = {p}
    for _ in range(n):
        a, b = g()
        if (a in res) + (b in res) == 1:
            cnt += 1
            res.update((a, b))
    print(cnt)