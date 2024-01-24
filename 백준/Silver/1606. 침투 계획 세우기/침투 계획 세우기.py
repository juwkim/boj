import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

x, y = g()
ans = 3 * (x + y) * (x + y + 1) + 1
if y:
    ans += y - 6 * (x + y)
print(ans)