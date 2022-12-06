n = int(input())
nums = [*map(int, input().split())]
a = nums[0]
nums[0] = min(nums[:2])
for i in range(1, n):
    if a < nums[i]:
        a, nums[i] = nums[i], a
    else:
        nums[i] = max(nums[i], nums[i-1])

print(*nums[1:])