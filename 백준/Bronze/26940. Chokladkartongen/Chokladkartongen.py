input()
nums = [*map(int, input().split())]
ans = 0
for a, b in zip(nums, nums[1:]):
    ans += a < b
print(ans)