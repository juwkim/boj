import sys
input = sys.stdin.readline
from collections import defaultdict

dic = defaultdict(list)
for _ in range(int(input())):
    x, y = map(int, input().split())
    dic[y].append(x)
for y in dic:
    dic[y].sort()

ymin = min(dic)
l1, r1 = dic[ymin][0], dic[ymin][-1]
for y in dic:
    d = y - ymin
    l1 = min(l1, dic[y][0] - d)
    r1 = max(r1, dic[y][-1] + d)

ymax = max(dic)
l2, r2 = dic[ymax][0], dic[ymax][-1]
for y in dic:
    d = ymax - y
    l2 = min(l2, dic[y][0] - d)
    r2 = max(r2, dic[y][-1] + d)
ans = min(r1 - l1, r2 - l2)
print(ans)