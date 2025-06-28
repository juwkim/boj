g = lambda: [*map(int, input().split())]

M, N = g()
T = g()
X = g()
dists = set()
for i in range(N - M + 1):
    seg = X[i:i+M]
    dx = seg[1] - seg[0]
    dt = T[1] - T[0]
    if all((seg[j] - seg[0]) * dt == (T[j] - T[0]) * dx for j in range(2, M)):
        dists.add(dx)
ans = sorted(dists)
print(len(ans))
print(*ans)