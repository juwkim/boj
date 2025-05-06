import sys
import heapq
g = lambda: map(int, sys.stdin.readline().split())

n, k = g()
ds = [[] for _ in range(n)]
for _ in range(n):
    t, d = g()
    ds[d].append(t)
ans, heap = 0, []
for i in range(k):
    for t in ds[i]:
        heapq.heappush(heap, t)
    if not heap:
        ans = "IMPOSSIBLE"
        break
    ans += heapq.heappop(heap)
print(ans)