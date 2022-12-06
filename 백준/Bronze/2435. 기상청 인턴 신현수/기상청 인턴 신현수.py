g = lambda: [*map(int, input().split())]

N, K = g()
nums = g()
ans = sum(nums[:K])
now = ans
for i in range(K, N):
    tmp = now + nums[i] - nums[i-K]
    ans = max(ans, tmp)
    now = tmp
print(ans)