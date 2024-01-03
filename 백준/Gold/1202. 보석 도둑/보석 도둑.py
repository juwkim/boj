import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

import heapq

N, K = g()
jewels = sorted(g() for _ in range(N)) # [무게, 가격]

ans = 0
idx = 0
heap = []
for bag in sorted(int(input()) for _ in range(K)):
    while idx < N and jewels[idx][0] <= bag:
        heapq.heappush(heap, -jewels[idx][1])
        idx += 1
    if heap:
        ans -= heapq.heappop(heap)
print(ans)