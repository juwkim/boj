import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
buf = [g() for _ in range(n)]
ans = float('inf')
for i in range(n - 1):
    x1, v1 = buf[i]
    for j in range(i + 1, n):
        x2, v2 = buf[j]
        if (x1 - x2) * (v1 - v2) >= 0:
            continue
        t = (x2 - x1) / (v1 - v2)
        ans = min(ans, t)
print(ans)