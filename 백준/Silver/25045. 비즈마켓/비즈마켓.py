import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
ans = 0
for A, B in zip(sorted(g(), reverse=True), sorted(g())):
    ans += max(A - B, 0)
print(ans)