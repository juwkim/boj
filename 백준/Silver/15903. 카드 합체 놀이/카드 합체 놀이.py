g = lambda: [*map(int, input().split())]

import heapq
n, m = g()
nums = g()
heapq.heapify(nums)
for _ in range(m):
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    add = a + b
    heapq.heappush(nums, add)
    heapq.heappush(nums, add)
print(sum(nums))