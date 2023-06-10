g = lambda: [*map(int, input().split())]

n, l = g()
ans = (1e9, 0)
for _ in range(1, n + 1):
    pos, vel = g()
    time = (l - pos) / vel
    ans = min(ans, (time, _))
print(ans[1])