n, c, *a = map(int, open(0).read().split())
queue = 0
ans, min_wait = "impossible", 1e18
for t in range(n):
    waiting = (queue + a[t]) // c
    if waiting < min(min_wait, n - t):
        ans, min_wait = t, waiting
    queue = max(0, queue + a[t] - c)
print(ans)