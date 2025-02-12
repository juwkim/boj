import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

input()
ans = 0
for c in g():
    x, y = g()
    if c: ans += max(0, y - x)
print(ans)