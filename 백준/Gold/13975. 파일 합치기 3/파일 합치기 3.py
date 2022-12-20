g = lambda: [*map(int, input().split())]
import heapq
for _ in range(int(input())):
    N = int(input())
    nums = g()
    heapq.heapify(nums)
    ans = 0
    for i in range(N - 1):
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        num = a + b
        heapq.heappush(nums, num)
        ans += num
    print(ans)