g = lambda: [*map(int, input().split())]

k, s = g()
nums = g()
if max(nums) < k:
    ans = -1
else:
    ans = sum(min(num, k - 1) for num in nums) + 1
print(ans)