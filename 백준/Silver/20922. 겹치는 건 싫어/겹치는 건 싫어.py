import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

N, K = g()
a = g()
l, r = 0, 0
cnt = Counter()
ans = 0
while r < N:
    if cnt[a[r]] == K:
        cnt[a[l]] -= 1
        l += 1
    else:
        cnt[a[r]] += 1
        r += 1
        ans = max(ans, r - l)
print(ans)