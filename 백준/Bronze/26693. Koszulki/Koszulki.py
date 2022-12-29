g = lambda: [*map(int, input().split())]

from collections import Counter
n, k = g()
cnt = Counter(g())
ans = 0
for num in sorted(cnt, reverse=True):
    ans += cnt[num]
    k -= cnt[num]
    if k <= 0:
        break
print(ans)