import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from collections import defaultdict

while (l:=g()) != [0]:
    n, m = l
    dic = [defaultdict(lambda: -1) for _ in range(4)]
    for _ in range(m):
        k, x, y, s, t = g()
        for _ in range(k):
            dic[0][x] += 1
            dic[1][y] += 1
            dic[2][x + y] += 1
            dic[3][x - y] += 1
            x += s
            y += t
    print(sum(sum(d.values()) for d in dic))