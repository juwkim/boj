g = lambda: [*map(int, input().split())]

N, M = g()
buf = []
cur = 0
for _ in range(N):
    d, v = g()
    buf += [v] * d

res = []
for _ in range(M):
    d, v = g()
    res += [v] * d
print(max(0, max(i - j for i, j in zip(res, buf))))