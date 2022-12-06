g = lambda: [*map(int, input().split())]

N, K = g()
nums = g()
for i in range(1, N):
    nums[i] += nums[i-1]

ans = nums[K-1]
for i in range(K, N):
    ans = max(ans, nums[i] - nums[i-K])
print(ans)