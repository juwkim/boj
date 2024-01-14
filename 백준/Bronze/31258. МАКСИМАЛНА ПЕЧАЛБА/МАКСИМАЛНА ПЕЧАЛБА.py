import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

cnt = min(g())
ans = sum(a * b for a, b in zip(sorted(g())[-cnt:], sorted(g())[-cnt:]))
print(cnt, ans)