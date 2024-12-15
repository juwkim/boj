import sys
input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
d = defaultdict(int)
for _ in range(k):
    *l, s = input().split()
    d[s] = max(d[s], len(l) + 1)
if sum(d.values()) <= n:
    print("YES")
else:
    print("NO")