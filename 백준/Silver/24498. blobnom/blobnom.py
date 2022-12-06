g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
ans = max(nums[0], nums[-1])
for i in range(1, N - 1):
    ans = max(ans, nums[i] + min(nums[i-1], nums[i+1]))
print(ans)