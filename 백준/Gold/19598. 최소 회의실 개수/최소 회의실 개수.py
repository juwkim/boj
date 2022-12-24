g = lambda: [*map(int, input().split())]

import heapq
nums = []
for s, e in sorted(g() for _ in range(int(input()))):
    if nums and nums[0] <= s:
        heapq.heappushpop(nums, e)
    else:
        heapq.heappush(nums, e)
print(len(nums))