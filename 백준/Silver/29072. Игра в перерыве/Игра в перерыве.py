from collections import Counter
import heapq

n, *a = map(int, open(0).read().split())
cnt = Counter(a)
hq = list(cnt.keys())
heapq.heapify(hq)
while len(hq) >= 2:
    x = heapq.heappop(hq)
    num = cnt[x] >> 1
    if num:
        v = x << 1
        if v not in cnt:
            heapq.heappush(hq, v)
        cnt[v] += num
print(hq[0] * (1 << cnt[hq[0]].bit_length() - 1))