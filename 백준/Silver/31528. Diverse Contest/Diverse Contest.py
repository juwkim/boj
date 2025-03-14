import sys
input = sys.stdin.readline
from itertools import combinations
from collections import Counter

n, k = map(int, input().split())
p = [input().split()[1:] for _ in range(n)]
ans = 0
for c in combinations(p, k):
    cnt = Counter()
    for tags in c:
        for tag in tags:
            cnt[tag] += 2
    ans += all(cnt[tag] <= k for tag in cnt)
print(ans)