import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
x = sorted(g())
dist = sum(x[i] - x[0] for i in range(1, n))
ans = dist
for i in range(1, n):
    dist += (x[i] - x[i - 1]) * (2 * i - n)
    ans += dist
print(ans)