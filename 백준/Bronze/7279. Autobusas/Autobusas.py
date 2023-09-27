import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
ans, cur = 0, 0
for _ in range(N):
    a, b = g()
    cur += a - b
    ans = max(ans, cur)
print(max(0, ans - K))