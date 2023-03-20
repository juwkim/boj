N = int(input())
nums = sorted(set(map(int, input().split())))
ans = nums[-2]
for i in range(len(nums) - 1):
    ans = max(ans, nums[-1] % nums[i])
print(ans)