n = int(input())
nums = sorted(i - num for i, num in enumerate(map(int, input().split())))
ans = sum(nums[i] - nums[0] for i in range(1, n))
cur = ans
for i in range(1, n):
    cur += (2 * i - n) * (nums[i] - nums[i - 1])
    ans = min(ans, cur)
print(ans)