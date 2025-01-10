import sys
input = sys.stdin.readline
from math import log
from collections import defaultdict

ans = 0
d = defaultdict(list)
for _ in range(int(input())):
    s, c = map(int, input().split())
    d[s].append(c)
for k, v in d.items():
    v.sort()
    ans += sum(log(v[len(v) - i - 1] / v[i]) for i in range(len(v) >> 1))
print(ans)