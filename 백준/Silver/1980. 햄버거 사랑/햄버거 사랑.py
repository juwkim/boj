g = lambda: [*map(int, input().split())]
n, m, t = g()
ans = (1e9, 0)
for i in range(1 + t//n):
    j, r = divmod(t - i * n, m)
    ans = min(ans, (r, - i - j))
print(-ans[1], ans[0])