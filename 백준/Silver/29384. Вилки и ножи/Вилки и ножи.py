import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())
import heapq

hq = []
n, m, k = g()
for _ in range(k):
    t, l, a = g()
    while hq and hq[0][0] <= t:
        n += 1
        m += hq[0][1]
        heapq.heappop(hq)
    if n and m >= a:
        n -= 1
        m -= a
        heapq.heappush(hq, (t + l, a))
        print('Yes')
    else:
        print('No')