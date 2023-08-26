N = int(input())
nums = [*map(int, input().split())]
print(sum(nums) - max(nums))