input = __import__('sys').stdin.readline
import heapq

N, M, K = map(int, input().split())
nums = [-int(input()) for _ in range(N)]
heapq.heapify(nums)
ans = 0
while K and nums:
    num = -heapq.heappop(nums)
    if num > M:
        q = min(K, num // M)
        ans += q * M
        K -= q
        heapq.heappush(nums, q * M - num)
    else:
        ans += num
        K -= 1
print(ans)