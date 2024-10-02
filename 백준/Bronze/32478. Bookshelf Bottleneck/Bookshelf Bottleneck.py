import sys
g = lambda: map(int, sys.stdin.readline().split())

n, H = g()
ans = 0
for _ in range(n):
    a, b, c = sorted(g())
    if a > H:
        ans = "impossible"
        break
    if b > H:
        ans += b
    else:
        ans += a
print(ans)