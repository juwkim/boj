g = lambda: map(int, input().split())

n, C = g()
ans = 1e9
for _ in range(n):
    p, d, v = g()
    ans = min(ans, p + d + C * v)
print(ans)