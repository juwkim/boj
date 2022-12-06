g = lambda: [*map(int, input().split())]

n, m = g()
times = g()
buf = set(g()[0] for _ in range(m))

ans = 0
for i in range(n):
    if i + 1 not in buf:
        ans = max(ans, times[i])
print(sum(times) - ans)