import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import combinations
from collections import Counter

*S, k = open(0).read().split()
k = int(k)
cnt = Counter()
for s in S:
    for l in combinations(s, k):
        cnt[''.join(l)] += 1
ans = sorted(k for k, v in cnt.items() if v >= 2)
if ans:
    print(*ans)
else:
    print(-1)