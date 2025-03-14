import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
from collections import defaultdict
from bisect import bisect

for _ in range(int(input())):
    n, m = g()
    ver, hor = defaultdict(list), defaultdict(list)
    for _ in range(n):
        x, y = g()
        ver[x].append(y)
        hor[y].append(x)
    for k in ver:
        ver[k].sort()
    for k in hor:
        hor[k].sort()
    view = set()
    ver_keys, hor_keys = list(ver.keys()), list(hor.keys())
    for _ in range(m):
        s = input()
        num = int(s[2:])
        if s[0] == 'x':
            for y in hor_keys:
                idx = bisect(hor[y], num)
                if idx < len(hor[x]):
                    view.add((hor[y][idx], y))
                if idx > 0:
                    view.add((hor[y][idx - 1], y))
        else:
            for x in ver_keys:
                idx = bisect(ver[x], num)
                if idx < len(ver[x]):
                    view.add((x, ver[x][idx]))
                if idx > 0:
                    view.add((x, ver[x][idx - 1]))    
    print(len(view))