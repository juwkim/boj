n, l, h, *p = map(int, open(0).read().split())
px = [0] * (n + 1)
for i in range(n):
    px[i + 1] = px[i] + p[i]
Min, Max = 1e9, 0
for d in range(l, h + 1):
    for i in range(1, d + 1):
        cnt = 0
        s, e = 0, i
        while True:
            cnt += px[e] - px[s] > 0
            if e == n:
                break
            s, e = e, min(e + d, n)
        Min, Max = min(Min, cnt), max(Max, cnt)
print(Min, Max)