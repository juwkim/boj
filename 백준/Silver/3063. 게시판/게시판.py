import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = g()
    ans = (x2 - x1) * (y2 - y1)
    ans -= max(0, min(x2, x4) - max(x1, x3)) * max(0, min(y2, y4) - max(y1, y3))
    print(ans)