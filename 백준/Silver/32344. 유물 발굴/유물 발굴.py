import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
from collections import defaultdict
size = lambda x: (d[x][2] - d[x][0] + 1) * (d[x][3] - d[x][1] + 1)
R, C = g()
N = int(input())
d = defaultdict(lambda: [R, C, 1, 1])
for _ in range(N):
    a, v, h = g()
    d[a][0] = min(d[a][0], v)
    d[a][1] = min(d[a][1], h)
    d[a][2] = max(d[a][2], v)
    d[a][3] = max(d[a][3], h)
k = min(d.keys(), key=lambda x: (-size(x), x))
print(k, size(k))