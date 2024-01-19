import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

px, py = [[] for _ in range(10001)], [[] for _ in range(10001)]
for _ in range(int(input())):
    x, y = g()
    px[x].append(y)
    py[y].append(x)
ans = 0
for i in range(10001):
    if px[i]:
        px[i].sort()
        for j in range(0, len(px[i]), 2):
            ans += px[i][j+1] - px[i][j]
    if py[i]:
        py[i].sort()
        for j in range(0, len(py[i]), 2):
            ans += py[i][j+1] - py[i][j]
print(ans)