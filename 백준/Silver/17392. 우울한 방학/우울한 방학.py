f = lambda x: x * (x + 1) * (2 * x + 1) // 6

N, M, *H = map(int, open(0).read().split())
cnt = N + sum(H)
if cnt >= M:
    print(0)
else:
    q, r = divmod(M - cnt, N + 1)
    print(r * f(q + 1) + (N + 1 - r) * f(q))