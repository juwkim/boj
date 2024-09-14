import sys
import heapq
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N, M, K = g()
hq = []
ans, cur = -1, 0
for v, c in sorted([g() for _ in range(K)], key=lambda x: x[1]):
    if len(hq) == N:
        cur -= heapq.heappop(hq)
    cur += v
    heapq.heappush(hq, v)
    if len(hq) == N and cur >= M:
        ans = c
        break
print(ans)