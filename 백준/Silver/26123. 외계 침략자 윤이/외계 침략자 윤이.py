N, D = map(int, input().split())
nums = [*map(int, input().split())]
base = max(0, max(nums) - D)
ans = sum(max(0, num - base) for num in nums)
print(ans)