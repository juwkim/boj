g = lambda: [*map(int, input().split())]

n, m = g()
a = [[0] * (m + 2)] + [[0] + g() + [0] for _ in range(n)] + [[0] * (m + 2)]
ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        ans += all(a[i][j] > a[i + dx][j + dy] for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
print(ans)