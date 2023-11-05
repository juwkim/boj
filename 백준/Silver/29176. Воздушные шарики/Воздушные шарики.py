import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

n, k = g()
cnt = Counter(g())
if len(cnt) >= k:
    ans = list(cnt.keys())[:k]
else:
    ans = list(cnt.keys())
    k -= len(cnt)
    for num in cnt:
        c = min(k, cnt[num] - 1)
        k -= c
        ans.extend([num]*c)
        if not k:
            break
print(*ans)