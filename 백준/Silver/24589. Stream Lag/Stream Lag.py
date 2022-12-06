g = lambda: [*map(int, input().split())]

n = int(input())
buf = [0] * n
for _ in range(n):
    t, i = g()
    buf[i-1] = t
ans = 0
cur = 1
for time in buf:
    if time > cur:
        ans += time - cur
        cur = time + 1
    else:
        cur += 1
print(ans)