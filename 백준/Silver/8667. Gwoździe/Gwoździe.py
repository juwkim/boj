g = lambda: [*map(int, input().split())]

from collections import Counter

n, k = g()
cnt = Counter(g())

last = 0
px_sum = {}
for key in sorted(cnt.keys(), reverse=True):
    px_sum[key] = last
    last = min(last + cnt[key], k)

num = max(cnt[x] + px_sum[x] for x in px_sum)
print(num)