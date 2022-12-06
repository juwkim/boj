n = int(input())
nums = [*map(int, input().split())]
for i in range(n):
    nums[i] = n + 1 - nums[i]
print(*nums)