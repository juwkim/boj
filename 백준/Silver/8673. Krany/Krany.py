g = lambda: [*map(int, input().split())]

n, w = g()
nums = sorted([num for num in g() if num > 0], reverse=True)
for i in range(1, len(nums)):
    nums[i] += nums[i - 1]

ans = 'NIE'
for i in range(len(nums) - 1, -1, -1):
    if nums[i] >= (i + 1) * w:
        ans = len(nums) - (i + 1)
        break
print(ans)