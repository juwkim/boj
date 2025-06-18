import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

n, m, k = g()
a = g()
diff = [0] * (n + 1)
for _ in range(m):
    l, r = g()
    diff[l-1] += 1
    diff[r] -= 1

px = [0] * n
cur = 0
for i in range(n):
    cur += diff[i]
    px[i] = cur

ans = sum(px[i] * a[i] for i in range(n))
for i in sorted(range(n), key=lambda i: px[i], reverse=True):
    if k == 0 or px[i] == 0:
        break
    d = min(a[i], k)
    ans -= px[i] * d
    k -= d
print(ans)