import heapq

N = int(input())
nums = [int(input()) for _ in range(N)]
heapq.heapify(nums)
ans = 0
for i in range(N - 1):
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    num = a + b
    heapq.heappush(nums, num)
    ans += num
print(ans)