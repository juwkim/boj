n = int(input())
nums = [*map(int, input().split())]
print(max(nums) * (n - 2) + sum(nums))