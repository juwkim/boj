g = lambda: [*map(int, input().split())]

N, M, T = g()
nums = g()

ans = nums[0] - M + max(0, T - nums[-1] - M)
for i in range(N-1):
    ans += max(0, nums[i+1] - nums[i] - 2 * M)
print(ans)