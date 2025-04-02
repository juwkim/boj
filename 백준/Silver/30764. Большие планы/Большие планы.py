import sys
g = lambda: map(int, sys.stdin.readline().split())

n, a, b, c = g()
px = [0] * (a + 2)
for _ in range(n):
    l, r = g()
    px[l] += 1
    px[r + 1] -= 1
for i in range(a): px[i + 1] += px[i]
ans, cur = "Yes", sum(px[:b])
for i in range(b, a + 1):
    cur += px[i] - px[i - b]
    if cur > c:
        ans = "No"
        break
print(ans)