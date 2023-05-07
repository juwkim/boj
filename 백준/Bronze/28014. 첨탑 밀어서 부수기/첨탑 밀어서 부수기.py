ans = 0
input()
nums = [0] + [*map(int, input().split())]
for a, b in zip(nums, nums[1:]):
    ans += a <= b
print(ans)