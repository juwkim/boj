import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
import heapq

N, K = g()
nums = [[] for _ in range(11)]
for _ in range(N):
    P, W = g()
    nums[P - 1].append(-W)
ans = 0
for l in nums:
    heapq.heapify(l)
    if not l:
        continue
    for _ in range(K):
        num = -heapq.heappop(l)
        if num == 1:
            continue
        heapq.heappush(l, 1 - num)
    if l:
        ans += -heapq.heappop(l)
print(ans)