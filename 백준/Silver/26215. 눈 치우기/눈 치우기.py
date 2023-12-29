import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

import heapq

N = int(input())
nums = [-num for num in g()]
heapq.heapify(nums)

ans = 0
while len(nums) > 1:
    a, b = heapq.heappop(nums), heapq.heappop(nums)
    ans += -b
    heapq.heappush(nums, a - b)
ans -= nums[0]
if ans > 1440:
    ans = -1
print(ans)