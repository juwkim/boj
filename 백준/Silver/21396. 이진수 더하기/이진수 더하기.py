import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
from collections import Counter

for _ in range(int(input())):
    n, x = g()
    cnt = Counter(g())
    if x: ans = sum(cnt[k] * cnt[x ^ k] for k in cnt) >> 1
    else: ans = sum(cnt[k] * (cnt[k] - 1) for k in cnt) >> 1
    print(ans)